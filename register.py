
from QichachaRegister import QichachaRegister
from w6888 import w6888_login, get_hm, release_hm
import _thread
def run():
    # 注册15个
    num =100
    for i in range(num):
        print("----------------start: "+ str(i+1) + "----------------")
        try:
            token = w6888_login("kkisabodybuilder", "eminem")
            hm = get_hm(token)
            print(hm)
            c = QichachaRegister()
            is_success = c.qichacha_register(hm, token)
            c.close()
        except Exception as e:
            print(e)
        print("----------------end: "+ str(i+1) + "----------------")
#
# def release():
#
#     release_hm(token, id)
if __name__ == "__main__":
    run()