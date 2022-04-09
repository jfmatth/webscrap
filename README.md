# Webscrap - Web Scrapping for keywords by website

Given a list of websites (full URL) and keywords, this will determine how many instances of that keyword are on that website for a particular time of the scrape.

This was a personal project of mine to find particular names on popular news sites to see how many times those names were mentioned.

## Installing

A standard Django app using a custom command.  See pipfile for all packages installed.

Technologies :
- Pipenv
- Docker (optional)
- Kubernetes / Helm (optional)
- dj-database-url
- waitress WSGI
- whitenoise

## Usage

After install, add the site / keywords to the scrap table via Django Admin, then run the custom command `manage.py scrape`.

If this is run in Kubernetes, then the HELM chart will install a Cronjob for hourly scraping.

