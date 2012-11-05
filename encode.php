<?php
if($argc<2)die("Usage:\n\tencode.php keywordfile [utf-8|gbk]");
set_time_limit(0);
ini_set("memory_limit","1024M");
$lines=explode("\n",file_get_contents($argv[1]));
$ret="";
$encode=isset($argv[2]);
foreach($lines as $line){
	$line=urlencode($encode?(mb_convert_encoding(trim($line),$argv[2])):trim($line));
	//这里可以写上格式
	$ret.="http://www.baidu.com/s?wd={$line}\n";
}
file_put_contents($argv[1]."_encode_".(isset($argv[2])?$argv[2]:"default").".txt",$ret);
?>

