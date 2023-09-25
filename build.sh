python -m venv env
env/Scripts/activate
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
