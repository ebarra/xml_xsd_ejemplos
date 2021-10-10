from flask import Flask, render_template,request,redirect,url_for # For flask implementation
from pymongo import MongoClient # Database connector
from bson.objectid import ObjectId # For ObjectId to work
from bson.errors import InvalidId # For catching InvalidId exception for ObjectId
import os

mongodb_host = 'localhost'
mongodb_port = 27017
#Configure the connection to the database
client = MongoClient(mongodb_host, mongodb_port)
#Select the database
db = client.todosborrar
#Select the collection
todos = db.todos 

app = Flask(__name__)
title = "TODO with Flask"
heading = "ToDo Reminder"

def redirect_url():
	return request.args.get('next') or request.referrer or url_for('index')

@app.route("/")
@app.route("/todos")
def lists ():
	#Display the all Tasks
	todos_l = todos.find()
	a1="active"
	return render_template('index.html',a1=a1,todos=todos_l,t=title,h=heading)

@app.route("/todos/uncompleted")
def tasks ():
	todos_l = todos.find({"done":"no"})
	a2="active"
	return render_template('index.html',a2=a2,todos=todos_l,t=title,h=heading)


@app.route("/todos/completed")
def completed ():
	todos_l = todos.find({"done":"yes"})
	a3="active"
	return render_template('index.html',a3=a3,todos=todos_l,t=title,h=heading)

@app.route("/todos/<todo_id>/done")
def done (todo_id):
	#Done-or-not ICON
	task=todos.find({"_id":ObjectId(todo_id)})
	if(task[0]["done"]=="yes"):
		todos.update({"_id":ObjectId(todo_id)}, {"$set": {"done":"no"}})
	else:
		todos.update({"_id":ObjectId(todo_id)}, {"$set": {"done":"yes"}})
	redir=redirect_url()	# Re-directed URL i.e. PREVIOUS URL from where it came into this one
	return redirect(redir)


@app.route("/todos", methods=['POST'])
def create ():
	#Adding a Task
	name=request.values.get("name")
	desc=request.values.get("desc")
	date=request.values.get("date")
	pr=request.values.get("pr")
	todos.insert({ "name":name, "desc":desc, "date":date, "pr":pr, "done":"no"})
	return redirect("/")

@app.route("/todos/<todo_id>/delete")
def remove (todo_id):
	todos.remove({"_id":ObjectId(todo_id)})
	return redirect("/")

@app.route("/todos/<todo_id>/update",methods=['GET'])
def get_update_form (todo_id):
	task=todos.find_one({"_id":ObjectId(todo_id)})
	return render_template('update.html',task=task,h=heading,t=title)

@app.route("/todos/<todo_id>/update", methods=['POST','PUT'])
def update_todo (todo_id):
	name=request.values.get("name")
	desc=request.values.get("desc")
	date=request.values.get("date")
	pr=request.values.get("pr")
	todos.update({"_id":ObjectId(todo_id)}, {'$set':{ "name":name, "desc":desc, "date":date, "pr":pr }})
	return redirect("/")

@app.route("/search", methods=['GET'])
def search():
	searchfield=request.values.get("searchfield")
	searchvalue=request.values.get("searchvalue")
	todos_l = todos.find({searchfield:searchvalue})
	a1="active"
	return render_template('index.html',a1=a1,todos=todos_l,searchfield=searchfield,searchvalue=searchvalue,t=title,h=heading)

@app.route("/about")
def about():
	return render_template('credits.html',t=title,h=heading)

if __name__ == "__main__":
	env = 'development'
	port = 5000
	app.run(host='0.0.0.0', port=port, debug=True)
