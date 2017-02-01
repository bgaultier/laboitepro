[![Build Status](https://api.travis-ci.org/laboiteproject/laboite-backend.svg?branch=master)](https://travis-ci.org/laboiteproject/laboite-backend)
[![Code Climate](https://codeclimate.com/github/laboiteproject/laboite-backend/badges/gpa.svg)](https://codeclimate.com/github/laboiteproject/laboite-backend)
[![Test Coverage](https://codeclimate.com/github/laboiteproject/laboite-backend/badges/coverage.svg)](https://codeclimate.com/github/laboiteproject/laboite-backend/coverage)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/laboiteproject/laboite-backend/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/laboiteproject/laboite-backend/?branch=master)

# laboîte
Django web app of the laboîte project http://laboite.cc/help

## Getting Started

Make sure you are using a virtual environment of some sort (e.g. `virtualenv` or
`pyenv`) and the following packages are installed :

* libxslt1-dev
* libxml2-dev
* python2.7-dev (depending on your version)
* zlib1g-dev
* libjpeg-dev
* libgif-dev
* libpng12-dev
* libgnutls28-dev

For exemple on linux distributions, use:
```
apt-get install libxslt1-dev libxml2-dev python2.7-dev zlib1g-dev libjpeg-dev libgif-dev libgif4 libpng12-dev libgnutls28-dev
```

```
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata sites
./manage.py createsuperuser
./manage.py runserver
```

You can then connect to the admin on http://127.0.0.1:8000/admin with the super
user you created above.
