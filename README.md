# CPSC 349 Project One

## Quickboard

Quickboard allows users to create simple lists about anything the think is worth sharing with the world. Users create subjects and list off things pertaining to that specific subject.


## Install

This project runs on a Docker container (Python 3) for easy use of downloading and installing Python dependencies. Download the latest, stable version of Docker Desktop for windows [here.](https://www.docker.com/products/docker-desktop)

* Download or clone the repo

* Extract folder

* Open the folder that is within the extracted folder in VS Code 

    * Example: `cpsc-349-project-one\cpsc-349-project-one`

Dev Container configuration file will be found and will automatically give you the option to "Reopen in Container" 

Docker Desktop - Filesharing notification will pop up
* Choose the "Share it" option

Open up terminal within VS Code to verify you have python and pip installed in the container

```
$ python --version
$ pip --version
```

Install project requirements

```
$ pip install -r requirements.txt
```

Run Flask app

```
$ export FLASK_APP=listo.py
$ flask run
```

Open browser and navigate to `http://127.0.0.1:5000/` to view project

## Team Members

[Presentation Video](https://youtu.be/az3ahisIBk4)
 
Team Member | Role | Github
------------ | ------------- | -------------
Antonio Lopez | Back-end | antonio-lopez
Javier Melendrez | Back-end | javimelendrez
Brianna Sharpe | Front-end | briannasharpe
Jose Alvarado | Front-end | Jalvarado115
