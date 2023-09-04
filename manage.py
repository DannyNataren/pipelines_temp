#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from decouple import config


def main():
    LISTA_ENTORNOS_VALIDOS = ["local", "tester", "prod"]
    ENTORNO = config("ENVIRONMENT")

    try:
        if ENTORNO not in LISTA_ENTORNOS_VALIDOS:
            raise ValueError(
                f"El entorno '{ENTORNO}' no es válido. Debe ser uno de: {', '.join(LISTA_ENTORNOS_VALIDOS)}")

        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pipelines_backend.settings.' + ENTORNO)
    except ValueError as e:
        print(f"Error: {e}")

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
    main()
