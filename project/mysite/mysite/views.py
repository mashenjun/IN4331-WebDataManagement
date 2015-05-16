__author__ = 'alienware'

import os
# os.environ['DJANGO_SETTINGS_MODULE'] = 'localsettings.py'

from django.template.loader import get_template
from django.shortcuts import render_to_response, render
from django.http import HttpResponse, Http404, HttpRequest, HttpResponseRedirect
from django.template import *
from django import template
from xml.etree import ElementTree
from eulexistdb import db
from lxml import etree
from .form import UploadFileForm
import requests
import subprocess
import libxml2
import shutil



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
    def remove_doc_exist(self,file_path):
        self.db.removeDocument(file_path)
        return

    def store_file(self,file=None):
        return self.db.load('''<code-table xml:id="access-condition-type-code">
    <code-table-name>work-types</code-table-name>
    <basis> http://shakespeare.about.com/od/theplays/a/Tragedy_Comedy_History.htm,
        http://www.nosweatshakespeare.com/shakespeare-plays/play-types/,
        http://shakespeare.nuvvo.com/lesson/4448-shakespeare-plays-comedies-tragedies-histories,
        http://www.examiner.com/article/shakespeare-101-how-are-shakespeare-s-plays-classified</basis>
    <description/>
    <items>
    </items>
    </code-table>'''
    ,"musics/a.xml",True)

quer0 = '''
declare default element namespace "http://www.tei-c.org/ns/1.0";
let $ms:=doc('/db/apps/shakespeare/data/'''

####query for poetry
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

quer4_1 ='''
for $result in $ms//text/body/div//lg[@type='stanza']/*[1]
return data($result/l[1])
'''

quer4_2 ='''
for $result in $ms//text/body/div//l[1]/text()
return data($result)
'''

querylist_1 ='''
for $result in $ms//text/body/div/lg['''

querylist_2=''']
return data($result)
'''

querylist_son_1='''
for $result in $ms//text/body/div['''

querylist_son_2=''']
return data($result/div['''

querylist_son_3=''']/l)'''

final='''
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

test1='''
for $result in $ms//text/body/div
return
     data($result/div/head)
'''

test2='''
for $result in $ms//text/body/div
return
     data($result/count(div))
'''


query_speaker_1='''
for $result in $ms//text/body/div/div
where $result/@xml:id=\''''

query_speaker_2='''\'
return
    data($result/sp/speaker)
'''

query_dialogue_1='''
for $result in $ms//text/body/div/div/sp
let $name := $result/speaker
where $result/../@xml:id=\''''

query_dialogue_2='''\'
return
    data(<b>{$result/(l|ab)}</b>)
'''

queryindex1 ='''
let $ms:=doc('apps/shakespeare/data/work-types.xml')
for $result in $ms//items/item
where $result/label!='The Two Noble Kinsmen'
return data($result/label)
'''

queryindex2 ='''
xquery version "3.0";
let $ms:=doc('apps/shakespeare/data/work-types.xml')
for $result in $ms//items/item
where $result/label!='The Two Noble Kinsmen'
return
data(<b>{$result/value[1]/text(),' ',$result/value[2]/text(),' ',$result/value[3]/text(),' ',$result/value[4]/text()}</b>)
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
    a = TryExist()
    myres = a.get_data(quer4_1)

    #print etree.fromstring(myres).text
    # data= requests
    print("-------------")
    print(myres)
    print("-------------")
    t = get_template('Xquery_test.html')
    html = t.render(Context({'content':myres}))
    return HttpResponse(html)

def eXist(request):
    # a = TryExist()
    # myres = a.get_data(quer1)
    # print (myres)

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
    t = get_template('summary.html')
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

def sha_index(request):
    a = TryExist()
    titlewithtype=list()
    whichtemplate=list()
    myres2 = a.get_data(queryindex1)
    myres = a.get_data(queryindex2)
    mystring_1 = a.get_data_string(queryindex1)
    mystring_2 = a.get_data_string(queryindex2)
    print ("############################")
    print (mystring_1)
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print (mystring_2)
    print ("############################")
    for j in range(0,len(myres)):
        myres[j]=myres[j].split()
        myres[j]=' , '.join(myres[j])
        if "Poetry" in myres[j]:

            whichtemplate.append('/sha_poetry/'+str(j+1 if j+1<27 else j+2))
        else :
            whichtemplate.append('/sha_npoetry/'+str(j+1 if j+1<27 else j+2))
    titlewithtype=zip(myres2,myres,whichtemplate)

    t = get_template('sha_index.html')
    html = t.render(Context({'title':titlewithtype}))
    return HttpResponse(html)

def addtag(x,y):
    result= list();
    for i in range(0,len(y)):
        result.append("<"+x+">"+str(y[i])+"</"+x+">")
    return result

