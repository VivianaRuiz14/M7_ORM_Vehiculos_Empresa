from typing import Any
from django.core.management.base import BaseCommand
from registro_conductores.services import *

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        print('agregando conductor')
        crear_conductor('pedro','perez', '2000-04-03')
       