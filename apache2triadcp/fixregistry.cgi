#!C:/apache2triadpath/perl/bin/perl.exe

print "Content-type: text/html\n\n";

use Win32::TieRegistry;

$Registry->Delimiter('/');

$k = "HKEY_LOCAL_MACHINE/System/CurrentControlSet";
$k1 = "HKEY_LOCAL_MACHINE/System/ControlSet001";
$k2 = "HKEY_LOCAL_MACHINE/System/ControlSet002";
@keys = ("$k/Services/mysql/","$k1/Services/mysql/","$k2/Services/mysql/");
@dkeys = ("$k/Services/Apache2+PHP+Perl/","$k1/Services/Apache2+PHP+Perl/","$k2/Services/Apache2+PHP+Perl/",
	"$k/Services/Apache2+PHP+Perl+SSL+MySQL/","$k1/Services/Apache2+PHP+Perl+SSL+MySQL/","$k2/Services/Apache2+PHP+Perl+SSL+MySQL/",
	"$k/Services/Apache2+PHP+SSL/","$k1/Services/Apache2+PHP+SSL/","$k2/Services/Apache2+PHP+SSL/",
	"$k/Services/Apache2+PHP/","$k1/Services/Apache2+PHP/","$k2/Services/Apache2+PHP/",
	"$k/Services/Apache2+PHP+Perl+Python+SSL/","$k1/Services/Apache2+PHP+Perl+Python+SSL/","$k2/Services/Apache2+PHP+Perl+Python+SSL/",
	"$k/Services/Apache2+PHP+Perl+Python/","$k1/Services/Apache2+PHP+Perl+Python/","$k2/Services/Apache2+PHP+Perl+Python/");

$FORM{'act'} = '';

&parseform();

if ($FORM{'act'}eq'Fix the found registry strings'){
print "<link rel=stylesheet href=style.css><title>Apache2Triad registry keys clean tool</title>";
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
print "<link rel=stylesheet href=style.css><title>Apache2Triad registry keys clean tool</title><body><center><p>&nbsp;</p>
<p><font size=5>Registry keys clean tool</font></p>
<p>This script will fix mysql registry keys from a old mysql instalation , with wrong service paths,  known to cause problems for apache2triad.</p>";

foreach $dkey (@dkeys){
		if (defined $Registry->{$dkey}) {
		push (@dkey,"$dkey");
		}
}
if (scalar(@dkey) ne "0"){
	$number = scalar(@dkey);
	print "<font color=red><b>Found $number bad keys</b>(old services)</font><br><br>";
}

foreach $keys (@keys){
	if (defined $Registry->{$keys}) {
		print "<b>$keys</b> exists<br>";
		push (@keys1,"$keys");
	}else{
		print "<b>$keys</b> does not exist<br>";
	}	
}

print "<br>";

foreach $keys1 (@keys1){
	$diskKey= $Registry->{"$keys1"} or  print "Can't read <b>$keys1</b> key: $^E\n";
	$data= $diskKey->{"/ImagePath"} or  print "Can't read $keys1<b>/ImagePath</b> value: $^E<br>";
	if ($data eq "C:\\apache2triadpath\\mysql\\bin\\mysqld.exe"){print"ImagePath for <b>$keys1</b> is corect ($data)<br>";}
	else{print"<font color=red>ImagePath for <b>$keys1</b> is wrong ($data)</font><br>";}
}

print "<form  action=$ENV{SCRIPT_NAME} method=post>
<input class=button type=submit name=act value=\"Fix the found registry strings\"></form>";

print "</center><p>&nbsp;</p>Written by Vlad Alexa Mancini</html>";

}


sub action {

foreach $key (@keys){
		if (defined $Registry->{$key}){
			push (@key,"$key");
	}
}
foreach $key (@key){
	$diskKey= $Registry->{"$key"} or  print "Can't read <b>$key</b> key: $^E\n";
	$data= $diskKey->{"/ImagePath"} or  print "Can't read $key<b>/ImagePath</b> value: $^E<br>";
	if ($data eq "C:\\apache2triadpath\\mysql\\bin\\mysqld.exe"){print"ImagePath ($data) for <b>$key</b> needed no corection <br>";}
	else{
	print"<font color=red>ImagePath for <b>$key</b> was fixed ($data)</font><br>";
	$diskKey->{"/ImagePath"} = "C:\\apache2triadpath\\mysql\\bin\\mysqld.exe";
	}
}


foreach $dkey (@dkeys){
		if (defined $Registry->{$dkey}) {
		push (@dkey,"$dkey");
		}
}
foreach $dkey (@dkey){
		$enum = $dkey . "Enum/";
		$params = $dkey . "Parameters/";
		$security = $dkey . "Security/";
		delete $Registry->{$enum};
		delete $Registry->{$params};
		delete $Registry->{$security};	
		$deleted = delete $Registry->{$dkey} or die "died while deleting $dkey with error( $! )";
		print "<br><font color=red><b>$dkey</b> was deleted</font><br>";
		print "<b>(</b><br>";
		foreach $del (%$deleted){
			print " $del <br> ";
		}
		print "<b>)</b><br>";
}


print "<br>All done<br>";
print "<a href=javascript:history.go(-2)>Go Back</a>";
}
exit;