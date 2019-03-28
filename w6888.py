
import requests as re

def w6888_login(id,psw):
    res = re.get("http://w6888.cn:9180/service.asmx/UserLoginStr?name={0}&psw={1}".format(id,psw))
    if res.status_code == 200:
        return res.content.decode('utf-8')
def get_hm(token,xmid="10832"):
    res = re.get("http://w6888.cn:9180/service.asmx/GetHMStr?token={0}&xmid={1}&sl=1&lx=0&a1=&a2=&pk=".format(token,xmid))
    if res.status_code == 200:
        hm = res.content.decode('utf-8').split("=")[1]
        return hm
def get_yzm(token,hm,xmid="10832"):
    try:
        res = re.get("http://w6888.cn:9180/service.asmx/GetYzmStr?token={0}&hm={1}&xmid={2}"
                 .format(token,hm,xmid))
        if res.status_code == 200:
            return res.content.decode('utf-8')
    except Exception as e:
        print(e)
        # release_hm(token,hm)
        return False
def release_hm(token,hm):
    res = re.get("http://w6888.cn:9180/service.asmx/sfHmStr?token={0}&hm={1}".format(token,id))
    if res.status_code == 200:
        if res.content.decode('utf-8') == 1:
            print("号码:"+hm+"释放成功")

def write_regsitered_hm(hm):
    with open("new_register.txt",mode='a+',encoding='utf=8') as f:
        f.writelines(hm+"\n")
