from flask import render_template
from allTimeRecipes import app, db
from allTimeRecipes.models import User, Recipes, Comments

@app.route("/")
def home():
    return render_template('home.html')