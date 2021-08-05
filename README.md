# get_pyrus_json.py python script

### Overview

This is a simple python script, which uses Pyrus API to download a task, a form or a catalog.
Two forms of the output are provided:
* JSON
* Human-readable (JSON in python pprint form).

Both forms are saved as *.json and *.txt format. You can use your preferred JSON viewer to analyze the result.
Author of this script uses JSON Formatter Chrome extension for that. (But remember to enable parsing of a local file 
in the settings)

###Script usage:
* Fill _**credentials.json**_ file with your Pyrus API credentials 
* Run script from its directory
    * To get the task #1234567 details in files _**t1234567.txt**_ and _**t1234567.json**_
        ```console
        $ python get_pyrus_json.py -t 1234567
        ```
        
        If ran with key `-v 3`, Pyrus API v3 is used
    
    * To get form #123456 details (similarly,  _**f123456.txt**_ and _**f123456.json**_ will be created).
        ```console
        $ python get_pyrus_json.py -f 123456
        ```

### Dependencies

This script uses pyrus-api - an official Python library from Pyrus. To install it simply type:
```console
pip install pyrus-api
```

Enjoy!
