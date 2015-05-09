__author__ = 'alienware'

from django.template.loader import get_template
from django.shortcuts import render_to_response, render
from django.http import HttpResponse, Http404, HttpRequest
from django.template import *
from xml.etree import ElementTree
from eulexistdb import db
import lxml.etree as ET 
import os
import requests

class TryExist:
    def __init__(self):
        self.db = db.ExistDB(server_url="http://localhost:8080/exist")
    def get_data(self, query):
        result = list()
        qresult = self.db.executeQuery(query)
        hits = self.db.getHits(qresult)
        for i in range(hits):
            result.append(str(self.db.retrieve(qresult, i)))
        return result

quer1 = '''
let $x:= doc("/db/movies/movies.xml")
return $x//year
'''

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

def Xquerytest(request):
    # a = TryExist()
    # myres = a.get_data(quer1)
    # print myres
    data= requests
    print("-------------")
    print(requests)
    print("-------------")
    t = get_template('Xquery_test.html')
    html = t.render(Context({'data':data}))
    return HttpResponse(html)

def eXist(request):
    director_list = []
    views = get_template('eXisttest.html')
    title = requests.get('http://localhost:8080/exist/rest/db/movies/movies.xml?_query=//title&_warp=no')
    genre = requests.get('http://localhost:8080/exist/rest/db/movies/movies.xml?_query=distinct-values(//genre)')
    directors = requests.get('http://localhost:8080/exist/rest/db/movies/movies.xml?_query=//director')
    actors = requests.get('http://localhost:8080/exist/rest/db/movies/movies.xml?_query=//actor')
    years = requests.get('http://localhost:8080/exist/rest/db/movies/movies.xml?_query=distinct-values(//year)')

    tree_director = ElementTree.fromstring(directors.content)
    for element in tree_director:
        name= element.find('last_name').text+' '+element.find('first_name').text
        # print (name)
        if name not in director_list:
            director_list.append(name)

    years_list=[]
    for i in ElementTree.fromstring(years.content).findall('*'):
        years_list.append(int(i.text))
    years_list.sort()
    # print (years_list)

    actor_list = []
    tree_actor = ElementTree.fromstring(actors.content)
    for element in tree_actor:
        name= element.find('last_name').text+' '+element.find('first_name').text
        if name not in actor_list:
            actor_list.append(name)

    tree_title = ElementTree.fromstring(title.content)
    tree_genre = ElementTree.fromstring(genre.content)
    # print (len(director_list))

    response = views.render(Context({'title': tree_title.findall('*'),'genre':tree_genre.findall('*'),'director':director_list,'actors':actor_list,
                                    'years':years_list}))
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

def sendrequest(request):
    import requests
    par_list=[]
    body=""
    mark="+"
    datastring=""
    for i in range(1,7,1):
        a='par'+str(i)
        b=str(request.GET[a])
        if(i==4):
            b=b.split(',')
            b.pop()
            #print (b)
        par_list.append(b)
    #print (len(par_list[3]))
    url="http://localhost:8080/exist/rest/db/movies/movies.xml?_query="
    # body=body+'movie[title=\"'+par_list[0]+'\"]/title'
    if par_list[0]!="":
        body=body+'title=\"'+par_list[0]+'\"'
    if par_list[0]=="":
        if par_list[1]!="":
            if body=="" :
                body = body+'genre=\"'+par_list[1]+'\"'
            else :
                body = body+' and '+'genre=\"'+par_list[1]+'\"'
        if par_list[2]!="":
            lastname= par_list[2].split(' ')[0]
            firstname= par_list[2].split(' ')[1]
            if body=="" :
                body = body+'director/last_name=\"'+lastname+'\"'+' and '+'director/first_name=\"'+firstname+'\"'
            else :
                body = body+' and '+'director/last_name=\"'+lastname+'\"'+' and '+'director/first_name=\"'+firstname+'\"'
        if par_list[3]!="":
            name=par_list[3]
            lastname='';
            firstname='';
            for x in range(0, len(name)):
                print(len(name[x].split(' ')))
                if len(name[x].split(' '))==2:
                    print ('<2>')
                    lastname= name[x].split(' ')[0]
                    firstname= name[x].split(' ')[1]
                elif len(name[x].split(' '))==3:
                    print ('<3>')
                    lastname = name[x].split(' ')[0]+" "+name[x].split(' ')[1]
                    firstname = name[x].split(' ')[2]
                if body=="":
                    body = body+'actor[last_name=\"'+lastname+'\"'+' and '+'first_name=\"'+firstname+'\"'+']'
                else :
                    body = body+' and '+'actor[last_name=\"'+lastname+'\"'+' and '+'first_name=\"'+firstname+'\"'+']'
        if par_list[4]!="":
            if body=="" :
                body = body+'year=\"'+par_list[4]+'\"'
            else :
                body = body+' and '+'year=\"'+par_list[4]+'\"'
        if par_list[5]!="":
            if body=="" :
                body = body+'summary[contains(.,\"'+par_list[5]+'\"'+')]'
            else :
                body = body+' and '+'summary[contains(.,\"'+par_list[5]+'\"'+')]'


    request_content= url+'//movie['+body+']/title'
    print (request_content)
    result=requests.get(request_content)
    #print (result.content)
    tree_title = ElementTree.fromstring(result.content)
    print (len(tree_title.findall('*')))
    if (len(tree_title.findall('*'))>1):
        for x in range(0, len(tree_title.findall('*'))-1):
            datastring=datastring+tree_title.findall('*')[x].text+mark
        datastring=datastring+tree_title.findall('*')[len(tree_title.findall('*'))-1].text

    elif (len(tree_title.findall('*'))==1):
        datastring= tree_title.findall('*')[0].text
    print (datastring)
    return HttpResponse(datastring)

def getsummery(request):

    return HttpResponse()

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

def summary(request, offset):
    print("---------------")
    print(str(offset))
    print("---------------")
    t = get_template('Xquery_test.html')
    request_content= "http://localhost:8080/exist/rest/db/movies/movies.xml?_query=//movie[title=\""+offset+"\"]/summary"
    content= requests.get(request_content)
    print(content.content)
    if "summary" in content.content:
        txt = content.content.split("<summary>")[1].split('</summary>')[0]
        result = txt
    else :
        result ='no summary'
    html = t.render(Context({'content':result}))
    return HttpResponse(html)

