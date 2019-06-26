'''
  百度文字识别api
'''


from aip import AipOcr
import re
APP_ID='16637095'
API_KEY ='2Y3fFKCqOzjWK4UlbgsKTZ6P'
SECRECT_KEY='AuU5bA138Sbb55KjdNm2ERDrpXjMVMwN'
client=AipOcr(APP_ID,API_KEY,SECRECT_KEY)
i=open(r'C:\Users\Administrator\Desktop\订单状态.png','rb')
img=i.read()
message=client.basicGeneral(img)
print(message)