def sha_poetry(request,offset):
    a = TryExist()
    temp='''let $ms:=doc('apps/shakespeare/data/work-types.xml')
    for $result in $ms//items/item['''+offset+''']/id
    return data($result)'''
    myres2 = a.get_data(temp)[0]
    myres2 = myres2.replace('sha-','')+'.xml\')'
    print("##############")
    print(myres2)
    print("##############")
    #query=quer0+myres2+quer2
    sha_title = a.get_data(quer0+myres2+quer1)
    sha_name = a.get_data(quer0+myres2+quer2)
    sha_resp = a.get_data(quer0+myres2+quer3)
    if str(offset)=="41" or str(offset)=="40":
        sha_body = a.get_data(quer0+myres2+quer4_1)
    else :
        sha_body = a.get_data(quer0+myres2+quer4_2)
    #print etree.fromstring(myres).text
    # data= requests
    print("-------------")
    print(sha_resp)
    print("-------------")
    sha_staff=zip(sha_name,sha_resp)
    t = get_template('sha_poetry.html')
    html = t.render(Context({'title': sha_title,'staff':sha_staff,'body':sha_body,'filename':myres2.split('.')[0]}))
    return HttpResponse(html)

def sha_npoetry(request,offset):
    print (offset)
    a = TryExist()
    temp='''let $ms:=doc('apps/shakespeare/data/work-types.xml')
    for $result in $ms//items/item['''+offset+''']/id
    return data($result)'''
    myres2 = a.get_data(temp)[0]
    myres2 = myres2.replace('sha-','')+'.xml\')'
    print("##############")
    print(myres2)
    print("##############")


    #query=quer0+myres2+quer2
    sha_title = a.get_data(quer0+myres2+quer1)
    sha_name = a.get_data(quer0+myres2+quer2)
    sha_resp = a.get_data(quer0+myres2+quer3)

    scene = a.get_data(quer0+myres2+test1)
    final_list =a.get_data(quer0+myres2+final)
    act_no = a.get_data(quer0+myres2+test2)
    b=list()
    c=list()
    x=0

    for num in act_no:
        b.append(final_list[x:x+int(num)])
        c.append(scene[x:x+int(num)])
        x=x+int(num)


    for i in range(b.__len__()):
        for j in range(len(b[i])):
            b[i][j]=b[i][j].split('*')
            b[i][j].pop()
            temp=b[i][j]
            b[i][j]=[]
            b[i][j].append(temp[0])
            b[i][j].append(','.join(temp[1:]))


    print c
    print ('====================')
    print b

    sha_staff=zip(sha_name,sha_resp)
    t = get_template('sha_npoetry.html')
    html = t.render(Context({'title': sha_title,'staff':sha_staff,'body':b,'filename':myres2.split('.')[0]}))
    return HttpResponse(html)

