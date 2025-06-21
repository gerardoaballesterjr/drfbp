import importlib
import os
import uuid

from django.conf import settings
from django.core import management


class Command(management.base.BaseCommand):
    def handle(self, *args, **options) -> None:
        self.path: str = importlib.import_module(
            os.environ.get("DJANGO_SETTINGS_MODULE")
        ).__file__

        self.update_settings()
        self.update_urls()

    def update_urls(self) -> None:
        self.url_path: str = importlib.import_module(settings.ROOT_URLCONF).__file__

        with open(self.url_path, "w") as file:
            file.write(
                f"from django import urls\n\n"
                f"from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView\n\n"
                f"urlpatterns = [\n\n"
                f'# urls.path("", urls.include("<YOUR_API_URL_PATH>")),\n\n'
                f'urls.path("docs/", SpectacularSwaggerView.as_view(url_name="schema")),\n\n'
                f'urls.path("schema/", SpectacularAPIView.as_view(), name="schema"),\n\n'
                f"]\n\n"
            )

        os.system(f"isort {self.url_path}")
        os.system(f"black {self.url_path}")

    def update_settings(self) -> None:
        with open(self.path, "w") as file:
            file.write(
                f"from pathlib import Path\n\n"
                f"from datetime import timedelta\n\n"
                f"from drfbp import utils\n\n"
                f"BASE_DIR = Path(__file__).resolve().parent.parent\n\n"
                f'SECRET_KEY = utils.env("SECRET_KEY", "{uuid.uuid4().hex}")\n\n'
                f'DEBUG = utils.env("DEBUG", "True").lower() == "true"\n\n'
                f'ALLOWED_HOSTS = utils.split(utils.env("ALLOWED_HOSTS", ""))\n\n'
                f'CORS_ALLOWED_ORIGINS = utils.split(utils.env("CORS_ALLOWED_ORIGINS", ""))\n\n'
                f"SECURE_HSTS_SECONDS = 3600\n\n"
                f"SECURE_HSTS_INCLUDE_SUBDOMAINS = True\n\n"
                f"SECURE_SSL_REDIRECT = not DEBUG\n\n"
                f"SESSION_COOKIE_SECURE = not DEBUG\n\n"
                f"CSRF_COOKIE_SECURE = not DEBUG\n\n"
                f"INSTALLED_APPS = [\n\n"
                f'"drfbp",\n\n'
                f'"django.contrib.auth",\n\n'
                f'"django.contrib.contenttypes",\n\n'
                f'"django.contrib.sessions",\n\n'
                f'"django.contrib.messages",\n\n'
                f'"django.contrib.staticfiles",\n\n'
                f'"rest_framework",\n\n'
                f'"rest_framework_simplejwt",\n\n'
                f'"rest_framework_simplejwt.token_blacklist",\n\n'
                f'"corsheaders",\n\n'
                f'"drf_spectacular",\n\n'
                f"]\n\n"
                f"REST_FRAMEWORK = {{\n\n"
                f'"DEFAULT_AUTHENTICATION_CLASSES": (\n\n'
                f'"rest_framework_simplejwt.authentication.JWTAuthentication",\n\n'
                f"),\n\n"
                f'"DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),\n\n'
                f'"DEFAULT_RENDERER_CLASSES": [\n\n'
                f'"rest_framework.renderers.JSONRenderer",\n\n'
                f"],\n\n"
                f'"DEFAULT_PARSER_CLASSES": [\n\n'
                f'"rest_framework.parsers.JSONParser",\n\n'
                f"],\n\n"
                f'"DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",\n\n'
                f"}}\n\n"
                f"SIMPLE_JWT = {{\n\n"
                f'"ACCESS_TOKEN_LIFETIME": timedelta(days=7),\n\n'
                f'"REFRESH_TOKEN_LIFETIME": timedelta(days=90),\n\n'
                f'"ROTATE_REFRESH_TOKENS": True,\n\n'
                f'"BLACKLIST_AFTER_ROTATION": True,\n\n'
                f'"UPDATE_LAST_LOGIN": False,\n\n'
                f'"TOKEN_OBTAIN_SERIALIZER": "<PATH_TO_YOUR_CUSTOM_OBTAIN_SERIALIZER>",\n\n'
                f'"USER_ID_FIELD": "id",\n\n'
                f'"USER_ID_CLAIM": "id",\n\n'
                f"}}\n\n"
                f"SPECTACULAR_SETTINGS = {{\n\n"
                f'"TITLE": "API Documentation",\n\n'
                f'"DESCRIPTION": "API Documentation",\n\n'
                f'"VERSION": "1.0.0",\n\n'
                f'"SERVE_INCLUDE_SCHEMA": False,\n\n'
                f'"COMPONENT_SPLIT_REQUEST": True,\n\n'
                f"}}\n\n"
                f"MIDDLEWARE = [\n\n"
                f'"django.middleware.security.SecurityMiddleware",\n\n'
                f'"whitenoise.middleware.WhiteNoiseMiddleware",\n\n'
                f'"django.contrib.sessions.middleware.SessionMiddleware",\n\n'
                f'"corsheaders.middleware.CorsMiddleware",\n\n'
                f'"django.middleware.common.CommonMiddleware",\n\n'
                f'"django.middleware.csrf.CsrfViewMiddleware",\n\n'
                f'"django.contrib.auth.middleware.AuthenticationMiddleware",\n\n'
                f'"django.contrib.messages.middleware.MessageMiddleware",\n\n'
                f'"django.middleware.clickjacking.XFrameOptionsMiddleware",\n\n'
                f"]\n\n"
                f'ROOT_URLCONF = "{settings.ROOT_URLCONF}"\n\n'
                f"TEMPLATES = [\n\n"
                f"{{\n\n"
                f'"BACKEND": "django.template.backends.django.DjangoTemplates",\n\n'
                f'"DIRS": [BASE_DIR / "templates"],\n\n'
                f'"APP_DIRS": True,\n\n'
                f'"OPTIONS": {{\n\n'
                f'"context_processors": [\n\n'
                f'"django.template.context_processors.request",\n\n'
                f'"django.contrib.auth.context_processors.auth",\n\n'
                f'"django.contrib.messages.context_processors.messages",\n\n'
                f"],\n\n"
                f"}},\n\n"
                f"}},\n\n"
                f"]\n\n"
                f'WSGI_APPLICATION = "{settings.WSGI_APPLICATION}"\n\n'
                f"DATABASES = {{\n\n"
                f'"default": {{\n\n'
                f'"ENGINE": "django.db.backends.postgresql",\n\n'
                f'"NAME": utils.env("NAME", ""),\n\n'
                f'"USER": utils.env("USER", ""),\n\n'
                f'"PASSWORD": utils.env("PASSWORD", ""),\n\n'
                f'"HOST": utils.env("HOST", ""),\n\n'
                f'"PORT": int(utils.env("PORT", "5432")),\n\n'
                f"}}\n\n"
                f"}}\n\n"
                f"AUTH_PASSWORD_VALIDATORS = [\n\n"
                f"{{\n\n"
                f'"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",\n\n'
                f"}},\n\n"
                f"{{\n\n"
                f'"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",\n\n'
                f"}},\n\n"
                f"{{\n\n"
                f'"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",\n\n'
                f"}},\n\n"
                f"{{\n\n"
                f'"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",\n\n'
                f"}},\n\n"
                f"]\n\n"
                f'LANGUAGE_CODE = "en-us"\n\n'
                f'TIME_ZONE = "UTC"\n\n'
                f"USE_I18N = True\n\n"
                f"USE_TZ = True\n\n"
                f'STATIC_URL = "staticfiles/"\n\n'
                f"if DEBUG:\n\n"
                f'\tSTATICFILES_DIRS = [BASE_DIR / "staticfiles"]\n\n'
                f"else:\n\n"
                f'\tSTATIC_ROOT = BASE_DIR / "staticfiles"\n\n'
                f'# AUTH_USER_MODEL = ""\n\n'
                f'EMAIL_HOST = utils.env("EMAIL_HOST", "")\n\n'
                f'EMAIL_HOST_USER = utils.env("EMAIL_HOST_USER", "")\n\n'
                f'EMAIL_HOST_PASSWORD = utils.env("EMAIL_HOST_PASSWORD", "")\n\n'
                f'EMAIL_PORT = int(utils.env("EMAIL_PORT", "587"))\n\n'
                f'EMAIL_USE_TLS = utils.env("EMAIL_USE_TLS", "True").lower() == "true"\n\n'
                f'EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"\n\n'
                f'DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"\n\n'
            )

        os.system(f"isort {self.path}")
        os.system(f"black {self.path}")
