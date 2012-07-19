;#####################################
;GLOBAL

SetDatablockOptimize off
SetDateSave off
SetCompressor bzip2
SetCompress force
CRCCheck on
CheckBitmap  triad.bmp
ShowInstDetails hide
ShowUninstDetails hide
SilentUnInstall normal
Icon triad.ico
UninstallIcon triadu.ico
WindowIcon on
SetOverwrite on
AutoCloseWindow true
InstallColors 000000 FFFFFF
XPStyle on

;#####################################
;DEFINES

!define VERSION 1.5.4
!define NAME Apache2Triad
!define NAME_SMALL apache2triad
!define Desc "apache server bundle"
!define REG_PROG "SOFTWARE\${NAME}"
!define REG_UNINST "Software\Microsoft\Windows\CurrentVersion\Uninstall\${NAME}"
!define /date NOW "(%y-%m-%d_%H-%M-%S)"

;#####################################
;VARIABLES

var SUB_KEY
var VALUE
var DATA_1
var DATA_2

;#####################################
;OPTIONS

InstallDir C:\apache2triad
OutFile "${NAME_SMALL}${VERSION}${NOW}.exe"
InstallDirRegKey HKLM ${REG_PROG} "Location"
Name "${NAME}"
Caption "${NAME} ${VERSION} for Win$R0"
DirText "Finally apache2triad can be installed in any location , still it's best to leave it to the default if you have no serious resons for doing otherwise ."
BrandingText "By Vlad Alexa Mancini"
;AddBrandingImage top 295|75
ComponentText  "On this page you can customize the Apache2Triad instalation , if in doubt just press next to do a default install as is recommended ."
CompletedText "${NAME} ${VERSION} setup has sucesfully completed"
UninstallCaption "${NAME} Uninstaller for Win$R0"
UninstallText "Uninstalling ${NAME} ${VERSION}"
LicenseData license.txt
LicenseText "After reading the license below please press the I Agree button in sign of compliance with it"

;#####################################
;Password Page

Function PassPage
pagetop:
   GetTempFileName $R9
   File /oname=$R9 passpage.nsi
   InstallOptions::dialog $R9

   Pop $0
   StrCmp $0 back pagebottom  ;user pressed back
   StrCmp $0 cancel pagebottom ;user pressed cancel

   ReadINIStr $0 $R9 "Field 6" "State"
   ReadINIStr $1 $R9 "Field 7" "State"
   StrCmp $0 $1 l_match l_nomatch

   l_match:
   goto l_skip  ;passwords matched

   l_nomatch:
   goto pagetop ;passwords did not match

   l_skip:
   StrCpy $R1 $1
pagebottom:
FunctionEnd

;#####################################
;Pages

Page components
Page directory
Page Custom PathCheck
Page Custom PassPage
Page Custom PassCheck
Page license
Page instfiles

UninstPage uninstConfirm
UninstPage components
UninstPage instfiles

;#####################################
;SECTIONS

Section "Copy ${NAME} files"
  SectionIn RO
  SetOutPath $INSTDIR
  File apache2\apache2triad_readme.txt
  ;ExecShell "open" "$INSTDIR\apache2triad_readme.txt" SW_SHOWMINIMIZED
  File /a /r apache2\*.*
  SetFileAttributes "$INSTDIR" SYSTEM
  StrCmp $R0 "9X" mon_9x
  StrCmp $R0 "NT" mon_nt
  mon_nt:
        File /oname=$INSTDIR\bin\apachemonitor.exe apachemonitornt.exe
  Goto done
  mon_9x:
        File /oname=$INSTDIR\bin\apachemonitor.exe apachemonitor9x.exe
  Goto done
  done:
MessageBox MB_OK "${NAME} ${VERSION} has been extracted to $INSTDIR , press ok to do post configuration ."
SectionEnd

Section "Add Apache2Triad user"
  SectionIn RO
StrCmp $R0 "9X" ap_9x
StrCmp $R0 "NT" ap_nt
ap_nt:
;if nt
  ExecWait "net user apache2triad $R1 /add"
  ExecWait '"$INSTDIR\bin\editrights.exe" -a SeServiceLogonRight -u apache2triad'
  WriteRegDWORD HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList" "apache2triad" "00000000"
Goto done
ap_9x:
;if 9x
Goto done
done:
SectionEnd

Section "Add paths to the enviroment"
  SectionIn RO
Push "$INSTDIR\bin"
  Call AddToPath
Push "$INSTDIR\perl\bin"
  Call AddToPath
Push "$INSTDIR\php\bin"
  Call AddToPath
Push "$INSTDIR\mysql\bin"
  Call AddToPath
Push "$INSTDIR\opssl\bin"
  Call AddToPath
Push "$INSTDIR\python\bin"
  Call AddToPath
Push "$INSTDIR\pgsql\bin"
  Call AddToPath
SectionEnd

SubSection "Copy configuration files"
Section "Install $WINDIR\my.ini"
    SetOutPath $WINDIR
    File my.ini
SectionEnd
Section "Install $WINDIR\odbc.ini"
    SetOutPath $WINDIR
    File odbc.ini
SectionEnd
Section "Install $WINDIR\php.ini"
    SetOutPath $WINDIR
    File php.ini
SectionEnd
SubSectionEnd

