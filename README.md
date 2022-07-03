# Flask-Docker Template

🐳 Template for a simple Flask-Docker service with hot reloading.

<br />

## Usage

1. Use/Pull/Fork this template
2. Navigate to the folder
3. Run `docker-compose up`

<br />

## Hot Reloading

- removing volumes malfunctions hot reloading
- installing new packages will _not_ trigger hot reloading.
In that case, you should remove the running container and rebuild the Docker
image (don't forget to update requirements.txt with the new package).

    Alternatively, you can execute installation in the container:
    - `docker exec -it <CONTAINER_ID> bash`
    - `pip3 install -r requirements.txt`

<br />

## Production Deploy

### container's content

The built container in production will only contain files/folders not ignored
by the `.dockerignore` file (wanted behaviour).

<br />

### docker-compose.yml

The `docker-compose.yml` file and `docker-compose` commands should not be used in
production. This file's purpose is to ease the local development,
including adding the hot reloading ability.

<br />

### command

When deploying the service to production, set
`gunicorn -b 0.0.0.0:8080 -w 1 --threads 3 -t 0 app:app`
as the container's "command".

Examples:

- In AWS ECS: Container Definitions -> command
- In GCP Cloud Run: Container command

> gunicorn 🦄 is a popular WSGI suitable for running the web server in production.
Tweak the number of workers, threads, and other flags based on how powerful your machine is.

<br />

## Errors

When you encounter an error (or unexpected behaviour) that you cannot solve:

1. Remove the Docker container and image

2. Then run `docker-compose build --no-cache flask-docker`

3. Lastly, run `docker-compose up flask-docker`

In case this does not fix the error, or you have any additional questions, feel free to open a GitHub issue.
