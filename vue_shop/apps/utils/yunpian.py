import requests
import json

class YunPian(object):
    def __init__(self,APIkey):
        self.APIkey = APIkey
        # 云片网发送短信的url
        self.single_send_url= "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self,code,mobile):
        parmas = {
            "apikey":self.APIkey,
            "mobile":mobile,
            # text填云片网的模板,需要和云片网一致
            'text':"【方智生鲜超市】#{code}#(#app#手机验证码，请完成验证)，如非本人操作，请忽略本短信".format(code=code)
        }
        response = requests.post(self.single_send_url,data=parmas)
        re_dict = json.load(response.text)
        return re_dict


if __name__ == "__main__":
    # 填入云片网的apikey = 55ba3ec9bdd5e2865d5a1ca48f9e5bd5
    yun_pian = YunPian('apikey的值')
    yun_pian.send_sms('2018','手机号码')