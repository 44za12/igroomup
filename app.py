from flask import Flask, render_template, flash, request, url_for, redirect, send_from_directory, send_file
from wtforms import Form, TextField, SelectField, SubmitField
from controller import control
app = Flask(__name__)
application = app
app.config.update(dict(
	Debug = True,
))
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
class Form(Form):
	company = TextField("company")
	name = TextField("name")
	email = TextField("email")
	role = SelectField("role")
	jobtype = SelectField("jobtype")
	submit = SubmitField("submit")
@app.route("/", methods=['GET', 'POST'])
def index():
	form = Form(request.form)
	if request.method == 'GET':
		return render_template('index.html', index="active", form=form)
	else:
		company=request.form['company']
		name=request.form['name']
		email=request.form['email']
		role=request.form['role']
		jobtype=request.form['jobtype']
		control(company,name,email,role,jobtype)
		return render_template('index.html', form=form,index="active", success=True)
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
	return render_template('contacts.html', contact="active")
@app.route("/blog", methods=['GET', 'POST'])
def blog():
	return render_template('blog.html', blog="active")
@app.route("/blogpost", methods=['GET', 'POST'])
def blogpost():
	return render_template('blog-post.html', blog="active")
@app.route('/download')
def downloadFile ():
    path = "brochure.pdf"
    return send_file(path, as_attachment=True)
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 4444))
    app.run(debug=True, host='0.0.0.0', port=port)