<?php

if ($action == "register") {
	system ("regsvr32 /s C:\apache2triadpath\php\bin\PHPDbgPS.dll");
	system ("DbgListener.exe -RegServer");
}
if ($action == "unregister") {
	system ("regsvr32 /s /u C:\apache2triadpath\php\bin\PHPDbgPS.dll");
	system ("DbgListener.exe -UnRegServer");
}

if ($action == "register" || $action == "unregister" ){
	echo "<script>window.alert(\"Sucesfully {$action}d dbg listener.\")</script>";
}
?>

<script language=javascript>
<!--
history.go(-2);
// -->
</script>