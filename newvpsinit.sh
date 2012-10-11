#!/bin/sh
if [ $# -gt 0 ]
then
	rootpwd=`apg  -n 1 -m 8 -x 8 -q`
	nobodypwd=`apg -n 1 -m 8 -x 8 -q`
	echo  `date`"\t"$1"\t"$rootpwd"\t"$nobodypwd >> passwd.txt
	echo  `date`"\t"$1"\t"$rootpwd"\t"$nobodypwd 

	#添加root的密钥
#	ssh-copy-id  root@$1
	echo "root密钥已经添加！"
	#添加sshd ip限制/更改密码
	ssh root@$1 "echo -e 'sshd:116.236.239.218:allow\nsshd:all:deny'>/etc/hosts.allow;/etc/init.d/ssh restart;echo 已经添加IP限制;echo -e '$rootpwd\n$rootpwd' | passwd root;echo -e '$nobodypwd\n$nobodypwd' | passwd nobody;"
	#更改root密码
		
else
	echo "需要传入IP或者域名"
fi
#ssh root@$i "echo -e 'sshd:116.236.239.218:allow\nsshd:all:deny'>/etc/hosts.allow;/etc/init.d/ssh restart"
