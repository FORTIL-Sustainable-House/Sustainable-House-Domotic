# Sustainable-House-Server

First version of the software for the Sustainable House domotic oriented project.
Information about the project will be added as development goes.

# INSTALLATION

Install python 3 and Pip
Execute the command here to get all resources required for execution.

```pip3 install -r requirement.txt```

Set the environment variable to instruct to flask which application you plan to run :

```export FLASK_APP=SusHouse_v1.py```

To setup the database, run the following lines :

```flask db init```

```flask db migrate```

```flask db upgrade```

Then to run the application proper  :

```flask run```
