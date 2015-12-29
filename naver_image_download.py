import urllib2
import xml.etree.ElementTree as ET


def naver_image_query(q):
 url = "http://openapi.naver.com/search?key=[Naver_Api_Key]&target=image&start=1&display=5&query="+q
 response = urllib2.urlopen(url)
 data = response.read()
 root = ET.fromstring(data)

 fileNo = 0

 for item in root.find("channel").findall("item"):
  title = item.find("title")
  link = item.find("link")
  thumbnail = item.find("thumbnail")
  print title.text
  print link.text
  print thumbnail.text

  contents = urllib2.urlopen(link.text).read()
  file(str(fileNo)+'.jpg', 'wb').write(contents)
  fileNo = fileNo + 1

naver_image_query("school")
