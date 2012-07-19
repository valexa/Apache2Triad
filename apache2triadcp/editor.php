<?php
$WINDIR = $_SERVER["WINDIR"];
$uri = $_SERVER["PHP_SELF"];
$date = date("Ymd");
$realdate = date("Y.m.d");

preg_match ("/^.*?@(.*)$/",$_SERVER["SERVER_ADMIN"],$domain);
$curdomain = $domain[1];

$apachea = array ("The Apache access log","C:/apache2triadpath/logs/access.log");
$apachee = array ("The Apache error log","C:/apache2triadpath/logs/error.log");
$mysqla = array ("The Mysql access log","C:/apache2triadpath/mysql/logs/myaccess.log");
$mysqle = array ("The Mysql error log","C:/apache2triadpath/mysql/logs/myerror.log");
$openssla = array ("The OpenSSL access log","C:/apache2triadpath/logs/ssl_access.log");
$openssle = array ("The OpenSSL error log","C:/apache2triadpath/logs/ssl_error.log");
$phplog = array ("The Php error log","C:/apache2triadpath/php/logs/php_error.log");
$slimftpdlog = array ("The SlimFTPd log","C:/apache2triadpath/ftp/slimftpd.log");
$mailsent = array ("The log of mail sent thru our server on $realdate","C:/apache2triadpath/mail/logs/smail-{$date}0000");
$mailrec = array ("The log of mail received thru our server on $realdate","C:/apache2triadpath/mail/logs/smtp-{$date}0000");
$mailread = array ("The log of mail read thru our server on $realdate","C:/apache2triadpath/mail/logs/pop3-{$date}0000");
$pgsqllog = array ("The PostgreSQL log","C:/apache2triadpath/pgsql/data/pg_log/postgresql-{$date}.log");

$httpdconf = array ("The Apache configuration file","C:/apache2triadpath/conf/httpd.conf");
$opensslcnf = array ("The Openssl configuration file","C:/apache2triadpath/Opssl/bin/openssl.cnf");
$phpini = array ("The Php configuration file","$WINDIR/php.ini");
$myini = array ("The Mysql configuration file","$WINDIR/my.ini");
$awstatslocalhostconf = array ("The Awstats configuration file for $curdomain","C:/apache2triadpath/htdocs/awstats/awstats.$curdomain.conf");
$phpmyadminconfigincphp = array ("The Phpmyadmin configuration file","C:/apache2triadpath/htdocs/phpMyAdmin/config.inc.php");
$phpxmailconfigphp = array ("The PHPXmail configuration file","C:/apache2triadpath/htdocs/phpxmail/config.php");
$uebimiauincconfigphp = array ("The UebiMiau configuration file","C:/apache2triadpath/htdocs/uebimiau/inc/config.php");
$slimftpdconf = array ("The SlimFTPd configuration file","C:/apache2triadpath/ftp/slimftpd.conf");
$xmailconf = array ("The Xmail configuration file","C:/apache2triadpath/mail/server.tab");
$phpsftpdconf = array ("The PHPsFTPd configuration file","C:/apache2triadpath/htdocs/phpsftpd/inc.conf.php");
$pgsqlconf = array ("The PostgreSQL configuration file","C:/apache2triadpath/pgsql/data/postgresql.conf");
 

$load=$_GET['load'];
$mesage = ${$load}[0];
$file = ${$load}[1];

if($_POST['action'] == "Write to file"){
        $feed=stripslashes($_POST['feed']);
        $mesg = "Written modifications to $file";
        $fhw = fopen("$file", "w");
        $ok = fwrite ($fhw,"$feed");
        fclose ($fhw);
}

function show_size($fname){
        $size = filesize($fname)+1 or die ("could not open $fname");
        if ($size >= 1073741824){ $size = round($size / 1073741824 * 100) / 100 . ' Gb'; }
        elseif ($size >= 1048576){ $size = round($size / 1048576 * 100) / 100 . ' Mb'; }
        elseif ($size >= 1024){        $size = round($size / 1024 * 100) / 100 . ' Kb'; }
        elseif ($size > 0){ $size = $size . ' b'; }
        else{ $size = 'NA'; }
        echo $size;
}

?>

<html>
<title>Apache2Triad Editor : <?php echo $mesage; ?></title>
<link rel=stylesheet href=style.css>
<center>
<p><font size=5><?php echo $mesage; ?></font></p>
<font color=red><?php if (isset($mesg)){echo $mesg;}else{echo "This allows for remote editing of config files";} ?></font><br>
You are editing : <b><?php echo $file; ?></b>&nbsp;<?php show_size($file); ?>&nbsp;<br>
<?php
if (filesize($file) > 1048576){
        die("File size is bigger than 1 megabyte , refusing to load it ");
}
?>
<form name="form" method="post" action="<?php echo "{$uri}?load={$load}"; ?>">
<textarea class=input name="feed" rows="27" wrap="OFF" style="width:100%"><?php echo file_get_contents($file); ?></textarea>
<br><input class=button type=submit name=action value="Refresh"> <input class=button type=submit name=action value="Write to file">
</form>

</center>Written by Vlad Alexa Mancini</html>