# what_time.py
# returns the current time when called at command line ('python manage.py what_time')
import os
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.core import management
from django.conf import settings
#from django.core.management import call_command

# 
class Command(BaseCommand):
    #
    help = 'Displays current time'

    #
    def handle(self, *args, **kwargs):
        management.call_command('dbbackup')
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)