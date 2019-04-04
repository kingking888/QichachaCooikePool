import requests
import time

from login import Qichacha
import json

def update_solr(user_name,user_cookie,isValid="True"):
    params = {"overwrite": "true", "commitWithin": 1000, "wt": "json"}
    solr_into_url = "http://blackbox01.jry.com:8983/solr/qichacha_cookie_shard1_replica2/update"
    headers = {"Content-Type": "application/json"}
    solr_data = [{"id": user_name,
                  "userCookie": {"set":user_cookie},
                  "logoutTime":{"set":0},
                  "createTime":{"set":time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))},
                  "lastUsedTime":{"set":time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))},
                  "isValid":{"set":isValid}}
                  ]
    a = json.dumps(solr_data, ensure_ascii=False)
    re = requests.post(solr_into_url, data=a,params=params,headers=headers)
    print(re.text)
def check_invalid_cookie():
    invalid = "http://blackbox01.jry.com:8983/solr/qichacha_cookie_shard1_replica2/select?q=isValid%3Afalse&rows=1000&wt=json&indent=true"
    res = requests.get(invalid)
    print(res.json()['response'])
    for doc in res.json()['response']['docs']:
        try:
            c = Qichacha()
            print(doc['id'])
            cookie = c.qichacha_login(doc['id'],"123456")
            c.close()
            update_solr(doc['id'],cookie)
            c.close()
        except Exception as e:
            print(e)
#
# def test():
#     id = "18783137343"
#     # cookie = "".join([_['name']+"="+_['value']+";" for _ in a])
#     cookie = "acw_tc=7a0e2b1315529652542844046e4600dec2eee9ccea164ecc7cadc4c0e5;_uab_collina=155296505777830027705897;UM_distinctid=16993ee3d459-0bfbe09aa792d08-4c312979-1fa400-16993ee3d462a8;QCCSESSID=ullk9lp1967ak9118ucfdcb6j7;hasShow=1;zg_did=%7B%22did%22%3A%20%2216993ee3d62412-046cc783922976-4c312979-1fa400-16993ee3d63191%22%7D;zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201552965057896%2C%22updated%22%3A%201552965102474%2C%22info%22%3A%201552965057905%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%2248957b8d214e7bbf3f2292d0c20bfa67%22%7D;CNZZDATA1254842228=921924930-1552964611-%7C1552964611;Hm_lvt_3456bee468c83cc63fb5147f119f1075=1552965058;Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1552965103;"
#     # check_invalid_cookie()
#     update_solr(id, cookie)
if __name__ == "__main__":
    while(True):
        check_invalid_cookie()
        time.sleep(5)
