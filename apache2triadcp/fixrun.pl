unless (0 < @ARGV && @ARGV < 2) {
    printf "Usage: $0 path\nNote: Path must have no trailing slash and a upercased drive letter\n";
    exit;
} 

use Win32::TieRegistry; 
$Registry->Delimiter('/'); 

@os = Win32::GetOSVersion();
if ($os[4] ne "2"){
print "This Script is for WinNT only";
exit;
}

$windir = $ENV{'WINDIR'};
$location = $ARGV[0];

$file = "$windir/WinSxS/Manifests/x86_Microsoft.VC80.CRT_1fc8b3b9a1e18e3b_8.0.50608.0_x-ww_6262d37f.Manifest";

$key = "HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Windows NT/CurrentVersion";

if (defined $Registry->{$key}){
	$diskKey = $Registry->{"$key"} or  print "Can't read : $key\n";
	$data = $diskKey->{"/CurrentVersion"} or  print "Can't read $key/CurrentVersion\n";
}

if ($data > 5.0){ 
mkdir "$windir/WinSxS";
mkdir "$windir/WinSxS/Manifests";
open(FILE,">$file") or die "Can't write $file\n";
print FILE <<DATA;
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
    <noInheritable></noInheritable>
    <assemblyIdentity type="win32" name="Microsoft.VC80.CRT" version="8.0.50608.0" processorArchitecture="x86" publicKeyToken="1fc8b3b9a1e18e3b"></assemblyIdentity>
    <file name="msvcr80.dll" hash="2a0d797a8c5eac76e54e98db9682e0938c614b45" hashalg="SHA1"><asmv2:hash xmlns:asmv2="urn:schemas-microsoft-com:asm.v2" xmlns:dsig="http://www.w3.org/2000/09/xmldsig#"><dsig:Transforms><dsig:Transform Algorithm="urn:schemas-microsoft-com:HashTransforms.Identity"></dsig:Transform></dsig:Transforms><dsig:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"></dsig:DigestMethod><dsig:DigestValue>phRUExlAeZ8BwmlD8VlO5udAnRE=</dsig:DigestValue></asmv2:hash></file>
    <file name="msvcp80.dll" hash="cc4ca55fb6aa6b7bb8577ab4b649ab77e42f8f91" hashalg="SHA1"><asmv2:hash xmlns:asmv2="urn:schemas-microsoft-com:asm.v2" xmlns:dsig="http://www.w3.org/2000/09/xmldsig#"><dsig:Transforms><dsig:Transform Algorithm="urn:schemas-microsoft-com:HashTransforms.Identity"></dsig:Transform></dsig:Transforms><dsig:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"></dsig:DigestMethod><dsig:DigestValue>7AY1JqoUvK3u/6bYWbOagGgAFbc=</dsig:DigestValue></asmv2:hash></file>
</assembly>
DATA
mkdir "$windir/WinSxS/x86_Microsoft.VC80.CRT_1fc8b3b9a1e18e3b_8.0.50608.0_x-ww_6262d37f";
system ("copy $location\\bin\\msvcp80.dll $windir\\WinSxS\\x86_Microsoft.VC80.CRT_1fc8b3b9a1e18e3b_8.0.50608.0_x-ww_6262d37f\\msvcp80.dll"); 
system ("copy $location\\bin\\msvcr80.dll $windir\\WinSxS\\x86_Microsoft.VC80.CRT_1fc8b3b9a1e18e3b_8.0.50608.0_x-ww_6262d37f\\msvcr80.dll"); 
close(FILE); 
	print "Your MS Windows NT $data Visual C++ 2005 Runtime Libraries had to be fixed\nPress enter to exit and consider downgrading to a better OS version\n"; 
	#$final = <STDIN>;
	#exit 0 if $final =~ m/^$/;
}else{
	print "Your MS Windows NT $data Visual C++ 2005 Runtime Libraries do not need fixing\n"; 
} 

exit;

