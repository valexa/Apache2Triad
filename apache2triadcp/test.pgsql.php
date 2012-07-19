<html>
<link rel=stylesheet href=style.css>
<center>
<span class=span0><span class=span1>
<?php
if (extension_loaded('pgsql')) {
    echo "<b>The pgsql php extension is loaded</b><br><br>";
}else{
    echo "<b>The pgsql php extension is not loaded</b>";
    die;
}
?>
<b>
<?php
$dbhost = "localhost";
$dbname = "template1";
$dbuser = "root";
$dbpass = "";
$dbtab = "pg_user";

$link = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass") or die ("Could not connect to $dbname on $dbhost with $dbuser@".$_SERVER[REMOTE_ADDR]);
echo "Connected successfully to $dbname on $dbhost with $dbuser@".$_SERVER[REMOTE_ADDR]."<br>\n";
if (pg_connection_busy($link)){die("Postgres server is busy, canceled execution.");}
$query = "SELECT usename,passwd,usesuper FROM $dbtab";
$result = pg_query($query) or die ("Query failed for table : $dbtab . ". pg_last_error($link));
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
while ($line = pg_fetch_assoc($result)) {
echo "<tr><td class=tdd>".$line['host']."&nbsp;</td>";
echo "<td class=tdl>".$line['usename']."&nbsp;</td>";
echo "<td class=tdd>".$line['passwd']."&nbsp;</td>";
echo "<td class=tdl>".$line['usesuper']."&nbsp;</td></tr>";
}
?>
<tr>
<td colspan=4 bgcolor=#D4D4D4><b>Databases</b></td>
</tr>
<?php
$db_list = pg_query("SELECT datname FROM pg_database");
$db = "0";
while ($row = pg_fetch_object($db_list)) {
                if (preg_match ("/0|4|8/", $db)){
                        print "<tr><td class=tdl> $row->datname </td>";
                }
                if (preg_match ("/3|7/", $db)){
                        print "<td class=tdl> $row->datname </td></tr>";
                }
                if (preg_match ("/1|2|5|6|9/", $db)){
                print "<td class=tdl> $row->datname </td>";
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
<?php $info = pg_version($link); ?>
<td class=tdd><?php echo pg_parameter_status($link,version); ?></td>
<td class=tdl><?php echo $info[client]; ?></td>
<td class=tdd>pg_parameter_status() not great in php</td>
<td class=tdl>serious status info not supported yet in pgsql</td>
</tr>
<tr>
<td colspan=4 class=tdark><b>PgSQL Version</b></td>
</tr>
<tr>
<td colspan=4 class=tdl><div align="center"><font face=Arial size=2>
<?php
$pg_version = pg_query("SELECT VERSION() AS version");
$version = pg_fetch_array($pg_version);
echo $version['version'];
?>
</font></div></td>
</tr>
<?php
pg_close($link);
?>
</table></p></font>
</center>Written by Vlad Alexa Mancini</html>