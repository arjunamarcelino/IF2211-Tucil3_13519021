from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory
from flask_wtf import FlaskForm
from wtforms import SelectField

import InputFile as i

app = Flask(__name__)
app.config["SECRET_KEY"] = 'IF2211-Tucil3_13519021'
app.config["DEBUG"] = True

class Form(FlaskForm):
    start = SelectField('start', choices=[])
    finish = SelectField('finish', choices=[])

@app.route('/', methods=['GET','POST'])
def home():
    form = Form()

    if request.method == 'POST' :
        start = i.tabAdj
        finish = i.tabAdj
        return '<h1>Start : {}, Finish : {}</h1>'.format(start, finish)
    return render_template('home.html',form = form)

app.run()