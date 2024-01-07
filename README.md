![GitHub watchers](https://img.shields.io/github/watchers/ny-daystar/dexia)
![GitHub forks](https://img.shields.io/github/forks/ny-daystar/dexia)
![GitHub Repo stars](https://img.shields.io/github/stars/ny-daystar/dexia)
![GitHub repo size](https://img.shields.io/github/repo-size/ny-daystar/dexia)
![GitHub language count](https://img.shields.io/github/languages/count/ny-daystar/dexia)
![GitHub top language](https://img.shields.io/github/languages/top/ny-daystar/dexia) <a href="https://codeclimate.com/github/ny-daystar/dexia/maintainability"><img src="https://api.codeclimate.com/v1/badges/715c6f3ffb08de5ca621/maintainability" /></a>  
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/m/ny-daystar/dexia/newArchitecture)
![GitHub issues](https://img.shields.io/github/issues/ny-daystar/dexia)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/ny-daystar/dexia)
![GitHub](https://img.shields.io/github/license/ny-daystar/dexia)
[![All Contributors](https://img.shields.io/badge/all_contributors-1-blue.svg?style=circular)](#contributors)

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)

# Dexia

Python scraper and api to fetch data about Formula 1 Calendar

**Version: 1.0.0**

## Summary

-   [Api routes](#api-routes)
-   [Requirements](#requirements)
-   [Get started](#get-started)
-   [OpenAPI](#openapi)
-   [How it works](#how-it-works)
-   [Get access to GSheet file](#generate-file-id)
-   [Unit tests](#tests)
-   [Docker setup Dexia](#docker-setup-dexia)
    -   [Dexia API](#app-api)
-   [Create Executable](#create-executable)
-   [Formatting](#formatting)
-   [Credits](#credits)

## Api routes

-   [Version of application](http://localhost:8080/swagger)

## Requirements

-   [Python](https://www.python.org/) >= 3.11.4
-   [Docker](https://docs.docker.com/desktop/linux/install/ubuntu/) >= 20.10
-   [Docker-compose](https://docs.docker.com/compose/install/) >= v2.12.2

## Get started

If you don't have python

```bash
$ [sudo] apt-get install python3
$ pip install virtualenv
```

1. Clone repository

```bash
git clone git@github.com:NY-Daystar/Dexia.git
```

2. Go into repository

```bash
cd Dexia
```

3. Setup virtual environment
   On Linux

```bash
virtualenv -p 3 .venv
```

On Windows

```bash
python -m venv .venv
```

4. Activate virtual environment
   On Linux

```bash
source .venv/bin/activate
```

On Windows

```bash
source .venv/Scripts/activate
```

5. Install dependencies

```bash
pip install -r requirements.txt
```

5. Create configuration file

```bash
cp config.example.json config.json
```

5. Execute python application

```bash
$  python .
```

## OpenAPI

OpenAPI is format by `swagger`.  
To access to OpenAPI Swagger:  
Go to the `localhost:8080/swagger` endpoint to get swagger access.

## How it works

The application scrap french website who gets data about formula 1 calendar
Serialize them in json files (default path: `./contents`)
Then api use this json file to generate REST collections (`Calendar`, `Grand Prix`, `Events`, ...)

## Tests

To execute production tests

```bash
python -m unittest -v
```

```bash
pytest
```

To execute all of unit tests

## Docker Setup Dexia

-   To restart app system

```bash
docker-compose build && docker-compose down && docker-compose up -d
```

-   Start API service then stop and show logs

```bash
$ docker-compose up -d api
$ docker-compose stop api
$ docker-compose logs -f api
```

### App API

Create file `config.json`

```json
{
	"debug": true,
	"scraper": true,
	"folder": "contents",
	"url": "https://f1i.autojournal.fr/calendrier-f1-2023-dates-horaires-grands-prix",
	"api": {
		"host": "127.0.0.1",
		"port": 8080
	}
}
```

-   `debug`: bool to activate debug logs
-   `scraper`: bool to activate or not the periodical scrapping
-   `folder`: folder where stored data scrapped
-   `url`: url where scrapping data
-   `api`: Define endpoint `host` and `port` for api listening

## Create executable

Module python used: pyinstaller

1. Execute this command

```bash
pyinstaller dexia.py
```

2. Then configure the folder `./dist/dexia`

    1. Add configuration file `config.json`

3. Zip the folder `./dist/dexia`

## Formatting

The source code is format with the [pep8 guidelines](https://peps.python.org/pep-0008/)  
The source code is validating by [pylint](https://pylint.pycqa.org/en/latest/)

### Credits

Made by Lucas NOGA.  
Licensed under GPLv3.
