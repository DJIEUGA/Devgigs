# DevGigs

An app for listing python and django jobs.

## Distinctiveness and Complexity

DevGigs was build from scratch by applying the knowledge that was acquired throughtout CS50's Web programming with Python and Javascript course. The app is totally responsive and much focus was put on the user interface and user experience in an effort to make the app intuitive as much as possible.

#### Functionalities:

##### Register and Login: 

Users can register and login on the platform via the register and login pages respectively. After registration/login, the user is redirected to the `index` page with a `Welcome` message which he make to disappear by clicking on the `x` icon on the message component.

#### Index Page:

Users whether login or not can see all listings.

##### Search Listing:

User whether login or not can search listings by typing in random keywords in the the search bar. If nothing is found, users should see no results else a result set of the listings will be displayed on the screen.

Users can also search listings by clicking on a tag of a given listing. All listings having that tag will be returned as search results.

##### Create Listing:

Users can create listings by providing the company name, title, description, company's email, job location, tags and an optional logo.

To create a new listing, the user should click on the `Post Job` button, which will display a modal containing a form. After filling the required fields, the user should click on "Create" button to send the request to the server which creates a new listing and return the `index` page.

##### Edit Listing:

By visiting the `/manage` web route, user can edit a listing by click on the `Edit` button of the corresponding listing. This will display a modal with a form whose input fields are prefilled with the values of the listing. After modifying the values od the intending input fields, you want to click on the `Save` button to save the updated listing and be redirected to that particular listing page with a `success` message instance similary to the one mentionned in the `######Register and Login` section.

`NB` : The modal form displayed when creating a listing and when editing a listing respectively is a the same modal component that is instanciated by overriding the content of the original modal found in `/devgigs/templates/devgigs/layout.html` at line 24. The javascript code that takes care of the create functionality is found in `/devgigs/static/devgigs/js/createModal.js` and that for the edit functionality is found in `/devgigs/static/devgigs/js/editListing.js`.


##### Delete Listing:

Similarly, by  visiting the `/manage` web route, user can delete a listing by clicking on the `Delete` button corresponding to that listing. Clicking on that `Delete` button, the user will be redirected to the same page with another `succces` message instance.

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

- `python manage.py makemigrations devgigs` in order to generate the necessary files for the database setup;
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

returns `index.html` with a success message.

#### `/manage`

Returns `manage.html` 

----------------------
#### `/edit/<int>`

Update a listing.

Returns `show.html` with a success message else it returns `manage.html` with an error message with an error occured!.

----------------------
#### `/delete/<int>`

Remove a listing from the database.

Returns `manage.html` with success message else return the same file with an error message.

----------------------
### User Authentication:

#### `/login`

Login registered users.

Returns `login.html`
  
--------------------
#### `/register`

Allows the registraion of new users.

Returns `register.html`

------------------------------
### API routes

#### `/listing/<int>`

Return JSON response listing data according to the provided ID via `GET` request.

## Any other additional information the staff should know about your project.

### MODELS

The app contains two models, namely: the USER model and the LISTING model

#### USER MODEL:

The user model extends AbstractUser class from django.contrib.auths.models which provide default fields like:

  - username 
  - password 
  - email
  - first_name 
  - last_name 
  - is_superuser 
  - is_staff
  - is_active 
  - date_joined 
  - groups and
  - user_permissions.


#### LISTING MODEL:

The listing model has the following fields:

  - User(Referenced from the User model)
  
  - email(the company email)
  
  - title(Job title)
  
  - description(Job description) 
  
  - company(The company name)
  
  - tags(keywords to facilited search)
  
  - location(Area where job is located)
  
  - logo(Company logo but can be allowed empty) and
  
  - timestamp

All these models are defined in `/devgigs/models.py`





  

