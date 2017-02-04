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
from logging import getLogger

# Create your views here.
logger = getLogger(__name__)


def index(request):
    args={}
    args["hour_list"]=range(0,24)
    args["minute_list"]=range(0,60)
    return render_to_response('website/index.html',
                              args,
                              context_instance=RequestContext(request))



def doooooo(request):
    hour=request.POST['hour']
    minute=request.POST['minute']
    little=request.POST['little']
    date=datetime.now()
    logger.info("make th")
    th = threading.Thread(target=utils.executer,args=(hour,minute,little,date))
#    utils.executer(hour,minute,little)
    logger.info("th.start()")
    th.start()

    #make args
    args={}
    args["hour"]=hour
    args["minute"]=minute
    args["little"]=little
    args["date"]=str(date)
    return render_to_response('website/doooooo.html',
                              args,
                              context_instance=RequestContext(request))