SubSection "Create autostarting services"
Section "Apache Service"
ExecWait '"$INSTDIR\bin\instsrv.exe" Apache2 $INSTDIR\bin\httpd.exe'
strcpy $SUB_KEY        "SYSTEM\CurrentControlSet\Services\Apache2\Parameters"
strcpy $VALUE        "ConfigArgs"
strcpy $DATA_1        "-f"
strcpy $DATA_2        "$INSTDIR\conf\httpd.conf"
Call RegWrite
WriteRegDWORD HKLM "SYSTEM\CurrentControlSet\Services\Apache2" "Type" "0x00000010"
WriteRegDWORD HKLM "SYSTEM\CurrentControlSet\Services\Apache2" "Start" "00000002"
WriteRegDWORD HKLM "SYSTEM\CurrentControlSet\Services\Apache2" "ErrorControl" "00000001"
WriteRegExpandStr HKLM "SYSTEM\CurrentControlSet\Services\Apache2" "ImagePath" '"$INSTDIR\bin\httpd.exe"$R5 -n Apache2 $R6'
WriteRegStr HKLM "SYSTEM\CurrentControlSet\Services\Apache2" "DisplayName" "Apache2Triad Apache2 Service"
WriteRegStr HKLM "SYSTEM\CurrentControlSet\Services\Apache2" "ObjectName" "LocalSystem"
WriteRegStr HKLM "SYSTEM\CurrentControlSet\Services\Apache2" "Description" "The apache server that provides httpd suport for apache2triad"
SectionEnd
Section "Apache Service(SSL)"
ExecWait '"$INSTDIR\bin\instsrv.exe" Apache2SSL $INSTDIR\bin\httpd.exe'
strcpy $SUB_KEY        "SYSTEM\CurrentControlSet\Services\Apache2SSL\Parameters"
strcpy $VALUE        "ConfigArgs"
strcpy $DATA_1        "-f"
strcpy $DATA_2        "$INSTDIR\conf\httpd.conf"
Call RegWrite
WriteRegDWORD HKLM "SYSTEM\CurrentControlSet\Services\Apache2SSL" "Type" "0x00000010"
WriteRegDWORD HKLM "SYSTEM\CurrentControlSet\Services\Apache2SSL" "Start" "00000003"
WriteRegDWORD HKLM "SYSTEM\CurrentControlSet\Services\Apache2SSL" "ErrorControl" "00000001"
WriteRegExpandStr HKLM "SYSTEM\CurrentControlSet\Services\Apache2SSL" "ImagePath" '"$INSTDIR\bin\httpd.exe"$R5 -D SSL -n Apache2SSL $R6'
WriteRegStr HKLM "SYSTEM\CurrentControlSet\Services\Apache2SSL" "DisplayName" "Apache2Triad Apache2 Service with SSL"
WriteRegStr HKLM "SYSTEM\CurrentControlSet\Services\Apache2SSL" "ObjectName" "LocalSystem"
WriteRegStr HKLM "SYSTEM\CurrentControlSet\Services\Apache2SSL" "Description" "The apache server that provides httpd with SSL suport for apache2triad"
SectionEnd
Section "Mysql Service"
ExecWait '"$INSTDIR\bin\instsrv.exe" MySql $INSTDIR\mysql\bin\mysqld.exe'
WriteRegDWORD HKLM "SYSTEM\CurrentControlSet\Services\MySql" "Type" "0x00000010"
WriteRegDWORD HKLM "SYSTEM\CurrentControlSet\Services\MySql" "Start" "00000002"
WriteRegDWORD HKLM "SYSTEM\CurrentControlSet\Services\MySql" "ErrorControl" "00000001"
WriteRegExpandStr HKLM "SYSTEM\CurrentControlSet\Services\MySql" "ImagePath" "$INSTDIR\mysql\bin\mysqld.exe"
WriteRegStr HKLM "SYSTEM\CurrentControlSet\Services\MySql" "DisplayName" "Apache2Triad MySql Service"
WriteRegStr HKLM "SYSTEM\CurrentControlSet\Services\MySql" "ObjectName" "LocalSystem"
WriteRegStr HKLM "SYSTEM\CurrentControlSet\Services\MySql" "Description" "The mysql server that provides mySQL database suport for apache2triad"
SectionEnd
Section "PostgreSQL Service"
ExecWait '"$INSTDIR\bin\instsrv.exe" PgSql $INSTDIR\pgsql\bin\pg_ctl.exe -a .\apache2triad -p $R1'
WriteRegDWORD HKLM "SYSTEM\CurrentControlSet\Services\PgSql" "Type" "0x00000010"
WriteRegDWORD HKLM "SYSTEM\CurrentControlSet\Services\PgSql" "Start" "00000003"
WriteRegDWORD HKLM "SYSTEM\CurrentControlSet\Services\PgSql" "ErrorControl" "00000001"
WriteRegExpandStr HKLM "SYSTEM\CurrentControlSet\Services\PgSql" "ImagePath" '"$INSTDIR\pgsql\bin\pg_ctl.exe" runservice -N PgSql -D $INSTDIR\pgsql\data\'
WriteRegStr HKLM "SYSTEM\CurrentControlSet\Services\PgSql" "DisplayName" "Apache2Triad PostgreSQL Service"
WriteRegStr HKLM "SYSTEM\CurrentControlSet\Services\PgSql" "ObjectName" ".\apache2triad"
WriteRegStr HKLM "SYSTEM\CurrentControlSet\Services\PgSql" "Description" "The postgresql server that provides pgSQL database suport for apache2triad"
SectionEnd
Section "Xmail Service"
ExecWait '"$INSTDIR\bin\instsrv.exe" XMail $INSTDIR\mail\bin\XMail.exe'
WriteRegDWORD HKLM "SYSTEM\CurrentControlSet\Services\XMail" "Type" "0x00000010"
WriteRegDWORD HKLM "SYSTEM\CurrentControlSet\Services\XMail" "Start" "00000002"
WriteRegDWORD HKLM "SYSTEM\CurrentControlSet\Services\XMail" "ErrorControl" "00000001"
WriteRegExpandStr HKLM "SYSTEM\CurrentControlSet\Services\XMail" "ImagePath" "$INSTDIR\mail\bin\XMail.exe"
WriteRegStr HKLM "SYSTEM\CurrentControlSet\Services\XMail" "DisplayName" "Apache2Triad Xmail Service"
WriteRegStr HKLM "SYSTEM\CurrentControlSet\Services\XMail" "ObjectName" "LocalSystem"
WriteRegStr HKLM "SYSTEM\CurrentControlSet\Services\XMail" "Description" "The xmail server that provides smtp/pop3 mail suport for apache2triad"
SectionEnd
Section "Slimftpd Service"
ExecWait '"$INSTDIR\bin\instsrv.exe" SlimFTPd $INSTDIR\ftp\SlimFTPd.exe -a .\apache2triad -p $R1'
WriteRegDWORD HKLM "SYSTEM\CurrentControlSet\Services\SlimFTPd" "Type" "0x00000010"
WriteRegDWORD HKLM "SYSTEM\CurrentControlSet\Services\SlimFTPd" "Start" "00000002"
WriteRegDWORD HKLM "SYSTEM\CurrentControlSet\Services\SlimFTPd" "ErrorControl" "00000001"
WriteRegExpandStr HKLM "SYSTEM\CurrentControlSet\Services\SlimFTPd" "ImagePath" '"$INSTDIR\ftp\SlimFTPd.exe" -service'
WriteRegStr HKLM "SYSTEM\CurrentControlSet\Services\SlimFTPd" "DisplayName" "Apache2Triad SlimFTPd Server"
WriteRegStr HKLM "SYSTEM\CurrentControlSet\Services\SlimFTPd" "ObjectName" ".\apache2triad"
WriteRegStr HKLM "SYSTEM\CurrentControlSet\Services\SlimFTPd" "Description" "The slimftpd server that provides ftp suport for apache2triad"
SectionEnd
SubSectionEnd

