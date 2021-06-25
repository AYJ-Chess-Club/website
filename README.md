# AYJ Chess Club site

<a href="">
  <img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/AYJ-Chess-Club/website/Build?logo=github&logoColor=949da5&style=plastic">
</a>
<a href="">
  <img alt="GitHub" src="https://img.shields.io/github/license/AYJ-Chess-Club/website?style=plastic">
</a>
<br>
<br>

A. Y. Jackson's Chess club website. Built using the Django framework with SQLite3 backend.

[Website](https://ayjchess.pythonanywhere.com)

## Getting started

### Using Python venv

Prerequisites:
- Python (3 is recommended)

Make a virtual environment

```shell
$ mkdir django-site && cd django-site
$ python -m venv venv
$ source venv/bin/activate
```

Clone the repo

```
$ git clone
$ cd
$ pip install -U -r requirements.txt
```

Add the following to the environmental variables file (`.env`). Make sure that you are in the project's root directory. 

```
django_secret=
```

Make migrations and run the server.

```
$ python manage.py makemigrations
$ python manage.py migrate
```

```
$ python manage.py runserver
```

View on [localhost:8000](http://localhost:8000) or [127.0.0.1:8000](http://127.0.0.1:8000) 

### Docker

Prerequisites:
- Docker
- Docker Compose

To run the Django app without installing anything (assuming you have the prerequisites):

```
$ sudo docker-compose up --build
```

View on [0.0.0.0:8000](http://0.0.0.0:8000)

## Contributing
Contributions to this project are appreciated, feel free to make a pull request or open an issue should there be one. Please open the pull request against the `dev` branch. 

## License
This project is licensed under [MIT](https://opensource.org/licenses/MIT). See [LICENSE]() file for more details.