
from django.template.loader import get_template
from django.shortcuts import render_to_response, render
from django.http import HttpResponse, Http404, HttpRequest
from django.template import *
from xml.etree import ElementTree
import os
import requests
from eulexistdb import db
import re
import subprocess
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

####query for poetry

quer0 = '''
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('/db/apps/shakespeare/data/'''

quer1 = '''
for $result in $ms//titleStmt/title
return data($result)
'''

quer2 = '''
for $result in $ms//titleStmt/respStmt/name
return data($result)
'''

quer3 = '''
for $result in $ms//titleStmt/respStmt/resp
return data($result)
'''

quer4 ='''
for $result in $ms//text/body/div/lg/l[1]
return data($result)
'''
####query for normal
query1 = '''
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('/db/apps/shakespeare/data/1h4.xml')
for $result in $ms//titleStmt/title
return data($result)
'''

query2 = '''
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('apps/shakespeare/data/1h4.xml')
for $result in $ms//titleStmt/respStmt/name
return data($result)
'''

query3 = '''
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('apps/shakespeare/data/lh4.xml')
for $result in $ms//titleStmt/respStmt/resp
return data($result)
'''

query_play='''
xquery version "3.0";
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('apps/shakespeare/data/1h4.xml')
for $result in $ms//text/body/div/div
where $result/@xml:id='sha-1h4101'
return
   data($result/head|$result/stage|$result/sp/speaker|$result/sp/l)
'''
query_speaker='''
xquery version "3.0";
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('apps/shakespeare/data/1h4.xml')
for $result in $ms//text/body/div/div
where $result/@xml:id='sha-1h4101'
return
    data($result/sp/speaker)
'''

query_dialogue='''
 declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('apps/shakespeare/data/1h4.xml')
for $result in $ms//text/body/div/div/sp
let $name := $result/speaker
where $result/../@xml:id='sha-1h4101'
return data(<b>{$result/l}</b>)
'''
# query4 ='''
# declare default element namespace "http://www.tei-c.org/ns/1.0";
# let $ms:=doc('apps/shakespeare/data/lov.xml')
# for $result in $ms//text/body/div/lg/l[1]/text()
# return data($result)
# '''
queryindex1 ='''
let $ms:=doc('apps/shakespeare/data/work-types.xml')
for $result in $ms//items/item
return data($result/label)
'''
queryindex2 ='''
xquery version "3.0";
let $ms:=doc('apps/shakespeare/data/work-types.xml')
for $result in $ms//items/item
return
   data(<b>{$result/value[1]/text(),' ',$result/value[2]/text(),' ',$result/value[3]/text(),' ',$result/value[4]/text()}</b>)
   '''
query4='''
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('apps/shakespeare/data/1h4.xml')
for $result in $ms//text/body/div/div
return
    data(<b>{$result/stage[1]}</b>)
'''
test1='''
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('apps/shakespeare/data/1h4.xml')
for $result in $ms//text/body/div
return
      data($result/div/head)
'''
test2='''
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('apps/shakespeare/data/1h4.xml')
for $result in $ms//text/body/div
return
      data($result/count(div))
'''

actor_no='''
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('apps/shakespeare/data/1h4.xml')
for $result in $ms//text/body/div/div
return
      data($result/count(distinct-values($result/sp/speaker)))
'''

actor_list='''
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('apps/shakespeare/data/1h4.xml')
for $result in $ms//text/body/div/div
return
   distinct-values($result//speaker)
'''

final='''
 xquery version "3.0";
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('apps/shakespeare/data/1h4.xml')
for $result in $ms//text/body/div/div
return
    data(
    <b>{$result/stage[1],'*'}
        {let $input := <b>{$result/head,$result/sp/speaker}</b>
    for $value in distinct-values($input/speaker)
    return <b>{$value,'*'}</b>
        }
    </b>)
'''


