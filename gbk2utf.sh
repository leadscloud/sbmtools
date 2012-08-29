#!/bin/sh
count=0
for i in `find -type f -name "*.html"`
do if [ $((count%100)) -eq 0 ]
then echo $count" "$i
fi
count=$((count+1))
iconv -f GBK -t UTF-8 $i > /tmp/t
mv /tmp/t $i
sed -i "s/gb2312/utf-8/ig" $i
done
echo "一共转换:"$count
#count=0;for i in `find -type f -name "*.html"`;do if [ $((count%100)) -eq 0 ];then echo $count" "$i;fi;count=$((count+1));iconv -f GBK -t UTF-8 $i > /tmp/t;mv /tmp/t $i;sed -i "s/gb2312/utf-8/ig" $i; done
