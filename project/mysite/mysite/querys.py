__author__ = 'mashenjun'
class querys():
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