SubSection "Aplication Registry Enteries"
Section "Xmail Registry Enteries"
WriteRegStr HKLM SOFTWARE\GNU\XMail "MAIL_ROOT" "$INSTDIR\mail"
WriteRegStr HKLM SOFTWARE\GNU\XMail "MAIL_CMD_LINE" "-Pl -Sl -Ql -Fl -Cl -Ll"
SectionEnd
Section "MyODBC Registry Enteries"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBCINST.INI\ODBC Drivers" "MyODBC" "Installed"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBCINST.INI\MyODBC" "Driver" "$INSTDIR\mysql\bin\myodbc~1.dll"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBCINST.INI\MyODBC" "Setup" "$INSTDIR\mysql\bin\myodbc~2.dll"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBCINST.INI\MyODBC" "APILevel" "2"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBCINST.INI\MyODBC" "ConnectFunctions" "YYN"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBCINST.INI\MyODBC" "DriverODBCVer" "5.0"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBCINST.INI\MyODBC" "FileUsage" "0"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBCINST.INI\MyODBC" "FileExtns" "*.txt"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBCINST.INI\MyODBC" "SQLLevel" "1"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBCINST.INI\MyODBC" "CPTimeout" "60"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBCINST.INI\MyODBC" "DSNHelpFile" "$INSTDIR\mysql\bin\my3dsn.hlp"
WriteRegDWORD HKLM "SOFTWARE\ODBC\ODBCINST.INI\MyODBC" "UsageCount" "0x00000001"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBC.INI\ODBC Data Sources" "MySQL" "MyODBC"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBC.INI\MySQL" "Driver" "$INSTDIR\mysql\bin\myodbc~1.dll"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBC.INI\MySQL" "Description" "MySQL ODBC Driver DSN"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBC.INI\MySQL" "Server" "localhost"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBC.INI\MySQL" "Database" ""
WriteRegStr HKLM "SOFTWARE\ODBC\ODBC.INI\MySQL" "User" "root"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBC.INI\MySQL" "Password" "$R1"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBC.INI\MySQL" "Port" "3306"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBC.INI\MySQL" "Option" "3"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBC.INI\MySQL" "Stmt" ""
SectionEnd
Section "PsqlODBC Registry Enteries"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBCINST.INI\ODBC Drivers" "PsqlODBC" "Installed"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBCINST.INI\PsqlODBC" "Driver" "$INSTDIR\pgsql\bin\psqlodbc.dll"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBCINST.INI\PsqlODBC" "Setup" "$INSTDIR\pgsql\bin\psqlodbc.dll"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBCINST.INI\PsqlODBC" "APILevel" "1"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBCINST.INI\PsqlODBC" "ConnectFunctions" "YYN"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBCINST.INI\PsqlODBC" "DriverODBCVer" "03.00"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBCINST.INI\PsqlODBC" "FileUsage" "0"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBCINST.INI\PsqlODBC" "SQLLevel" "1"
WriteRegDWORD HKLM "SOFTWARE\ODBC\ODBCINST.INI\PsqlODBC" "UsageCount" "0x00000001"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBC.INI\ODBC Data Sources" "PostgreSQL" "PsqlODBC"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBC.INI\PostgreSQL" "Driver" "$INSTDIR\pgsql\bin\psqlodbc.dll"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBC.INI\PostgreSQL" "Description" "PostgreSQL ODBC Driver DSN"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBC.INI\PostgreSQL" "Servername" "localhost"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBC.INI\PostgreSQL" "Database" ""
WriteRegStr HKLM "SOFTWARE\ODBC\ODBC.INI\PostgreSQL" "Username" "root"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBC.INI\PostgreSQL" "Password" ""
WriteRegStr HKLM "SOFTWARE\ODBC\ODBC.INI\PostgreSQL" "Port" "5432"
WriteRegStr HKLM "SOFTWARE\ODBC\ODBC.INI\PostgreSQL" "Protocol" "6.4"
SectionEnd
Section "Python Registry Enteries"
WriteRegStr HKLM SOFTWARE\Python\PythonService\2.3 "" "$INSTDIR\Python\Lib\site-packages\win32\PythonService.exe"
WriteRegStr HKLM Software\Python\PythonCore\2.3\InstallPath "" "$INSTDIR\python"
WriteRegStr HKLM Software\Python\PythonCore\2.3\Modules "" ""
WriteRegStr HKLM Software\Python\PythonCore\2.3\Modules\pywintypes "" "$INSTDIR\python\bin\PyWinTypes23.dll"
WriteRegStr HKLM Software\Python\PythonCore\2.3\Modules\pythoncom "" "$INSTDIR\python\bin\pythoncom23.dll"
WriteRegStr HKLM Software\Python\PythonCore\2.3\Modules\Pythonwin "" "$INSTDIR\Python\Lib\site-packages\Pythonwin"
WriteRegStr HKLM Software\Python\PythonCore\2.3\PythonPath "" "$INSTDIR\Python\Lib;$INSTDIR\python\Lib\lib-tk;$INSTDIR\Python\bin;$INSTDIR\Python\Lib\site-packages\spyce"
WriteRegStr HKLM Software\Python\PythonCore\2.3\PythonPath\win32 "" "$INSTDIR\Python\Lib\site-packages\win32;$INSTDIR\Python\Lib\site-packages\win32\lib"
WriteRegStr HKLM Software\Python\PythonCore\2.3\PythonPath\win32com "" "$INSTDIR\Python\Lib\site-packages"
WriteRegStr HKLM Software\Python\PythonCore\2.3\PythonPath\Pythonwin "" "$INSTDIR\Python\Lib\site-packages\Pythonwin"
SectionEnd
Section "PostgreSQL Registry Enteries"
WriteRegStr HKLM Software\PostgreSQL\Installations\{APACHE-2-TRIAD-DEF-INSTALL} "Version" "8"
WriteRegStr HKLM Software\PostgreSQL\Installations\{APACHE-2-TRIAD-DEF-INSTALL} "Base Directory" "$INSTDIR\pgsql\"
WriteRegStr HKLM Software\PostgreSQL\Installations\{APACHE-2-TRIAD-DEF-INSTALL} "Data Directory" "$INSTDIR\pgsql\data\"
WriteRegDWORD HKLM Software\PostgreSQL\Installations\{APACHE-2-TRIAD-DEF-INSTALL} "Port" "00001538"
WriteRegStr HKLM Software\PostgreSQL\Installations\{APACHE-2-TRIAD-DEF-INSTALL} "Bin Directory" "$INSTDIR\pgsql\bin\"
WriteRegStr HKLM Software\PostgreSQL\Installations\{APACHE-2-TRIAD-DEF-INSTALL} "Service ID" "pgsql"
WriteRegStr HKLM Software\PostgreSQL\Installations\{APACHE-2-TRIAD-DEF-INSTALL} "Lib Directory" "$INSTDIR\pgsql\lib\"
WriteRegStr HKLM Software\PostgreSQL\Services\pgsql "Display Name" "Apache2Triad PostgreSQL Service"
WriteRegStr HKLM Software\PostgreSQL\Services\pgsql "Service Account" ".\apache2triad"
WriteRegStr HKLM Software\PostgreSQL\Services\pgsql "Data Directory" "$INSTDIR\pgsql\data\"
WriteRegDWORD HKLM Software\PostgreSQL\Services\pgsql "Port" "0x00001538"
WriteRegStr HKLM Software\PostgreSQL\Services\pgsql "Database Superuser" "root"
WriteRegStr HKLM Software\PostgreSQL\Services\pgsql "Encoding" "SQL_ASCII"
WriteRegStr HKLM Software\PostgreSQL\Services\pgsql "Locale" "C"
WriteRegStr HKLM Software\PostgreSQL\Services\pgsql "Product Code" "{APACHE-2-TRIAD-DEF-INSTALL}"
WriteRegStr HKCU "Software\pgAdmin III\Servers" "Server1" "localhost"
WriteRegStr HKCU "Software\pgAdmin III\Servers" "Description1" "Apache2Triad PostgreSQL Service"
WriteRegStr HKCU "Software\pgAdmin III\Servers" "ServiceID1" "pgsql"
WriteRegDWORD HKCU "Software\pgAdmin III\Servers" "Port1" "0x00001538"
WriteRegStr HKCU "Software\pgAdmin III\Servers" "Trusted1" "true"
WriteRegStr HKCU "Software\pgAdmin III\Servers" "Database1" "template1"
WriteRegStr HKCU "Software\pgAdmin III\Servers" "Username1" "root"
WriteRegStr HKCU "Software\pgAdmin III\Servers" "LastDatabase1" "template1"
WriteRegStr HKCU "Software\pgAdmin III\Servers" "LastSchema1" "public"
WriteRegDWORD HKCU "Software\pgAdmin III\Servers" "SSL1" "0x00000000"
WriteRegDWORD HKCU "Software\pgAdmin III\Servers" "Count" "0x00000001"
SectionEnd
SubSectionEnd

