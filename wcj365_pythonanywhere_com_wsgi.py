# This file contains the WSGI configuration required to serve up your
# web application at http://wcj365.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# +++++++++++ GENERAL DEBUGGING TIPS +++++++++++
# getting imports and sys.path right can be fiddly!
# We've tried to collect some general tips here:
# https://help.pythonanywhere.com/pages/DebuggingImportError

# Below are templates for Django and Flask.  You should update the file
# appropriately for the web framework you're using, and then
# click the 'Reload /yourdomain.com/' button on the 'Web' tab to make your site
# live.

# +++++++++++ VIRTUALENV +++++++++++
# If you want to use a virtualenv, set its path on the web app setup tab.
# Then come back here and import your application object as per the
# instructions below

# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
#import os
#import sys
#
## assuming your django settings file is at '/home/wcj365/mysite/mysite/settings.py'
## and your manage.py is is at '/home/wcj365/mysite/manage.py'
#path = '/home/wcj365/mysite'
#if path not in sys.path:
#    sys.path.append(path)
#
#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
#
## then:
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()


# +++++++++++ FLASK +++++++++++
# Flask works like any other WSGI-compatible framework, we just need
# to import the application.  Often Flask apps are called "app" so we
# may need to rename it during the import:
#
#
import sys
#
## The "/home/wcj365" below specifies your home
## directory -- the rest should be the directory you uploaded your Flask
## code to underneath the home directory.  So if you just ran
## "git clone git@github.com/myusername/myproject.git"
## ...or uploaded files to the directory "myproject", then you should
## specify "/home/wcj365/myproject"
path = '/home/wcj365/flask-sql'
if path not in sys.path:
    sys.path.append(path)
#
from hello import app as application  # noqa
#
# NB -- many Flask guides suggest you use a file called run.py; that's
# not necessary on PythonAnywhere.  And you should make sure your code
# does *not* invoke the flask development server with app.run(), as it
# will prevent your wsgi file from working.
