import json
import os
import webbrowser
import schedule
import subprocess
import time
import logging
import datetime

logging.basicConfig(filename='tasks.log', level=logging.INFO,format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def openApp(args, target_date=None):
    current_date = datetime.date.today()
    if target_date is not None and current_date != target_date:
        return
    try:
        subprocess.call(args)
        logging.info(f'Opened app "{args}"')
    except FileNotFoundError:
        logging.error(f'Could not open app "{args}"')


def openUrl(args, target_date=None):
    current_date = datetime.date.today()
    if target_date is not None and current_date != target_date:
        return
    try:
        webbrowser.open(args)
        logging.info(f'Opened URL "{args}"')
    except Exception as e:
        logging.error(f'Could not open URL "{args}": {e}')


def runCommand(args, target_date=None):
    current_date = datetime.date.today()
    if target_date is not None and current_date != target_date:
        return
    try:
        os.system(args)
        logging.info(f'Executed command "{args}"')
    except Exception as e:
        logging.error(f'Could not execute command "{args}": {e}')


def schedule_tasks():
    with open('tasks.json') as f:
        tasks = json.load(f)
        for task in tasks:
            task_name = task['task_name']
            Action = task['Action']
            args = task['args']
            schedule_obj = task['schedule']
            schedule_type = schedule_obj['type']
            
            # Get the function object based on its name
            function = globals().get(Action)

            # Schedule the task
            try:
                if schedule_type == 'daily':    
                    schedule_time = schedule_obj['time']
                    schedule.every().day.at(schedule_time).do(function, args)
                elif schedule_type == 'date':
                    schedule_time = schedule_obj['time']
                    schedule_date_time = datetime.datetime.strptime(schedule_obj['date'] + ' ' + schedule_obj['time'], '%Y-%m-%d %H:%M')
                    schedule.every().day.at(schedule_time).do(function, args, target_date=schedule_date_time.date())
                logging.info(
                    f'Scheduled task "{task_name}" to run at {schedule_time} ({schedule_type})')
            except Exception as e:
                logging.error(f'scheduling task "{task_name}": {e}')

    # Keep the scheduler running
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    schedule_tasks()
