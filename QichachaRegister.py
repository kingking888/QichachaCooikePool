from time import sleep
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from fateadm_api import TestFunc
from w6888 import get_yzm, release_hm, write_regsitered_hm

SlIDER_LEN = 308


class QichachaRegister:
    def __init__(self):
        self.b1 = webdriver.Firefox(executable_path="C:/geckodriver.exe")
        self.b1.get("https://www.qichacha.com/user_register")

    def close(self):
        self.b1.close()

    def qichacha_register(self, id,token,password = '123456'):
        '''
        :Description：登录企查查平台：https://www.qichacha.com/user_login?back=%2F
        :return:
        '''
        # self.b1.delete_all_cookies()
        sleep(1)
        # self.b1.find_element_by_xpath("//a[@id='normalLogin']").click()
        # 填写用户名
        user = self.b1.find_element_by_xpath("//input[@id='phone']")
        user.send_keys(id)
        # 输入密码
        pd = self.b1.find_element_by_xpath("//input[@id='pswd']")
        pd.send_keys(password)
        # 定位验证码
        while (True):
            try:
                slider = self.b1.find_element_by_xpath("//span[@id='nc_1_n1z']")
                ActionChains(self.b1).click_and_hold(slider).perform()
                ActionChains(self.b1).move_by_offset(xoffset=SlIDER_LEN, yoffset=0).perform()
                sleep(1)
                break
            except NoSuchElementException as e:
                print("定位验证码中")
            except Exception as e:
                print(e)
        # 截图验证码，下载验证码，使用接码平台来识别验证码
        identifying_code_pic = "yzm/"+time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time())) + ".png"
        while (True):
            trytime=0
            if trytime > 60:
                release_hm(token,id)
                return
            try:
                self.b1.find_element_by_xpath("//div[@id='nc_1__imgCaptcha_img']//img").screenshot(identifying_code_pic)
                break
            except NoSuchElementException as nSuch:
                print("加载验证码中")
                pass
            except Exception as e:
                print(e)
                pass
            trytime+=1
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
        # 点击获取验证
        while (True):
            try:
                self.b1.find_element_by_xpath("//a[@class='text-primary vcode-btn get-mobile-code']").click()
                break
            except NoSuchElementException as nSuch:
                print("点击获取验证码确认按钮中")
                pass
            except Exception as e:
                print(e)
                pass
            sleep(1)
        # 等待短信验证码
        dxyzm = str()
        while(True):
            wait_time = 0
            content = get_yzm( token,id)

            if wait_time > 30 or content == False:
                print("收不到验证码，放弃。")
                return
            if  content != "-1" and content != "0" and content != '1':
                dxyzm =  content[content.rfind("。") - 6:content.rfind("。")]
                print("短信验证码为:"+dxyzm)

                break
            else:
                sleep(5)
                wait_time += 1
                # print("获取短信验证码中")
        # 填写短信验证码
        while (True):
            try:
                yzm_click = self.b1.find_element_by_xpath("//input[@id='vcodeNormal']")
                yzm_click.send_keys(dxyzm)
                break
            except NoSuchElementException as nSuch:
                print("点击获取验证码确认按钮中")
                pass
            except Exception as e:
                print(e)
                pass
            sleep(1)
        # 点击注册
        while (True):
            try:
                self.b1.find_element_by_xpath("//button[@class='btn btn-primary btn-block m-t-md login-btn']").click()
                break
            except NoSuchElementException as nSuch:
                print("点击注册按钮中")
                pass
            except Exception as e:
                print(e)
                pass
            sleep(1)
        print(id)
        while(True):
            try:
                if self.b1.current_url == 'https://www.qichacha.com/':
                    print("注册成功")
                    write_regsitered_hm(id)
                    release_hm(token,id)
                    break


            except Exception as e:
                print(e)
            sleep(1)



