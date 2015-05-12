__author__ = 'alienware'

from django.template.loader import get_template
from django.shortcuts import render_to_response, render
from django.http import HttpResponse, Http404, HttpRequest
from django.template import *
from xml.etree import ElementTree
import os
import requests
from eulexistdb import db

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

####query for poetry
quer1 = '''
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('/db/apps/shakespeare/data/lov.xml')
for $result in $ms//titleStmt/title
return $result
'''

quer2 = '''
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('apps/shakespeare/data/lov.xml')
for $result in $ms//titleStmt/respStmt/name
return $result
'''

quer3 = '''
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('apps/shakespeare/data/lov.xml')
for $result in $ms//titleStmt/respStmt/resp
return $result
'''

quer4 ='''
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('apps/shakespeare/data/lov.xml')
for $result in $ms//text/body/div/lg/l[1]/text()
return $result
'''
####query for normal
query1 = '''
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('/db/apps/shakespeare/data/1h4.xml')
for $result in $ms//titleStmt/title
return $result
'''

query2 = '''
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('apps/shakespeare/data/1h4.xml')
for $result in $ms//titleStmt/respStmt/name
return data($result)
'''

query3 = '''
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('apps/shakespeare/data/lov.xml')
for $result in $ms//titleStmt/respStmt/resp
return data($result)
'''

query4 ='''
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('apps/shakespeare/data/lov.xml')
for $result in $ms//text/body/div/lg/l[1]/text()
return data($result)
'''

def eXist(request):
    a = TryExist()
    myres = a.get_data(quer1)
    print (myres)
    myres = a.get_data(quer2)
    print (myres)
    myres = a.get_data(quer3)
    print (myres)
    myres = a.get_data(quer4)
    for j in range(0,len(myres)):
        myres[j]=myres[j][1:]
        myres[j]=myres[j].lstrip()
        myres[j]=myres[j].strip()
    print (myres)



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




