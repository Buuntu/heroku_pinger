from apscheduler.schedulers.blocking import BlockingScheduler
import os
import requests
import sys

sched = BlockingScheduler()

if(not 'PING_HOST' in os.environ):
    sys.exit('PING_HOST environment variable is not set')

hostname = os.environ['PING_HOST']

@sched.scheduled_job('interval', minutes=28)
def timed_job():
    response = requests.get(hostname)

    #and then check the response...
    if response.status_code == 200:
        print(hostname, 'is up!')
    else:
        print(hostname, 'is down!')

sched.start()

