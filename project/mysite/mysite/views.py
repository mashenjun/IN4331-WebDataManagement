__author__ = 'alienware'

from django.template.loader import get_template
from django.shortcuts import render_to_response, render
from django.http import HttpResponse, Http404, HttpRequest
from django.template import *
from xml.etree import ElementTree
import os
import requests




def viewCSV(request):
    return  render_to_response('viewCSV.html')

def viewTotal(request):
    return  render_to_response('viewTotal.html')

def index(request):
    return  render_to_response('index.html')

def JavaRead(request):
    t = get_template('JavaRead.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def Result(request):
    t = get_template('Result.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def eXist(request):
    director_list = []
    views = get_template('eXisttest.html')
    title = requests.get('http://localhost:8080/exist/rest/db/movies?_query=//title&_warp=no')
    genre = requests.get('http://localhost:8080/exist/rest/db/movies?_query=distinct-values(//genre)')
    directors = requests.get('http://localhost:8080/exist/rest/db/movies?_query=//director')
    tree_director = ElementTree.fromstring(directors.content)
    for element in tree_director:
        name= element.find('last_name').text+' '+element.find('first_name').text
        print (name)
        if name not in director_list:
            director_list.append(name)

    tree_title = ElementTree.fromstring(title.content)
    tree_genre = ElementTree.fromstring(genre.content)
    print (len(director_list))

    response = views.render(Context({'title': tree_title.findall('*'),'genre':tree_genre.findall('*'),'director':director_list}))
    return HttpResponse(response)



def selecttweets(Num):
    import csv
    tweetscontent=''
    i=1
    uncertaintweets=open('./static/uncertaintweets.csv','w',newline='')
    writer=csv.writer(uncertaintweets)

    with open('./static/uncertain.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            tweet=row[0]
            writer.writerow([tweet])
            i=i+1
            if i>Num:
                 break

        writer=csv.writer(f)

    uncertaintweets.close()

def postdata(Num):
    import csv
    import requests

    API_KEY = "NUbs14x8-jenQy1tnSJ5"
    job_id = "707980"
    #Num = request.GET['Num']
    selecttweets(Num)

    file_path = "./static/uncertaintweets.csv"
    csv_file = open(file_path, 'rb')

    request_url = "https://api.crowdflower.com/v1/jobs/{}/upload".format(job_id)
    headers = {'content-type': 'text/csv'}
    payload = { 'key': API_KEY }
    print(os.getcwd())
    requests.put(request_url, data=csv_file, params=payload, headers=headers)

def main(request):
    import csv
    import requests
    Num= int(request.GET['Num'])

    API_KEY = "NUbs14x8-jenQy1tnSJ5"
    job_id = "707980"
    #Num = request.GET['Num']
    tweetscontent=''
    i=1
    uncertaintweets=open(os.path.join(os.path.dirname(__file__),'static/uncertaintweets.csv'),'w',newline='')
    #'E:/programming/Python/IR/mysite/mysite/static/uncertaintweets.csv'
    writer=csv.writer(uncertaintweets)

    with open(os.path.join(os.path.dirname(__file__),'static/uncertain.csv')) as f:
        #'E:/programming/Python/IR/mysite/mysite/static/uncertain.csv'
        reader = csv.reader(f)
        for row in reader:
            tweet=row[0]
            writer.writerow([tweet])
            i=i+1
            if i>Num:
                 break

        writer=csv.writer(f)

    uncertaintweets.close()

    file_path = os.path.join(os.path.dirname(__file__),'static/uncertaintweets.csv')
        #"E:/programming/Python/IR/mysite/mysite/static/uncertaintweets.csv"
    csv_file = open(file_path, 'rb')

    request_url = "https://api.crowdflower.com/v1/jobs/{}/upload".format(job_id)
    headers = {'content-type': 'text/csv'}
    payload = { 'key': API_KEY }

    requests.put(request_url, data=csv_file, params=payload, headers=headers)
    return HttpResponse("Success!!!")

