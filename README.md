Example ETOR application
========================

using:
    django - awesome python web framework
    django-tastypie - delicious api for django
    backbone - evolved structure for client-side javascript
    
to get started:
---------------
(these instructions work best on linux)

Install python2.7

install pip

create a project folder

create a virtual environment:
    
    virtualenv --no-site-packages venv

clone this repository:
    
    git clone https://github.com/timothypage/etor.git

activate your virtual environment:

    source venv/bin/activate

install dependencies from included file

    pip install -r dependencies

create your local sqlite3 database:

    python manage.py syncdb
    ...follow and answer prompts to create admin login
    ...this will load a sample dataset from initial_data.json automatically!

run the development server:

    python manage.py runserver

Point your browser to localhost:8000

