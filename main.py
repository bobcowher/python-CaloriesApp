from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import StringField, SubmitField, Form, SelectField
from calorie import Calorie
from temperature import Temperature

class HomePage(MethodView):


    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):


    def get(self):
        calorie_form = CalorieForm()

        return render_template('calories_form.html', calorie_form=calorie_form)

    def post(self):
        calorie_form = CalorieForm(request.form)

        temperature = Temperature(city=calorie_form.city.data, country=calorie_form.country.data)

        calorie = Calorie(weight=calorie_form.weight.data,
                          height=(float(calorie_form.height_feet.data) * 12) + float(calorie_form.height_inches.data),
                          age=calorie_form.age.data,
                          gender=calorie_form.gender.data,
                          temperature=temperature.get()
                          )

        return render_template('calories_form.html',
                               result=True,
                               calorie_form=calorie_form,
                               calories=calorie.calculate())

class CalorieForm(Form):
    weight = StringField("Weight(lbs): ", default=265)
    height_feet = StringField("Height(feet): ", default=5)
    height_inches = StringField("Height(inches): ", default=11)
    gender = SelectField("Gender: ", choices=['Male', 'Female'])
    age = StringField("Age(years): ", default=29)

    # total_height_inches = (int(height_feet) * 12) + int(height_inches)

    city = StringField("City: ", default='Alabaster')
    country = StringField("Country: ", default='USA')

    button = SubmitField('Calculate')


app = Flask(__name__)

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories-form', view_func=CaloriesFormPage.as_view('calories_form_page'))

app.run(debug=True)