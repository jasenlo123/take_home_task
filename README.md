# CS162 Web Application
Hi Prof Stern, this is a blog-dashboard web application built in Flask, with CSS help from Bootstrap, and a sqlite database. Basic CRUD methods for blog posts are available for the user. 

### Additional Features
- Authenticating as an admin or a member user with log-in and log-out functionality. Admin can update or delete all posts, while members can only update or delete their own posts. No register new user feature.

  - Admin Login:
  ```
      "email": "aranmu@example.com",
      "password": "helloworld",
  ```

  - Member Login:
  ```
      "email": "neanthal@example.com",
      "password": "worldhello",
  ```

### Repository Strucutre
Since I divided the application code into different modules such as ```forms.py```, ```routes.py```, and ```models.py```, I ran into circular import issues. For instance, when I tried to call the ```models.py``` module from ```app.py``` in the same folder, Python wouldn't be able to import ```app.py``` because Python names the running script ```__main__```. Thus, I structured the main application code in the ```dashboard``` folder as a package and a ```app.py``` initialisation script to prevent. The templates folder in the ```dashboard``` package contains the Jinja templates.

- Repo Tree
```
├── README.md
├── app.py
├── dashboard
│   ├── __init__.py
│   ├── dashboard.db
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── static
│   │   └── main.css
│   └── templates
│       ├── dashboard.html
│       ├── home.html
│       ├── layout.html
│       ├── login.html
│       ├── new_post.html
│       └── post.html
├── requirements.txt
├── test.py
└── user.json
```

### How To Run
```
$ python3.6 -m venv .venv 
$ source .venv/bin/activate
$ pip3 install -r requirements.txt
$ export FLASK_APP=app.py
$ flask run
```


### Unittests
1. Run unittest discover to find all tests:
```
python3 -m unittest discover test
```
