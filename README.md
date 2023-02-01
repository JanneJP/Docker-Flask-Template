# Docker-Flask-Template

I found myself creating the same basic project structure from scratch anytime I would start a new webdev project, so I finally decided to create a template project for it.

The template includes a flask app with blueprints for errors and the main index page. There is a placeholder database model set up to make sure all the databse related stuff is in working order. Bootstrap is used for styling due to it's barebones simplicity.

The database of choice is postgresql just due to it's popularity.

Testing is handled with pytest, with the placeholder model testing included, again, to make sure all that stuff works.

Along with this, the project is meant to run on docker. A dev and production dockerfiles are included.

Traefik used as reverse proxy, and to handle TLS certs

## Tech

- Python (Flask, SQLAlchemy)
- Traefik
- Docker
- Postgresql

<hr>

## Development environment setup

Create virtual environment in `services/web/` and activate it

    python -m venv env

    env/Scripts/activate

Upgrade pip and install dependencies

    pip install --upgrade pip

    pip install -r requirements.txt

Install pytest and run tests

    pip install pytest

    pytest

Verify local project works

    python manage.py run

Navigate to `127.0.0.1:5000`

Verify docker project works

    docker compose -f docker-compose.development.yml up

Navigate to `web.localhost`

Check that traefik dashboard works by navigating to `web.localhost:8080`

<hr>

## Testing environment setup

Create `.env.db.testing` file according to `example.env.db.production` in `environments/`

- `POSTGRES_USER` database user
- `POSTGRES_PASSWORD` database user password
- `POSTGRES_DB` database name

Create `.env.testing` file according to `example.env.production` in `environments/`

- `DATABASE_URL` edit in values from `.env.db.testing`

Create a `traefik.testing.toml` configuration file according to `example.traefik.production.toml` in `services/traefik/`

- In `[certificatesResolvers]`, change in your email adress for staging and production

at project root with docker compose files, create a `.env` file according to `example.env`

- `WEB_HOST` should be your domain name (localhost can be used for testing)

Start testing environment

    docker compose -f docker-compose.testing.yml up

Navigate to `web.<WEB_HOST>`

<hr>

## Production environment setup

Create `.env.db.production` file according to `example.env.db.production` in `environments/`

- `POSTGRES_USER` database user
- `POSTGRES_PASSWORD` database user password
- `POSTGRES_DB` database name

Create `.env.production` file according to `example.env.production` in `environments/`

- `DATABASE_URL` edit in values from `.env.db.production`

Create a `traefik.production.toml` configuration file according to `example.traefik.production.toml` in `services/traefik`

- In `[certificatesResolvers]`, change in your email adress for staging and production

at project root with docker compose files, create a `.env` file according to `example.env`

- `WEB_HOST` should be your domain name

Start production environment

    docker compose -f docker-compose.production.yml up

Navigate to `web.<WEB_HOST>`
