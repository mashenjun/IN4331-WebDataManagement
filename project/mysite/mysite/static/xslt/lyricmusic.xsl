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
      <!--<script>-->
        <!--<xsl:attribute name="type">text/javascript</xsl:attribute>-->

      <!--</script>-->
    </head>
    <body>
      <h2>My Music List</h2>
        <table class="ui table">
          <tr>
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