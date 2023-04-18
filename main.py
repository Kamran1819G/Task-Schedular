# import csv
import json
import os
import webbrowser
import schedule
import subprocess
import time
import logging


def open_app(args):
    try:
        subprocess.call([args])
    except FileNotFoundError:
        print(f'Could not find the file "{args}"')


def open_url(args):
    try:
        webbrowser.open(args)
    except Exception as e:
        print(f'Could not open URL "{args}"')


def run_command(args):
    os.system(args)


# def schedule_tasks():
#    with open('tasks.csv') as f:
#        reader = csv.DictReader(f)
#        for row in reader:
#            task_name = row['task_name']
#            function_name = row['function']
#            args = row['args']
#            schedule_str = row['schedule']
#
#            # Get the function object based on its name
#            function = globals().get(function_name)
#
#            # Schedule the task
#            schedule.every().day.at(schedule_str).do(function, args)
#            print(f'Scheduled task "{task_name}" to run at {schedule_str}')


def schedule_tasks():
    with open('tasks.json') as f:
        tasks = json.load(f)
        for task in tasks:
            task_name = task['task_name']
            function_name = task['function']
            args = task['args']
            schedule_str = task['schedule']

            # Get the function object based on its name
            function = globals().get(function_name)

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
