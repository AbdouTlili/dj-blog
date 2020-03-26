# dj-blog
this is a base blog project that allows : signup (with email confirmation ), signin, create, edit and delete posts.
the blog is built using 
- Django 3.0.4
- PostgreSQL 11
- WhiteNoise 5.0.1


## Running the site locally :
- go to the file dir :

```
cd dj-blog
```
- create a virtual environment and intall the dependancies :
```
pipenv install
```
- activate the virtual environment :
```
pipenv shell
```
- setup the database either by :

  1 - or just un-comment the SQLite3 setup in ```settings.py ``` and commenting PostgreSQL

  2 - updating the URL in  ``` DATABASES ``` in the settings :
  
  
  URL schema :

|   Engine   |         Django Backend        |                   URL                   |
|:----------:|:-----------------------------:|:---------------------------------------:|
| PostgreSQL | django.db.backends.postgresql | postgres://USER:PASSWORD@HOST:PORT/NAME |
|    MySQL   |    django.db.backends.mysql   |   mysql://USER:PASSWORD@HOST:PORT/NAME  |
|   Oracle   |   django.db.backends.oracle   |  oracle://USER:PASSWORD@HOST:PORT/NAME  


- migrate :
```
python manage.py migrate
```
- setting up some environment variables for the SMTP service :

PS : you can just add these directly to your ```settings.py```

```
export SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
export EMAIL_HOST = 'smtp.sendgrid.net'
export EMAIL_HOST_USER = 'apikey'
export EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
export EMAIL_PORT = 587
export EMAIL_USE_TLS = True
```

  or you can just use your Gmail for local testing by exporting or adding just  ```EMAIL_HOST ``` ```EMAIL_HOST_USER``` ```EMAIL_HOST_PASSWORD ```


- and you're done ! you just need to run the local server :
```
python manage.py runserver
```


## Deployment :

first you neeed to update the environment variables in the ```env``` file in the project directory  

i chose heroku for the deployment, so you need to have a heroku active account (it is free though), logged in heroku CLI

1- create a heroku app :
```
heroku create <name-of-the-app>
```
2- adding the app to the remote :
```
heroku git:remote -a <name-of-the-app>
```
3- setting up the environment variables that you updated :
```
heroku config:set $(< env )
```
4- add an commit the changes that you made :
```
git add -A ; git commit -m "post deployment commit"
```
and you're done deploying !
just push the changes to the heroku Dyno 
```
git push heroku master
```
and ``` heroku open ``` when the push is done to visit the blog online

### contribution/issues :
feel free  to add anything or ask :D

