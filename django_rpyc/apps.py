import os
import importlib.util

from django.apps import AppConfig, apps
from django.conf import settings


class DjangoRpycConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_rpyc"

    def ready(self) -> None:
        """
        Executes code when the Django application is ready.

        This method is called when the Django application is fully loaded and ready to run.
        It loads the specified module for each app in the project, if the module exists.

        Reason being that the module may contain code that needs to be executed when the Django
        application is ready so that it does not require manual intervention by importing
        the module in the project's `__init__.py` file or corresponding app's `apps.py` ready method.

        Returns:
            None
        """
        DJANGO_RPYC_FILENAME = getattr(settings, "DJANGO_RPYC_FILENAME", "django_rpyc")

        for app in apps.get_app_configs():
            try:
                module_path = os.path.join(app.path, f"{DJANGO_RPYC_FILENAME}.py")

                if os.path.exists(module_path):
                    spec = importlib.util.spec_from_file_location(
                        f"{app.name}.{DJANGO_RPYC_FILENAME}", module_path
                    )
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

            except Exception as e:
                print(f"Failed to load {DJANGO_RPYC_FILENAME} from {app.name}: {e}")

        return super().ready()
