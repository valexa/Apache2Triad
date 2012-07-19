<html>
<head>
<link rel=stylesheet href=style.css>
<title>Apache2Triad Mysql Configuration GUI</title>
</head>
<body>
<center>
<font size=5>Apache2Triad Mysql Configuration</font><br><br>
<font color=red>After running this script you should restart mysql for changes to take effect.</font><br>
<?php

$WINDIR = $_SERVER["WINDIR"];
$PHP = new Config ("$WINDIR\my.ini");

$PHP->Var_Checkname =array ('log-bin','log-warnings','skip-bdb','skip-innodb');

$PHP->Var_Checktext =array ("Log Binary","Log Warnings","Disable BerkleyDB Support"," Disable InnoDb Support");

$PHP->Var_Name =array ("bind-address =",
"port =",
"slave-load-tmpdir =",
"tmpdir =",
"basedir =",
"datadir =",
"log =",
"log-error =");

$PHP->Var_Text =array ("Address",
"Port",
"SlaveLoad Tmpdir",
"Temp Directory",
"Base Directory",
"Data Directory",
"Log File",
"Error Log File");

$PHP->Var_Desc =array ("The IP address the server will listen on",
"The port number the server will listen on",
"Temporary directory for slave loading",
"Temporary directory",
"The base directory",
"The data directory",
"The path and name of the access log",
"The path and name of the error log");

$step=$_POST['Submit'];
if ($step=="Save Changes") {
    $PHP->replace_checkvalues ($_POST);
    $PHP->replace_values ($_POST);
    echo "<font color=red><b>Your changes have been made sucssesfuly.</b></font><br><br>";
}
echo '<form action="'.$_SERVER["PHP_SELF"].'" name=f method="POST">';
$PHP->echo_checkvalues ();
$PHP->echo_values ();
echo '<br><br><input class=button type=submit value="Save Changes" name=Submit></form>'."\n";
class Config {
    var $contents;
    var $name;
    var $Var_Checkname;
    var $Var_Checktext;
    var $Var_Name;
    var $Var_Text;
    var $Var_Desc;
    var $classnum;

    function Config ($file_name) {
        $this->name=$file_name;
        $fd = fopen ($this->name, "r");
        $this->contents = fread ($fd, filesize ($file_name));
        fclose ($fd);
        $this->classnumber=$GLOBALS["$Configclassnumber"]=$GLOBALS["$Configclassnumber"]+1;
    }

    function f_write () {
        $fd = fopen ($this->name, "w");
        $ok = fwrite ($fd, $this->contents);
        fclose ($fd);
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
                echo '<b>[ '.$Var_Checktext.'<input type=checkbox name="'.$Var_ID.'" value="Enable" checked> ] </b>'."\n";
            } elseif (preg_match('/\n#'.$Var_Checkname.'/i', $this->contents)) {
                echo '<b>[ '.$Var_Checktext.'<input type=checkbox name="'.$Var_ID.'" value="Enable"> ] </b>'."\n";
            }
            $item=$item+1;
        }
        echo "<br></div>";
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
                $this->contents=preg_replace('/\n#'.$loop.'/i', "\n\\1$loop", $this->contents, 1);
            } elseif (isset($data) && $data=="Disable") {
                $this->contents=preg_replace('/\n'.$loop.'/i', "\n#\\1$loop", $this->contents, 1);
            }
            $item=$item+1;
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
</center>Written by Vlad Alexa Mancini</html>