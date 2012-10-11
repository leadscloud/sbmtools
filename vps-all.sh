#!/bin/sh
vps="106.187.35.214
106.187.91.26
106.187.103.23
106.187.102.107
ubuntu.eagle-project.org
www.eshibang.com
198.58.96.62
66.175.214.46"

for i in $vps
do 
	echo "正在处理\t"$i;
	plink -l root -v -pw shibang416 $i "wget http://www.kposui.com/httpd-substitute.conf -O /opt/lampp/etc/extra/httpd-substitute.conf && /opt/lampp/lampp restartapache"
done
