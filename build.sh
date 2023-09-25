# build.sh
pip install -r requirements.txt
python3 manage.py collectstatic --noinput
python3 manage.py makemigrations devgigs
python3 manage.py migrate
