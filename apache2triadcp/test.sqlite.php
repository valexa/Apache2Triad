<html>
<link rel=stylesheet href=style.css>
<center>
<span class=span0><span class=span1>
<?php
if (extension_loaded('sqlite')) {
    echo "<b>The sqlite php extension is loaded</b><br><br>";
}else{
    echo "<b>The sqlite php extension is not loaded</b>";
    die;
}
?>
<b>
<?php
$dbhost = "";
$dbname = "C:\apache2triadpath\htdocs\phpsqliteadmin\phpsla.sqlite";
$dbuser = "";
$dbpass = "";
$dbtab = "users";

$link = sqlite_open($dbname) or die ("Could not connect to $dbname on $dbhost with $dbuser@".$_SERVER[REMOTE_ADDR]);
echo "Connected successfully to $dbname on $dbhost with $dbuser@".$_SERVER[REMOTE_ADDR]."<br>\n";
$query = "SELECT login,password,realname,email FROM $dbtab";
$result = sqlite_query ($query,$link) or die ("Query failed for table : $dbtab . " . sqlite_error_string(sqlite_last_error($link)));
?>
</b>

<br><br>
<b>host : </b><?php echo $dbhost; ?>
<br><br>
<b>user : </b><?php echo $dbuser; ?>
<br><br>
<b>password : </b><?php echo $dbpass; ?>
<br><br>
<b>database : </b><?php echo $dbname; ?>
<br><br>
<b>table : </b><?php echo $dbtab; ?>
</span></span>

<table width=88% class=table border=0 cellpadding=4 cellspacing=1>

<tr>
<td class=tdark><b>Mail</b></td>
<td class=tdg><b>User</b></td>
<td  class=tdark><b>Password</b></td>
<td class=tdg><b>Name</b></td>
</tr>
<?php
while ($line = sqlite_fetch_array($result)) {
echo "<tr><td class=tdd>".$line['email']."&nbsp;</td>";
echo "<td class=tdl>".$line['login']."&nbsp;</td>";
echo "<td class=tdd>".$line['password']."&nbsp;</td>";
echo "<td class=tdl>".$line['realname']."&nbsp;</td></tr>";
}
?>
<tr>
<td colspan=4 bgcolor=#D4D4D4><b>Databases</b></td>
</tr>
<?php
                print "<tr><td class=tdl> phpsla.sqlite </td>";
                print "<td class=tdl colspan=3 align=center> SQLite does not mantain list of databases </td></tr>";
?>
<tr>
<td class=tdark><b>Server Version</b></td>
<td class=tdg><b>Client Version</b></td>
<td class=tdark><b>Host Information</b></td>
<td class=tdg><b>Protocol Information</b></td>
</tr>
<tr>
<td class=tdd><?php echo sqlite_libversion(); ?></td>
<td class=tdl><?php echo phpversion(); ?> </td>
<td class=tdd><?php echo $_SERVER['SERVER_SOFTWARE']; ?> </td>
<td class=tdl><?php echo $_SERVER['SERVER_PROTOCOL']; ?> </td>
</tr>

<tr>
<td colspan=4 class=tdark><b>SQLite Version</b></td>
</tr>
<tr>
<td colspan=4 class=tdl><div align="center"><font face=Arial size=2>
<?php
ob_start();
phpinfo();
$php_info .= ob_get_contents();
ob_end_clean();
preg_match ("/<td class=\"v\">(.*?sqlite\.c.*?)<\/td>/",$php_info,$info);
echo $info['1'];
?>
</font></div></td>
</tr>
<?php
sqlite_close($link);
?>
</table></p></font>
</center>Written by Vlad Alexa Mancini</html>