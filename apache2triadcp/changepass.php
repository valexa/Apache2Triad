<?php

$WINDIR = $_SERVER["WINDIR"];

// files with plain-text passwords
$files = array ('C:\apache2triadpath\htdocs\apache2triadcp\proceses.cgi',
'C:\apache2triadpath\htdocs\apache2triadcp\test.mysql.php',
'C:\apache2triadpath\htdocs\phpsftpd\inc.conf.php',
'C:\apache2triadpath\ftp\slimftpd.conf',
$WINDIR.'\my.ini');

// files with xmail encrypted passwords
$xm_files = array ('C:\apache2triadpath\mail\ctrlaccounts.tab',
'C:\apache2triadpath\htdocs\phpxmail\servers.php',
'C:\apache2triadpath\mail\mailusers.tab');

// obvious really ......
$htpasswd_file = 'C:\apache2triadpath\htdocs\.htpasswd';
$htpasswd_exe = 'C:\apache2triadpath\bin\htpasswd.exe';

// xmail password encryption. phpxmail version
function xmcrypt ($password) {
    $crypt = "";
    for ($i = 0; $i < strlen($password); $i++) {
        $byte = dechex((ord(substr($password, $i, 1)) ^ 101) & 255);
        $byte = str_pad($byte, 2, '0', STR_PAD_LEFT);
        $crypt .= $byte;
    }
    return strtolower($crypt);
}

// replace $find with $repalce in $file
function replace_pass($file,$find,$replace) {
    $fh = fopen($file, "r");
    if (!$fh) {
        return 0;
    } else {
        $content = fread($fh, filesize($file));
        fclose($fh);
        $content = ereg_replace($find ,$replace, $content);
        $fh = fopen($file, "w");
        fwrite($fh, $content);
        fclose($fh);
        return 1;
    }
}

// check for script being in http_basic_auth zone
if ($_SERVER['PHP_AUTH_PW']) {
    $plain_pass['old'] = addslashes($_SERVER['PHP_AUTH_PW']);
    $plain_pass['old'] = stripslashes($plain_pass['old']);
} else {
    die("You need to be authenticated in order to run this script");
}

// check for form submital
if (isset($_GET['cmd']) && $_GET['cmd']=="change_passwords") {

    // check for blank password
    if (empty($_POST['pass_new'])) {
        die("You submitted a blank password, please try again");
    } else {
        $plain_pass['old'] = addslashes($PHP_AUTH_PW);
        $plain_pass['old'] = stripslashes($plain_pass['old']);
        $plain_pass['new'] = addslashes($_POST['pass_new']);
        $plain_pass['new'] = stripslashes($_POST['pass_new']);

        // check for illegal chars
        if (preg_match("/\W/", $plain_pass['new'])) {
            die("Passwords may only contain alphanumeric chars");
        }
    }

    // encrypt passwords for xmail
    $xm_pass['old'] = xmcrypt($plain_pass['old']);
    $xm_pass['new'] = xmcrypt($plain_pass['new']);

    // start changing passwords. die on mysql errors
    mysql_connect('localhost', 'root', $plain_pass['old']) or die ("Unable to connect to the mysql server. Check that it's running");
    mysql_select_db('mysql') or die ("Unable to select database!");
    mysql_query("UPDATE user SET Password=PASSWORD('".mysql_escape_string($plain_pass['new'])."') WHERE user='root'") or die("Unable to set mysql password");
    mysql_query("FLUSH PRIVILEGES");
    mysql_close();
    // mysql pass changed. must NOT die

    // set http_auth password
    $hpassword = $plain_pass['new'];
    system("$htpasswd_exe -b $htpasswd_file root $hpassword");
    
    // set windows password for apache2triad user 
    system("net user apache2triad ". $plain_pass['new']); 
     
    // set PgSQl Login Password In Services 
    system("sc config PgSql password=". $plain_pass['new']); 
     
    // set slimftpd login password in services 
    system("sc config SlimFTPd password=". $plain_pass['new']); 

    // setup array for list of files in which replace_pass() failed
    $errorList = array();

    // replace ecrytped passwords in $xm_files
    foreach ($xm_files as $xm_file) {
        $res = replace_pass($xm_file, $xm_pass['old'], $xm_pass['new']);
        // if replace_pass() failed, add filename to list of failed files
        if ($res=="0") { $errorList[] = $xm_file; }
    }
    // replace plain-text passwords in $files
    foreach ($files as $file) {
        $res = replace_pass($file, $plain_pass['old'], $plain_pass['new']);
        // if replace_pass() failed, add filename to list of failed files
        if ($res=="0") { $errorList[] = $file; }
    }

    // succes message with final passwords
    $success = "<p><font size=4 color=red>Password has been changed<br>From: <b>".htmlspecialchars($plain_pass['old'])."</b> to: <b>".htmlspecialchars($plain_pass['new'])."</b></font><br><a href=javascript:history.go(-2)>Go Back</a></p>\n";
}

// html
?>
<html><head>
<link rel=stylesheet href=style.css>
<title>Apache2Triad password update tool</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head><body>
<center>
<p><font size=5>Password update tool</font></p>
<?php

// print success message if exists
echo $success;

// print list of files in which replace_pass() failed if exists
if (sizeof($errorList) != 0) {
    echo "<font color=red><p>Failed replacing password in the following file(s):\n  <ul>\n";
    for ($x=0; $x<sizeof($errorList); $x++) { echo "    <li>$errorList[$x]\n"; }
    echo "  </ul></p>\n<p>You should now manually replace the password in the above files</p></font>\n";
}

//more html
?>
<p>This script will update all the files that use it with a new password.
<br>You must not have a password with common or dictionary words because of security and because this script can
<br>break the files it modifies if your password for example is "mysql" and you change it to "somethingelse"
<br>A good example password is "10your23name45"
<br><font color=red>Its best that you now restart the services or the computer for xmail and slimftpd to update their settings</font>
<br><br>
</p>
<form name="changepass" method="post" action="?cmd=change_passwords">
  <table width="100%"  border="0">
    <tr>
      <td width="50%" align="right">Old Password : </td>
      <td width="50%" align="left"><input class=input name="pass_old" type="text" value="<? echo htmlspecialchars($plain_pass['old']); ?>" disabled></td></tr>
    <tr>
      <td align="right">New Password : </td>
      <td align="left"><input class=input name="pass_new" type="text" value="<? echo htmlspecialchars($plain_pass['new']); ?>"> (case-sensitive)</td>
    </tr>
  </table>
  <p><input class=button type=submit value="Change Pass"></p>
</form>
<br>
</center>Written by Mark Magiera Kolatracks</html>