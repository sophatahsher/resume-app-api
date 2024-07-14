
## Run flacke8 testing
```
docker-compose run --rm django sh -c "flake8"
```

## create Django Project "app"
```
docker-compose run --rm django sh -c "django-admin startproject app ."
```

## create new app "user"
```
docker-compose run --rm django sh -c "python manage.py startapp user"
```