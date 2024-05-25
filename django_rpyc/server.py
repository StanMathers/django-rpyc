from typing import Dict, Type

import rpyc
from rpyc.utils.server import ThreadedServer


class DjangoRpycService(rpyc.Service):
    """
    A class that represents a Django Rpyc Service.

    This class extends the `rpyc.Service` class and provides methods for adding services,
    getting service names, and using a specific service.

    Attributes:
        MAPPING (Dict[str, Type[rpyc.Service]]): A dictionary that maps service names to their corresponding service classes.
    """

    MAPPING: Dict[str, Type[rpyc.Service]] = {}

    @classmethod
    def add_service(cls, name: str, service: Type[rpyc.Service]):
        """
        Adds a service to the mapping.

        Args:
            name (str): The name of the service.
            service (Type[rpyc.Service]): The service class.

        Returns:
            Type[rpyc.Service]: The added service class.
        """
        cls.MAPPING[name] = service
        return service

    def exposed_get_service_names(self):
        """
        Returns a list of service names.

        Returns:
            List[str]: A list of service names.
        """
        return list(self.MAPPING.keys())

    def exposed_use(self, name: str):
        """
        Uses a specific service.

        Args:
            name (str): The name of the service to use.

        Returns:
            rpyc.Service: An instance of the specified service.

        Raises:
            ValueError: If the specified service is not found in the mapping.
        """
        if name not in self.MAPPING:
            raise ValueError(f"Service {name} not found")
        return self.MAPPING[name]()
