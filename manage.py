#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main(env):
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'chuthe.settings.{env}')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    envs = ["PROD", "STAGING", "DEV", "LOCAL"]

    env = os.getenv("CHUTHE_ENV")
    if env:
        main(env.lower())
    else:
        raise EnvironmentError("PLEASE EXPORT YOUR ENV: {envs}")
