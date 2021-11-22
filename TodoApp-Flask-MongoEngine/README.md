# To-Do-List

Implementado a partir del proyecto: https://github.com/prashant-shahi/ToDo-List-using-Flask-and-MongoDB
To-Do-List is mini-project made with Flask and MongoDB

## Built using :
```sh
	Flask : Python Based mini-Webframework
	MongoDB : Database Server
	Mongoengine : Database Connector ( For creating connectiong between MongoDB and Flask )
	HTML5 (jinja2) : For Form and Table
```

## Descargar e instalar el código del proyecto

Descarguese y descomprima el código de la carpeta moodle.

Navegue a través de un terminal a la carpeta TodoApp-Flask-MongoEngine.
```
> cd TodoApp-Flask-MongoEngine
```

Una vez dentro de la carpeta, se instalan las dependencias. Para ello debe crear un virtual environment de la siguiente manera:

```
[LINUX/MAC] > python3 -m venv venv
[WINDOWS] > py.exe -m venv env
```

Si no tiene instalado venv, Lo puede instalar de la siguiente manera:

```
[LINUX/MAC] > python3 -m pip install --user virtualenv
[WINDOWS] > py.exe -m pip install --user virtualenv
```

Una vez creado el virtual environment lo activamos para poder instalar las dependencias:

```
[LINUX/MAC] > source venv/bin/activate
[WINDOWS] > .\env\Scripts\activate
```

Instalamos las dependencias con pip:

```
> pip3 install -r requirements.txt 
```

## Ejecutar la aplicación

Debemos tener arrancado MongoDB. Dependiendo de cómo lo hayamos instalado arrancará solo al iniciar la máquina o tendremos que ir a ejecutar el programa "mongod" a la carpeta bin donde hayamos realizado la instalación.

```
[LINUX/MAC] > python3 app.py
[WINDOWS] > py.exe app.py

#Go to http://localhost:5000 with any of browsers and DONE !!
#To exit press Ctrl+C
```

