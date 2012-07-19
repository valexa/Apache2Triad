#!C:/apache2triadpath/perl/bin/perl.exe

print "Content-type: text/html\n\n";

@files = ("c:/my.cnf","$ENV{'WINDIR'}/system/php5ts.dll","$ENV{'WINDIR'}/system32/php5ts.dll","$ENV{'WINDIR'}/system/perl58.dll","$ENV{'WINDIR'}/system32/perl58.dll","$ENV{'WINDIR'}/system/ntwdblib.dll","$ENV{'WINDIR'}/system32/ntwdblib.dll","$ENV{'WINDIR'}/system/libeay32.dll","$ENV{'WINDIR'}/system32/libeay32.dll","$ENV{'WINDIR'}/system/ssleay32.dll","$ENV{'WINDIR'}/system32/ssleay32.dll");

$FORM{'act'} = '';

&parseform();

if ($FORM{'act'}eq'Delete the found files'){
print "<link rel=stylesheet href=style.css><title>Apache2Triad old instalations clean tool</title>";
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
<title>Apache2Triad old instalations clean tool</title><body><center><p>&nbsp;</p>
<p><font size=5>Old instalations clean tool</font></p>
<p>This script will search for some files from old instalations of php mysql and perl , known to cause problems for apache2triad.</p>";

foreach $file (@files){
	if (open (FILE,"$file")){
		print "<font color=red>Found <b>$file</b></font><br>";
		close (FILE);
		push (@files1,"$file");
	}else{
		print "Did not find <b>$file</b><br>";
	}
}

print "<form  action=$ENV{SCRIPT_NAME} method=post>
<input class=button type=submit name=act value=\"Delete the found files\"></form>";

print "</center><p>&nbsp;</p>Written by Vlad Alexa Mancini</html>";

}


sub action {

foreach $file (@files){
	if (open (FILE,"$file")){
		close (FILE);
		push (@files1,"$file");
	}
}

foreach $file (@files1){
	unlink "$file";
	print "Deleted <b>$file</b><br>";
}

print "<br>All done<br>";
print "<a href=javascript:history.go(-2)>Go Back</a>";
}
exit;
