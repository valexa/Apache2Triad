#!C:/apache2triadpath/perl/bin/perl.exe

print "Content-type: text/html\n\n";

$sendmail = 'C:\apache2triadpath\mail\bin\sendmail.exe';

$FORM{'act'} = '';

&parseform();

if ($FORM{'act'}eq'Send the test mail'){
print "<title>Apache2Triad sendmail test script</title>";
&action;
}else{
&entry;
}
exit;

sub parseform() {
if($ENV{'REQUEST_METHOD'} eq 'GET'){
$buffer=$ENV{'QUERY_STRING'}; 
}elsif($ENV{'REQUEST_METHOD'} eq 'POST'){ 
read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});} 
@pairs = split(/&/, $buffer);
foreach $pair (@pairs) {
($name, $value) = split(/=/, $pair);
$value =~ tr/+/ /;
$value =~s/%([a-fA-F0-9][a-fA-F0-9])/pack("c",hex($1))/eg; 
$FORM{$name} = $value;}
}


sub entry {
print "<link rel=stylesheet href=style.css>
<title>Apache2Triad sendmail test script</title><body><center><p>&nbsp;</p>
<p><font size=5>Sendmail test script</font></p>
<p>This script sends a email to the apache serveradmin email adress ( $ENV{'SERVER_ADMIN'} )</p>
<font color=red>If you want to test other local email adresses you have to create them first<br></font>
";


print "<form  action=$ENV{SCRIPT_NAME} method=post>
Email : <input class=input type=text size=59 maxlength=40 name=email_to value=$ENV{'SERVER_ADMIN'}><br>
Subject :<input class=input type=text size=58 maxlength=40 name=subject value=\"Apache2triad mail test\"><br>
<textarea class=input name=body cols=50 rows=20 wrap=VIRTUAL>
Mailserver test email\n
Your mail server is ok ,sendmail is in :\n
C:/apache2triadpath/mail/bin/sendmail.exe\n
</textarea><br>
<input class=button type=submit name=act value=\"Send the test mail\"></form>";

print "</center>Written by Vlad Alexa Mancini</html>";

}


sub action {

$email_to = $FORM{'email_to'};
$email_from = $ENV{'SERVER_ADMIN'};
$body = $FORM{'body'};
$subject = $FORM{'subject'};

open (MAIL, "|$sendmail $email_to") or die ("Can't open $sendmail");
print MAIL "Subject: $subject\n";
print MAIL "To: $email_to\n";
print MAIL "From: $email_from\n";
print MAIL "Return-Path: $email_from\n";
print MAIL "X-Mailer: Sendmail\n";
print MAIL qq!
$body

!;
close(MAIL);

print "Email sucesfully sent to $email_to<br>";

print "All done<br>";

print "<a href=javascript:history.go(-2)>Go Back</a>";

}
exit;
