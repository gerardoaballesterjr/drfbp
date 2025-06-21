# drfbp

**drfbp** (Django REST Framework Boilerplate) is a Django app that provides powerful management commands to automate the repetitive, low-level setup needed for building APIs with Django and Django REST Framework. It is built to scale with your project — whether you're scaffolding a CRUD API, generating serializers, or extending your workflow with custom utilities.

> ⚡ Speed up your development. <br>
> 🧱 Build smarter, not harder. <br>
> 🧰 One toolbox, many commands. <br>

## ✨ Features

- ✅ Command-based interface — Easily extendable via Django management commands
- 🔧 Boilerplate generation — Generate views, serializers, permissions, and routers in seconds
- ⚙️ Formatted out of the box — Auto-formats with black and isort
  -🧩 DRF-ready — Designed for use with Django REST Framework
- 💼 Project-friendly — Clean, modular output that fits real-world project structures
- 📦 Installation
  Install from PyPI:

```bash
pip install drfbp
```

Or install locally for development:

```bash
pip install -e .
```

## ⚙️ Setup

To enable the included management commands, add drfbp to your Django project's INSTALLED_APPS:

```python
# settings.py

INSTALLED_APPS = [
    ...
    "drfbp",
]
```

## 🛠 Available Commands

📌 `crud` — Generate REST API boilerplate for a Django model
Scaffolds the full API structure for any registered model, including views, serializers, permissions, and routes.

### 🔄 Usage

```bash
python manage.py crud <app> <model> <path>
```

- `app`: Django app label containing the model.
- `model`: Model class name.
- `path`: Output directory for the generated files.

### 💡 Example

```bash
python manage.py crud blog post api/blog/post
```

This generates:

- `api/blog/post/serializers.py`
- `api/blog/post/views.py`
- `api/blog/post/permissions.py`
- `api/blog/post/urls.py`

All files are import-ready and formatted with isort and black.

## 📁 Output Overview

| File             | Description                   |
| ---------------- | ----------------------------- |
| `serializers.py` | DRF ModelSerializer           |
| `views.py`       | DRF ModelViewSet              |
| `permissions.py` | Customizable permission class |
| `urls.py`        | Router-based URL config       |

## 🔧 Requirements

- Python 3.7+
- Django 3.2+
- Django REST Framework

## 🤝 Contributing

New command ideas, fixes, or improvements are always welcome.

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

Please follow Django and Python community conventions.

## 🪪 License

MIT License. See [LICENSE](!github.com/gerardoaballesterjr/drfbp/blob/main/LICENSE.txt) for more details.

## 💡 Inspiration

Born from the need to automate boilerplate in production projects, drfbp aims to give Django developers more time for logic, less time spent on setup.
