﻿# DevGigs

An app for listing python and django jobs.

## Distinctiveness and Complexity
DevGigs was build from scratch by applying the knowledge that was acquired throughtout CS50's Web programming with Python and Javascript course. The app is totally responsive and much focus was put on the user interface and user experience in an effort to make the app intuitive as much as possible.

## Content of each file created:
  - `/devgigs/static/devgigs/images` contains static images.
 
  - `/devgigs/static/devgigs/js/flashMessage.js` Contains javascript implementation of flash message components.

  - `/devgigs/static/devgigs/js/editListing.js` Contains the logic to show the form for editing a listing.
  
  - `/devgigs/static/devgigs/js/createModal.js` Contains the logic to show the form for creating a listing.
  
  - `/devgigs/static/devgigs/styles.css` contains app's global css styles.
  
  - `/devgigs/templates/devgigs/index.html`  For displaying all listings.
  
  - `/devgigs/templates/devgigs/show.html` For displaying a single listing.
  
  - `/devgigs/templates/devgigs/manage.html` For editing and deleting listings.
  
  - `/devgigs/templates/devgigs/layout.html` Defines the app's layout.
  
  - `/devgigs/templates/devgigs/login.html` For displaying the login form.
  
  - `/devgigs/templates/devgigs/register.html` For displaying the registration form.
  - `/devgigs/media/images` Contains images uploaded by user.
  - `/devgigs/urls.py` Contains applications routes


## How to run the application.

### Setup:
Run the following commands in your terminal:

- `python manage.py makemigrations` in order to generate the necessary files for the database setup;
- `python manage.py migrate` to execute the previous setup files created;
- `python manage.py runserver` to run the server

By default, the server adress is `http://127.0.0.1:8000/`. Copy the forementioned link in your browser url and hit enter. 

## Features.

### Web routes:

#### `/` (home page)

Fetches all listings from the database.
Search listings by all thier atttributes.

Returns `index.html`

----------------------
#### `/show/<int>`

Fetch a single listing from the database.

Returns `show.html`

----------------------
#### `/create` 

Inserts a new listing into the database.

returns `index.html` with a success message

#### `/manage`

Returns `manage.html` 

----------------------
#### `/edit/<int>`

Update a listing.

Returns `show.html` with a success message else it returns `manage.html` with an error message with an error occured!.

----------------------
#### `/delete/<int>`

Remove a listing from the database

Returns `manage.html` with success message 





  

