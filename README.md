# Webscrap - Web Scrapping for keywords by website

Given a list of websites (full URL) and keywords, this will determine how many instances of that keyword are on that website for a particular time of the scrape.

This was a personal project of mine to find particular names on popular news sites to see how many times those names were mentioned.

## Technologies used

- Pipenv
- Docker (optional)
- Kubernetes / Helm (optional)
    - Crunchy Postgres operator
    - Postgres DB (using above)
- dj-database-url
- waitress WSGI
- whitenoise

## Installtion - Locally

1. Clone the repo
```
git clone https://github.com/jfmatth/webscrap.git
```

2. setup the environment
```
pipenv shell
```
This should install all needed dependecies in Pipenv file

3. django migrate and superuser
```
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

4. Add some sites to scrape

We use pylons waitress to serve WSGI, like withing the container, so use that here
```
waitress-serve  --listen=0.0.0.0:8080 webscrap.wsgi:application
```

Add some records to the Scrape table, make sure to include the http or https prefix.  

Once you have some records in the DB, lets ask webscrap to scrape them

5. Run the custom management command 
(You will need to stop the waitress server for this)

```
python manage.py scrape
```

6. Validate the collection and counts

Run the server again, and validate the results in the Result table.

7. Run on PIKU
- Adjust settings.py to account for DJ_DATABASE

## Installation - Kubernetes

Requirements:
- Kubernetes 1.22
- Crunchy Postgres operator v5.05
- Helm 3.x


1. Install the Database
```
cd _kubernetes/db
helm install db .
```

This will install the postgres DB using the crunchy operator 

2. Adjust the ingress to match what you need in your Kubernetes environment

    Edit the value.yaml file

```
...
ingress:
  enabled: true
  className: ""
  annotations: {}
    # kubernetes.io/ingress.class: nginx
    # kubernetes.io/tls-acme: "true"
  hosts:
    - host: scrape.192.168.2.101.nip.io  <<<<< ---- Edit this line
      paths:
        - path: /
          pathType: ImplementationSpecific
  tls: []
  #  - secretName: chart-example-tls
  #    hosts:
  #      - chart-example.local
...
```


2. Install the app
```
cd _kubernetes/app
helm install app .
```

3. Find the running app container, exec into it and run migrate and createsuperuser

4. Login to the admin site and create scrapes

5. Optional - run scrap immediately

There is a cronjob in Kubernetes that runs every hour to scrape the sites, but you can run it immediately if you like

```
kubectl create job --from=cronjob/app
```

This will create a job immediately and run the scrape.  Check the DB for results

# Enjoy