<html>
<head>
<link rel=stylesheet href=style.css>
<title>Apache2Triad PHP Configuration GUI</title>
</head>
<body>
<center>
<font size=5>Apache2Triad PHP Configuration</font><br><br>
<font color=red>After running this script you should restart apache for changes to take effect.</font><br>
To enable Zend Optimizer the script will disable all the other two extensions, and to enable other extensions you need to disable Zend Optimizer.<br>
<?php

$PHP = new Config ($_SERVER["WINDIR"]."\php.ini");

$PHP->Var_Compatname =array ('zend_extension_ts = C:\apache2triadpath\php\extensions\zendoptimizer.dll');

$PHP->Var_Compattext =array ("Zend Optimizer");

$PHP->Var_Checkname =array ('extension = xdebug.dll','extension = dbg.dll');

$PHP->Var_Checktext =array ("Xdebug","Dbg Extension");

$PHP->Var_Name =array ("safe_mode =",
"expose_php =",
"register_globals =",
"magic_quotes_gpc =",
"register_long_arrays =",
"register_argc_argv =",
"max_execution_time =",
"memory_limit =",
"display_errors =",
"html_errors =",
"mysql.trace_mode =",
"post_max_size =",
"upload_max_filesize =",
"SMTP =",
"sendmail_from =",
"asp_tags =",
"cgi.nph =",
"session.use_cookies =");

$PHP->Var_Text =array ("PHP Safe mode",
"Show PHP signature",
"Register globals",
"Magic gpg quotes",
"Register long arrays",
"Register Argc Argv",
"Maximum execution time",
"Memory limit per script",
"Show errors in browser",
"Show HTML in errors",
"Trace Mysql errors",
"Maximum size of POST data",
"Maximum size for uploads",
"SMTP Server",
"Email Address for Sendmail",
"Enable ASP tags",
"Enable CGI NPH Status",
"Enable use of session cookies");

$PHP->Var_Desc =array ("Where On enables PHP's safe mode",
"When On PHP exposes itself by adding its signature to the header",
"When On the EGPCS (Environment, GET, POST, Cookie, Server) variables are registered as global variables",
"Magic gpc quotes for automatically escaping incoming GET/POST/Cookie data",
"Whether or not to register the old-style input arrays like HTTP_GET_VARS,disable for performance",
"Whether or not to declare the argv&argc variables which contain the GET info, disable for performance",
"In seconds, the maximum time each script is allowed to run before it is terminated by PHP",
"8M = 8MB . Specifies the maximum amount of memory in bytes allocated per script",
"When On errors will be shown on screen as part of the HTML output",
"Enable the inclusion of HTML tags in error messages,not for production boxes",
"Warnings for table or index scans and SQL errors will be displayed",
"8M = 8MB, Sets max size of post data allowed. This setting also affects file upload",
"Where 2M = 2MB. Specifies the maximum allowed size for an uploaded file",
"A valid DNS name or IP address of the SMTP server PHP should use to send mail",
"A valid From: address on the above server. Specifies which address should be used to send mail",
"Where On enables the use of ASP-like >% %< tags in addition to the usual >?php ?< tags",
"Valid values are: 1, 0. If cgi.nph is enabled it will force cgi to always sent Status: 200 with every request",
"Valid values are: 1, 0. When set to 1 the module will use cookies to store the session id on the client side");

$step=$_POST['Submit'];
if ($step=="Save Changes") {
    $PHP->replace_checkvalues ($_POST);
    $PHP->replace_compatvalues ($_POST);
    $PHP->replace_values ($_POST);
    echo "<font color=red><b>Your changes have been made sucssesfuly.</b></font><br><br>";
}
echo '<form action="'.$_SERVER["PHP_SELF"].'" name=f method="POST">';
echo "<b>[ <a href=dbg.php?action=register>Register Dbg Listener</a> ]&nbsp;[ <a href=dbg.php?action=unregister>Unregister Dbg Listener</a> ]</b>";
$PHP->echo_checkvalues ();
$PHP->echo_compatvalues ();
$PHP->echo_values ();
echo '<br><br><input class=button type=submit value="Save Changes" name=Submit></form>'."\n";
class Config {
    var $contents;
    var $name;
    var $Var_Compatname;
    var $Var_Compattext;
    var $Var_Checkname;
    var $Var_Checktext;
    var $Var_Name;
    var $Var_Text;
    var $Var_Desc;
    var $classnum;

    function Config ($file_name) {
        $this->name=$file_name;
        $fd = fopen ($this->name, "r") or die("Could not open ".$this->name);
        $this->contents = fread ($fd, filesize ($file_name)) or die("Could not read ".$this->name);
        fclose ($fd) or die("Could not close ".$this->name);
        $this->classnumber=$GLOBALS["$Configclassnumber"]=$GLOBALS["$Configclassnumber"]+1;
    }

