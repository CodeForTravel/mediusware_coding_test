#!/bin/sh

echo "*** Pulling the Latest Source Code ***"
git pull
sleep 5
echo "*** Source Code has been updated. ***"

pip install -r requirements.txt

# python3 manage.py clean_pyc
cd frontend
sudo yarn run build

cd ..
python3 manage.py migrate
python3 manage.py collectstatic --noinput

sudo systemctl daemon-reload
sudo systemctl restart gunicorn_example.service
sudo systemctl restart gunicorn_example_tasks.service
sudo service nginx restart
