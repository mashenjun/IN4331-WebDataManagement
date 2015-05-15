from django.views.decorators.csrf import csrf_protect

__author__ = 'mashenjun'

from django.template.loader import get_template
from django.shortcuts import render_to_response, render
from django.http import HttpResponse, Http404, HttpRequest, HttpResponseRedirect
from django.template import *
from django import template
from xml.etree import ElementTree
from eulexistdb import db
from lxml import etree
import os
import requests
import subprocess
import libxml2
import shutil
from .form import UploadFileForm

class TryExist:
    def __init__(self):
        self.db = db.ExistDB()
    def get_data(self, query):
        result = list()
        qresult = self.db.executeQuery(query)
        #mresult = self.db.query(query)
        #print(mresult)
        hits = self.db.getHits(qresult)
        for i in range(hits):
            result.append( str(self.db.retrieve(qresult, i)))
        return result
    def get_doc(self, filepath):
        result = self.db.getDoc(filepath)
        return result
    def get_data_string(self,query):
        result = ""
        qresult = self.db.executeQuery(query)
        hits = self.db.getHits(qresult)
        for i in range(hits):
            result = result + str(self.db.retrieve(qresult, i))
        return result
    def upload_to_exist(self,file,path):
        self.db.load(file,path)
        return

def uploadfile(request):
    t = get_template('uploadfile.html')
    form = UploadFileForm()
    html = t.render(Context({"form":form}))
    return HttpResponse(html)

def handle_uploaded_file(f,name):
    print "/db/musics/"+name
    a = TryExist()
    a.upload_to_exist(f,"/db/musics/"+name)
    # destination= open(os.path.join(os.path.dirname(__file__),'static/'+name),'wb+')
    # for chunk in f.chunks():
    #     destination.write(chunk)

def upload_file(request,offset):
    if request.method =='POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'],offset)
            return HttpResponseRedirect('/uploadfile/')
    else:
        t=t = get_template('uploadfile.html')
        form = UploadFileForm()
        html = t.render(Context({"form":form}))
        return HttpResponse(html)
