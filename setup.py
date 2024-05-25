from typing import Union
from setuptools import setup, find_packages


def get_version() -> Union[str, None]:
    with open("django_rpyc/__init__.py") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip("'")
setup(
    version=get_version(),
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'rpyc',
    ]
)