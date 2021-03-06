import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_drinks")
def get_drinks():
    drinks = list(mongo.db.drinks.find())
    return render_template("drinks.html", drinks=drinks)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    drinks = list(mongo.db.drinks.find({"$text": {"$search": query}}))
    return render_template("drinks.html", drinks=drinks)


@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        # checking if username is already existing in the db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Lounge name already exists")
            return redirect(url_for("join"))

        join = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(join)

        # puts the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("You are now part of the Lounge!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("join.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Wrong Lounge Name and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Wrong Lounge Name and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have left the Lounge")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_drink", methods=["GET", "POST"])
def add_drink():
    if request.method == "POST":
        drink = {
            "category_name": request.form.get("category_name"),
            "drink_name": request.form.get("drink_name"),
            "drink_ingredients": request.form.get("drink_ingredients"),
            "drink_method": request.form.get("drink_method"),
            "drink_garnish": request.form.get("drink_garnish"),
            "social_media": request.form.get("social_media"),
            "made_by": session["user"]
        }
        mongo.db.drinks.insert_one(drink)
        flash("Drink has been added to the Lounge")
        return redirect(url_for("get_drinks"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_drink.html", categories=categories)


@app.route("/edit_drink/<drink_id>", methods=["GET", "POST"])
def edit_drink(drink_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "drink_name": request.form.get("drink_name"),
            "drink_ingredients": request.form.get("drink_ingredients"),
            "drink_method": request.form.get("drink_method"),
            "drink_garnish": request.form.get("drink_garnish"),
            "social_media": request.form.get("social_media"),
            "made_by": session["user"]
        }
        mongo.db.drinks.update({"_id": ObjectId(drink_id)}, submit)
        flash("Drink has been updated")

    drink = mongo.db.drinks.find_one({"_id": ObjectId(drink_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_drink.html", drink=drink, categories=categories)


@app.route("/delete_drink/<drink_id>")
def delete_drink(drink_id):
    mongo.db.drinks.remove({"_id": ObjectId(drink_id)})
    flash("Drink has been removed")
    return redirect(url_for("get_drinks"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Style Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Style Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Style has been deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
