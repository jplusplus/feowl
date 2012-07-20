from re import search
from os import getcwd

# Check for dev in path, dev will bind the port to 8001, live to 8000
seaching_path = 'dev'
if search(seaching_path, getcwd()).group() == seaching_path:
    port = '8001'
    logfile = '/var/log/gunicorn/gunicorn-%s.log' % seaching_path
    proc_name = 'gunicorn-%s' % seaching_path
else:
    port = '8000'
    logfile = '/var/log/gunicorn/gunicorn.log'

bind = '127.0.0.1:' + port
backlog = 2048
loglevel = 'info'

daemon = True
