<html>
<link rel=stylesheet href=style.css>
<center>
<span class=span0><span class=span1>
<?php
if (extension_loaded('mysql')) {
    echo "<b>The mysql php extension is loaded</b><br><br>";
}else{
    echo "<b>The mysql php extension is not loaded</b>";
    die;
}
?>
<b>
<?php
$dbhost = "localhost";
$dbname = "mysql";
$dbuser = "root";
$dbpass = "apache2triadpass";
$dbtab = "user";

$link = mysql_connect($dbhost, $dbuser, $dbpass) or die ("Could not connect to $dbname on $dbhost with $dbuser@".$_SERVER[REMOTE_ADDR]);
echo "Connected successfully to $dbname on $dbhost with $dbuser@".$_SERVER[REMOTE_ADDR]."<br>\n";
mysql_select_db ($dbname) or die ("Could not select database named : $dbname" . mysql_error());
$query = "SELECT Host,User,Password,Super_priv FROM $dbtab";
$result = mysql_query ($query) or die ("Query failed for table : $dbtab . " . mysql_error());
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
<td class=tdark><b>Host</b></td>
<td class=tdg><b>User</b></td>
<td  class=tdark><b>Password</b></td>
<td class=tdg><b>Superadmin</b></td>
</tr>
<?php
while ($line = mysql_fetch_assoc($result)) {
echo "<tr><td class=tdd>".$line['Host']."&nbsp;</td>";
echo "<td class=tdl>".$line['User']."&nbsp;</td>";
echo "<td class=tdd>".$line['Password']."&nbsp;</td>";
echo "<td class=tdl>".$line['Super_priv']."&nbsp;</td></tr>";
}
?>
<tr>
<td colspan=4 bgcolor=#D4D4D4><b>Databases</b></td>
</tr>
<?php
$db_list = mysql_list_dbs($link);
$db = "0";
while ($row = mysql_fetch_object($db_list)) {
                if (preg_match ("/0|4|8/", $db)){
                        print "<tr><td class=tdl> $row->Database </td>";
                }
                if (preg_match ("/3|7/", $db)){
                        print "<td class=tdl> $row->Database </td></tr>";
                }
                if (preg_match ("/1|2|5|6|9/", $db)){
                print "<td class=tdl> $row->Database </td>";
                }
                $db = $db + 1;
}
?>
<tr>
<td class=tdark><b>Server Version</b></td>
<td class=tdg><b>Client Version</b></td>
<td class=tdark><b>Host Information</b></td>
<td class=tdg><b>Protocol Information</b></td>
</tr>
<tr>
<td class=tdd><?php echo mysql_get_server_info(); ?></td>
<td class=tdl><?php echo mysql_get_client_info(); ?> </td>
<td class=tdd><?php echo mysql_get_host_info(); ?> </td>
<td class=tdl><?php echo mysql_get_proto_info(); ?> </td>
</tr>

<tr>
<td colspan=4 class=tdark><b>MySQL Status</b></td>
</tr>
<tr>
<td colspan=4 class=tdl><div align="center"><font face=Arial size=2>
<?php
print_r(mysql_stat($link));
?>
</font></div></td>
</tr>
<?php
mysql_close($link);
?>
</table></p></font>
</center>Written by Vlad Alexa Mancini</html>