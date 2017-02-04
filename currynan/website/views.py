#django library
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import Context, loader, RequestContext

#self made library
import utils

#general library
import threading
import time
from datetime import datetime
# Create your views here.


def index(request):
    return render_to_response('website/index.html',context_instance=RequestContext(request))



def doooooo(request):
    hour=request.POST['hour']
    minute=request.POST['minute']
    little=request.POST['little']
    th = threading.Thread(target=utils.executer,args=(hour,minute,little))
#    utils.executer(hour,minute,little)
    th.start()

    #make args
    args={}
    args["hour"]=hour
    args["minute"]=minute
    args["little"]=little
    args["date"]=str(datetime.now())
    return render_to_response('website/doooooo.html',
                              args,
                              context_instance=RequestContext(request))