def sha_index(request):
    a = TryExist()
    speaker=a.get_data(query_speaker)
    dialogue=a.get_data(query_dialogue)
    print len(dialogue)
    print speaker
    t = get_template('Xquery_test.html')
    html = t.render(Context({'type':dialogue}))
    return HttpResponse(html)

    # a = TryExist()
    # scene=a.get_data(query_play)
    # print scene


    # a = TryExist()
    # scene = a.get_data(test1)
    # final_list=a.get_data(final)
    # act_no = a.get_data(test2)
    # b=list()
    # c=list()
    # x=0
    # for num in act_no:
    #     b.append(final_list[x:x+int(num)])
    #     c.append(scene[x:x+int(num)])
    #     x=x+int(num)
    #
    #
    # for i in range(b.__len__()):
    #     for j in range(len(b[i])):
    #          b[i][j]=b[i][j].split('*')
    #          b[i][j].pop()
    #          temp=b[i][j]
    #          b[i][j]=[]
    #          b[i][j].append(temp[0])
    #          b[i][j].append(','.join(temp[1:]))
    #
    #
    # print c
    # print b
    #
    #
    #
    # return HttpResponse("hello world")
    # a = TryExist()
    # offset='2'
    # temp='''let $ms:=doc('apps/shakespeare/data/work-types.xml')
    # for $result in $ms//items/item['''+offset+''']/id
    # return  data($result)'''
    #
    # print temp
    # print "???????"
    # myres22 = a.get_data(temp)[0]
    #
    # print myres22
    # myres22 = myres22.replace('sha-','')+'.xml\')'
    # query=quer0+myres22+quer4
    #
    # myres3 = a.get_data(query)
    # print myres3
    # t = get_template('Xquery_test.html')
    # html=t.render(Context({'type':myres3,'title':myres3}))
    # return HttpResponse(html)
    # a = TryExist()
    # myres2 = a.get_data(queryindex1)
    # myres = a.get_data(queryindex2)
    # for j in range(0,len(myres)):
    #     myres[j]=myres[j].split()
    #     myres[j]=' , '.join(myres[j])
    # t = get_template('Xquery_test.html')
    # html = t.render(Context({'type':myres,'title':myres2}))
    # print myres2
    # return HttpResponse(html)

# def querytitle():
#     a = TryExist()
#     myres = a.get_data(queryindex1)
#     print myres


def poetry(request):
    a = TryExist()
    myres = a.get_data(quer4)
    for j in range(0,len(myres)):
        myres[j]=myres[j][1:]
        myres[j]=myres[j].lstrip()
        myres[j]=myres[j].strip()
        myres[j]=myres[j].translate('!!!','xe')#?????
    return


def eXist(request):

    a = TryExist()
    myres = a.get_data(queryindex1)
    print myres
    # myres = a.get_data(quer2)
    # print myres
    # myres = a.get_data(quer3)
    # print myres
    # myres = a.get_data(quer4)
    # for j in range(0,len(myres)):
    #     myres[j]=myres[j][1:]
    #     myres[j]=myres[j].lstrip()
    #     myres[j]=myres[j].strip()
    #     myres[j]=myres[j].replace("xe2","\'")
    # print myres



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


def sha_poetry(request,offset):
    a = TryExist()

    temp='''let $ms:=doc('apps/shakespeare/data/work-types.xml')
    for $result in $ms//items/item/id[../label=\''''+offset+'\']'+'''
    return  data($result)'''
    myres2 = a.get_data(temp)
    print myres2
    # sha_title = a.get_data(quer1)
    # sha_body = a.get_data(quer4)
    #print etree.fromstring(myres).text
    # data= requests
    # print("-------------")
    # print(sha_body)
    # print("-------------")
    # t = get_template('Xquery_test.html')
    # html = t.render(Context({'content':sha_body}))
    # return HttpResponse(html)

def sha_npoetry(request,offset):
    print (offset)
    t = get_template('sha_npoetry.html')
    html = t.render(Context({}))
    return HttpResponse(html)

def music(request):
    r=requests.get("http://localhost:8080/exist/rest/db/movies/movies.xml", stream=True)
    local_filename="movie.xml"
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()

    # print r.content
    subprocess.call(["musicxml2ly","lg-5367080.xml"])
    subprocess.call(["lilypond","lg-5367080.ly"])
    with open('lg-5367080.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=Music.pdf'
    return HttpResponse("html")


