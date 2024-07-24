
## Run flacke8 testing
```
docker-compose run --rm app sh -c "flake8"
```

## create Django Project "app"
```
docker-compose run --rm app sh -c "django-admin startproject app ."
```

## create new app "user"
```
docker-compose run --rm app sh -c "python manage.py startapp user"
```