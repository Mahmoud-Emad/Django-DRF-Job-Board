# Target ` Job Board `

## Description:
* Simple API job board web application built by Django and DRF.
* [You can see it live now](https://target-job-board-app.herokuapp.com/)


## Installation:
* There is a few packages were used in this application such as: django, djangorestframework djangorestframework-simpleJWT
* Docker:
    * Run `docker build .`
    * Run `docker-compose build` to build the docker image
    * Run `docker-compose up`
* Python:
    * You have to create environment and this is the first step, check command below
    * for windows try tio use this `python -m venv (name_of_env)`
    * To activate it use `.\Scripts\activate`
    * for mac try tio use this `python3 -m venv (name_of_env)`
    * To activate it use "source `(name_of_env)/bin/activate`
    * try to install packages using requirements.txt file using this command ` pip install -r requirements.txt `
    * After using commands above you just have to use `python manage.py migrate` then `python manage.py runserver`


## After Installation:
* Go to [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/) to see our OpenAPI documentation
* Go to [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) to see our api endpoints, specification

## UserType and Permissions:
* You can register as a job seeker or employer to take permission to access different endpoints based on your user type
* Use [http://127.0.0.1:8000/api/job-seekers/register/](http://127.0.0.1:8000/api/job-seekers/register/) endpoint to register a new account on as a job-seeker
* while you can use [http://127.0.0.1:8000/api/employers/register/](http://127.0.0.1:8000/api/employers/register/) endpoint to register a new account as an employer


## After registration:
* as a job-seeker, you can :
    - Login
    - Browse the most recent jobs
    - Apply to job
    - Get jobs you were applied on 
    - Searching about job
    - See top companies
    - Update profile information
    - DELETE your account

* as employer, you can :
    - Login
    - Post a new job
    - See who applied for your jobs
    - See top companies
    - Searching about job
    - Close the job you posted
    - Update profile information
    - DELETE your account

* #####  Ech user has permissions based on his user type

## How to login?:
- Go to [http://127.0.0.1:8000/api/auth/sign-in/](http://127.0.0.1:8000/api/auth/sign-in/) endpoint to take a token
- Put your `Bearer <token>` in authorization button to take access, `now you are logged in`

## Run Tests:
- To Run unit tests there are two options:
    - Docker:
        - `docker-compose run web sh -c "python manage.py test"`.
    - Python:
        - `python manage.py test`.

## Admin Dashboard:
- To access Admin dashboard 
    - Local
        - [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
    - Live
        - [http://target-job-board-app.herokuapp.com/admin/](http://target-job-board-app.herokuapp.com/admin/)
    
    - admin credentials are: `admin@target.com`, `0000`

## Note:
- Feel free to contact me if there are any problem
- Still working on the Docker part till now 
