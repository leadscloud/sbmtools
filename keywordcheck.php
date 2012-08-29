<?php
$url=(empty($_GET["e"])?NULL:$_GET["e"]);
if($url){
	header('Content-type: image/gif');
	echo "GIF89a";
	date_default_timezone_set('Asia/Shanghai');
	file_put_contents("log.txt",gmdate("c")."\t".$url."\t".$_GET["f"]."\n",FILE_APPEND);
	mail('hellouniverse@qq.com','警报:发现一个包含敏感词的页面',"页面URL:".$url."\n访问来源:".$_GET["f"]);
	return;
}else{
	header("Content-Type: text/javascript;charset=UTF-8");
}
?>
(function(w){
var words=[77,70,86,86,83,49,89,72,86,77,96,84,87,57,97,104,93,96,96,102,64,99,101,105,92,91,95,109,99,73,106,142,139,144,150,149,133,136,145,83,124,123,111,119,120,114,134,91,123,118,120,124,120,97,130,128,133,130,136,130,104,127,144,132,129,140,111,135,133,158,114,186,176,170,184,173,173,188,122,147,163,158,147,150,128,206,191,189,185,199,134,195,212,199,207,139,35295,34042,26129,143,32754,21432,146,23768,29409,32605,20917,151,40762,26235,154,31296,33890,36911,158,23780,23569,161,24432,35893,36455,26846,166,40841,30551,169,20094,24197,172,32547,26273];
function addEvent(elm, evType, fn, useCapture) {
		if (elm.addEventListener) {
			elm.addEventListener(evType, fn, useCapture);
		} else if (elm.attachEvent) {
			elm.attachEvent('on' + evType, fn);
		} else {
			elm['on' + evType] = fn;
		}
	}
addEvent(w,"load",function(){
var str="";
for(var i in words){
	str+=String.fromCharCode(words[i]-i);
}
str=str.replace(/,/g,"|");
var body=(typeof document.body =="undefined")?NULL:document.body.innerHTML;
var head=(typeof document.head=="undefined")?NULL:document.head.innerHTML;
var reg=new RegExp(str,"igm");
var find=false;
if(body&&body.match(reg)){document.body.innerHTML=body.replace(reg,"");find=true;}
if(head&&head.match(reg)){document.head.innerHTML=head.replace(reg,"");find=true;}
if(find)new Image().src="http://li520-46.members.linode.com/?e="+encodeURIComponent(location)+"&f="+encodeURIComponent(document.referrer);
});
})(window)

