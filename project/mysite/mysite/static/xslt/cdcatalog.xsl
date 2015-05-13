<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
  <html>
    <head>
      
    </head>
    <body>
      <h2>My Music Collection</h2>
        <table border="1">
          <tr bgcolor="#9acd32">
            <th style="text-align:left">Name</th>
          </tr>
          <xsl:for-each select="result/collection/resource">
          <tr>
            <td>
            	<a>
            	<xsl:attribute name="href">/music_PDF/<xsl:value-of select="@name"/></xsl:attribute>
            		<xsl:value-of select="@name"/>
            	</a>
            </td>
          </tr>
          </xsl:for-each>
        </table>
    </body>
  </html>
</xsl:template>
</xsl:stylesheet>