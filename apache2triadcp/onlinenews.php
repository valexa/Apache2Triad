<html>
<head>
<link rel="stylesheet" href="style.css">
<title>Apache2Triad News</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<link rel="SHORTCUT ICON" href="favicon.ico">
</head>
<body background="gfx/lines.gif">
<div align="center"><b><span style="font-size: 16.0pt"><a name="Top"></a></span></b>
</div>
<TABLE width="99%" border=0 cellPadding=0 cellSpacing=0 class=ttb>
  <TBODY>
    <TR>
      <TD><IMG alt="" height=12 src="gfx/tt12_l.gif"
      width=10></TD>
      <TD class=tt12bkg><IMG alt="" height=12
      src="gfx/spacer.gif" width=200></TD>
      <TD><IMG alt="" height=12 src="gfx/tt12_r.gif"
      width=10></TD>
    </TR>
  </TBODY>
</TABLE>
<TABLE width="99%" border=0 cellPadding=10 cellSpacing=0 class=bodyline>
  <TR>
      
    <TD class="logo"><div align="center"><a href="http://apache2triad.net"><img src="http://apache2triad.net/gfx/apache2triad_logo.gif" border="0"></a></div></TD>
  </TR>
  <TBODY>
    <TR>
      <TD width="995">
         <blockquote>
          <blockquote>
            <p>&nbsp;</p>
            <p><font size="4" face="Georgia, Times New Roman, Times, serif">Apache2Triad News</font>
</p>
            <p>
<?php

$_item = array();
$_depth = array();
$_tags = array("dummy");
/* "dummy" prevents unecessary subtraction
* in the $_depth indexes */

function initArray()
{
    global $_item;
    $_item = array("TITLE"=>"", "LINK"=>"", "DESCRIPTION"=>"", "URL"=>"", "ID"=>"");
}

function startElement($parser, $name){
    global $_depth, $_tags, $_item;

    if (($name=="ITEM") ||($name=="CHANNEL") || ($name=="IMAGE") || ($name=="ENTRY")) {
        initArray();
    }
    @$_depth[$parser]++;
    array_push($_tags, $name);
}

function endElement($parser, $name){
    global $_depth, $_tags, $_item;

    array_pop($_tags);
    $_depth[$parser]--;
    switch ($name) {

        case "ITEM":
            echo "<p align=left><a href={$_item['LINK']}><b>{$_item['TITLE']}</b></a><br>".nl2br($_item['DESCRIPTION'])."<br></p>\n";
            initArray();
            break;
    }
}

function parseData($parser, $text){
    global $_depth, $_tags, $_item;

    $crap = preg_replace ("/\s/", "", $text);
    /* is the data just whitespace?
       if so, we don't want it! */

    if ($crap) {
        $text = preg_replace ("/^\s+/", "", $text);
        /* get rid of leading whitespace */
        if (@$_item[$_tags[$_depth[$parser]]]) {
            $_item[$_tags[$_depth[$parser]]] .= $text;
        } else {
            $_item[$_tags[$_depth[$parser]]] = $text;
        }
    }
}

function parseRDF($file){
    global $_depth, $_tags, $_item;

    $xml_parser = xml_parser_create();
    initArray();

    /* Set up event handlers */
    xml_set_element_handler($xml_parser, "startElement", "endElement");
    xml_set_character_data_handler($xml_parser, "parseData");

    /* Open up the file */
    $fp = fopen ($file, "r") or die ("Could not open $file for input");

    while ($data = fread ($fp, 4096)) {
        if (!xml_parse($xml_parser, $data, feof($fp))) {
            die (sprintf("XML error: %s at line %d", xml_error_string(xml_get_error_code($xml_parser)), xml_get_current_line_number($xml_parser)));
        }
    }

    fclose($fp);
    xml_parser_free($xml_parser);
}

parseRDF("http://apache2triad.net/phpbb2feed.php?type=rss");

?>
            </p>
            <p>&nbsp;            </p>
          </blockquote>
            </blockquote>						
    </TD>
    </TR>
  </TBODY>
</TABLE>
<TABLE width="99%" border=0 cellPadding=0 cellSpacing=0 class=ttb>
  <TBODY>
    <TR>
      <TD><IMG alt="" height=12 src="gfx/tb12_l.gif"
      width=10></TD>
      <TD class=tb12bkg><IMG alt="" height=12
      src="gfx/spacer.gif" width=200></TD>
      <TD><IMG alt="" height=12 src="gfx/tb12_r.gif"
      width=10></TD>
    </TR>
  </TBODY>
</TABLE>
<div>
  <div align="center">
<div align="center">
      <div align="center">
<div align="center"><b><span style="font-size:16.0pt"></span></b></div>
    <div align="center">
</div>
      </div>
    </div>
    <p><font color="#999999" size="1" face="Verdana, Arial, Helvetica, sans-serif">Apache2TriadCP by <a href="http://alexamancini.com" target="_blank">Vlad Alexa Mancini</a><br>
   
Programming by <a href="http://nextcode.org">NextCode</a> 
Graphics by <a href="http://nextdesign.eu.org">NextDesign</a> <br>
      <br>
            </font></p>
  </div>
</div>
</body>
</html>