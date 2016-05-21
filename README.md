# automatic-happiness

## Some badges
[![Build Status](https://travis-ci.org/qwergram/automatic-happiness.svg?branch=development)](https://travis-ci.org/qwergram/automatic-happiness)

## What is this?
A really big sandbox for me ([Norton Pengra](http://qwergram.github.io)) to play in. Here are the current features so far...

### /qwergram_api/
The core code of everything; this code is deployed to an ec2 instance.
Currently, it resides at [ec2-54-187-86-84.us-west-2.compute.amazonaws.com](http://ec2-54-187-86-84.us-west-2.compute.amazonaws.com/api/v1).

#### /qwergram_api/articles/
The main the app, it is written with [django-rest-framework](http://www.django-rest-framework.org/),
The current routes look like:

```
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'articles', views.CodeArticleViewSet)
router.register(r'ideas', views.PotentialIdeaViewSet)
router.register(r'shares', views.RepostViewSet)

urlpatterns = [
    url(r'api-auth/', include('rest_framework.urls')),
    url(r'api-auth/token/', authview.obtain_auth_token),
    url(r'repos/', views.GithubViewSet.as_view()),
    url(r'', include(router.urls)),
]
```
These routes live at `/api/v1/`

### /qwergram_bots/
These are the bots I've written to do various tasks for me. Some scrape data, some
send emails, etc. They might not necessarily be written in Python. Most likely, they're
an excuse for me to pick up a new programming language.

#### /qwergram_bots/smtp/
Contains HydrogenBot and LithiumBot, both handle reading and sending emails respectively.
Created for the purpose so I can email the bots articles to be published in 24 hours.

#### /qwergram_bots/github/
Contains HeliumBot, which handles realtime github scraping. Targets repos specifically.

### /qwergram_react/
The entire front end that is deployed to [qwergram.github.io](http://qwergram.github.io).
Utilizes Facebook's ReactJS and Jest for testing.

### /qwergram_devops/
I tried to use ansible... but I found it was easier to just write bash scripts to deploy to aws
and github pages. This script only works on \*nix based machines as of right now.

## How do I use this tool?
Er. It'd be difficult. I haven't tested this with other accounts. However if you wanted to try,
you do need to edit the `.secrets.sh` file and export the following in there:

```
SECRET_KEY
DEBUG_MODE
ADMIN_USER
ADMIN_PASS
DB_HOST
DB_NAME
DB_PORT
DB_USERNAME
DB_PASSWORD
EMAIL_PORT
EMAIL_ADDR
EMAIL_ADMIN
EMAIL_PASS
EMAIL_HOST
EMAIL_IMAP
SERVER_LOCATION
SERVER_USER
SERVER_KEY
SERVER_REPO
CLIENT_REPO
GITHUB_USER
GITHUB_PASS
```

In addition, you'll need to install the following:
- django
- requests
- django-nose
- django-cors-headers
- djangorestframework
