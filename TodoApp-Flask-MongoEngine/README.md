# To-Do-List

Implementado a partir del proyecto: https://github.com/prashant-shahi/ToDo-List-using-Flask-and-MongoDB
To-Do-List is mini-project made with Flask and MongoDB

## Built using :
```sh
	Flask : Python Based mini-Webframework
	MongoDB : Database Server
	Pymongo : Database Connector ( For creating connectiong between MongoDB and Flask )
	HTML5 (jinja2) : For Form and Table
```

## Set up environment for using this repo:
```
Install Python ( If you don't have already )
	$ sudo apt-get install python

Install MongoDB ( Make sure you install it properly )
	$ sudo apt install -y mongodb


Create virtual environment
	$ python3 -m virtualenv venv

Install dependecies:
	$ source venv/bin/activate


Install Dependencies of the application (Flask, Bson and PyMongo)
	$ pip install -r requirements.txt
```

## Run the application
```
Run MongoDB
1) Start MongoDB
	$ sudo service mongod start
2) Stop MongoDB
	$ sudo service mongod stop

Run the Flask file(app.py)
	$ python app.py

Go to http://localhost:5000 with any of browsers and DONE !!
	$ open http://localhost:5000

To exit press Ctrl+C
```

