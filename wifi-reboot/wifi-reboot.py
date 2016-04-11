#!/usr/bin/env python
# A script to reboot TP-LINK TL-MR3020, 3G Wireless N Router

import requests

import sys

from clint.textui import prompt, puts, colored, validators
from clint import arguments

args = arguments.Args()

s_message = 'Restarting...'

puts(colored.cyan('Reboot TP-LINK TL-MR3020, 3G Wireless N Router'))

def reboot():
    # GET http://100.100.100.1/userRpm/SysRebootRpm.htm

    try:
        response = requests.get(
            url="http://100.100.100.1/userRpm/SysRebootRpm.htm",
            params={
                "Reboot": "Rebbot",
            },
            auth=('admin', 'admin'),
        )
    except requests.exceptions.RequestException:
        puts(colored.red('HTTP Request failed, Router is not connected'))
        sys.exit()

    return response

if (args.get(0) == '-f'):
    force = True
else:
    force = prompt.yn(colored.yellow('Restart your Wi-Fi router ?'))

if force:
    puts(colored.magenta('Restaring your router'))
    status = reboot()
    # print status
    if s_message in status.text:
        puts(colored.green('Router is getting restarted, please wait ...'))
    else:
        puts(colored.red('Something is wrong, router is not restarted.'))
else:
    puts(colored.green('Restart aborted.'))
				
# send_request()
