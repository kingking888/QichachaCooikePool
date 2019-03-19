import time
from time import sleep
from PIL import Image
from io import BytesIO
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from fateadm_api import TestFunc

SlIDER_LEN = 308
def qichacha_login(id,password):
    '''
    :Description：登录企查查平台：https://www.qichacha.com/user_login?back=%2F
    :return:
    '''
    # b1.delete_all_cookies()
    b1.find_element_by_xpath("//a[@id='normalLogin']").click()
    # 填写用户名
    user = b1.find_element_by_xpath("//input[@id='nameNormal']")
    user.send_keys(id)
    # 输入密码
    pd = b1.find_element_by_xpath("//input[@id='pwdNormal']")
    pd.send_keys(password)
    # 定位验证码
    slider = b1.find_element_by_xpath("//span[@id='nc_1_n1z']")
    ActionChains(b1).click_and_hold(slider).perform()
    ActionChains(b1).move_by_offset(xoffset=SlIDER_LEN,yoffset=0).perform()
    # 截图验证码，下载验证码，使用接码平台来识别验证码
    identifying_code_pic =time.strftime('%Y%m%d-%H%M%S',time.localtime(time.time()))+".png"
    while(True):
        try:
            b1.find_element_by_xpath("//div[@id='nc_1__imgCaptcha_img']//img").screenshot(identifying_code_pic)
            break
        except NoSuchElementException as nSuch:
            print("加载验证码中")
            pass
        except Exception as e:
            pass
        sleep(1)
    identifying_code = TestFunc(identifying_code_pic)
    # 填写验证码
    yzm = b1.find_element_by_xpath("//input[@id='nc_1_captcha_input']")
    sleep(3)
    yzm.send_keys(identifying_code.value)
    # 点击验证码确认按钮
    b1.find_element_by_xpath("//div[@id='nc_1_scale_submit']").click()
    while(True):
        sleep(3)
        if 'user_login' not in b1.current_url:
            print("进入页面...")
            break
        else:
            print("点击中...")
            b1.find_element_by_xpath("//button[@class='btn btn-primary btn-block m-t-md login-btn']").click()
    # 点击
    close_weixin()
    search()
    get_search_cookie()
def get_search_cookie():
    i = 0
    while(i<5):
        if "search?key" in b1.current_url:
            a = b1.get_cookies()
            print(a)
            return a
        else:
            sleep(3)
            print("加载中...")
        i+=1
    print("xx")
def close_weixin():
    try_time = 0
    while(try_time<10):
        sleep(3)
        print(try_time)
        try:
            # b1.find_element_by_xpath("//div[@id='bindWxQrcode']")
            b1.find_element_by_xpath("//button[@class='close']").click()
            print("成功关闭微信界面")
            return
        except:
            pass

            print("无微信界面")
        try_time += 1
def search(word = "京东"):

    b1.find_element_by_xpath("//input[@id='searchkey']").send_keys(word)
    # 注意这里停顿 保证搜索按钮可以加载
    sleep(3)
    c = b1.find_element_by_xpath("//span[@class='input-group-btn']")
    c.click()
def while_wait():
    while(True):
        sleep(0.5)


        break

print("xx")
if __name__ == "__main__":
    b1 = webdriver.Firefox(executable_path="D:/geckodriver.exe")
    b1.get("https://www.qichacha.com/user_login")
    qichacha_login("18224089826","123456")

