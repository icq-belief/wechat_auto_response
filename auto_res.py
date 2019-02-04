import itchat, time, requests, random
from itchat.content import *

replied = []

@itchat.msg_register([TEXT])
def text_reply(msg):
  for m in msg['Text']:
    if m in ['新','年','春','节'] and msg['FromUserName'] not in replied:
      sendGreeting(msg)
      break
    else:
      pass
    # if ('年' or '新' or '春' or '节') in msg['Text'] and msg['FromUserName'] not in replied:


@itchat.msg_register([PICTURE, RECORDING, VIDEO, SHARING])
def other_reply(msg):
  if msg['FromUserName'] not in replied:
    sendGreeting(msg)

def sendGreeting(msg):
  global replied
  friend = itchat.search_friends(userName=msg['FromUserName'])
  time.sleep(10)
  itchat.send((friend['RemarkName']+'，'+getRandomGreeting()), msg['FromUserName'])
  replied.append(msg['FromUserName'])

def getRandomGreeting():
  response = requests.get("http://www.xjihe.com/api/life/greetings?festival=新年&page=10", headers = {'apiKey':'sQS2ylErlfm9Ao2oNPqw6TqMYbJjbs4g'})
  results = response.json()['result']
  greeting = results[random.randrange(len(results))]['words']
  return greeting
if __name__ == '__main__':

  itchat.auto_login(enableCmdQR=2,hotReload=True)
  itchat.run()