SubSection "Create start menu shortcuts"
Section "Required"
  SectionIn RO
  CreateDirectory "$STARTMENU\${NAME}"
  CreateShortCut "$STARTMENU\${NAME}\Readme.lnk" "$INSTDIR\apache2triad_readme.txt" "" ""
  CreateShortCut "$STARTMENU\${NAME}\Apache2TriadManager.lnk" "$INSTDIR\bin\a2tm.exe" "" ""      
  CreateShortCut "$STARTMENU\${NAME}\ApacheMonitor.lnk" "$INSTDIR\bin\apachemonitor.exe" "" ""
  CreateShortCut "$STARTMENU\${NAME}\MySQLMonitor.lnk" "$INSTDIR\mysql\bin\MySQLSystemTrayMonitor.exe" "" ""
  CreateShortCut "$STARTMENU\${NAME}\Uninstall.lnk" "$INSTDIR\uninstall.exe" "" "$INSTDIR\uninstall.exe" 0
  SetOutPath $STARTMENU\${NAME}
  File *.url
SectionEnd
Section "MySQL"
  SetOutPath "$INSTDIR\mysql\bin"
  CreateShortCut "$STARTMENU\${NAME}\MySQLAdmin.lnk" "$INSTDIR\mysql\bin\MySQLAdministrator.exe" "" ""
SectionEnd
Section "PostgreSQL"
  SetOutPath "$INSTDIR\pgsql\bin"
  CreateShortCut "$STARTMENU\${NAME}\PgAdmin.lnk" "$INSTDIR\pgsql\bin\pgadmin3.exe" "" ""
SectionEnd
Section "SSL"
  SetOutPath "$INSTDIR\opssl\bin"
  CreateShortCut "$STARTMENU\${NAME}\SSLCert.lnk" "$INSTDIR\opssl\bin\sslcert.exe" "" ""
SectionEnd
Section "Php"
  CreateDirectory "$STARTMENU\${NAME}\Php"
  SetOutPath "$INSTDIR\php\bin"
  CreateShortCut "$STARTMENU\${NAME}\Php\DbgListener.lnk" "$INSTDIR\php\bin\DbgListener.exe " "" ""
SectionEnd
Section "Perl"
  CreateDirectory "$STARTMENU\${NAME}\Perl"
  SetOutPath "$INSTDIR\perl\bin"
  CreateShortCut "$STARTMENU\${NAME}\Perl\PerlPPM.lnk" "$INSTDIR\perl\bin\perlppm.exe" "" ""
SectionEnd
Section "Python"
  CreateDirectory "$STARTMENU\${NAME}\Python"
  SetOutPath "$INSTDIR\python\bin"
  CreateShortCut "$STARTMENU\${NAME}\Python\PythonPPM.lnk" "$INSTDIR\python\bin\pythonppm.exe" "" ""
  SetOutPath "$INSTDIR\python\lib\site-packages\pythonwin"
  CreateShortCut "$STARTMENU\${NAME}\Python\PythonWin.lnk" "$INSTDIR\python\lib\site-packages\pythonwin\pythonwin.exe" "" ""
  SetOutPath "$INSTDIR\python\Lib\idlelib"
  CreateShortCut "$STARTMENU\${NAME}\Python\Idle.lnk" "$INSTDIR\python\bin\pythonw.exe" "$INSTDIR\python\Lib\idlelib\idle.pyw" "$INSTDIR\python\bin\pythonw.exe"
  SetOutPath "$INSTDIR\python\Lib\site-packages\wxPython\tools\boa"
  CreateShortCut "$STARTMENU\${NAME}\Python\Boa.lnk" "$INSTDIR\python\bin\pythonw.exe" "$INSTDIR\python\Lib\site-packages\wxPython\tools\boa\Boa.pyw" "$INSTDIR\python\Lib\site-packages\wxPython\tools\boa\Images\Icons\Boa.ico"
  SetOutPath "$INSTDIR\python\Lib\site-packages\wxPython\tools\XRCed"
  CreateShortCut "$STARTMENU\${NAME}\Python\XRCed.lnk" "$INSTDIR\python\bin\pythonw.exe" "$INSTDIR\python\Lib\site-packages\wxPython\tools\XRCed\xrced.pyw" "$INSTDIR\python\Lib\site-packages\wxPython\tools\XRCed\xrced.ico"
  SetOutPath "$INSTDIR\python\Lib\site-packages\wxPython\py"
  CreateShortCut "$STARTMENU\${NAME}\Python\PyShell.lnk" "$INSTDIR\python\bin\pythonw.exe" "$INSTDIR\python\Lib\site-packages\wxPython\py\PyShell.pyw" "$INSTDIR\python\Lib\site-packages\wxPython\py\PyShell.ico"
  CreateShortCut "$STARTMENU\${NAME}\Python\PyAlaCarte.lnk" "$INSTDIR\python\bin\pythonw.exe" "$INSTDIR\python\Lib\site-packages\wxPython\py\PyAlaCarte.pyw" "$INSTDIR\python\Lib\site-packages\wxPython\py\Py.ico"
  CreateShortCut "$STARTMENU\${NAME}\Python\PyAlaMode.lnk" "$INSTDIR\python\bin\pythonw.exe" "$INSTDIR\python\Lib\site-packages\wxPython\py\PyAlaMode.pyw" "$INSTDIR\python\Lib\site-packages\wxPython\py\Pyam.ico"
SectionEnd
SubSectionEnd

