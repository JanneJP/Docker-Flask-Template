# Docker-Flask-Template

I found myself creating the same basic project structure from scratch anytime I would start a new webdev project, so I finally decided to create a template project for it.

The template includes a flask app with blueprints for errors and the main index page. There is a placeholder database model set up to make sure all the databse related stuff is in working order. Bootstrap is used for styling due to it's barebones simplicity.

The database of choice is postgresql just due to it's popularity.

Testing is handled with pytest, with the placeholder model testing included, again, to make sure all that stuff works.

Along with this, the project is meant to run on docker. A dev and production dockerfiles are included.

Nginx is used as a webserver

## Tech

- Python (Flask, SQLAlchemy)
- Nginx
- Docker
- Postgresql

## TODO

- Find out where the pytest database file is being created at