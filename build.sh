pip install -r requirements.txt
py manage.py collectstatic --noinput
py manage.py makemigrations devgigs
py manage.py migrate
