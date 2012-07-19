<?php

$location = $GLOBALS['argv'][1];

$data["preferred_state"] = "stable";
$data["bin_dir"] = "$location\php\bin";
$data["php_dir"] = "$location\php\pear";
$data["doc_dir"] = "$location\php\pear\docs";
$data["data_dir"] = "$location\php\pear\data";
$data["test_dir"] = "$location\php\pear\\tests";
$data["php_bin"] = "$location\php\bin\php-cgi.exe";

$contents = "#pear_Config 0.9\n" . serialize($data);

$fh = fopen("$location\php\bin\pear.ini", "w") or die ("could not open $fname");
fwrite($fh,$contents) or die ("could not write to $fname");
fclose($fh);

?>