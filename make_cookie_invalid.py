from cookie_pool import update_solr
#
with open("qichacha.password",encoding='utf-8',mode='r') as f:
    a = f.readlines()
for i in a:
    print(i.replace("\n",""))
    update_solr(i.replace("\n",""),"x","False")
# update_solr("13944595031","acw_tc=2a51048515559020333501303e9d24b8b28d188cb1a1f30443221e9ad8;_uab_collina=155590177723025587700153;UM_distinctid=16a42f905d344-0317dcd68e4a62-4c312f7f-1fa400-16a42f905d435b;QCCSESSID=tvak1jebt99dju85csbcggrj97;hasShow=1;zg_did=%7B%22did%22%3A%20%2216a42f904ee59-0b1d65388ee5368-4c312f7f-1fa400-16a42f904ef2b0%22%7D;zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201555901777139%2C%22updated%22%3A%201555901800377%2C%22info%22%3A%201555901777143%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22cuid%22%3A%20%22e000da1d756b8790437d62dc86a79e43%22%7D;CNZZDATA1254842228=11866743-1555897952-%7C1555897952;Hm_lvt_3456bee468c83cc63fb5147f119f1075=1555901778;Hm_lpvt_3456bee468c83cc63fb5147f119f1075=1555901801;","True")