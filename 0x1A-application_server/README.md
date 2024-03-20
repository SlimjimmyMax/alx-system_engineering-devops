# Application Server vs Web Server

An application server hosts applications and provides business logic, while a web server handles HTTP requests and serves static assets. Application servers support programming languages like Python, Ruby, etc. Web servers like Nginx are better at handling static content efficiently.

# How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04

The linked DigitalOcean tutorial explains how to deploy a Flask app using Gunicorn for the application server and Nginx as a reverse proxy. Do not install Gunicorn in a virtualenv, install it globally.

# Running Gunicorn 

Gunicorn runs Flask apps in a production environment. It handles starting and stopping processes and can integrate with Nginx.

# Flask and Strict Slashes

Flask's default behavior is to redirect paths with trailing slashes to their non-trailing counterpart. This can cause issues in production, so it should be disabled by setting `strict_slashes=False` on the app.

# Upstart Documentation

Upstart is a service manager for starting tasks and services during system boot and monitoring them. Its documentation explains how to configure Upstart jobs.
