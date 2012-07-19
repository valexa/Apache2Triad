unless (0 < @ARGV && @ARGV < 2) {
    printf "Usage: $0 path\nNote: Path must have no trailing slash and a upercased drive letter\n";
    exit;
}

$windir = $ENV{'WINDIR'};
$location = $ARGV[0];

if ($location =~ m/^(.*):\\(\S*)$/g){
        $loc_drv = $1;
        $loc_dir = $2;
}

$loc_dir =~ tr~\\~/~;

$location = "$loc_drv:/$loc_dir";

push (@fnames,"$windir/my.ini");
push (@fnames,"$windir/odbc.ini");
push (@fnames,"$windir/php.ini");
push (@fnames,"$location/apache2triad_readme.txt");
push (@fnames,"$location/opssl/apache2triad_openssl.txt");
push (@fnames,"$location/opssl/bin/openssl.cnf");
push (@fnames,"$location/opssl/bin/sslcert.ini");
push (@fnames,"$location/conf/httpd.conf");
push (@fnames,"$location/conf/httpd.default.conf");
push (@fnames,"$location/conf/ssl.conf");
push (@fnames,"$location/ftp/slimftpd.conf");
push (@fnames,"$location/python/Lib/site-packages/spyce/spyce.conf");
push (@fnames,"$location/perl/bin/perlindex.bat");
push (@fnames,"$location/perl/lib/CORE/config.h");
push (@fnames,"$location/perl/lib/Config.pm");
push (@fnames,"$location/perl/site/lib/Apache2/Apache/MyHandler.pm");
push (@fnames,"$location/perl/lib/Config_heavy.pl"); 
push (@fnames,"$location/perl/site/lib/ppm.xml");
push (@fnames,"$location/php/bin/pear.bat");
push (@fnames,"$location/php/pear/pearcmd.php");
push (@fnames,"$location/php/pear/PEAR/Config.php");
push (@fnames,"$location/php/pear/tests/DB/tests/driver/setup.inc.cvs");
push (@fnames,"$location/php/pear/tests/DB/tests/include.inc");
push (@fnames,"$location/htdocs/awstats/awstats.localhost.conf");
push (@fnames,"$location/htdocs/awstats/awredir.cgi");
push (@fnames,"$location/htdocs/awstats/awstats.cgi");
push (@fnames,"$location/htdocs/awstats/.htaccess");
push (@fnames,"$location/htdocs/phpsftpd/inc.conf.php");
push (@fnames,"$location/htdocs/phpsqliteadmin/.htaccess");
push (@fnames,"$location/htdocs/phpsqliteadmin/config.php");
push (@fnames,"$location/htdocs/phppgadmin/conf/config.inc.php");
push (@fnames,"$location/htdocs/phppgadmin/.htaccess");
push (@fnames,"$location/htdocs/uebimiau/inc/config.php");
push (@fnames,"$location/htdocs/apache2triadcp/webpear.php");
push (@fnames,"$location/htdocs/apache2triadcp/.htaccess");
push (@fnames,"$location/htdocs/apache2triadcp/index.html");
push (@fnames,"$location/htdocs/apache2triadcp/access.cgi");
push (@fnames,"$location/htdocs/apache2triadcp/security.cgi");
push (@fnames,"$location/htdocs/apache2triadcp/changedom.cgi");
push (@fnames,"$location/htdocs/apache2triadcp/changepass.php");
push (@fnames,"$location/htdocs/apache2triadcp/count.cgi");
push (@fnames,"$location/htdocs/apache2triadcp/dbg.php");
push (@fnames,"$location/htdocs/apache2triadcp/editor.php");
push (@fnames,"$location/htdocs/apache2triadcp/error.cgi");
push (@fnames,"$location/htdocs/apache2triadcp/fixfiles.cgi");
push (@fnames,"$location/htdocs/apache2triadcp/fixregistry.cgi");
push (@fnames,"$location/htdocs/apache2triadcp/protect.cgi");
push (@fnames,"$location/htdocs/apache2triadcp/fixcgi.cgi");
push (@fnames,"$location/htdocs/apache2triadcp/guihttpd.cgi");
push (@fnames,"$location/htdocs/apache2triadcp/readme.php");
push (@fnames,"$location/htdocs/apache2triadcp/guiphp.php");
push (@fnames,"$location/htdocs/apache2triadcp/guipgsql.php");
push (@fnames,"$location/htdocs/apache2triadcp/info.cgi");
push (@fnames,"$location/htdocs/apache2triadcp/proceses.cgi");
push (@fnames,"$location/htdocs/apache2triadcp/services.cgi");
push (@fnames,"$location/htdocs/apache2triadcp/test.cgi");
push (@fnames,"$location/htdocs/apache2triadcp/test.py");
push (@fnames,"$location/htdocs/apache2triadcp/info.py");
push (@fnames,"$location/htdocs/apache2triadcp/test.mail.cgi");
push (@fnames,"$location/htdocs/apache2triadcp/test.sqlite.php");

sub parse {
  if (open (FILE,"+< $fname")){
  @data=<FILE>;
  truncate (FILE,0);
  close (FILE);
  open (FILE,"+< $fname");
        foreach $d (@data){
                $d =~ s~C:\/apache2triadpath~$loc_drv:\/$loc_dir~g ;
                $d =~ s~C:\\apache2triadpath~$loc_drv:\\$loc_dir~g ;
                $d =~ s~C:\\\/apache2triadpath~$loc_drv:\\\/$loc_dir~g ;
                $d =~ s~C:\\\\apache2triadpath~$loc_drv:\\\\$loc_dir~g ;
                print FILE $d;
        }
  close (FILE);
  }else{ print "$fname not found !!\n"; $problems += 1; }
  return $problems;
}

print "Changing all paths to $location\n\n";
$problems = 0;

foreach $fname (@fnames) {
       parse();
}

if ($problems != 0){
          print "\n$problems files were not found ,if you did not do a custom \ninstall report this to apache2triad.net \n(Do not post screenshots , copy/paste the text intead) Press enter to exit\n";
          $final = <STDIN>;
          exit 0 if $final =~ m/^$/;
}

exit;