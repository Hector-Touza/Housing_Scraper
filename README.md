# A simple scraper to retrieve housing data from idealista.com #

This scraper navigates to all houses in a given area and retrieves it's features.  
The raw data is stored as a pandas DataFrame and dumped into a json.

## Getting started ##

Clone this repository  
Install requirements  
Change parameters in `./config/config.py`:
- `starting_url` => url of the zone you want to scrap
- `driver_path` => filepath to your ChromeWebdriver


##Avoiding detection ##

This scraper should not trigger any bot detection, provided you:
- Use it from a residential IP (i.e. are not launching this from some cloud service)
- Don't use it with a fresh Chrome profile (you should have navigation history, extensions, cookies...)  
- Maintain generous wait times between pages (configured by default)  

In any case, the application will detect and attempt to click on any reCAPTCHAs.  
Crawling should continue if you meet reCAPTCHAs score.

##Future Work ##

- Refactor into a pip-installable package  
- Refactor print statements into a proper logging.  
- Add functionality to resume interrupted crawls (useful for zones with a lot of houses)