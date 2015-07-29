#
#
# Author : fcbruce <fcbruce8964@gmail.com>
#
# Time : Wed 29 Jul 2015 12:49:09 PM CST
#
#

import re
import requests
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

fuid=open('uid.txt','r')
fcid=open('cid.txt','r')
fResult=open('result.txt','w')

def calc(cid,uids):
  #init
  result={}
  for i in uids.values():
    result[i]={}

  #reveive data
  url='http://acm.hust.edu.cn/vjudge/data/contest_standing/'+cid+'.json'
  r=requests.get(url)

  #analyse data, by regular expression
  pattern=re.compile(r'\d+,\d+,\d+,\d+')
  get= pattern.findall(r.text)

  #calculate
  for i in get : 
    uid,pid,isac,time=map(str,i.split(','))
    if uid in uids.values() and isac == '1': result[uid][pid]=1
  return result


uids={} #key Team Name, value uid
count={} #key uid, value problems number

#read team information
for line in fuid:
  name,uid=line.split()
  uids[name]=uid
  count[uid]=0

#Title
fResult.write('%15s' % ('Contest id'),)
for i in uids: fResult.write( '%20s' % (i),)
fResult.write('\n') 

#read contest information and calculate
for line in fcid:
  cid,name=line.split()
  print cid,name
  tmp=calc(cid,uids)
  fResult.write( '%15s' % (cid),)
  for name in uids.keys():
    uid=uids[name]
    count[uid]+=len(tmp[uid])
    fResult.write( '%20s' % (len(tmp[uid])),)
  fResult.write('\n')

fResult.write( '%15s' % ('Total'),)

for uid in uids.values():
  fResult.write( '%20s' % (count[uid]),)

fResult.write('\n')
  

  


