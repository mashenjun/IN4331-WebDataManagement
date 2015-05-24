<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
  <html>
    <head>
      <xsl:text disable-output-escaping="yes">&lt;script src="/static/js/jquery-1.11.2.min.js" language="Javascript"</xsl:text><xsl:text disable-output-escaping="yes"> &gt;</xsl:text><xsl:text disable-output-escaping="yes">&lt;/script&gt;</xsl:text>
      <!--<link>-->
        <!--<xsl:attribute name="type">text/css</xsl:attribute>-->
        <!--<xsl:attribute name="rel">stylesheet</xsl:attribute>-->
        <!--<xsl:attribute name="href">/static/CSS/semantic.min.css</xsl:attribute>-->
      <!--</link>-->
        <link>
            <xsl:attribute name="type">text/css</xsl:attribute>
            <xsl:attribute name="rel">stylesheet</xsl:attribute>
            <xsl:attribute name="href">/static/CSS/bootstrap.css</xsl:attribute>
        </link>
      <xsl:text disable-output-escaping="yes">&lt;script src="/static/js/bootstrap.min.js" language="Javascript"</xsl:text><xsl:text disable-output-escaping="yes"> &gt;</xsl:text><xsl:text disable-output-escaping="yes">&lt;/script&gt;</xsl:text>
      <xsl:text disable-output-escaping="yes">&lt;script src="http://www.midijs.net/lib/midi.js" language="javascript" </xsl:text><xsl:text disable-output-escaping="yes"> &gt;</xsl:text><xsl:text disable-output-escaping="yes">&lt;/script&gt;</xsl:text>
      <script>
        <xsl:attribute name="type">text/javascript</xsl:attribute>

        <xsl:text disable-output-escaping="yes">
          $(document).ready(
            function(){
                <!--document.getElementById('id_file').setAttribute("class","btn")-->
                document.getElementById('id_file').onchange = uploadOnChange;
                function uploadOnChange() {
                    var filename = this.value;
                    var lastIndex = filename.lastIndexOf("\\");
                    if (lastIndex >= 0) {
                        filename = filename.substring(lastIndex + 1);
                    }
                    document.getElementById('uploadform').setAttribute("action","/upload_file/"+filename+"/");
                    }
                }
            );

              function create_and_play(url) {
                $.get("/create_midi/",{'url':url},function(result){
                console.log('/static/'+url+'.midi');
                MIDIjs.play('/static/'+url+'.midi');
          });
          }
            function remove_file(url){
                $.get('//')
            }
          </xsl:text>
      </script>
    </head>
    <body background="/static/eight.png">
        <ul class="pager" >
          <li><a href="/web_data_index/">home</a></li>
        </ul>
      <h2 align="center">My Music Collection</h2>
        <hr/>
        <form  id="uploadform" enctype="multipart/form-data" method="POST" action="/upload_file/">
             <div align="center" class="form-group">
    <!--{% csrf_token %}-->
            {{form.as_p}}
        <input class="btn btn-default" type="submit" value="Upload" id="b_submit"/>
            </div>
        </form>
        <hr/>
        <table class="table table-striped table-hover">
          <tr class="info">
                <th style="text-align:left;color:white">Name</th>
              <th style="text-align:left;color:white">Option</th>
          </tr>
          <xsl:for-each select="result/collection/resource">
          <tr>
            <td>
            	<a>
            	<xsl:attribute name="href">/music_PDF/<xsl:value-of select="@name"/></xsl:attribute>
              <xsl:attribute name="target">_blank</xsl:attribute>
            		<xsl:value-of select="@name"/>
            	</a>

            </td>
              <td>
                  <a>
            	<xsl:attribute name="href">#</xsl:attribute>
                      <xsl:attribute name="style">text-decoration: none</xsl:attribute>
                <xsl:attribute name="onClick">create_and_play("<xsl:value-of select="@name"/>");</xsl:attribute>
            		Play
            	</a>
                  <a>
            	<xsl:attribute name="href">#</xsl:attribute>
                      <xsl:attribute name="style">text-decoration: none</xsl:attribute>
                <xsl:attribute name="onClick">MIDIjs.stop();</xsl:attribute>
            		Stop
            	</a>
                  <a>
            	<xsl:attribute name="href">#</xsl:attribute>
                      <xsl:attribute name="style">text-decoration: none</xsl:attribute>
                <xsl:attribute name="onClick"></xsl:attribute>

            	<xsl:attribute name="href">/music_Lyric/<xsl:value-of select="@name"/></xsl:attribute>
                      <xsl:attribute name="style">text-decoration: none</xsl:attribute>
            		Lyric
            	</a>
                   <a>
            	<xsl:attribute name="href">/remove_file/<xsl:value-of select="@name"/></xsl:attribute>
                      <xsl:attribute name="style">text-decoration: none</xsl:attribute>
            		Remove
            	</a>
              </td>
          </tr>
          </xsl:for-each>
        </table>

        <hr/>
        <form class="form-horizontal" method="get" action="/search/" target="_blank">

        <table cellpadding="0px" cellspacing="0px">
        <tr align="center">
            <td height="30px">

            Search for Lyric:
        </td>
        <td height="32px" style="border-style:solid none solid solid;border-color:#4B7B9F;border-width:1px;">
        <input type="text" name="lyric" style="width:150px; border:0px solid; height:32px; padding:0px 0px; position:relative;"/>
        </td>
        <td height="32px" style="border-style:solid;border-color:#4B7B9F;border-width:1px;">
        <input type="submit" value=""  style="border-style: none; background: url('/static/searchbutton3.png') no-repeat; width: 32px; height: 32px;"/>
        </td>
        </tr>
        </table>
        </form>

    </body>
  </html>
</xsl:template>
</xsl:stylesheet>