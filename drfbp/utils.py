import os
import uuid


def uuid_generator():
    return uuid.uuid4().hex


def slug_generator(instance, slug=None):
    slug = slug if slug is not None else uuid_generator()
    if instance.__class__.objects.filter(slug=slug).exists():
        return slug_generator(instance, uuid_generator())
    return slug


def env(key: str, default: str = "") -> str:
    return os.environ.get(key, default)


def split(value: str, sep: str = ",") -> list:
    return list(filter(None, map(str.strip, value.split(sep))))
