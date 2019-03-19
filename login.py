import time
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from fateadm_api import TestFunc

SlIDER_LEN = 308


class Qichacha:

    def __init__(self):
        self.b1 = webdriver.Firefox(executable_path="D:/geckodriver.exe")
        self.b1.get("https://www.qichacha.com/user_login")
    def close(self):
        self.b1.close()
    def qichacha_login(self, id, password):
        '''
        :Description：登录企查查平台：https://www.qichacha.com/user_login?back=%2F
        :return:
        '''
        # self.b1.delete_all_cookies()
        sleep(1)
        self.b1.find_element_by_xpath("//a[@id='normalLogin']").click()
        # 填写用户名
        user = self.b1.find_element_by_xpath("//input[@id='nameNormal']")
        user.send_keys(id)
        # 输入密码
        pd = self.b1.find_element_by_xpath("//input[@id='pwdNormal']")
        pd.send_keys(password)
        # 定位验证码
        while(True):
            try:
                slider = self.b1.find_element_by_xpath("//span[@id='nc_1_n1z']")
                ActionChains(self.b1).click_and_hold(slider).perform()
                ActionChains(self.b1).move_by_offset(xoffset=SlIDER_LEN, yoffset=0).perform()
                sleep(1)
                break
            except NoSuchElementException as e:
                print("定位验证码")
            except Exception as e:
                print(e)
        # 截图验证码，下载验证码，使用接码平台来识别验证码
        identifying_code_pic = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time())) + ".png"
        while (True):
            try:
                self.b1.find_element_by_xpath("//div[@id='nc_1__imgCaptcha_img']//img").screenshot(identifying_code_pic)
                break
            except NoSuchElementException as nSuch:
                print("加载验证码中")
                pass
            except Exception as e:
                print(e)
                pass
            sleep(1)
        identifying_code = TestFunc(identifying_code_pic)
        # 填写验证码
        while (True):
            try:
                yzm = self.b1.find_element_by_xpath("//input[@id='nc_1_captcha_input']")
                yzm.send_keys(identifying_code.value)
                break
            except NoSuchElementException as nSuch:
                print("加载验证码输入框中")
                pass
            except Exception as e:
                print(e)
                pass
            sleep(1)
        # 点击验证码确认按钮
        while (True):
            try:
                self.b1.find_element_by_xpath("//div[@id='nc_1_scale_submit']").click()
                break
            except NoSuchElementException as nSuch:
                print("点击验证码确认按钮中")
                pass
            except Exception as e:
                print(e)
                pass
            sleep(1)
        while (True):
            sleep(3)
            if 'user_login' not in self.b1.current_url:
                print("进入页面...")
                break
            else:
                print("点击中...")
                self.b1.find_element_by_xpath("//button[@class='btn btn-primary btn-block m-t-md login-btn']").click()
        # 点击
        self.close_weixin()
        self.search()
        return "".join([_['name']+"="+_['value']+";" for _ in self.get_search_cookie()])

    def get_search_cookie(self):
        i = 0
        while (i < 5):
            if "search?key" in self.b1.current_url:
                a = self.b1.get_cookies()
                print(a)
                return a
            else:
                sleep(3)
                print("加载中...")
            i += 1
        print("xx")

    def close_weixin(self):
        try_time = 0
        while (try_time < 10):
            sleep(4)
            print(try_time)
            try:
                # self.b1.find_element_by_xpath("//div[@id='bindWxQrcode']")
                self.b1.find_element_by_xpath("//button[@class='close']").click()
                print("成功关闭微信界面")
                return
            except NoSuchElementException as nSuch:
                print("暂时无微信界面")
            except Exception as e:
                print(e)
                pass

            try_time += 1
        print("一直无微信界面继续操作...")

    def search(self,word="京东"):

        self.b1.find_element_by_xpath("//input[@id='searchkey']").send_keys(word)
        # 注意这里停顿 保证搜索按钮可以加载
        while (True):
            sleep(3)
            try:
                c = self.b1.find_element_by_xpath("//span[@class='input-group-btn']")
                c.click()
                break
            except NoSuchElementException as nSuch:
                print("点击搜索键中")
                pass
            except Exception as e:
                print(e)
                pass

    def while_wait(self):
        while (True):
            sleep(0.5)

            break
if __name__ == "__main__":
    c = Qichacha()
    cookie = c.qichacha_login("15834664125", "123456")
    c.close()