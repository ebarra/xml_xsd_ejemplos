from flask import Flask, render_template,request,redirect,url_for
from flask_mongoengine import MongoEngine
import logging
from pymongo import monitoring

#Logs mongoengine
log = logging.getLogger()
log.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG)

class CommandLogger(monitoring.CommandListener):

    def started(self, event):
        log.debug("Command {0.command_name} with request id "
                 "{0.request_id} started on server "
                 "{0.connection_id}".format(event))

    def succeeded(self, event):
        log.debug("Command {0.command_name} with request id "
                 "{0.request_id} on server {0.connection_id} "
                 "succeeded in {0.duration_micros} "
                 "microseconds".format(event))

    def failed(self, event):
        log.debug("Command {0.command_name} with request id "
                 "{0.request_id} on server {0.connection_id} "
                 "failed in {0.duration_micros} "
                 "microseconds".format(event))

monitoring.register(CommandLogger())

app = Flask(__name__)
title = "TODO with Flask"
heading = "ToDo Reminder MongoEngine"
app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost/todos'
}

db = MongoEngine()
db.init_app(app)

import model


def redirect_url():
	return request.args.get('next') or request.referrer or url_for('index')

@app.route("/")
@app.route("/todos")
def list_all ():
	#Display all the Tasks
	todos_l = model.Todo.objects.all()
	a1="active"
	return render_template('index.html',a1=a1,todos=todos_l,t=title,h=heading)

@app.route("/todos/uncompleted")
def list_uncompleted ():
	#Display the Uncompleted Tasks
	todos_l = model.Todo.objects(done="no")
	a2="active"
	return render_template('index.html',a2=a2,todos=todos_l,t=title,h=heading)


@app.route("/todos/completed")
def list_completed ():
	#Display the Completed Tasks
	todos_l = model.Todo.objects(done="yes")
	a3="active"
	return render_template('index.html',a3=a3,todos=todos_l,t=title,h=heading)

@app.route("/todos/<todo_id>/done")
def mark_done (todo_id):
	#Done-or-not ICON
	task=model.Todo.objects.get(id=todo_id)
	if(task.done=="yes"):
		task.done="no"
	else:
		task.done="yes"
	task.save()
	redir=redirect_url()	# Re-directed URL i.e. PREVIOUS URL from where it came into this one
	return redirect(redir)


@app.route("/todos", methods=['POST'])
def create ():
	#Adding a Task
	name=request.values.get("name")
	desc=request.values.get("desc")
	date=request.values.get("date")
	pr=request.values.get("pr")
		
	new_todo = model.Todo(name=name, desc=desc, date=date,pr=pr,done="no")
	new_todo.save()
	return redirect("/todos")


@app.route("/todos/<todo_id>/delete")
def remove (todo_id):
	#Deleting a Task with various references
	task = model.Todo.objects.get(id=todo_id)
	task.delete()
	return redirect("/")

@app.route("/todos/<todo_id>/update")
def get_update_form (todo_id):
	task = model.Todo.objects.get(id=todo_id)
	return render_template('update.html',task=task,h=heading,t=title)

@app.route("/todos/<todo_id>/update", methods=['POST'])
def update (todo_id):
	#Updating a Task with various references
	task = model.Todo.objects.get(id=todo_id)
	task.name=request.values.get("name")
	task.desc=request.values.get("desc")
	task.date=request.values.get("date")
	task.pr=request.values.get("pr")
	task.save()
	return redirect("/")


@app.route("/search")
def search():
	searchfield=request.values.get("searchfield")
	searchvalue=request.values.get("searchvalue")
	todos_l=model.Todo.objects(__raw__={searchfield:searchvalue})
	a1="active"
	return render_template('index.html',a1=a1,todos=todos_l,searchfield=searchfield,searchvalue=searchvalue,t=title,h=heading)


@app.route("/about")
def about():
	return render_template('credits.html',t=title,h=heading)

if __name__ == "__main__":
	env = 'development'
	port = 5000
	app.run(host='0.0.0.0', port=port, debug=True)
