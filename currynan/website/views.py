from django.shortcuts import render, render_to_response

from django.http import HttpResponse
from django.template import Context, loader, RequestContext
import utils
import time
# Create your views here.


def index(request):
#    t = loader.get_template('website/index.html')
#    c=Context({
#        'latest_poll_list': latest_poll_list,
#    })
#    return HttpResponse(t.render(c))
    return render_to_response('website/index.html',context_instance=RequestContext(request))



def doooooo(request):
    number=21
    utils.GPIOstart(number)
    time.sleep(2)
    utils.GPIOcleanup()
    return render_to_response('website/index.html',context_instance=RequestContext(request))
#    return render_to_response('website/doooooo.html',cotext_instance=RequestContext(request))
#    return HttpResponse("exec!")
#doooooo.html
