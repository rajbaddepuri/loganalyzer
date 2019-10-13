from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .forms import log_form
from .dbOperations import *
import logging
from .logger import Logger

import os
log = Logger.get_logger(loglevel=logging.DEBUG)
# Create your views here.

def home_view(request):
    log.info("Rendering home page")
    return render(request,'home.html')

def form_view(request):
    raj=log_form(request.POST or None,request.FILES or None)
    log.info('the requested file save into a variable')
    existing_log_path = get_log_path()
    if existing_log_path is not None:
        log.warning("Selected file is already under monitoring. Please use monitoring tab")
        return HttpResponse("<h1>File is already under monitor, please use monitor tab</h1>")
    if raj.is_valid():
        #instance=raj.save(commit=False)
        log.debug("Form page validated, hence reading the selected access log file")
        log_file=request.FILES['file']
        log.debug("selected log file name " +str(log_file))
        fs=FileSystemStorage()
        log_file_path=fs.path(log_file.name)
        log.debug("Log file path is : " +str(log_file_path))
        insert_log_path(log_file_path)
        for i in (log_file.readlines()):
            value=str(i).split(" ")
            dict_value=dict()
            dict_value["ip_adress"]=value[0][2:len(value[0])]
            dict_value["date_time"] = value[3][1:len(value[3])]
            dict_value["method"] = value[5][1:len(value[5])]
            dict_value["url_loction"] = value[6]
            dict_value["res_code"] = value[8]
            dict_value["memory"] = value[9]
            if not insert_log_values(dict_value):
                log.info("Values inserted successfully")
                return HttpResponse("<h1>Not succes fully inserted</h1>")
                #return render(request,'form.html',{'raj':raj})
    return render(request,'form.html',{'raj':raj})
def bye_view(request):
    return render(request,'bye.html')