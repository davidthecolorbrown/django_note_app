# cron.py 
# backup database for project by calling 'dbbackup' twice per day (@6AM and @6PM)
import os
from django.core import management
from django.conf import settings

# function executing backups (cronjobs)
def backup():
    # call the management command 'db_backup' 
    management.call_command('db_backup')
