#!C:/apache2triadpath/perl/bin/perl.exe

print "Content-type: text/html\n\n";

use Win32::TieRegistry;

$Registry->Delimiter('/');

@keys = ("HKEY_LOCAL_MACHINE/SYSTEM/CurrentControlSet/Services/Apache2/",
"HKEY_LOCAL_MACHINE/SYSTEM/CurrentControlSet/Services/Apache2SSL/",
"HKEY_LOCAL_MACHINE/SYSTEM/CurrentControlSet/Services/Mysql/",
"HKEY_LOCAL_MACHINE/SYSTEM/CurrentControlSet/Services/Pgsql/",
"HKEY_LOCAL_MACHINE/SYSTEM/CurrentControlSet/Services/Xmail/",
"HKEY_LOCAL_MACHINE/SYSTEM/CurrentControlSet/Services/Slimftpd/");

$FORM{'act'} = '';

@os = Win32::GetOSVersion();
if ($os[4] ne "2"){
print "This Services Administration Script is for WinNT only";
exit;
}

&parseform();
if ($FORM{'act'}eq'Services Autostart'){ &action; }else{ &entry; }
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

foreach $keys (@keys){
        if (defined $Registry->{$keys}){
                                push (@keys1,"$keys");
        }
}

foreach $keys1 (@keys1){
	$keys1 =~ m/^HKEY_LOCAL_MACHINE\/SYSTEM\/CurrentControlSet\/Services\/(.*)\//;
	$name = $1;
	$diskKey = $Registry->{"$keys1"} or  print "<font size=2>Can't read :<b>$keys1</b> key: ($^E)</font><br>";
	$data = $diskKey->{"/Start"} or  print "<font size=2>Can't read $keys1<br>/Start</b> value: ($^E)</font><br>";
	if ($data eq "0x00000002"){${$name} = "checked";}
}

if ($Apache2 eq "checked"){$ApacheSSL = "disabled";}
if ($Apache2SSL eq "checked"){$Apache = "disabled";}

print "
<form class=form action=$ENV{SCRIPT_NAME} method=post>
<table border=0 cellspacing=6 cellpadding=0>
  <tr>
    <td>
<fieldset>
<legend><input type=checkbox name=Apache2 value=on onclick=this.form.submit(); $Apache2 $Apache></legend>
Autostart Apache
</fieldset>
    </td>
    <td>
<fieldset>
<legend><input type=checkbox name=Apache2SSL value=on onclick=this.form.submit(); $Apache2SSL $ApacheSSL></legend>
Autostart Apache SSL
</fieldset>
    </td>
    <td>
<fieldset>
<legend><input type=checkbox name=Mysql value=on onclick=this.form.submit(); $Mysql></legend>
Autostart Mysql
</fieldset>
    </td>
    <td>
<fieldset>
<legend><input type=checkbox name=Pgsql value=on onclick=this.form.submit(); $Pgsql></legend>
Autostart Postgres
</fieldset>
    </td>
    <td>
<fieldset>
<legend><input type=checkbox name=Xmail value=on onclick=this.form.submit(); $Xmail></legend>
Autostart Xmail
</fieldset>
    </td>
    <td>
<fieldset>
<legend><input type=checkbox name=Slimftpd value=on onclick=this.form.submit(); $Slimftpd></legend>
Autostart Slimftpd
</fieldset>
    </td>
  </tr>
</table>
<input type=hidden name=act value=\"Services Autostart\"></form>
";

}


sub action {

if ($FORM{'Apache2'} eq "on" ){$Apache2="on";}else{$Apache2="off"}
if ($FORM{'Apache2SSL'} eq "on" ){$Apache2SSL="on";}else{$Apache2SSL="off"}
if ($FORM{'Mysql'} eq "on"){$Mysql="on";}else{$Mysql="off"}
if ($FORM{'Pgsql'} eq "on"){$Pgsql="on";}else{$Pgsql="off"}
if ($FORM{'Xmail'} eq "on"){$Xmail="on";}else{$Xmail="off"}
if ($FORM{'Slimftpd'} eq "on"){$Slimftpd="on";}else{$Slimftpd="off"}


foreach $keys (@keys){
        if (defined $Registry->{$keys}){
                                push (@keys1,"$keys");
        }
}

foreach $keys1 (@keys1){
        $keys1 =~ m/^HKEY_LOCAL_MACHINE\/SYSTEM\/CurrentControlSet\/Services\/(.*)\//;
        $name = $1;
        $diskKey = $Registry->{"$keys1"} or  print "<font size=2>Can't read :<b>$keys1</b> key: ($^E)</font><br>";
        $data = $diskKey->{"/Start"} or  print "<font size=2>Can't read $keys1<br>/Start</b> value: ($^E)</font><br>";

        if ($name eq "Apache2"){
                        if ($Apache2 eq "on"){$diskKey->{"/Start"} = [ "0x00000002", "REG_DWORD" ];}
                        if ($Apache2 eq "off"){$diskKey->{"/Start"} = [ "0x00000003", "REG_DWORD" ];}
        }
        if ($name eq "Apache2SSL"){
                        if ($Apache2SSL eq "on"){$diskKey->{"/Start"} = [ "0x00000002", "REG_DWORD" ];}
                        if ($Apache2SSL eq "off"){$diskKey->{"/Start"} = [ "0x00000003", "REG_DWORD" ];}
        }
        if ($name eq "Mysql"){
                        if ($Mysql eq "on"){$diskKey->{"/Start"} = [ "0x00000002", "REG_DWORD" ];}
                        if ($Mysql eq "off"){$diskKey->{"/Start"} = [ "0x00000003", "REG_DWORD" ];}
        }
        if ($name eq "Pgsql"){
                        if ($Pgsql eq "on"){$diskKey->{"/Start"} = [ "0x00000002", "REG_DWORD" ];}
                        if ($Pgsql eq "off"){$diskKey->{"/Start"} = [ "0x00000003", "REG_DWORD" ];}
        }
        if ($name eq "Xmail"){
                        if ($Xmail eq "on"){$diskKey->{"/Start"} = [ "0x00000002", "REG_DWORD" ];}
                        if ($Xmail eq "off"){$diskKey->{"/Start"} = [ "0x00000003", "REG_DWORD" ];}
        }
        if ($name eq "Slimftpd"){
                        if ($Slimftpd eq "on"){$diskKey->{"/Start"} = [ "0x00000002", "REG_DWORD" ];}
                        if ($Slimftpd eq "off"){$diskKey->{"/Start"} = [ "0x00000003", "REG_DWORD" ];}
        }


}

print "<script>window.location.replace('index.html#sp');</script>";
}
exit;