import logging
from rpyc.utils.server import ThreadedServer

from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = "Starts the RPyC server"

    def add_arguments(self, parser):
        parser.add_argument(
            "--port",
            type=int,
            default=getattr(settings, "DJANGO_RPYC_PORT", 18861),
            help="The port to start the RPyC server on",
        )

    def handle(self, *args, **options):
        from django_rpyc.server import DjangoRpycService

        logging.info("Starting RPyC server...")
        t = ThreadedServer(DjangoRpycService, port=options["port"])
        t.start()
