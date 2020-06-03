from flask import Flask, render_template, flash, request, url_for, redirect, send_from_directory, send_file
from wtforms import Form, TextField, TextAreaField, SubmitField
from controller import control
import os
app = Flask(__name__)
application = app
app.config.update(dict(
	Debug = True,
))
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
class Form(Form):
	name = TextField("name")
	organisation = TextField("organisation")
	phone = TextField("phone")
	email = TextField("email")
	message = TextAreaField("message")
	submit = SubmitField("submit")
@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template('index.html', index="active")
@app.route("/about", methods=['GET', 'POST'])
def about():
	return render_template('about.html', about="active")
@app.route("/zeesaa", methods=['GET', 'POST'])
def zeesaa():
	return render_template('zeesaa.html', zeesaa="active")
@app.route("/razitor", methods=['GET', 'POST'])
def razitor():
	return render_template('razitor.html', razitor="active")
@app.route("/contact", methods=['GET', 'POST'])
def contact():
	form = Form(request.form)
	if request.method == 'GET':
		return render_template('contacts.html', contact="active", form=form)
	else:
		name=request.form['name']
		organisation=request.form['organisation']
		phone=request.form['phone']
		email=request.form['email']
		message=request.form['message']
		control(name,organisation,phone,email,message)
	return render_template('contacts.html', contact="active", form=form, success=True)
@app.route("/blog", methods=['GET', 'POST'])
def blog():
	return render_template('coming-soon.html', blog="active")
@app.route("/blogpost", methods=['GET', 'POST'])
def blogpost():
	return render_template('blog-post.html', blog="active")
@app.route('/download')
def downloadFile ():
    path = "static/brochure.pdf"
    return send_file(path, as_attachment=True)
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4444))
    app.run(debug=True, host='0.0.0.0', port=port)