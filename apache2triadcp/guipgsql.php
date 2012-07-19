<html>
<head>
<link rel=stylesheet href=style.css>
<title>Apache2Triad PostgreSQL Configuration GUI</title>
</head>
<body>
<center>
<font size=5>Apache2Triad PostgreSQL Configuration</font><br><br>
<font color=red>After running this script you should restart pgsql for changes to take effect.</font><br>
<?php

$PHP = new Config ("C:/apache2triadpath/pgsql/data/postgresql.conf ");

$PHP->Var_Checkname =array ('foo');

$PHP->Var_Checktext =array ("Bar");

$PHP->Var_Name =array ("listen_addresses =",
"port =",
"max_locks_per_transaction =",
"deadlock_timeout =",
"ssl =",
"password_encryption =",
"log_connections =",
"log_disconnections =",
"log_hostname =");

$PHP->Var_Text =array ("Address",
"Port",
"Locks Per Transaction",
"Deadlock Timeout",
"Enable SSL",
"Password Encryption",
"Log Connections",
"Log Disconnections",
"Log Hostnames");

$PHP->Var_Desc =array ("The IP address/hostname the server will listen on",
"The port number the server will listen on",
"Min 10, ~200*max_connections bytes each",
"Deadlock timeout in milliseconds",
"Whether to enable SSL encrypted connections (true/false)",
"Whether to use password encryption (true/false)",
"Whether to log connections (true/false)",
"Whether to log disconnections (true/false)",
"Whether to log hostnames (true/false)");

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