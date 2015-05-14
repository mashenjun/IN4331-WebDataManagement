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
      <xsl:text disable-output-escaping="yes">&lt;script src="http://www.midijs.net/lib/midi.js" language="javascript" </xsl:text><xsl:text disable-output-escaping="yes"> &gt;</xsl:text><xsl:text disable-output-escaping="yes">&lt;/script&gt;</xsl:text>
      <script>
        <xsl:attribute name="type">text/javascript</xsl:attribute>
              function create_and_play(url) {

                $.get("/create_midi/",{'url':url},function(result){
                console.log('/static/'+url+'.midi');
                MIDIjs.play('/static/'+url+'.midi');
          });


          }
      </script>
    </head>
    <body>
      <h2>My Music Collection</h2>
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
              </td>
          </tr>
          </xsl:for-each>
        </table>

    </body>
  </html>
</xsl:template>
</xsl:stylesheet>