def sha_poetry_list(request,offset):
    a = TryExist()
    #print (str(offset))
    filename=str(offset).split('@')[0]+'.xml\')'
    num = str(offset).split('@')[1]
    num_1 = str(int(num)//20+1)
    num_2 = str(int(num)%20)
    if str(offset).__contains__('son'):
        query = quer0+filename+querylist_son_1+num_1+querylist_son_2+num_2+querylist_son_3
        new_sha_list=a.get_data(query)
    else:
        query= quer0+filename+querylist_1+num+querylist_2
        sha_list = a.get_data(query)
        new_sha_list = str(sha_list[0]).split("\n")
        while '\s' in new_sha_list:
             new_sha_list.remove('\s')

    # print("#################################")
    # print(num,num_1,num_2)
    # print(query)
    # print (new_sha_list)
    # print (str(offset))
    # print("#################################")
    t = get_template('sha_poetry_list.html')
    html = t.render(Context({'listcontent':new_sha_list}))
    return HttpResponse(html)

def sha_npoetry_list(request,offset):
    print(offset)
    a = TryExist()
    new_dialogue=list()
    filename = str(offset).split('@')[0]+'.xml\')'
    act = str(offset).split('@')[1]
    sc = str(offset).split('@')[2]
    act_sc = 'sha-'+str(offset).split('@')[0]+str(offset).split('@')[1]+'0'+str(offset).split('@')[2]
    speaker = a.get_data(quer0+filename+query_speaker_1+act_sc+query_speaker_2)
    dialogue = a.get_data(quer0+filename+query_dialogue_1+act_sc+query_dialogue_2)
    for i in range(0,len(dialogue)):
        new_dialogue.append(dialogue[i].split('\n'))
        print("#################################")
        print (dialogue[i])
        print (dialogue[i].split('\n'))

        print("#################################")
    print(len(new_dialogue))
    content_list = zip(speaker,new_dialogue)
    t = get_template('sha_npoetry_list.html')
    html = t.render(Context({'act_sc':'Act '+act+', Scene '+sc,'content':content_list}))
    return HttpResponse(html)

def xslttest(request):
    # with open(os.path.join(os.path.dirname(__file__),'static/cdcatalog.xml'), 'r') as myfile:
    #     data =myfile.read()
    xml_tree = etree.parse(os.path.join(os.path.dirname(__file__),'static/xslt/cdcatalog.xml'))
    xslt_tree = etree.XSLT(etree.parse(os.path.join(os.path.dirname(__file__),'static/xslt/cdcatalog.xsl')))
    result_tree = xslt_tree(xml_tree)
    return HttpResponse(etree.tostring(result_tree))

def pdfreturn(request):
    a = TryExist()
    result = etree.fromstring(a.get_doc('/musics/Canoe_Song.xml'))
    subprocess.call(["musicxml2ly",result])
    return HttpResponse();

def music_index(request):
    head = '<?xml version="1.0" encoding="UTF-8"?> ' \
           '<?xml-stylesheet type="text/xsl" href="cdcatalog.xsl"?>'
    music_filename_xml = head+requests.get('http://localhost:8080/exist/rest/db/musics').content.replace("exist:","")
    music_filename_xml_1 = music_filename_xml.replace(".xml","")
    xml_tree = etree.fromstring(music_filename_xml_1)
    xslt_tree = etree.XSLT(etree.parse(os.path.join(os.path.dirname(__file__),'static/xslt/cdcatalog.xsl')))
    data = xslt_tree(xml_tree)

    # html = t.render(Context({"data":tag}))
    t=Template(etree.tostring(data))
    form = UploadFileForm()
    html = t.render(Context({"form":form}))
    return HttpResponse(html);

def music_PDF(request,offest):
    fake=str(offest)
    url_file="http://localhost:8080/exist/rest/db/musics/"+fake+".xml"
    r=requests.get(url_file, stream=True)
    local_filename=fake+".xml"

    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    print os.path.dirname(os.path.abspath(__file__))

    os.system('rm *.pdf')
    os.system('rm *.midi')

    subprocess.call(["musicxml2ly","-m",local_filename])
    subprocess.call(["lilypond",fake+".ly"])

    os.remove(fake+".ly")
    os.remove(fake+".xml")
    shutil.move(fake+".midi", os.path.dirname(os.path.abspath(__file__))+"/static/"+fake+".midi")

    with open(fake+'.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=Music.pdf'
    # return HttpResponse("html")
    return response

def create_midi(request):
    fake=str(request.GET['url'])
    url_file="http://localhost:8080/exist/rest/db/musics/"+fake+".xml"
    r=requests.get(url_file, stream=True)
    local_filename=fake+".xml"

    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    print os.path.dirname(os.path.abspath(__file__))

    os.system('rm *.pdf')
    os.system('rm *.midi')

    subprocess.call(["musicxml2ly","-m",local_filename])
    subprocess.call(["lilypond",fake+".ly"])

    os.remove(fake+".ly")
    os.remove(fake+".xml")
    shutil.move(fake+".midi", os.path.dirname(os.path.abspath(__file__))+"/static/"+fake+".midi")

    with open(fake+'.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=Music.pdf'
    # return HttpResponse("html")
    return HttpResponse("success")


query_lyric1='''
<result>
{
let $ms:=doc('/db/musics/'''

query_lyric2='''
for $result in $ms//lyric
return $result
}
</result>
'''

query_lyric3='''
<result>
{
let $ms:=doc('/db/musics/Binchois.xml')
for $result in $ms//lyric
return ($result)
}
</result>
'''
def music_Lyric(request,offset):
    a = TryExist()
    fake=str(offset)
    head = '<?xml version="1.0" encoding="UTF-8"?> ' \
           '<?xml-stylesheet type="text/xsl" href="cdcatalog.xsl"?>'

    # lyric_filename_xml=head+a.get_data_string(query_lyric1+fake+".xml')"+query_lyric2).replace("exist:","")
    lyric_filename_xml=a.get_data_string(query_lyric1+fake+".xml')"+query_lyric2)
    xml_tree = etree.fromstring(lyric_filename_xml)
    xslt_tree = etree.XSLT(etree.parse(os.path.join(os.path.dirname(__file__),'static/xslt/lyricmusic.xsl')))
    data = xslt_tree(xml_tree)
    # return  HttpResponse("http")
    return HttpResponse(etree.tostring(data))

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
            return HttpResponseRedirect('/music_index/')
    else:
        return HttpResponse("Error 404 page not found")

def remove_file(request,offset):
    name =offset
    a=TryExist()
    a.remove_doc_exist("/db/musics/"+name+".xml")
    return HttpResponseRedirect('/music_index/')