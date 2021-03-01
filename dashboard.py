from flask import Flask, render_template
app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)

