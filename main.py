import json
import os
import webbrowser
import schedule
import subprocess
import time
import logging

# Set up logging
logging.basicConfig(filename='tasks.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def openApp(args):
    try:
        path = args
        subprocess.call([path])
        logging.info(f'Opened app "{args}"')
    except FileNotFoundError:
        logging.error(f'Could not open app "{args}"')


def openUrl(args):
    try:
        webbrowser.open(args)
        logging.info(f'Opened URL "{args}"')
    except Exception as e:
        logging.error(f'Could not open URL "{args}": {e}')


def runCommand(args):
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
            schedule_str = task['schedule']

            # Get the function object based on its name
            function = globals().get(Action)

            # Schedule the task
            try:
                schedule.every().day.at(schedule_str).do(function, args)
                logging.info(
                    f'Scheduled task "{task_name}" to run at {schedule_str}')
            except Exception as e:
                logging.error(f'Error scheduling task "{task_name}": {e}')

    # Keep the scheduler running
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    schedule_tasks()