SubSection "Create shell extensions"
Section "Php extensions"
WriteRegStr HKCR ".php" "" "Php"
WriteRegStr HKCR "Php" "" "PHP Hypertext Processor file"
WriteRegStr HKCR "Php\shell\Open\command" "" '"$INSTDIR\PHP\bin\PHP.exe" "%1"'
WriteRegStr HKCR "Php\DefaultIcon" "" "$INSTDIR\PHP\bin\php.ico,0"
WriteRegStr HKCR ".inc" "" "Inc"
WriteRegStr HKCR "Inc" "" "PHP include file"
WriteRegStr HKCR "Inc\DefaultIcon" "" "$INSTDIR\PHP\bin\php.ico,0"
SectionEnd
Section "Perl extensions"
WriteRegStr HKCR ".pl" "" "Perl"
WriteRegStr HKCR "Perl" "" "Perl script file"
WriteRegStr HKCR "Perl\shell\Open\command" "" '"$INSTDIR\Perl\bin\perl.exe" "%1"'
WriteRegStr HKCR "Perl\DefaultIcon" "" "$INSTDIR\Perl\bin\mod_perl.ico,0"
WriteRegStr HKCR ".cgi" "" "Cgi"
WriteRegStr HKCR "Cgi" "" "CGI Perl script file"
WriteRegStr HKCR "Cgi\DefaultIcon" "" "$INSTDIR\Perl\bin\perl.exe,0"
SectionEnd
Section "Python extensions"
WriteRegStr HKCR ".py" "" "Python"
WriteRegStr HKCR "Python" "" "CGI Python script file"
WriteRegStr HKCR "Python\shell\Open\command" "" '"$INSTDIR\Python\bin\python.exe" "%1"'
WriteRegStr HKCR "Python\DefaultIcon" "" "$INSTDIR\Python\Bin\python.exe,0"
WriteRegStr HKCR ".pyc" "" "Pythonc"
WriteRegStr HKCR "Pythonc" "" "Python Compiled Script"
WriteRegStr HKCR "Pythonc\shell\Open\command" "" '"$INSTDIR\Python\bin\python.exe" "%1"'
WriteRegStr HKCR "Pythonc\DefaultIcon" "" "$INSTDIR\Python\BIN\pyc.ico,0"
WriteRegStr HKCR ".pyd" "" "Pythond"
WriteRegStr HKCR "Pythond" "" "Python Library"
WriteRegStr HKCR "Pythond\DefaultIcon" "" "$INSTDIR\Python\BIN\pyd.ico,0"
WriteRegStr HKCR ".pyw" "" "Pythonw"
WriteRegStr HKCR "Pythonw" "" "Python Startup Script"
WriteRegStr HKCR "Pythonw\shell\Open\command" "" '"$INSTDIR\Python\BIN\pythonw.exe" "%1"'
WriteRegStr HKCR "Pythonw\DefaultIcon" "" "$INSTDIR\Python\BIN\pythonw.exe,0"
WriteRegStr HKCR ".psp" "" "PSP"
WriteRegStr HKCR "PSP" "" "Python Server Page"
WriteRegStr HKCR "PSP\shell\Open\command" "" '"notepad.exe" "%1"'
WriteRegStr HKCR "PSP\DefaultIcon" "" "$INSTDIR\python\bin\psp.ico ,0"
WriteRegStr HKCR ".spy" "" "Spyce"
WriteRegStr HKCR "Spyce" "" "Spyce dynamic HTML file"
WriteRegStr HKCR "Spyce\shell\Open\command" "" '"notepad.exe" "%1"'
WriteRegStr HKCR "Spyce\DefaultIcon" "" "$INSTDIR\python\Lib\site-packages\spyce\spyce.ico ,0"
WriteRegStr HKCR "Spyce\shell" "" "compile"
WriteRegStr HKCR "Spyce\shell\compile" "" "Compile Spyce"
WriteRegStr HKCR "Spyce\shell\compile\command" "" '"$INSTDIR\PYTHON\BIN\PYTHON.EXE\" $INSTDIR\python\Lib\site-packages\spyce\run_spyceCmd.py -O %1'
SectionEnd
Section "Sql extensions"
WriteRegStr HKCR ".sql" "" "Sql"
WriteRegStr HKCR "Sql" "" "SQL Query File"
WriteRegStr HKCR "Sql\DefaultIcon" "" "$INSTDIR\sql.ico,0"
SectionEnd
SubSectionEnd


SubSection "Create enviroment variables"
Section "OPENSSL_CONF"
WriteRegStr HKCU Environment "OPENSSL_CONF" "$INSTDIR\opssl\bin"
SectionEnd
Section "SSLEAY_CONF"
WriteRegStr HKCU Environment "SSLEAY_CONF" "$INSTDIR\opssl\bin"
SectionEnd
Section "PHP_PEAR_SYSCONF_DIR"
WriteRegStr HKCU Environment "PHP_PEAR_SYSCONF_DIR" "$INSTDIR\php"
SectionEnd
Section "PHP_PEAR_INSTALL_DIR"
WriteRegStr HKCU Environment "PHP_PEAR_INSTALL_DIR" "$INSTDIR\php\pear"
SectionEnd
Section "PHP_PEAR_DOC_DIR"
WriteRegStr HKCU Environment "PHP_PEAR_DOC_DIR" "$INSTDIR\php\pear\docs"
SectionEnd
Section "PHP_PEAR_BIN_DIR"
WriteRegStr HKCU Environment "PHP_PEAR_BIN_DIR" "$INSTDIR\php\bin"
SectionEnd
Section "PHP_PEAR_DATA_DIR"
WriteRegStr HKCU Environment "PHP_PEAR_DATA_DIR" "$INSTDIR\php\pear\data"
SectionEnd
Section "PHP_PEAR_PHP_BIN"
WriteRegStr HKCU Environment "PHP_PEAR_PHP_BIN" "$INSTDIR\php\bin\php-cgi.exe"
SectionEnd
Section "PHP_PEAR_TEST_DIR"
WriteRegStr HKCU Environment "PHP_PEAR_TEST_DIR" "$INSTDIR\php\pear\tests"
SectionEnd
Section "APACHE2TRIAD_DIR"
WriteRegStr HKCU Environment "APACHE2TRIAD_DIR" "$INSTDIR"
SectionEnd
Section "PPM_DAT"
WriteRegStr HKCU Environment "PPM_DAT" "$INSTDIR\perl\site\lib\"
SectionEnd
SubSectionEnd

SubSection "Fixes, Mendings and Cleanup"
Section "Win98 System Enviroment fix"
  StrCmp $R0 "9X" conf_9x
  StrCmp $R0 "NT" conf_nt
  conf_nt:
  Goto done
  conf_9x:
FileOpen $1 "C:\config.sys" a
FileSeek $1 0 END
FileWrite $1 "$\r$\nSHELL=command.com /e:956 /p$\r$\n"
FileClose $1
  Goto done
  done:
SectionEnd
Section "Delete leftowers from other install kits"
Delete C:\my.cnf
Delete $WINDIR\system\php4ts.dll
Delete $WINDIR\system\php5ts.dll
Delete $WINDIR\system32\php4ts.dll
Delete $WINDIR\system\perl58.dll
Delete $WINDIR\system32\perl58.dll
Delete $WINDIR\system\ntwdblib.dll
Delete $WINDIR\system32\ntwdblib.dll
Delete $WINDIR\system\libeay32.dll
Delete $WINDIR\system32\libeay32.dll
Delete $WINDIR\system\ssleay32.dll
Delete $WINDIR\system32\ssleay32.dll
SectionEnd
SubSectionEnd

