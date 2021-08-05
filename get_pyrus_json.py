"""
This is a simple python script, which uses Pyrus API to download task, form or catalog.
Two forms of the output provided:
- JSON
- Human readable (JSON in python pprint form)

Script usage:

Fill credentials.json file with your Pyrus API credentials
Run script from its directory
To get the task #1234567 details in files t<task_id>.txt and t<task_id>.json

$ python get_pyrus_json.py -t 1234567
If ran with key -v 3, Pyrus API v3 is used

To get form #123456 details (similarly, t<task_id>.txt and t<task_id>.json will be created.

$ python get_pyrus_json.py -f 123456
Enjoy!
"""


import argparse
import pprint
import json
import logging
from pyrus import client

CONFIG = 'credentials.json'
logger = logging.getLogger("GetPyrusJSON")


def read_login_info():
    with open(CONFIG) as f:
        obj = json.loads(f.read())
    return obj['login'], obj['security_key']


def initialize():
    """
    Get login parameters, create pyrusAPI instance, make authorization and check for errors
    :return: pyrusAPI instance
    """
    login, token = read_login_info()

    pyrus_cli = client.PyrusAPI(login=login, security_key=token)
    logger.debug(f'Initializing Pyrus API')
    result = pyrus_cli.auth()
    if not result.success:
        logger.error(f'Error while logging in. Error description: {result.error}')
        exit(code=result.error_code)
    return pyrus_cli


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--task", action="store", help="id of a task to download", type=int)
    parser.add_argument("-f", "--form", action="store", help="id of a form to download", type=int)
    parser.add_argument("-c", "--catalog", action="store", help="id of a catalog to download", type=int)
    parser.add_argument("-v", "--version", action="store", help="API version to use", type=int)

    args = parser.parse_args()
    pyrus_client = initialize()

    if not args.task and not args.form and not args.catalog:
        print('use -h to get help\nuse either -f or -t or -c to get output')
        exit()
    elif args.task:
        if args.version == 3:
            print("Using v3!!")
            url = f"https://pyrus.com/restapi/v3/task/{args.task}"
        else:
            url = pyrus_client._create_url(f'/tasks/{args.task}')
        print(f'Pretty printing task {args.task}:\n==============================')
        filename = f"t{args.task}"
    elif args.form:
        url = pyrus_client._create_url(f'/forms/{args.form}')
        print(f'Pretty printing form {args.form}:\n==============================')
        filename = f"f{args.form}"
    else:
        url = pyrus_client._create_url(f'/catalogs/{args.catalog}')
        print(f'Pretty printing catalog {args.catalog}:\n==============================')
        filename = f"c{args.catalog}"
    response = pyrus_client._perform_get_request(url)
    pprint.pprint(response)
    with open(filename + ".txt", "w", encoding="utf-8") as f:
        pprint.pprint(response, f)
    with open(filename + ".json", "w", encoding="utf-8") as f:
        json.dump(response, f)
