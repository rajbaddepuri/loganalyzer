from django.core.files import File
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.core.files.storage import FileSystemStorage
from .forms import log_form
from .dbOperations import *
import logging
from .logger import Logger
from django.views.decorators.csrf import csrf_exempt
import simplejson

import os
_log = Logger.get_logger(loglevel=logging.DEBUG)
# Create your views here.

def home_view(request):
    log.info("Rendering home page")
    return render(request,'home.html')


def form_view(request):
    _form = log_form(request.POST or None,request.FILES or None)
    log.info('the requested file save into a variable')
    existing_log_path = get_log_path()
    if existing_log_path is not None:
        log.warning("Selected file is already under monitoring. Please use monitoring tab")
        return HttpResponse("<h1>File is already under monitor, please use monitor tab</h1>")
    if _form.is_valid():
        #instance=raj.save(commit=False)
        log.debug("Form page validated, hence reading the selected access log file")
        log_file=request.FILES['file'] # file containg data stored log_file
        log.debug("selected log file name " +str(log_file))
        fs=FileSystemStorage()
        log_file_path=fs.path(log_file.name) #file path stored
        log.debug("Log file path is : " +str(log_file_path))
        print()
        #insert_log_path(log_file_path)
        # if not process_file_data(log_file.readlines()):
        #     return HttpResponse("<h1>Not succes fully inserted</h1>")
    return render(request,'form.html',{"form":_form})


def get_values_view(request):
    existing_count = get_count_db()
    print(existing_count)
    existing_file = get_log_path()
    if existing_file is None:
        log.warning("No file found in DB. Please goto Upload New tab to initiate operations")
    return JsonResponse({'COUNT': str(existing_count), 'PATH': str(existing_file)})

def monitor_view(request):
    existing_log_path = get_log_path()
    ip_address = get_ip_adress()
    return render(request,"monitor.html",{'ip_address':ip_address, 'path':existing_log_path})

def filter_data_with_ip_address(requset):
    ip_add_req = requset.POST.get('selectedIpAdress')
    db_result = get_all_values(ip_add_req)
    processed_res = []
    for rec in db_result:
        rec_dict = {}
        rec_dict['DATE'] = rec[0]
        rec_dict['STATUS_CODE'] = rec[1]
        rec_dict['MEMORY'] = rec[2]
        rec_dict['URL_LOCATION'] = rec[3]
        rec_dict['METHOD'] = rec[4]
        processed_res.append(rec_dict)
    return JsonResponse({'record':processed_res})

#
# def getmonitr_path(request):
#     existing_log_path = get_log_path()
#     monitor_details = {
#         'FILE_PATH': existing_log_path,
#     }
#     data = simplejson.dumps(monitor_details)
#     return HttpResponse(data,content_type='application/json')
# def ip_adress(request):

