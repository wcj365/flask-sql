#!/usr/bin/env python3

from flask import Flask, request, render_template, jsonify

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/test.db'

db = SQLAlchemy(app)


class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    population = db.Column(db.Integer)

    def serialize(self):

        return {
            'id': self.id,
            'name': self.name,
            'population': self.population,
        }


@app.route('/')
def hello():
    return 'Hello there!\n'

@app.route("/greeting", methods=["GET"])
def greet():
    name=request.args.get("name","Guest")
    msg = f'Hello {name}'

    return msg, 200, {'Content-Type': 'text/plain; charset=utf-8'}  

@app.route("/greeting2", methods=["GET"])
def greet2():
    name = request.args.get("name", "Guest")
    return render_template("index.html", name=name)    

@app.route("/about", methods=["GET"])
def about():
    return app.send_static_file("about.html")    

@app.route('/cities')
def all():

    cities = City.query.all()

    return jsonify(cities=[city.serialize() for city in cities])
