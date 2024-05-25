import logging
from typing import Type, Callable, Optional, Any

from .server import DjangoRpycService


def register(name: Optional[Any] = None) -> Callable[[Type], Type]:
    """
    Decorator function used to register a service in Django Rpyc.

    Args:
        name (Optional[Any]): The name of the service. If not provided, the name will be derived from the class name.

    Returns:
        Callable[[Type], Type]: The decorator function.

    Example:
    ```
        @register("my_service")
        class MyService:
            pass
    ```
        This will register the service with the name `my_service`.

    ```
        @register
        class MyService:
            pass
    ```

        This will register the service with the name `myservice`.
    """

    logging.info(f"Registering service {name}")

    def decorator(service: Type) -> Type:
        nonlocal name

        if callable(name):
            name = service.__name__.lower()

        logging.info(f"Registered: Name: {name}, Class: {service.__name__}")

        DjangoRpycService.add_service(name, service)
        print(f"Registered: Name: {name}, Class: {service.__name__}")

        return service

    return decorator if not callable(name) else decorator(name)
