from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func
from sqlalchemy.sql.functions import random
from dataclasses import dataclass
from sqlalchemy.exc import IntegrityError

"""
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
@dataclass  # We can make this class a dataclass to make serialization simpler
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record


# Get a random cafe
@app.route("/random", methods=["GET"])
def get_random_cafe():
    random_cafe = db.session.execute(db.select(Cafe).order_by(func.random())).scalar()
    return jsonify(Cafe=random_cafe)


# Get all cafes in the database
@app.route("/all", methods=["GET"])
def get_all_cafes():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()

    return jsonify(cafes=all_cafes)


# Get Cafes Based on Location
@app.route("/search", methods=["GET"])
def search_location():
    location = (request.args.get("loc")).title()
    cafes_in_location = (
        db.session.execute(db.select(Cafe).where(Cafe.location == location))
        .scalars()
        .all()
    )
    if cafes_in_location:
        return jsonify(cafes=cafes_in_location)
    else:
        return jsonify(
            errors={"Not Found": "Sorry, we don't have a cafe at that location."}
        )


# HTTP POST - Create Record
# Add new cafes to the api
@app.route("/add", methods=["POST"])
def add_cafe():
    try:
        new_cafe = Cafe(
            name=request.form["name"].title(),
            img_url=request.form["img_url"],
            map_url=request.form["map_url"],
            location=request.form["location"],
            seats=request.form["seats"],
            has_wifi=bool(request.form["has_wifi"]),
            has_sockets=bool(request.form["has_sockets"]),
            has_toilet=bool(request.form["has_toilet"]),
            coffee_price=request.form["coffee_price"],
            can_take_calls=bool(request.form["can_take_calls"]),
        )
        db.session.add(new_cafe)
        db.session.commit()
        response = {"Success": f"Successfully added {request.form['name']}."}
    except IntegrityError:
        response = {"error": f"{request.form['name']} could not be added."}
    return jsonify(response=response)


# HTTP PUT/PATCH - Update Record
# Update coffee prices using the id
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe_to_update = db.session.get(entity=Cafe, ident=cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = request.args.get("new_price")
        db.session.commit()
        response = {"success": "Successfully updated the price."}
        response_code = 200
    else:
        response = {
            "error": {
                "Not Found": "Sorry a cafe with that id was not found in the database."
            }
        }
        response_code = 404

    return jsonify(response), response_code


# HTTP DELETE - Delete Record
# Delete a record (cafe) from the database
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    api_key = request.args.get("api-key")
    if api_key == "TopSecretAPIKey":
        cafe_to_remove = db.session.get(entity=Cafe, ident=cafe_id)
        if cafe_to_remove:
            db.session.delete(cafe_to_remove)
            db.session.commit()
            return jsonify(
                response={
                    "success": f"cafe with id {cafe_id} has been removed from the database."
                }
            ), 200
        else:
            return jsonify(
                error={
                    "Not Found": "Sorry a cafe with that id has not been found in the database."
                }
            ), 404
    else:
        return jsonify(
            {
                "error": "Sorry, that's not allowed. Make sure you have the correct api key."
            }
        ), 403


# READ DOCS
@app.route("/documentation", methods=["GET"])
def read_docs():
    return render_template("cafe_wifi_docs.html")


if __name__ == "__main__":
    app.run(debug=True)
