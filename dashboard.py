from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'de26a2ccabac416b0cc068d4051cee04'


posts = [
    {
        'author': 'Konti Tester',
        'title': 'Blog Post 1',
        'content': 'post content',
        'date_posted': "yesterday"
    },
    {
        'author': 'Konti Tester 2',
        'title': 'Blog Post 2',
        'content': 'more content',
        'date_posted': "yesterday"

    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'testing@test.com' and form.password.data == 'testpassword':
            flash('You  have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)

