import time
from time import sleep
from PIL import Image
from io import BytesIO
from selenium import webdriver

from fateadm_api import TestFunc


def laima_login():
    '''
    :Description：登录来码接码平台：http://www.w6888.cn/
    :return:
    '''
    # 填写用户名
    user = b2.find_element_by_xpath("//input[@id='yhmc']")
    user.send_keys("kkisabodybuilder")
    # 输入密码
    pd = b2.find_element_by_xpath("//input[@id='psw']")
    pd.send_keys("eminem")
    # 截图验证码，下载验证码，使用接码平台来识别验证码
    identifying_code_pic =time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))+".png"
    b2.find_element_by_xpath("//img[@id='imgRandom']").screenshot(identifying_code_pic)
    identifying_code = TestFunc(identifying_code_pic)
    # 填写验证码
    yzm = b2.find_element_by_xpath("//input[@id='yzm']")
    yzm.send_keys(identifying_code.value)
    # 点击登录按钮
    b2.find_element_by_xpath("//input[@id='btnOK']").click()
    print("xx")
def while_wait():
    while(True):
        sleep(0.5)

        break
b1 = webdriver.Firefox()
b2 = webdriver.Firefox()
b1.get("https://www.qichacha.com/user_register")
b2.get("http://www.w6888.cn/index.html")
#
laima_login()
# 提交表单
# b2.find_element_by_xpath("//*[@id='su']").click()

print("xx")