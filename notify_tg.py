import requests
import urllib.parse
import urllib.request
def send_notify(text, desp, send_key=''):
    """
    发送通知消息的函数。
    
    参数:
    - text: 消息的正文，字符串类型。
    - desp: 消息的描述，字符串类型。
    - send_key: 发送密钥，可选参数，默认为空字符串。用于API认证。
    
    返回值:
    - result: 发送结果，字符串类型。一般为API返回的状态信息。
    """

    alltext = text + desp
    url = f'https://vercel.virola.me/api/send?sendkey={send_key}'
    postdata = urllib.parse.urlencode({'text': alltext }).encode('utf-8')

    req = urllib.request.Request(url, data=postdata, method='POST')
    with urllib.request.urlopen(req) as response:
        result = response.read().decode('utf-8')
    return result
