# Data Source

Realtor.com

# Scraping Tool

[HomeHarvest](https://github.com/Bunsly/HomeHarvest)

# main.py args

options:
  -h, --help            show this help message and exit
  -l LOCATION, --location LOCATION
                        Location to scrape home data for
  -r RADIUS, --radius RADIUS
                        The radius to scrape home data for, using the location as the centerpoint
  -f FILENAME, --filename FILENAME
                        Name of the CSV file to create, or append listing data to if it exists

## Example
py main.py -l "San Diego, CA" -r 20 -f "San_Diego_CA_Daily_Listings.csv"

# Windows Automation

Achieved using Task Scheduler

1. Hit the Windows key and search "Task Scheduler"
2. Select "Create Task..." in the right-most pane
3. Give it a Name/description so you can identify it
4. Select "Run whether user is logged on or not"
5. Move to "Triggers" tab and select "New..."
6. Enter your preferred scraping interval
7. Move to the "Actions" tab and select "New..."
8. Enter "py" or "python" into the "Program/script:" box
9. Enter your "<PATH_TO_THIS_REPO>\main.py -l "San Diego, CA" -r 20 -f "San_Diego_CA_Daily_Listings.csv"" 
   into the "Add arguments (optional):" box. Change arguments to your desired args
10. Click "Ok", then Click "Ok" again
11. Enter credentials, if prompted

Ta-Da! You've successfully automated scraping daily listings from your desired location