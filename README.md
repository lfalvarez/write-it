You write it, and we deliver it.
================================

[![Build Status](https://travis-ci.org/lfalvarez/write-it.png?branch=master)](https://travis-ci.org/ciudadanointeligente/write-it)
[![Coverage Status](https://coveralls.io/repos/lfalvarez/write-it/badge.png?branch=master)](https://coveralls.io/r/ciudadanointeligente/write-it)
[![Code Health](https://landscape.io/github/lfalvarez/write-it/master/landscape.png)](https://landscape.io/github/ciudadanointeligente/write-it/master)

Write-it is an application that aims to deliver messages to people whose contacts are to be private or the messages should be public, for example: members of congress. 

Write-it is a layer on top of the [popolo standard](http://www.popoloproject.com/) from where it takes the people and adds contacts. The way it delivers messages is using plugins for example: mailit. And this approach allows for future ways of delivering for example: twitter, whatsapp, fax or pager.

Future uses are in [votainteligente](http://www.votainteligente.cl) to replace the old "preguntales" (You can [check here](http://municipales2012.votainteligente.cl/valdivia/preguntales), to see how it used to work) feature, could be in the way for the site [writetothem](http://www.writetothem.com/) and any parlamentary monitoring site.



Installation
------------

System Requirements
-------------------

 * [Elasticsearch](http://www.elasticsearch.org/)

 Sometimes it's required

 * [Urllib3](http://urllib3.readthedocs.org/en/latest/)

Write-it is built using Django. You should install Django and its dependencies inside a virtualenv. We suggest you use [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) to create and manage virtualenvs, so if you don’t already have it, [go install it](http://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation), remembering in particular to add the required lines to your shell startup file.

With virtualenvwrapper installed, clone this repo, `cd` into it, and create a virtualenv:

    git clone git@github.com:lfalvarez/write-it.git
    cd write-it
    mkvirtualenv writeit

Install the requirements:

    pip install -r requirements.txt

Set up the database, creating an admin user when prompted:

    ./manage.py syncdb && ./manage.py migrate

Then run the server:

    ./manage.py runserver


Testing
-------
For testing you could run ./test.sh

Coverage Analysis
-----------------
For coverage analysis run ./coverage.sh


API clients
-----------

Write-it has been used mostly through it's REST API for which there are a number of API clients.
The github repos and the status of the development are listed below:
- [writeit-rails](https://github.com/ciudadanointeligente/writeit-rails) ALPHA
- [writeit-django](https://github.com/ciudadanointeligente/writeit-django) ALPHA


There are instructions to install write-it in heroku
----------------------------------------------------
The instructions are in [the following link](deploying_to_heroku.md).
