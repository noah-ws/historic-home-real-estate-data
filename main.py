import argparse
import os

from homeharvest import scrape_property
from datetime import datetime

def main():
	parser = argparse.ArgumentParser(description="Home Harvest Property Scraper")

	parser.add_argument(
		"-l",
		"--location",
		type=str,
		default=None,
		help="Location to scrape home data for",
	)

	parser.add_argument(
		"-r",
		"--radius",
		type=int,
		default=20,
		help="The radius to scrape home data for, using the location as the centerpoint",
	)

	parser.add_argument(
		"-f",
		"--filename",
		type=str,
		default=None,
		help="Name of the CSV file to create, or append listing data to if it exists",
	)

	args = parser.parse_args()
	if not args.location:
		raise Exception('Location required!')
	
	if not args.filename:
		raise Exception('File name required!')
	
	properties = scrape_property(
	  location=args.location,
	  radius=args.radius, # Miles
	  listing_type="for_sale",
	  property_type=['single_family'],
	  past_days=1,
	  exclude_pending=True
	)

	properties = properties.drop_duplicates(subset=['property_id'])
	print(f"Number of properties listed today: {len(properties)}")

	# Save the current scrape to the history folder
	absDirectoryPath = os.path.dirname(os.path.abspath(__file__))
	current_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
	filename = f"HomeHarvest_{current_timestamp}.csv"
	scrapeHistoryDirectory= f'{absDirectoryPath}/ListingData/ScrapeHistory'
	os.makedirs(scrapeHistoryDirectory, exist_ok=True)
	properties.to_csv(f'{scrapeHistoryDirectory}/{filename}', mode='a', index=False, header=False)

	# Save the current scrape to the running data file
	listdataDataSubPath = args.location.upper().replace(" ", "")
	filePathPrefix = f'{absDirectoryPath}/ListingData/{listdataDataSubPath}'
	os.makedirs(filePathPrefix, exist_ok=True)
	filePath = f'{filePathPrefix}/{args.filename}'
	if os.path.exists(filePath):
		properties.to_csv(filePath, mode='a', index=False, header=False)
	else:
		properties.to_csv(filePath, index=False)


if __name__ == "__main__":
	main()
