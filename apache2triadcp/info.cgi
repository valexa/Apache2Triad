#!C:/apache2triadpath/perl/bin/perl.exe

print "Content-type:  text/html\n\n";

#
# general info
#

print <<HTML;
      <html><link rel=stylesheet href=style.css>
      <h2 align=center>general info</h2>
      <p>
      <table class=table border=0 cellpadding=4 cellspacing=1 width=100%>
             <tr>
                 <td width=35% class=tdd><b>perl version:</b></td>
                 <td width=65% class=tdl>$]</td>
             </tr>
             <tr>
                 <td class=tdd><b>perl compiled on:</b></td>
                 <td class=tdl>$^O</td>
             </tr>
             <tr>
                 <td class=tdd><b>perl executable:</b></td>
                 <td class=tdl>$^X</td>
             </tr>
             <tr>
                 <td class=tdd><b>location of perl:</b></td>
                 <td class=tdl>
HTML

$per = $^X ;
$per =~ s/perl.exe|PERL.EXE//;
@perlloc = ("$per");
foreach $loc(@perlloc){
        print "$loc<br>\n";
}

print <<HTML;
      </td></tr><tr><td class=tdd> <b>include paths:</b></td><td class=tdl>
HTML

foreach $item(@INC){
        if ($item ne "."){
            print "$item <br>\n";
        }
}

print <<HTML;
      </td></tr></table>
HTML

#
# environment variables
#

print <<HTML;
        <h2 align=center>environment variables</h2><table class=table border=0 cellpadding=4 cellspacing=1 width=100%>
        <tr><td class=tdark ><b>Server Variable</b></td><td class=tdg ><b>Value</b></td></tr>
HTML

foreach $fieldname(keys %ENV){
        print "<tr><td width=35% class=tdd><font size=-1>$fieldname<font></td>\n";
        print "<td width=65% class=tdl><font size=-1>$ENV{$fieldname}&nbsp;<font></td></tr>\n";
}

print <<HTML;
      </table>
HTML

#
# perl modules
#

use File::Find;

sub count {
    return $found{$a}[1] cmp $found{$b}[1];
}

sub ModuleScanner {
    if ($File::Find::name =~ /\.pm$/){
            open(FILE,$File::Find::name) || return;
            while(<FILE>){
                   if (/^ *package +(\S+);/){
                           push (@modules, $1);
                           last;
                   }
            }
    }
}

find(\&ModuleScanner,@INC);
foreach $line(@modules){
        $match = lc($line);
        if ($found{$line}[0] >0){
               $found{$line} = [$found{$line}[0]+1,$match]
        }else{
               $found{$line} = ["1",$match];
        }
}
@modules = sort count keys(%found);

print <<HTML;
      <h2 align=center>perl modules</h2><table class=table border=0 cellpadding=4 cellspacing=1 width=100%>
HTML

$count=0;
foreach $mod(@modules){
      chomp $mod;
      $count++;
      if ($count == 1){
         print "<tr><td class=tdl>$mod</td>\n";
      }
      if ($count == 2){
         print "<td class=tdl>$mod</td>\n";
      }
      if ($count == 3){
         print "<td class=tdl>$mod</td></tr>\n";
         $count = 0;
      }
}

print <<HTML;
      </table></html>
HTML

exit;
