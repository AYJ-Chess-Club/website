import os
import dotenv
from pathlib import Path
from django.contrib.messages import constants as messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Find and load .env file
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("django_secret")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["0.0.0.0", "127.0.0.1", "localhost"]


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "app",
    "members",
    "ckeditor",
    "comment",
    "martor",
]

# Comments
COMMENT_ALLOW_ANONYMOUS = False


# Martor config
MARTOR_ENABLE_CONFIGS = {
    "emoji": "true",  # to enable/disable emoji icons.
    "imgur": "false",  # to enable/disable imgur/custom uploader.
    "mention": "true",  # to enable/disable mention
    "jquery": "true",  # to include/revoke jquery (require for admin default django)
    "living": "true",  # to enable/disable live updates in preview
    "spellcheck": "true",  # to enable/disable spellcheck in form textareas
    "hljs": "true",  # to enable/disable hljs highlighting in preview
}

MARTOR_TOOLBAR_BUTTONS = [
    "bold",
    "italic",
    "horizontal",
    "heading",
    "pre-code",
    "blockquote",
    "unordered-list",
    "ordered-list",
    "link",
    "image-link",
    "image-upload",
    "direct-mention",
    "toggle-maximize",
]


# MARTOR_MARKDOWN_BASE_EMOJI_URL = 'https://www.webfx.com/tools/emoji-cheat-sheet/graphics/emojis/'
MARTOR_MARKDOWN_BASE_MENTION_URL = (
    "https://ayjchess.pythonanywhere.com/members/profile/"
)

MARTOR_MARKDOWN_EXTENSIONS = [
    "markdown.extensions.extra",
    "markdown.extensions.nl2br",
    "markdown.extensions.smarty",
    "markdown.extensions.fenced_code",
    # Custom markdown extensions.
    "martor.extensions.urlize",
    "martor.extensions.del_ins",  # ~~strikethrough~~ and ++underscores++
    "martor.extensions.mention",  # to parse markdown mention
    "martor.extensions.emoji",  # to parse markdown emoji
    "martor.extensions.mdx_video",  # to parse embed/iframe video
    "martor.extensions.escape_html",  # to handle the XSS vulnerabilities
]

MARTOR_THEME = "semantic"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "chess_site.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "chess_site.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/Toronto"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles/")

# Django Messages
MESSAGE_TAGS = {
    messages.DEBUG: "alert-secondary",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# CKEDITOR
CKEDITOR_CONFIGS = {
    "default": {
        "allowedContent": True,
        "toolbar": "Custom",
        "toolbar_Custom": [
            ["Styles", "Format", "Font", "FontSize", "CodeSnippet"],
            [
                "Bold",
                "Italic",
                "Underline",
                "Strike",
                "-",
                "Undo",
                "Redo",
                "-",
                "Cut",
                "Copy",
                "Paste",
                "Find",
                "Replace",
                "-",
                "Outdent",
                "Indent",
                "-",
                "Print",
            ],
            [
                "NumberedList",
                "BulletedList",
                "-",
                "JustifyLeft",
                "JustifyCenter",
                "JustifyRight",
                "JustifyBlock",
            ],
            [
                "Image",
                "Table",
                "-",
                "Link",
                "Flash",
                "Smiley",
                "TextColor",
                "BGColor",
                "Source",
            ],
        ],
        "height": 600,
        "width": "auto",
        "extraPlugins": ",".join(["codesnippet"]),
    },
}

# SMTP
EMAIL_USE_TLS = True
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
MAILER_EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = "AYJ Chess Club <noreply@ayjchess.pythonanywhere.com>"

# AUTH
LOGIN_URL = "/members/login/"

# Admin settings

JAZZMIN_SETTINGS = {
    "site_title": "AYJ Chess Admin",
    "site_header": "AYJ Chess Admin",
    "welcome_sign": "Login",
    "site_logo": "AYJ_Chess_Logo.svg",
    "copyright": "AYJ Chess Club",
    "show_ui_builder": True,
    "topmenu_links": [
        {"name": "Back to Home",  "url": "home"},

        {"name": "Support", "url": "https://github.com/AYJ-Chess-Club/website#issues--support", "new_window": True},


        {"name": "Discord",  "url": "https://discord.gg/tvVD5baNth", "new_window": True},
    ],
    "search_model": "auth.User",
}



JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": True,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success",
    },
    "actions_sticky_top": False,
}
