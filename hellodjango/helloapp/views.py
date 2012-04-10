from django.template import Context, loader
import time
from django.http import HttpResponse

def hello_view(request):
    """ Simple Hello World View """
    t = loader.get_template('helloworld.html')
    c = Context({
        'current_time': time.time(),
    })
    return HttpResponse(t.render(c))
