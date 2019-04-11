from cookie_pool import update_solr
from login import Qichacha


def add_cookie():
    with open(file="new_register.txt",mode="r",encoding="utf-8") as f:
        a = f.readlines()
        print(a)
    for id in a:
        i = id.strip()
        print(i)
        c = Qichacha()
        try:
            cookie = c.qichacha_login(i, "123456")
        except Exception as e:
            print(e)
        c.close()
        if len(cookie)>0:
            update_solr(i, cookie)



if __name__ == "__main__":
    add_cookie()