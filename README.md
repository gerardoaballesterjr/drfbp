# drfbp

**drfbp** (Django REST Framework Boilerplate) is a Django app designed to streamline the development of REST APIs using Django and Django REST Framework. It provides powerful management commands to automate repetitive setup tasks, allowing developers to focus on core logic rather than boilerplate code.

> ⚡ Speed up your development. <br>
> 🧱 Build smarter, not harder. <br>
> 🧰 One toolbox, many commands. <br>

## ✨ Features

- ✅ **Command-based Interface**: Easily extendable via Django management commands.
- 🔧 **Boilerplate Generation**: Quickly generate views, serializers, permissions, and URL configurations for your API.
- ⚙️ **Automated Formatting**: Integrates with `black` and `isort` for consistent code style out of the box.
- 🧩 **DRF-Ready**: Specifically designed for seamless integration with Django REST Framework.
- 💼 **Project-Friendly Output**: Generates clean, modular code that fits well into real-world project structures.
- 🔒 **Secure Settings**: Provides a management command to set up secure Django settings, including JWT authentication, CORS, and database configurations.
- 📄 **API Documentation**: Automatically configures `drf-spectacular` for OpenAPI schema generation and Swagger UI documentation.

## 📦 Installation

Install from PyPI:

```bash
pip install drfbp
```

Or install locally for development:

```bash
pip install -e .
```

## ⚙️ Setup

To enable the included management commands, add `drfbp` to your Django project's `INSTALLED_APPS`:

```python
# settings.py

INSTALLED_APPS = [
    # ...
    "drfbp",
]
```

## 🛠 Available Commands

### 📌 `crud` — Generate REST API boilerplate for a Django model

This command scaffolds the full API structure for any registered Django model, including views, serializers, permissions, and URL routes.

#### 🔄 Usage

```bash
python manage.py crud <app> <model> <path>
```

- `app`: The Django app label containing the model (e.g., `blog`).
- `model`: The name of the model class (e.g., `Post`).
- `path`: The output directory for the generated API files (e.g., `api/blog/post`).

#### 💡 Example

```bash
python manage.py crud blog post api/blog/post
```

This command generates the following files:

- `api/blog/post/serializers.py`: A DRF `ModelSerializer` for the specified model.
- `api/blog/post/views.py`: A DRF `ModelViewSet` for handling CRUD operations.
- `api/blog/post/permissions.py`: A customizable `BasePermission` class.
- `api/blog/post/urls.py`: A router-based URL configuration for the API endpoint.

All generated files are import-ready and automatically formatted with `isort` and `black`.

### 📌 `settings` — Configure Django project settings and URL patterns

This command automates the setup of essential Django settings and URL configurations, including security, authentication, and API documentation.

#### 🔄 Usage

```bash
python manage.py settings
```

#### 💡 What it does:

- **Updates `settings.py`**:
  - Configures `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, `CORS_ALLOWED_ORIGINS` from environment variables.
  - Sets up security headers (`SECURE_HSTS_SECONDS`, `SECURE_HSTS_INCLUDE_SUBDOMAINS`, `SECURE_SSL_REDIRECT`, `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`).
  - Adds `drfbp`, `rest_framework`, `rest_framework_simplejwt`, `rest_framework_simplejwt.token_blacklist`, `corsheaders`, and `drf_spectacular` to `INSTALLED_APPS`.
  - Configures `REST_FRAMEWORK` defaults for authentication (JWT), permissions (IsAuthenticated), renderers (JSON), parsers (JSON), and schema class (`drf_spectacular`).
  - Sets up `SIMPLE_JWT` with token lifetimes, rotation, and blacklisting.
  - Configures `SPECTACULAR_SETTINGS` for API documentation title, description, and version.
  - Adds necessary middleware, including `SecurityMiddleware`, `WhiteNoiseMiddleware`, `CorsMiddleware`, and others.
  - Configures database settings for PostgreSQL using environment variables.
  - Sets up email backend settings from environment variables.
- **Updates `urls.py`**:
  - Includes `drf-spectacular` URLs for API schema (`/schema/`) and Swagger UI documentation (`/docs/`).
  - Provides a placeholder for your API's root URL path.

## 🔧 Requirements

- Python 3.7+
- Django 3.2+
- Django REST Framework
- `djangorestframework-simplejwt`
- `django-cors-headers`
- `drf-spectacular`
- `whitenoise` (for static files in production)
- `psycopg2-binary` (for PostgreSQL database)

## 🤝 Contributing

New command ideas, bug fixes, or improvements are always welcome.

1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

Please follow Django and Python community conventions.

## 🪪 License

MIT License. See [LICENSE.txt](LICENSE.txt) for more details.

## 💡 Inspiration

Born from the need to automate boilerplate in production projects, drfbp aims to give Django developers more time for logic, less time spent on setup.
