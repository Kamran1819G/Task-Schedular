import json
import os
import webbrowser
import schedule
import subprocess
import time
import logging
import datetime

# Set up logging
logging.basicConfig(filename='tasks.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


def openApp(args, target_date=None):
    current_date = datetime.date.today()
    if target_date is not None and current_date != target_date:
        return
    try:
        path = args
        subprocess.call([path])
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