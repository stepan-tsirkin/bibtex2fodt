
head = """<?xml version="1.0" encoding="UTF-8"?>

<office:document xmlns:officeooo="http://openoffice.org/2009/office" xmlns:css3t="http://www.w3.org/TR/css3-text/" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rpt="http://openoffice.org/2005/report" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:config="urn:oasis:names:tc:opendocument:xmlns:config:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:xforms="http://www.w3.org/2002/xforms" office:version="1.3" office:mimetype="application/vnd.oasis.opendocument.text">

 <office:automatic-styles>
  <style:style style:name="Table1" style:family="table">
   <style:table-properties style:width="6.6931in" table:align="margins"/>
  </style:style>
  <style:style style:name="Table1.A" style:family="table-column">
   <style:table-column-properties style:column-width="1.6736in" style:rel-column-width="16383*"/>
  </style:style>
  <style:style style:name="Table1.A1" style:family="table-cell">
   <style:table-cell-properties style:writing-mode="page"/>
  </style:style>
  <style:style style:name="Table1.4" style:family="table-row">
   <style:table-row-properties style:min-row-height="0.2375in"/>
  </style:style>
  <style:style style:name="P1" style:family="paragraph" style:parent-style-name="Table_20_Contents">
   <style:text-properties officeooo:rsid="0009db38" officeooo:paragraph-rsid="0009db38"/>
  </style:style>
  <style:page-layout style:name="pm1">
   <style:page-layout-properties fo:page-width="8.2681in" fo:page-height="11.6929in" style:num-format="1" style:print-orientation="portrait" fo:margin-top="0.7874in" fo:margin-bottom="0.7874in" fo:margin-left="0.7874in" fo:margin-right="0.7874in" style:writing-mode="lr-tb" style:footnote-max-height="0in" loext:margin-gutter="0in">
    <style:footnote-sep style:width="0.0071in" style:distance-before-sep="0.0398in" style:distance-after-sep="0.0398in" style:line-style="solid" style:adjustment="left" style:rel-width="25%" style:color="#000000"/>
   </style:page-layout-properties>
   <style:header-style/>
   <style:footer-style/>
  </style:page-layout>
 </office:automatic-styles>

 <office:body>
  <office:text>
"""

foot = """  </office:text>
 </office:body>
</office:document>
"""


table_template = """   <table:table table:name="Table1" table:style-name="Table1">
    <table:table-column table:style-name="Table1.A" table:number-columns-repeated="3"/>
    <table:table-column table:style-name="Table1.D"/>
    <table:table-row>
     <table:table-cell office:value-type="string">
      <text:p text:style-name="P1">{entry1}</text:p>
     </table:table-cell>
     <table:table-cell office:value-type="string">
      <text:p text:style-name="Standard"/>
     </table:table-cell>
     <table:table-cell office:value-type="string">
      <text:p text:style-name="Standard"/>
     </table:table-cell>
     <table:table-cell office:value-type="string">
      <text:p text:style-name="P1">{entry5}</text:p>
     </table:table-cell>
    </table:table-row>
    <table:table-row>
     <table:table-cell office:value-type="string">
      <text:p text:style-name="Standard"/>
     </table:table-cell>
     <table:table-cell table:number-columns-spanned="3" office:value-type="string">
      <text:p text:style-name="P1">{entry2}</text:p>
     </table:table-cell>
     <table:covered-table-cell/>
     <table:covered-table-cell/>
    </table:table-row>
    <table:table-row>
     <table:table-cell office:value-type="string">
      <text:p text:style-name="Standard"/>
     </table:table-cell>
     <table:table-cell table:number-columns-spanned="3" office:value-type="string">
      <text:p text:style-name="P1">{entry3}</text:p>
     </table:table-cell>
     <table:covered-table-cell/>
     <table:covered-table-cell/>
    </table:table-row>
    <table:table-row table:style-name="Table1.4">
     <table:table-cell office:value-type="string">
      <text:p text:style-name="Standard"/>
     </table:table-cell>
     <table:table-cell office:value-type="string">
      <text:p text:style-name="Standard"/>
     </table:table-cell>
     <table:table-cell office:value-type="string">
      <text:p text:style-name="P1">{entry4}</text:p>
     </table:table-cell>
     <table:table-cell office:value-type="string">
      <text:p text:style-name="P1">{entry6}</text:p>
     </table:table-cell>
    </table:table-row>
   </table:table>
"""


fout = open("tables.fodt","w")
fout.write(head)

for i in range(4):
    fout.write(table_template.format(
        entry1=str(i)+" to",
        entry2=str(i)+" do",
        entry3=str(i)+" or",
        entry4=str(i)+" not",
        entry5=str(i)+" to",
        entry6=str(i)+" do"
        ) )
    fout.write(""" <text:p text:style-name="Standard"/> \n""")

fout.write(foot)

fout.close()