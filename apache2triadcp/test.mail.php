<link rel=stylesheet href=style.css>
<title>Apache2Triad PHP mail() test script</title><body><center><p>&nbsp;</p>
<p><font size=5>PHP mail() test script</font></p>
<p>This script sends a email to the apache serveradmin email adress ( <?php echo $_SERVER["SERVER_ADMIN"]; ?> )</p>
<font color=red>If you want to test other local email adresses you have to create them first<br></font>

<?php
//if emal is set send email notice
if ($submit && $subject && $body && $mail_to) {
	$mail_to  = $_SERVER["SERVER_ADMIN"];
	$mail_from= $_SERVER["SERVER_ADMIN"];
	$subject = $_POST['subject'];
	$body = $_POST['body'];
	$headers = "Return-Path: $mail_from\nFrom: $mail_from\nX-Mailer: PHPmail";
	mail($mail_to, $subject, $body, $headers);
echo "Email sucesfully sent to $mail_to<br>";
echo "All done<br>";
echo "<a href=javascript:history.go(-2)>Go Back</a>";
}
?>

<form action=test.mail.php method=post>
Email : <input class=input type=text size=59 maxlength=40 name=mail_to value=<?php echo $_SERVER["SERVER_ADMIN"]; ?> ><br>
Subject :<input class=input type=text size=58 maxlength=40 name=subject value="Apache2triad mail test"><br>
<textarea class=input name=body cols=50 rows=20 wrap=VIRTUAL>
Mailserver test email

Your mail server and php config is ok

and php mail() is working fine
</textarea><br>
<input class=button type=submit name=submit value="Send the test mail"></form>


</center>Written by Vlad Alexa Mancini</html>
