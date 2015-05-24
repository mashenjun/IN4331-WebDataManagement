<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
  <html>
    <head>
      <xsl:text disable-output-escaping="yes">&lt;script src="/static/js/jquery-1.11.2.min.js" language="Javascript"</xsl:text><xsl:text disable-output-escaping="yes"> &gt;</xsl:text><xsl:text disable-output-escaping="yes">&lt;/script&gt;</xsl:text>
      <link>
            <xsl:attribute name="type">text/css</xsl:attribute>
            <xsl:attribute name="rel">stylesheet</xsl:attribute>
            <xsl:attribute name="href">/static/CSS/bootstrap.css</xsl:attribute>
        </link>
      <xsl:text disable-output-escaping="yes">&lt;script src="/static/js/bootstrap.min.js" language="Javascript"</xsl:text><xsl:text disable-output-escaping="yes"> &gt;</xsl:text><xsl:text disable-output-escaping="yes">&lt;/script&gt;</xsl:text>
      <xsl:text disable-output-escaping="yes">&lt;script src="http://www.midijs.net/lib/midi.js" language="javascript" </xsl:text><xsl:text disable-output-escaping="yes"> &gt;</xsl:text><xsl:text disable-output-escaping="yes">&lt;/script&gt;</xsl:text>
      <!--<script>-->
        <!--<xsl:attribute name="type">text/javascript</xsl:attribute>-->

      <!--</script>-->
    </head>
    <body background="/static/eight.png">
        <ul class="pager" >
          <li><a href="/music_index/">back</a></li>
        </ul>
      <h2 align="center">My Music List</h2>
        <table class="table table-striped table-hover">
          <tr class="info">
                <th style="text-align:left">Syllabic</th>
              <th style="text-align:left">Text</th>
          </tr>
          <xsl:for-each select="//lyric">
          <tr>
            <td>
            	<p>
            		<xsl:value-of select="syllabic/text()"/>
            	</p>

            </td>
              <td>
                  <p>
            		<xsl:value-of select="text/text()"/>
            	</p>
              </td>
          </tr>
          </xsl:for-each>
        </table>



    </body>
  </html>
</xsl:template>
</xsl:stylesheet>