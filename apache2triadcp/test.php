<html>
<link rel=stylesheet href=style.css>
<center>
<span class=span0><span class=span1>

<b><?php echo "PHP is working fine"; ?></b>

<br><br>
<b>server software : </b><?php echo $_SERVER["SERVER_SOFTWARE"]; ?>
<br><br>
<b>client software : </b><?php echo $_SERVER["HTTP_USER_AGENT"]; ?>
<br><br>
<b>http referer : </b><?php echo $_SERVER["HTTP_REFERER"]; ?>
<br><br>
<b>opened file : </b><?php echo $_SERVER["SCRIPT_FILENAME"]; ?>
<br><br>
<b>server adress :</b><?php echo $_SERVER["HTTP_HOST"]; ?>
<br><br>
<b>your adress : </b><?php echo $_SERVER["REMOTE_ADDR"]; ?>
</span></span>

<table width=88% class=table border=0 cellpadding=4 cellspacing=1>
<tr><td class=tdark ><b>Server Variable</b></td><td class=tdg ><b>Value</b></td></tr>

<?php foreach($_SERVER as $variable=> $value) { ?>

<tr><td class=tdd><font size=-1><?php echo "$variable"; ?></font></td>
<td class=tdl><font size=-1><?php echo "$value"; ?>&nbsp;</font></td></tr>

<?php } ?>
</table></p></font>

</center>Written by Vlad Alexa Mancini</html>