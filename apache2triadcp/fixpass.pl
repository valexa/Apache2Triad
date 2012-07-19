unless (1 < @ARGV && @ARGV < 3) {
    printf "Usage: $0 password path\nNote: Path must have no trailing slash and a upercased drive letter\n";
    exit;
}

$windir = $ENV{'WINDIR'};
$newpass = $ARGV[0];
$location = $ARGV[1];

push (@fnames,"$windir/my.ini");
push (@fnames,"$location/ftp/slimftpd.conf");
push (@fnames,"$location/htdocs/phpsftpd/inc.conf.php");
push (@fnames,"$location/htdocs/apache2triadcp/proceses.cgi");
push (@fnames,"$location/htdocs/apache2triadcp/test.mysql.php");

push (@xnames,"$location/mail/ctrlaccounts.tab");
push (@xnames,"$location/mail/mailusers.tab");
push (@xnames,"$location/htdocs/phpxmail/servers.php");

sub parse {
  my ($fname,$old,$new) = @_;
  if (open (FILE,"+< $fname")){
  @data=<FILE>;
  truncate (FILE,0);
  close (FILE);
  open (FILE,"+< $fname");
        foreach $d (@data){
                $d =~ s~$old~$new~g ;
                print FILE $d;
        }
  close (FILE);
  }else{ print "Password for $fname not changed !!\n"; $problems += 1; }
  return $problems;
}

sub report {
      my ($fname) = @_;
        print "Password for $fname not changed !!\n";
        $problems += 1;
      return $problems;
}

print "Setting password to $newpass , using path $location\n\n";
$problems = 0;

# set mysql password
system("$location/mysql/bin/mysqladmin.exe -uroot --password= password $newpass") and report("Mysql");

# set apache password
system("$location/bin/htpasswd.exe -b $location/htdocs/.htpasswd root $newpass") and report("Apache");

# set xmail password
$xpass = qx("$location/mail/bin/xmcrypt.exe $newpass") or report("Xmail");
chomp($xpass);
foreach $fname (@xnames) {
       parse($fname,'11170c040115041616',$xpass);
}

# set password in plaintext files
foreach $fname (@fnames) {
       parse($fname,'apache2triadpass',$newpass);
}

if ($problems != 0){
          print "\nWe were unable to set the password $problems times , \nReport this to apache2triad.net \n(Do not post screenshots , copy/paste the text intead) Press enter to exit\n";
          $final = <STDIN>;
          exit 0 if $final =~ m/^$/;
}

exit;