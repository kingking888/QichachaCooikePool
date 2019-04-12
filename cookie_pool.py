import requests
import time

from login import Qichacha
import json

from setting import SOLR_LOCAL


def update_solr(user_name,user_cookie,isLogIn="True"):
    params = {"overwrite": "true", "commitWithin": 1000, "wt": "json"}
    solr_into_url = SOLR_LOCAL
    headers = {"Content-Type": "application/json"}
    solr_data = [{"id": user_name,
                  "userCookie": {"set":user_cookie},
                  "loginTime":{"set":time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))},
                  "lastUsedTime": {"set": time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))},
                  "isLogIn": {"set":isLogIn},
                  "isBanned": {"set": "False"},
                  "logoutTime":{"set":0},
                  "BannedTime":{"set":0}}
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
            if len(cookie) > 0:
                update_solr(doc['id'],cookie)

        except Exception as e:
            print(e)

if __name__ == "__main__":
    while(True):
        check_invalid_cookie()
        time.sleep(5)
