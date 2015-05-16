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

          </xsl:text>
      </script>
    </head>
    <body>
      <h2 align="center">Lyric Search Outcome</h2>

        <table  class="ui table" style="width:100%">
          <tr>
                <th style="text-align:center">
                    Name1
                </th>
          </tr>
          <xsl:for-each select="result/work-title">
          <tr>
              <td align="center">
                  <p>
                    <xsl:value-of select="text()"/>
            	</p>

              </td>
          </tr>
          </xsl:for-each>
        </table>




    </body>
  </html>
</xsl:template>
</xsl:stylesheet>