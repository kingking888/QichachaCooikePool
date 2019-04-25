import requests

from cookie_pool import update_solr
from login import Qichacha
from setting import SOLR_1


def is_in_solr(id):
    res = requests.get(SOLR_1.format(str(id)))

    return res.json()['response']['numFound']>0
def add_cookie():
    with open(file="qichacha.password",mode="r",encoding="utf-8") as f:
        a = f.readlines()
        print(a)
    for id in a:
        i = id.strip()
        print(i)
        if not is_in_solr(i):
            c = Qichacha()
            try:
                cookie = c.qichacha_login(i, "123456")
                c.close()
                if len(cookie) > 0:
                    update_solr(i, cookie)
            except Exception as e:
                print(e)




if __name__ == "__main__":
    add_cookie()