Section ""
;write version info
  FileOpen $0 "$INSTDIR\htdocs\apache2triadcp\version.txt" w
  FileWrite $0 "${VERSION}"
  FileClose $0
  WriteRegStr HKLM ${REG_PROG} "Version" "${VERSION}"
  WriteRegStr HKLM ${REG_PROG} "Location" "$INSTDIR"
;write uninstaler
  WriteUninstaller $INSTDIR\uninstall.exe
  WriteRegStr HKLM "${REG_UNINST}" "DisplayName" "${NAME}: ${DESC}"
  WriteRegStr HKLM "${REG_UNINST}" "UninstallString" '"$INSTDIR\uninstall.exe"'
;do postconfiguration
  ExecWait '"$INSTDIR\perl\bin\perl.exe" $INSTDIR\htdocs\apache2triadcp\fixrun.pl $INSTDIR'
  Sleep 1000
  ExecWait '"$INSTDIR\perl\bin\perl.exe" $INSTDIR\htdocs\apache2triadcp\fixpath.pl $INSTDIR'
  Sleep 1000
  Exec "$INSTDIR\mysql\bin\mysqld.exe --standalone"
  Sleep 1000
  ExecWait '"$INSTDIR\perl\bin\perl.exe" $INSTDIR\htdocs\apache2triadcp\fixpass.pl $R1 $INSTDIR'
  Sleep 1000
  ExecWait '"$INSTDIR\php\bin\php.exe" -c $INSTDIR\php\bin\basic.ini $INSTDIR\htdocs\apache2triadcp\fixpear.php $INSTDIR'
  Sleep 1000
  ExecWait 'runas /user:apache2triad "$INSTDIR\pgsql\bin\initdb.exe -U root -D $INSTDIR\pgsql\data\"'
  Sleep 10000
SectionEnd

Section "un.Stop services"
SectionIn RO
StrCmp $R0 "9X" ap_9x
StrCmp $R0 "NT" ap_nt
ap_nt:
;if nt
ExecWait "net stop MySql"
ExecWait "net stop XMail"
ExecWait "net stop SlimFTPd"
ExecWait "net stop Apache2"
ExecWait "net stop Apache2SSL"
ExecWait "net stop PgSQL"
Sleep 1000
Goto done
ap_9x:
;if 9x
ExecWait "killproc /K mysqld.exe"
ExecWait "killproc /K slimftpd.exe"
ExecWait "killproc /K httpd.exe"
ExecWait "killproc /K MySQLAdministrator.exe"
ExecWait "killproc /K MySQLSystemTrayMonitor.exe"
ExecWait "killproc /K MySQLQueryBrowser.exe"
ExecWait "killproc /K apachemonitor.exe"
ExecWait "killproc /K a2tm.exe"
Sleep 1000
Goto done
done:
SectionEnd
Section "un.Remove services"
SectionIn RO
ExecWait '"$INSTDIR\bin\instsrv.exe" Apache2 remove'
ExecWait '"$INSTDIR\bin\instsrv.exe" Apache2SSL remove'
ExecWait '"$INSTDIR\bin\instsrv.exe" MySql remove'
ExecWait '"$INSTDIR\bin\instsrv.exe" PgSQL remove'
ExecWait '"$INSTDIR\bin\instsrv.exe" XMail remove'
ExecWait '"$INSTDIR\bin\instsrv.exe" SlimFTPd remove'
SectionEnd
Section "un.Remove paths"
SectionIn RO
Push "$INSTDIR\bin"
  Call un.RemoveFromPath
Push "$INSTDIR\perl\bin"
  Call un.RemoveFromPath
Push "$INSTDIR\php\bin"
  Call un.RemoveFromPath
Push "$INSTDIR\mysql\bin"
  Call un.RemoveFromPath
Push "$INSTDIR\opssl\bin"
  Call un.RemoveFromPath
Push "$INSTDIR\python\bin"
  Call un.RemoveFromPath
Push "$INSTDIR\pgsql\bin"
  Call un.RemoveFromPath
SectionEnd
Section "un.Remove shortcuts"
SectionIn RO
  RMDir /r "$STARTMENU\${NAME}"
SectionEnd
Section "un.Remove configuration files"
SectionIn RO
  Delete $WINDIR\my.ini
  Delete $WINDIR\odbc.ini
  Delete $WINDIR\php.ini
SectionEnd
Section "un.Remove enviroment variables"
SectionIn RO
DeleteRegValue HKCU Environment "OPENSSL_CONF"
DeleteRegValue HKCU Environment "SSLEAY_CONF"
DeleteRegValue HKCU Environment "PHP_PEAR_SYSCONF_DIR"
DeleteRegValue HKCU Environment "PHP_PEAR_INSTALL_DIR"
DeleteRegValue HKCU Environment "PHP_PEAR_DOC_DIR"
DeleteRegValue HKCU Environment "PHP_PEAR_BIN_DIR"
DeleteRegValue HKCU Environment "PHP_PEAR_DATA_DIR"
DeleteRegValue HKCU Environment "PHP_PEAR_PHP_BIN"
DeleteRegValue HKCU Environment "PHP_PEAR_TEST_DIR"
DeleteRegValue HKCU Environment "APACHE2TRIAD_DIR"
DeleteRegValue HKCU Environment "PPM_DAT"
SectionEnd
Section "un.Remove aplication registry enteries"
SectionIn RO
DeleteRegKey HKLM SOFTWARE\ODBC\ODBCINST.INI\MyODBC
DeleteRegValue HKLM "SOFTWARE\ODBC\ODBCINST.INI\ODBC Drivers" "MyODBC"
DeleteRegValue HKLM "SOFTWARE\ODBC\ODBC.INI\ODBC Data Sources" "MySQL"
DeleteRegKey HKCU SOFTWARE\ODBC\ODBC.INI\MySQL
DeleteRegKey HKLM SOFTWARE\ODBC\ODBCINST.INI\PsqlODBC
DeleteRegValue HKLM "SOFTWARE\ODBC\ODBCINST.INI\ODBC Drivers" "PsqlODBC"
DeleteRegValue HKLM "SOFTWARE\ODBC\ODBC.INI\ODBC Data Sources" "PostgreSQL"
DeleteRegKey HKCU SOFTWARE\ODBC\ODBC.INI\PostgreSQL
DeleteRegKey HKLM SOFTWARE\GNU\XMail
DeleteRegKey HKLM Software\Python
DeleteRegKey HKLM Software\PostgreSQL
DeleteRegKey HKCU "Software\pgAdmin III"
SectionEnd
Section "un.Remove apache2triad user"
SectionIn RO
StrCmp $R0 "9X" ap_9x
StrCmp $R0 "NT" ap_nt
ap_nt:
;if nt
 ExecWait '"$INSTDIR\bin\editrights.exe" -r SeServiceLogonRight -u apache2triad'
 ExecWait "net user apache2triad /delete"
 RMDir /r "C:\Documents and Settings\apache2triad"
