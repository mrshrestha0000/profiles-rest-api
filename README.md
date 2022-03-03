# profiles REST API
profile REST API course code.

# creating ssh keys
ls ~./ssh
ssh-keygen -t rsa -b 4096 -C "success123shrestha@gmail.com"
passphrase : 1234

# git
username: mrshrestha0000
PAT - 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

# vegrant
vegrant up

vegrant ssh
exit

# git push
add .
git commit -am ""
git push origin

# setup virtual Environment
python -m venv ~/env
source ~/env/bin/activate

# install requirements
pip install -r requirements

# start project and app
django-admin startproject profiles_project .
python manage.py startapp profiles_api

# add app in projetct
setting -> installed app -> app_name

# runserver
python3 manage.py runserver

# make migration
in env - 
python manage.py makemigration <app name><profile_api>
python manage.py migrate
