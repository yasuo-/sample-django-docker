# USAGE

### docker
```
$ docker-compose build
$ docker-compose up
or
$ docker-compose up -d
```

### python3.7 + virtualenv

install pyenv
virtualenv file name is env from google cloud python sample
```
$ pyenv local 3.7.0
$ virtualenv env
$ source env/bin/activate
(env) $ deactivate
```

### Djaongo starter command
#### admin
```
$ sudo docker-compose run web django-admin startproject app .
```
### application
```
$ sudo docker-compose run web python manage.py startapp app .
```
in apps folder
```
$ sudo docker-compose run web python manage.py startapp users ./apps/users
```

### makemigrations & migrate
```
$ sudo docker-compose run web python manage.py makemigrations
$ sudo docker-compose run web python manage.py migrate
```

### createsuperuser
```
$ sudo docker-compose run web python manage.py createsuperuser
```
