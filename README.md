# Flask Web Application Development
## Environments
- Development Environment: notebooks.ai
- Production Environment: pythonanywhere.com
- Source Code Repository: GitHub (this repo)
## Components
- Flask
- sqlite3
- flask_sqlalchemy
## References: 
- http://zetcode.com/python/flask/
- https://www.twilio.com/blog/how-run-flask-application
- https://smallbusiness.chron.com/use-sqlite-ubuntu-46774.html
## Steps
1. To install flask

`$pip install -U Flask`

2. To install -U flask_sqlalchemy

- `$pip install -U flask_sqlalchemy`
- "-U" = "--updates"

3. To combine 1 and 2 into a single requirements.txt file
The requirements.txt file contains two simple lines:
```
flask
flask_sqlapchemy
```
`$install -r requirements.txt`

4. to Run flask

- `$export FLASK_APP="/app/webapps/hello/hello.py"`

- `$flask run`

## sqlite3 on Ubuntu 

1. How to install sqlite3 on ubuntu?

`$apt-get install sqlite3 libsqlite3-dev` or

`$sudo apt-get install sqlite3 libsqlite3-dev`if you are not admin/root

2. How to create a new database?

`$sqlite3 dbname.db`

This will take you to sqlite3 interactive shell `sqlite>`
- `sqlite>.help` for help
- `sqlite3>.quit` to exit
- `sqlite>.read myscript.sql` to run a SQL script
- `sqlite>select * from cities;` to run a query

3. How to connect to an existing DB?

`$sqlite3 dbname.db`

or

`$sqlite3` then `sqlite>.open dbname.db`



