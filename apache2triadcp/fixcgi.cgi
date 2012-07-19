#!C:/apache2triadpath/perl/bin/perl.exe

print "Content-type: text/html\n\n";

&parseform();

if ($FORM{'act'}eq'Proceed'){
print "<link rel=stylesheet href=style.css><title>Apache2Triad cgi files headers fix tool</title>";
&convert;
}else{
&message;
}
exit;


sub message {
print <<HTML;
<link rel=stylesheet href=style.css>
<title>Apache2Triad cgi files headers fix tool</title><body><center><p>&nbsp;</p>
<p><font size=5>Cgi file headers fix tool</font></p>
<p>This script will fix the path to the cgi executable on the first line of all cgi scripts under the path you specify</p>
<form  action="$ENV{SCRIPT_NAME}" method="post"><b>
[ Fix perl <input type=radio name=lang value=perl checked> ]&nbsp;
[ Fix python <input type=radio name=lang value=python> ]<br><br>
Path : <input size=50 type=text name=path value=\"C:/apache2triadpath/htdocs/apache2triadcp\"><br><br></b>
<input class=button type=submit name="act" value="Proceed"></form>
</center>Written by Vlad Alexa Mancini</html>
HTML
}

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


sub convert {
my $path=$FORM{'path'};
if ($FORM{'lang'}eq'perl'){my $include=" cgi ";}
if ($FORM{'lang'}eq'python'){my $include=" py ";}
my @names;
my $name;
opendir DIR,"$path";
$name=readdir DIR;
$name=readdir DIR;
@names=grep{!-d $_}readdir DIR;
closedir DIR;
foreach $name (@names){
	if (-d "$path/$name"){convert ("$path/$name")};
	@namess=split(/\./, $name);
	if (!(-d "$path/$name")&&(!($include= /@namess[$namess+1]/)||(@namess[$namess+1]eq''))){
	open (FILE,"$path/$name");
	binmode FILE;
	@lines=<FILE>;
	close (FILE);
	if (@lines[0]=~ /$FORM{'lang'}/i) {
	@lines[0]="\#\!C:\/apache2triadpath\/$FORM{'lang'}\/bin\/$FORM{'lang'}.exe\r\n";
	open (FILE,">$path/$name");
	binmode FILE;
	print FILE @lines;
	close (FILE);
	print "$path/$name - <b>converted</b><br>";
	}else{
	print "$path/$name - does not need conversion<br>";
   }
  }
 }
print "<br>All done<br>";
print "<a href=javascript:history.go(-2)>Go Back</a>";
}