Goto done
ap_9x:
;if 9x
Goto done
done:
SectionEnd
Section "un.Remove files"
SectionIn RO
  RMDir /r "$INSTDIR\mysql"
  RMDir /r "$INSTDIR\pgsql"
  RMDir /r "$INSTDIR\perl"
  RMDir /r "$INSTDIR\php"
  RMDir /r "$INSTDIR\python"
  RMDir /r "$INSTDIR\htdocs"
  RMDir /r "$INSTDIR"
SectionEnd
Section "un.Remove uninstaller"
SectionIn RO
  Delete $INSTDIR\uninstall.exe
  DeleteRegKey HKLM ${REG_UNINST}
  DeleteRegKey HKLM ${REG_PROG}
SectionEnd

;#####################################
;FUNCTIONS

Function .onInit
;get the os
Call GetOs
Pop $R0
;lil code to make corect service
StrCmp $R0 "9X" ap_9x
StrCmp $R0 "NT" ap_nt
ap_nt:
StrCpy $R5 ""
StrCpy $R6 "-k runservice"
Goto done
ap_9x:
StrCpy $R5 "-D AEX"
StrCpy $R6 "-k start"
Goto done
done:
;make sure its not installed
Call PreUninst
FunctionEnd

Function .onInstSuccess
  HideWindow
MessageBox MB_OK "${NAME} ${VERSION} has been successfully configured , press ok to reboot ."
  Reboot
FunctionEnd

Function un.onInit
Call un.GetOs
Pop $R0
  MessageBox MB_OK|MB_ICONEXCLAMATION "Everything under $INSTDIR will be deleted , make sure to backup your files and export your databases before proceeding."
FunctionEnd

Function un.onUninstSuccess
  HideWindow
MessageBox MB_OK "${NAME} ${VERSION} has been entirely removed."
FunctionEnd

;====================================================
; Check for spaces.

Function PathCheck
Push $INSTDIR
Push " "
Call StrStr
Pop $R0
  StrCmp $R0 "" l_match l_nomatch
  l_match:
  goto end
  l_nomatch:
  MessageBox MB_OK|MB_ICONEXCLAMATION "No spaces are allowed !"
  Quit
  goto end
end:
FunctionEnd

Function PassCheck
Push $R1
Push " "
Call StrStr
Pop $R0
  StrCmp $R0 "" l_match l_nomatch
  l_match:
  goto end
  l_nomatch:
  MessageBox MB_OK|MB_ICONEXCLAMATION "No spaces are allowed !"
  Quit
  goto end
end:
FunctionEnd
;====================================================

;====================================================
; Getos - gets NT or 9X depending on os.
Function GetOs
Push $R0
ReadRegStr $R0 HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion" CurrentVersion
IfErrors lbl_win9x lbl_winnt

lbl_winnt:
StrCpy $R0 "NT"
Goto lbl_done

lbl_win9x:
StrCpy $R0 "9X"
Goto lbl_done

lbl_done:
Exch $R0
FunctionEnd
;====================================================

;====================================================
; Getos - gets NT or 9X depending on os.
Function un.GetOs
Push $R0
ReadRegStr $R0 HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion" CurrentVersion
IfErrors lbl_win9x lbl_winnt

lbl_winnt:
StrCpy $R0 "NT"
Goto lbl_done

lbl_win9x:
StrCpy $R0 "9X"
Goto lbl_done

lbl_done:
Exch $R0
FunctionEnd
;====================================================

;====================================================
; PreUninst - checks to see if the program is allready installed
Function PreUninst
  ReadRegStr $1 HKLM "${REG_PROG}" Version
  StrCmp $1 "" done cont
cont:
  HideWindow
  MessageBox MB_OK|MB_ICONEXCLAMATION "${NAME} $1 is already installed.$\n$\nPlease remove it before installing ${VERSION}."
  Abort
done:
FunctionEnd
;====================================================

!verbose 3
!include "WinMessages.NSH"
!verbose 4
;====================================================
; AddToPath - Adds the given dir to the search path.
;        Input - head of the stack
;        Note - Win9x systems requires reboot
;====================================================
Function AddToPath
  Exch $0
  Push $1

  Call IsNT
  Pop $1
  StrCmp $1 1 AddToPath_NT
    ; Not on NT
    StrCpy $1 $WINDIR 2
    FileOpen $1 "$1\autoexec.bat" a
    FileSeek $1 0 END
    GetFullPathName /SHORT $0 $0
    FileWrite $1 "$\r$\nSET PATH=%PATH%;$0$\r$\n"
    FileClose $1
    Goto AddToPath_done

  AddToPath_NT:
    ReadRegStr $1 HKLM "SYSTEM\CurrentControlSet\Control\Session Manager\Environment" "PATH"
    StrCmp $1 "" AddToPath_NTdoIt
      StrCpy $0 "$1;$0"
      Goto AddToPath_NTdoIt
    AddToPath_NTdoIt:
      WriteRegExpandStr HKLM "SYSTEM\CurrentControlSet\Control\Session Manager\Environment" "PATH" $0
      SendMessage ${HWND_BROADCAST} ${WM_WININICHANGE} 0 "STR:Environment" /TIMEOUT=5000

  AddToPath_done:
    Pop $1
    Pop $0
FunctionEnd

;====================================================
; RemoveFromPath - Remove a given dir from the path
;     Input: head of the stack
;====================================================
Function un.RemoveFromPath
  Exch $0
  Push $1
  Push $2
  Push $3
  Push $4

  Call un.IsNT
  Pop $1
  StrCmp $1 1 unRemoveFromPath_NT
    ; Not on NT
    StrCpy $1 $WINDIR 2
    FileOpen $1 "$1\autoexec.bat" r
    GetTempFileName $4
    FileOpen $2 $4 w
    GetFullPathName /SHORT $0 $0
    StrCpy $0 "SET PATH=%PATH%;$0"
    SetRebootFlag true
    Goto unRemoveFromPath_dosLoop

    unRemoveFromPath_dosLoop:
      FileRead $1 $3
      StrCmp $3 "$0$\r$\n" unRemoveFromPath_dosLoop
      StrCmp $3 "$0$\n" unRemoveFromPath_dosLoop
      StrCmp $3 "$0" unRemoveFromPath_dosLoop
      StrCmp $3 "" unRemoveFromPath_dosLoopEnd
      FileWrite $2 $3
      Goto unRemoveFromPath_dosLoop

    unRemoveFromPath_dosLoopEnd:
      FileClose $2
      FileClose $1
      StrCpy $1 $WINDIR 2
      Delete "$1\autoexec.bat"
      CopyFiles /SILENT $4 "$1\autoexec.bat"
      Delete $4
      Goto unRemoveFromPath_done

  unRemoveFromPath_NT:
    StrLen $2 $0
    ReadRegStr $1 HKLM "SYSTEM\CurrentControlSet\Control\Session Manager\Environment" "PATH"
    Push $1
    Push $0
    Call un.StrStr ; Find $0 in $1
    Pop $0 ; pos of our dir
    IntCmp $0 -1 unRemoveFromPath_done
      ; else, it is in path
      StrCpy $3 $1 $0 ; $3 now has the part of the path before our dir
      IntOp $2 $2 + $0 ; $2 now contains the pos after our dir in the path (';')
      IntOp $2 $2 + 1 ; $2 now containts the pos after our dir and the semicolon.
      StrLen $0 $1
      StrCpy $1 $1 $0 $2
      StrCpy $3 "$3$1"

      WriteRegExpandStr HKLM "SYSTEM\CurrentControlSet\Control\Session Manager\Environment" "PATH" $3
      SendMessage ${HWND_BROADCAST} ${WM_WININICHANGE} 0 "STR:Environment" /TIMEOUT=5000

  unRemoveFromPath_done:
    Pop $4
    Pop $3
    Pop $2
    Pop $1
    Pop $0