    function f_write () {
        $fd = fopen ($this->name, "w") or die("Could not open ".$this->name);
        $ok = fwrite ($fd, $this->contents) or die("Could not write to ".$this->name);
        fclose ($fd) or die("Could not close ".$this->name);
    }

    function echo_checkvalues () {
        $item=0;
        echo '<div align=center>';
        foreach ($this->Var_Checkname as $loop) {
            $Var_ID="C1".$this->classnumber."i".$item;
            $Var_Checkname=$this->Var_Checkname[$item];
            $Var_Checktext=$this->Var_Checktext[$item];
            echo '<input type="hidden" name="'.$Var_ID.'" value="Disable">';
            if (preg_match('/\n'.$Var_Checkname.'/i', $this->contents)) {
                echo '<b>[ Enable '.$Var_Checktext.'<input type=checkbox name="'.$Var_ID.'" value="Enable" checked> ] </b>'."\n";
            } elseif (preg_match('/\n;'.$Var_Checkname.'/i', $this->contents)) {
                echo '<b>[ Enable '.$Var_Checktext.'<input type=checkbox name="'.$Var_ID.'" value="Enable"> ] </b>'."\n";
            }
            $item=$item+1;
        }
        echo "<br></div>";
    }

    function echo_compatvalues () {
        $item=0;
        echo '<div align=center>';
        foreach ($this->Var_Compatname as $loop) {
            unset($enabled);
            unset($disabled);
            $Var_Compatname=$this->Var_Compatname[$item];
            $Var_Compattext=$this->Var_Compattext[$item];
            if (strstr($this->contents, "\n".$Var_Compatname)) {
                $enabled = "checked";
            } elseif (strstr($this->contents, "\n;".$Var_Compatname)) {
                $disabled = "checked";
            }
            echo '<b>[ <font color=red>Enable '.$Var_Compattext.'</font><input type=radio name="C2" value="'.$item.'" '.$enabled.'> ] </b>'."\n";
            $item=$item+1;
        }
        echo '<b>[ <font color=red>Disabled</font><input type=radio name="C2" value="Disable" '.$disabled.'> ] </b><br></div>';
    }

    function echo_values () {
        echo '<table width="100%" valign="top" border="0" cellspacing="0" cellpadding="0">';
        $item=0;
        foreach ($this->Var_Name as $loop) {
            $Var_ID="C3".$this->classnumber."i".$item;
            $Var_Name=$this->Var_Name[$item];
            $Var_Text=$this->Var_Text[$item];
            preg_match("/\n\s*$Var_Name\s+([^\n]+)/i", $this->contents, $tag);
            echo '<tr><td valign="top" align="right" width="30%"><br><b>'.$Var_Text.' :</b></td>';
            echo '<td><br><input class=input type=text name="'.$Var_ID.'" size=75 maxlength=2048 value="'.$tag[1].'"><br>'.$Var_Desc=$this->Var_Desc[$item].'.</td></tr>'."\n";
            $item=$item+1;
        }
        echo "</table>";
    }

    function replace_checkvalues ($_POST) {
        $item=0;
        foreach ($this->Var_Checkname as $loop) {
            $Var_ID="C1".$this->classnumber."i".$item;
            $data=$_POST[$Var_ID];
            if (isset($data) && $data=="Enable") {
                $this->contents=str_replace("\n;$loop", "\n$loop", $this->contents) or die ("Configuration replace failed");
            } elseif (isset($data) && $data=="Disable") {
                $this->contents=str_replace("\n$loop", "\n;$loop", $this->contents) or die ("Configuration replace failed");
            }
            $item=$item+1;
        }
        $this->f_write ();
    }

    function replace_compatvalues ($_POST) {
        $data=$_POST['C2'];
        if (isset($data) && is_numeric($data)) {
            foreach ($this->Var_Checkname as $loop) {
                $this->contents=str_replace("\n$loop", "\n;$loop", $this->contents) or die ("Configuration replace failed");
            }
            foreach ($this->Var_Compatname as $loop) {
                $this->contents=str_replace("\n$loop", "\n;$loop", $this->contents) or die ("Configuration replace failed");
            }
            $this->contents=str_replace("\n;".$this->Var_Compatname[$data], "\n".$this->Var_Compatname[$data], $this->contents);
        } elseif (isset($data) && $data=="Disable") {
            foreach ($this->Var_Compatname as $loop) {
                $this->contents=str_replace("\n$loop", "\n;$loop", $this->contents) or die ("Configuration replace failed");
            }
        }
        $this->f_write ();
    }

    function replace_values ($_POST) {
        $item=0;
        foreach ($this->Var_Name as $loop) {
            $Var_ID="C3".$this->classnumber."i".$item;
            $data=$_POST[$Var_ID];
            $this->contents=preg_replace("/\n(s*$loop)\s+([^\n]+)/i", "\n\\1 $data\r", $this->contents, 1);
            $item=$item+1;
        }
        $this->f_write ();
    }
}

?>
<br>
</center>Written by Mark Magiera Kolatracks</html>