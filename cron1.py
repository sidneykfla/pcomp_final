from crontab import CronTab
cron = CronTab(user='pi')
job = cron.new(command="python3 /home/pi/final/decrement.py")
job.minute.every(15)

cron.write()
