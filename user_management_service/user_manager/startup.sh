#!/bin/bash

# run wait for postgres script
#./wait-for-postgres.sh $HOST

# run db migrations
python manage.py migrate

# run django application
python manage.py runserver 0.0.0.0:8000