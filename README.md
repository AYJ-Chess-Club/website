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

The following steps are **important**:

Comment out the `urls.py` and `views.py` files in `app/` and `members/`.

This is what is should look like.

views.py

```python
# from foo import bar
...
# class HomeView(ListView):
#     model = Announcement
#     template_name = "pages/home.html"
#     paginate_by = 5
#     query_set = Announcement.objects.all()
#     context_object_name = "announcements"
#     ordering = ["-announcement_date"]

...
```

urls.py

```python
# from foo import bar

urlpatterns = [
  # path("", HomeView.as_view(), name="home")
]
```

In addition, comment out this particular section in models.py

```python
class Lesson(models.Model):

    """
    comment this ↓
    """
    # difficulty_levels = lessonDifficulty.objects.all().values_list(
    #     "difficulty", "difficulty"
    # )

    # difficulty_levels_list = []

    # for difficulty in difficulty_levels:
    #     difficulty_levels_list.append(difficulty)

    """
    add this ↓
    """
    difficulty_levels = 0

    title = models.CharField(max_length=225)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=225, choices=difficulty_levels)
    body = RichTextField(blank=True, null=True)
    lesson_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + "-" + str(self.lesson_date) + "-" + str(self.author)

    def get_absolute_url(self):
        return reverse("home")
```

After that, you can make migrations.

```shell
$ python manage.py makemigrations
$ python manage.py migrate
```

Before uncommenting everything else, create a super user.

```shell
$ python manage.py createsuperuser
```

Run the server

```shell
$ python manage.py runserver
```

Then go into the admin interface and add in the lesson difficulties: "Beginner", "Intermediate", "Advanced". 

Then uncomment everything and run the server. Everything should work properly.

View on [localhost:8000](http://localhost:8000) or [127.0.0.1:8000](http://127.0.0.1:8000) 

### Docker

**Requires some configuring to make it work, refer to the steps above**

Prerequisites:
- Docker
- Docker Compose

To run the Django app without installing anything (assuming you have the prerequisites):

```
$ sudo docker-compose up --build
```

View on [0.0.0.0:8000](http://0.0.0.0:8000)

## Issues & Support
If you do run into trouble either setting it up, or using the [website](https://ayjchess.pythonanywhere.com) don't hesitate to open an issue. However, if you don't have a Github account, you can email <a href="mailto:liang.mike.to@gmail.com">@yak-fumblepack</a>.


## Contributing
Contributions to this project are appreciated, feel free to make a pull request or open an issue should there be one. Please open the pull request against the `dev` branch. 

## License
This project is licensed under [MIT](https://opensource.org/licenses/MIT). See [LICENSE]() file for more details.