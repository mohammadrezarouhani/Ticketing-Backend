from datetime import datetime as dt
from pathlib import Path


def profile_image_upload(instance,path):
    date=dt.now()
    date=dt.strftime(date,'%Y-%m-%D')
    return Path('profile')/date/path


def archive_file_upload(instance,path):
    date=dt.now()
    date=dt.strftime(date,'%Y-%m-%d')
    return Path('archive')/date/path


def message_file_upload(instance,path):
    date=dt.now()
    date=dt.strftime(date,'%Y-%m-%D')
    return Path('message')/date/path
