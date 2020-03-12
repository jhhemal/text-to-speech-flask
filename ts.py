from flask import Flask, render_template, redirect, url_for
from forms import TextForm
from gtts import gTTS
import os
import subprocess, sys
app = Flask(__name__)
app.config['SECRET_KEY'] = '1a1f32e9c2d79fbc89fc61918235d0e5'

@app.route('/', methods=['GET','POST'])
def index():
    form = TextForm()
    text=None
    pt =None
    if form.validate_on_submit():
        text = form.text.data
        language = 'en'
        output = gTTS(text=text, lang=language, slow=False)
        output.save("static/output.mp3")
        form.text.data = ''
    return render_template('index.html', form=form, txt=text)

if __name__ == '__main__':
    app.run(debug=True)