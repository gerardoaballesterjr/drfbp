import os

from django import apps
from django.core import management


class Command(management.base.BaseCommand):
    def add_arguments(self, parser) -> None:
        parser.add_argument("app", type=str)
        parser.add_argument("model", type=str)
        parser.add_argument("path", type=str)

    def handle(self, *args, **options) -> None:
        self.app: str = options.get("app")
        self.model: str = options.get("model")
        self.path: str = options.get("path")

        self.setmodel()
        self.model_name = self.model.__name__
        self.meta_model_name = self.model._meta.model_name
        self.mkdirs()

        self.create_serializers()
        self.create_permissions()
        self.create_urls()
        self.create_views()

        os.system(f"isort {self.abspath}")
        os.system(f"black {self.abspath}")

    def setmodel(self) -> None:
        try:
            self.model = apps.apps.get_model(self.app, self.model)
        except LookupError as exception:
            raise management.base.CommandError(str(exception))

    def mkdirs(self) -> None:
        self.abspath: str = os.path.abspath(self.path)
        if os.path.exists(self.abspath) and os.listdir(self.abspath):
            raise management.base.CommandError(
                f"The directory '{self.abspath}' already exists and is not empty. "
                "Please specify an empty directory or a new path."
            )
        os.makedirs(self.abspath, exist_ok=True)
        open(os.path.join(self.abspath, "__init__.py"), "w").close()

    def create_serializers(self) -> None:
        with open(os.path.join(self.abspath, "serializers.py"), "w") as file:
            file.write(
                f"from rest_framework import serializers\n"
                f"from {self.app} import models\n"
                f"class {self.model_name}ModelSerializer(serializers.ModelSerializer):\n"
                f"\tclass Meta:\n"
                f"\t\tmodel = models.{self.model_name}\n"
                f"\t\texclude = []\n"
                f"\t\tread_only_fields = []\n"
            )

    def create_permissions(self) -> None:
        with open(os.path.join(self.abspath, "permissions.py"), "w") as file:
            file.write(
                f"from rest_framework import permissions\n"
                f"class {self.model_name}BasePermission(permissions.BasePermission):\n"
                f"\tdef has_permission(self, request, view):\n"
                f"\t\treturn True\n"
            )

    def create_urls(self) -> None:
        with open(os.path.join(self.abspath, "urls.py"), "w") as file:
            file.write(
                f"from django import urls\n"
                f"from rest_framework import routers\n"
                f"from {self.path.replace(os.sep, ".")} import views\n"
                f"router = routers.DefaultRouter()\n"
                f"router.register(r'', views.{self.model_name}ModelViewSet, basename='{self.meta_model_name}')\n"
                f"urlpatterns = [urls.path('', urls.include(router.urls)),]\n"
            )

    def create_views(self) -> None:
        with open(os.path.join(self.abspath, "views.py"), "w") as file:
            file.write(
                f"from rest_framework import permissions, viewsets\n"
                f"from {self.app} import models\n"
                f"from {self.path.replace(os.sep, ".")}.permissions import {self.model_name}BasePermission\n"
                f"from {self.path.replace(os.sep, ".")}.serializers import {self.model_name}ModelSerializer\n"
                f"class {self.model_name}ModelViewSet(viewsets.ModelViewSet):\n"
                f"\tqueryset = models.{self.model_name}.objects.all()\n"
                f"\tserializer_class = {self.model_name}ModelSerializer\n"
                f"\tpermission_classes = [permissions.IsAuthenticated, {self.model_name}BasePermission]\n"
                f"\thttp_method_names = ['get', 'post', 'put', 'delete']\n"
                f"\tlookup_field = 'id'\n"
                f"\tdef get_queryset(self):\n"
                f"\t\treturn super().get_queryset()\n"
            )
