from cookie_pool import update_solr
from login import Qichacha


def add_cookie():
    with open(file="new_register.txt",mode="r",encoding="utf-8") as f:
        a = f.readlines()
        print(a)
    for id in a:
        try:
            i = id.strip()
            print(i)
            c = Qichacha()
            cookie = c.qichacha_login(i, "123456")
            c.close()
            update_solr(i, cookie)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    add_cookie()