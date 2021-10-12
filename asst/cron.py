# cron.py 
# backup database for project by calling 'dbbackup' twice per day (@6AM and @6PM)
import os
from django.core import management
from django.conf import settings
#from django_cron import CronJobBase, Schedule

'''
# class for executing backups (cronjobs)
class Backup(CronJobBase):
#class Backup():
    # 
    #management.call_command('dbbackup')

    # set runtimes and schedule job 
    RUN_AT_TIMES = ['6:00', '18:00']
    #RUN_AT_TIMES = ['10:55', '11:00']
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    
    #RUN_EVERY_MINS = 1 # every minute 
    #schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    
    # name of the app and cronjob class to call
    code = 'asst.Backup'

    # use django management() to call 'dbbackup' command 
    def do(self):
        management.call_command('dbbackup')
'''

# class for executing backups (cronjobs)
#class Backup():
    # 
    #management.call_command('dbbackup')
    management.call_command('db_backup')




# function executing backups (cronjobs)
def backup():
    # 
    #management.call_command('dbbackup')
    management.call_command('db_backup')
