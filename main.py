from calorie import Calorie
from temperature import Temperature
from flask.views import MethodView
from wtforms import Form,StringField, SubmitField
from flask import Flask, render_template, request

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')

class CaloriesFormPage(MethodView):

    def get(self):
        calories_form = CaloriesForm()

        return render_template('calories_form_page.html',
                               caloriesform = calories_form)
    def post(self):
        pass