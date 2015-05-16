<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
  <html>
    <head>
      <xsl:text disable-output-escaping="yes">&lt;script src="/static/js/jquery-1.11.2.min.js" language="Javascript"</xsl:text><xsl:text disable-output-escaping="yes"> &gt;</xsl:text><xsl:text disable-output-escaping="yes">&lt;/script&gt;</xsl:text>
      <link>
        <xsl:attribute name="type">text/css</xsl:attribute>
        <xsl:attribute name="rel">stylesheet</xsl:attribute>
        <xsl:attribute name="href">/static/CSS/semantic.min.css</xsl:attribute>
      </link>
        <link>
        <xsl:attribute name="type">text/css</xsl:attribute>
        <xsl:attribute name="rel">stylesheet</xsl:attribute>
        <xsl:attribute name="href">/static/CSS/loading.css</xsl:attribute>
      </link>
      <xsl:text disable-output-escaping="yes">&lt;script src="/static/js/semantic.min.js" language="Javascript"</xsl:text><xsl:text disable-output-escaping="yes"> &gt;</xsl:text><xsl:text disable-output-escaping="yes">&lt;/script&gt;</xsl:text>
      <xsl:text disable-output-escaping="yes">&lt;script src="/static/js/midi.js" language="javascript" </xsl:text><xsl:text disable-output-escaping="yes"> &gt;</xsl:text><xsl:text disable-output-escaping="yes">&lt;/script&gt;</xsl:text>
      <script>
        <xsl:attribute name="type">text/javascript</xsl:attribute>

        <xsl:text disable-output-escaping="yes">
          $(document).ready(
    function(){

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
    <body>
      <h2>My Music Collection</h2>
        <hr/>
        <form id="uploadform" enctype="multipart/form-data" method="POST" action="/upload_file/">
    <!--{% csrf_token %}-->
            {{form.as_p}}
        <input type="submit" value="Upload" id="b_submit"/>
        </form>
        <hr/>
        <table class="ui table">
          <tr>
                <th style="text-align:left">Name</th>
              <th style="text-align:left">Option</th>
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

    </body>
  </html>
</xsl:template>
</xsl:stylesheet>