FunctionEnd

;====================================================
; IsNT - Returns 1 if the current system is NT, 0
;        otherwise.
;     Output: head of the stack
;====================================================
Function IsNT
  Push $0
  ReadRegStr $0 HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion" CurrentVersion
  StrCmp $0 "" 0 IsNT_yes
  ; we are not NT.
  Pop $0
  Push 0
  Return

  IsNT_yes:
    ; NT!!!
    Pop $0
    Push 1
FunctionEnd

;====================================================
; un.StrStr - Finds a given string in another given string.
;               Returns -1 if not found and the pos if found.
;          Input: head of the stack - string to find
;                      second in the stack - string to find in
;          Output: head of the stack
;====================================================
Function un.StrStr
  Push $0
  Exch
  Pop $0 ; $0 now have the string to find
  Push $1
  Exch 2
  Pop $1 ; $1 now have the string to find in
  Exch
  Push $2
  Push $3
  Push $4
  Push $5

  StrCpy $2 -1
  StrLen $3 $0
  StrLen $4 $1
  IntOp $4 $4 - $3

  unStrStr_loop:
    IntOp $2 $2 + 1
    IntCmp $2 $4 0 0 unStrStrReturn_notFound
    StrCpy $5 $1 $3 $2
    StrCmp $5 $0 unStrStr_done unStrStr_loop

  unStrStrReturn_notFound:
    StrCpy $2 -1

  unStrStr_done:
    Pop $5
    Pop $4
    Pop $3
    Exch $2
    Exch 2
    Pop $0
    Pop $1
FunctionEnd

;====================================================
; un.IsNT - Returns 1 if the current system is NT, 0
;        otherwise.
;     Output: head of the stack
;====================================================
Function un.IsNT
  Push $0
  ReadRegStr $0 HKLM "SOFTWARE\Microsoft\Windows NT\CurrentVersion" CurrentVersion
  StrCmp $0 "" 0 unIsNT_yes
  ; we are not NT.
  Pop $0
  Push 0
  Return

  unIsNT_yes:
    ; NT!!!
    Pop $0
    Push 1
FunctionEnd

;====================================================
; RegWrite - writes windows registry strings
;  especially usefull for making REG_MULTI_SZ
;  strings as they are not implemented into NSIS
;====================================================
Function RegWrite
!define HKEY_CLASSES_ROOT        0x80000000
!define HKEY_CURRENT_USER        0x80000001
!define HKEY_LOCAL_MACHINE       0x80000002
!define HKEY_USERS               0x80000003
!define HKEY_PERFORMANCE_DATA    0x80000004
!define HKEY_PERFORMANCE_TEXT    0x80000050
!define HKEY_PERFORMANCE_NLSTEXT 0x80000060
!define HKEY_CURRENT_CONFIG      0x80000005
!define HKEY_DYN_DATA            0x80000006

!define KEY_QUERY_VALUE          0x0001
!define KEY_SET_VALUE            0x0002
!define KEY_CREATE_SUB_KEY       0x0004
!define KEY_ENUMERATE_SUB_KEYS   0x0008
!define KEY_NOTIFY               0x0010
!define KEY_CREATE_LINK          0x0020

!define REG_NONE                 0
!define REG_SZ                   1
!define REG_EXPAND_SZ            2
!define REG_BINARY               3
!define REG_DWORD                4
!define REG_DWORD_LITTLE_ENDIAN  4
!define REG_DWORD_BIG_ENDIAN     5
!define REG_LINK                 6
!define REG_MULTI_SZ             7

!define RegCreateKey             "Advapi32::RegCreateKeyA(i, t, *i) i"
!define RegSetValueEx            "Advapi32::RegSetValueExA(i, t, i, i, i, i) i"
!define RegCloseKey              "Advapi32::RegCloseKeyA(i) i"

  SetPluginUnload alwaysoff
  ; Create a buffer for the multi_sz value
  System::Call "*(&t${NSIS_MAX_STRLEN}) i.r1"
  ; Open/create the registry key
  System::Call "${RegCreateKey}(${HKEY_LOCAL_MACHINE}, '$SUB_KEY', .r0) .r9"
  ; Failed?
  IntCmp $9 0 write
    MessageBox MB_OK|MB_ICONSTOP "Can't create registry key! ($9)"
    Goto noClose

  write:
    ; Fill in the buffer with our strings
    StrCpy $2 $1                            ; Initial position

    StrLen $9 '$DATA_1'                   ; Length of first string
    IntOp $9 $9 + 1                         ; Plus null
    System::Call "*$2(&t$9 '$DATA_1')"    ; Place the string
    IntOp $2 $2 + $9                        ; Advance to the next position

    StrLen $9 '$DATA_2'                   ; Length of second string
    IntOp $9 $9 + 1                         ; Plus null
    System::Call "*$2(&t$9 '$DATA_2')"    ; Place the string
    IntOp $2 $2 + $9                        ; Advance to the next position

    System::Call "*$2(&t1 '')"              ; Place the terminating null
    IntOp $2 $2 + 1                         ; Advance to the next position

    ; Create/write the value
    IntOp $2 $2 - $1                        ; Total length
    System::Call "${RegSetValueEx}(r0, '$VALUE', 0, ${REG_MULTI_SZ}, r1, r2) .r9"
    ; Failed?
    IntCmp $9 0 done
      MessageBox MB_OK|MB_ICONSTOP "Can't set key value! ($9)"
      Goto done

  done:
    ; Close the registry key
    System::Call "${RegCloseKey}(r0)"

noClose:
  ; Clear the buffer
  SetPluginUnload manual
  System::Free $1
FunctionEnd


Function StrStr
  Exch $R1 ; st=haystack,old$R1, $R1=needle
  Exch    ; st=old$R1,haystack
  Exch $R2 ; st=old$R1,old$R2, $R2=haystack
  Push $R3
  Push $R4
  Push $R5
  StrLen $R3 $R1
  StrCpy $R4 0
  ; $R1=needle
  ; $R2=haystack
  ; $R3=len(needle)
  ; $R4=cnt
  ; $R5=tmp
  loop:
    StrCpy $R5 $R2 $R3 $R4
    StrCmp $R5 $R1 done
    StrCmp $R5 "" done
    IntOp $R4 $R4 + 1
    Goto loop
  done:
  StrCpy $R1 $R2 "" $R4
  Pop $R5
  Pop $R4
  Pop $R3
  Pop $R2
  Exch $R1
FunctionEnd