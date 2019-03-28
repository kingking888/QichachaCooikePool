
from QichachaRegister import QichachaRegister
from w6888 import w6888_login, get_hm

if __name__ == "__main__":
    token = w6888_login("kkisabodybuilder","eminem")
    hm = get_hm(token)
    print(hm)
    c = QichachaRegister()
    is_success = c.qichacha_register(hm,token)
    c.close()


