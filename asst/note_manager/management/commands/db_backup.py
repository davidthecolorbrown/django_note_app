# db_backup.py
# django management command
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
        # use django-dbbackup module to backup database in '/var/backups/'
        management.call_command('dbbackup')
        # get time 
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)