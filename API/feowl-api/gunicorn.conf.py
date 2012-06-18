from re import search
from os import getcwd

# Check for dev in path, dev will bind the port to 8001, live to 8000
if search('dev', getcwd()).group() == 'dev':
    port = '8001'
else:
    port = '8000'

bind = '127.0.0.1:' + port
backlog = 2048
logfile = '/var/log/gunicorn/gunicorn.log'
loglevel = 'info'

daemon = True

proc_name = 'gunicorn'
