#coding=gbk
# -*- coding: utf-8 -*-
import pycurl
import wave
from pyaudio import PyAudio,paInt16
import urllib.request
import json

framerate=8000
NUM_SAMPLES=2000
channels=1
sampwidth=2
TIME=2
def save_wave_file(filename,data):
    '''save the date to the wavfile'''
    wf=wave.open(filename,'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth) 
    wf.setframerate(framerate)
    wf.writeframes(b"".join(data))
    wf.close()

def my_record():
    pa=PyAudio()
    stream=pa.open(format = paInt16,channels=1,
                   rate=framerate,input=True,
                   frames_per_buffer=NUM_SAMPLES)
    my_buf=[]
    count=0
    while count<TIME*10:#����¼��ʱ��
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count+=1
        print('.')
    save_wave_file('01.wav',my_buf)
    stream.close()

def get_token():
    apiKey="Pqza5qCUNa1LQFkTebH8NDwT" #
    secreKey="W2iS5ZInNqS3ax6Q3LrG1nLU6HWc0mVV" 
    auth_url="https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id="+apiKey+"&client_secret="+secreKey;

    res=urllib.request.urlopen(auth_url)
    json_data=res.read()
    #print('type:',type(json_data))
    return json.loads(json_data)['access_token']

def dump_res(buf):
    #print('buf=',buf)
    my_temp=json.loads(buf)
    if(my_temp['err_no']==3301):
        print('ʶ��ʧ��')
        return
    my_list=my_temp['result']
    #print(type(my_list))
    #print('mylist[0]: ',my_list[0])
    print(my_list)

def use_cloud(token):
    fp=wave.open('01.wav','rb')
    nf = fp.getnframes()  # ��ȡ�ļ��Ĳ���������
    #print('sampwidth:', fp.getsampwidth())
    #print('framerate:', fp.getframerate())
    #print('channels:', fp.getnchannels())
    f_len = nf * 2  # �ļ����ȼ��㣬ÿ������2���ֽ�
    audio_data = fp.readframes(nf)

    cuid="gfhdygrt"
    srv_url='http://vop.baidu.com/server_api' + '?cuid=' + cuid + '&token=' +token
    http_header=[
        'Content-Type:audio/pcm;rate=8000',
        'Content-Length: %d' % f_len
    ]
    c=pycurl.Curl()
    c.setopt(pycurl.URL,str(srv_url)) #curl doesn't support unicode ����һ����ַ
    #c.setopt(c.RETURNTRANSFER,1)
    c.setopt(c.HTTPHEADER,http_header)#����һ��ͷ����ֻ�����б��������ֵ�
    c.setopt(c.POST,1)#����
    c.setopt(c.CONNECTTIMEOUT,80)#��������ʱ��
    c.setopt(c.TIMEOUT,80)#����ʱ��
    c.setopt(c.WRITEFUNCTION,dump_res)
    c.setopt(c.POSTFIELDS,audio_data)
    c.setopt(c.POSTFIELDSIZE,f_len)
    c.perform() # pycurl.perform() has no return val


if __name__ == '__main__':
    my_record()
    print('ʶ��ɹ���')
    use_cloud(get_token())
#https://blog.csdn.net/yexiaohhjk/article/details/73134815?utm_source=blogxgwz4




# ~ import requests
# ~ import json

# ~ # ¼��
# ~ # from record import Record
# ~ from Record import Record
# ~ record=Record(channels=1)
# ~ audioData=record.record(2)

# ~ # ��ȡtoken
# ~ from secret import API_KEY,SECRET_KEY
# ~ authUrl='https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials' \
        # ~ '&client_id=' + API_KEY + '&client_secret=' +SECRET_KEY
# ~ response=requests.get(authUrl)
# ~ res = json.loads(response.content)
# ~ token=res['access_token']

# ~ # ����ʶ��
# ~ cuid='xxxxxxxxxx'
# ~ srvUrl='http://vop.baidu.com/server_api'+'?cuid='+cuid+'&token='+token
# ~ httpHeader={
    # ~ 'Content-Type':'audio/wav; rate=8000',
# ~ }

# ~ response=requests.post(srvUrl,headers=httpHeader,data=audioData)
# ~ res=json.loads(response.content)
# ~ text=res['result'][0]

# ~ print (u'\nʶ������')
# ~ print (text)
# ~ #https://blog.csdn.net/qd_ltf/article/details/79704792

############################################################################
# ~ import requests
# ~ import json
# ~ import uuid
# ~ import base64

# ~ def get_token():
    # ~ url = "https://openapi.baidu.com/oauth/2.0/token"
    # ~ grant_type = "client_credentials"
    # ~ api_key = "Pqza5qCUNa1LQFkTebH8NDwT"                     # �Լ������Ӧ��
    # ~ secret_key = "W2iS5ZInNqS3ax6Q3LrG1nLU6HWc0mVV"            # �Լ������Ӧ��
    # ~ data = {'grant_type': 'client_credentials', 'client_id': api_key, 'client_secret': secret_key}
    # ~ r = requests.post(url, data=data)
    # ~ token = json.loads(r.text).get("access_token")
    # ~ return token


# ~ def recognize(sig, rate, token):
    # ~ url = "http://vop.baidu.com/server_api"
    # ~ speech_length = len(sig)
    # ~ speech = base64.b64encode(sig).decode("utf-8")
    # ~ mac_address = uuid.UUID(int=uuid.getnode()).hex[-12:]
    # ~ rate = rate
    # ~ data = {
        # ~ "format": "wav",
        # ~ "lan": "zh",
        # ~ "token": token,
        # ~ "len": speech_length,
        # ~ "rate": rate,
        # ~ "speech": speech,
        # ~ "cuid": mac_address,
        # ~ "channel": 1,
    # ~ }
    # ~ data_length = len(json.dumps(data).encode("utf-8"))
    # ~ headers = {"Content-Type": "application/json",
               # ~ "Content-Length": data_length}
    # ~ r = requests.post(url, data=json.dumps(data), headers=headers)
    # ~ print(r.text)


# ~ filename = "miao.wav"

# ~ signal = open(filename, "rb").read()
# ~ rate = 8000

# ~ token = get_token()
# ~ recognize(signal, rate, token)

# ~ from aip import AipSpeech
 
# ~ """ ��� APPID AK SK """
# ~ APP_ID = '14494700'
# ~ API_KEY = 'Pqza5qCUNa1LQFkTebH8NDwT'
# ~ SECRET_KEY = 'W2iS5ZInNqS3ax6Q3LrG1nLU6HWc0mVV'
 
# ~ client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# ~ # ��ȡ�ļ�
# ~ def get_file_content(filePath):
    # ~ with open(filePath, 'rb') as fp:
        # ~ return fp.read()
 
# ~ # ʶ�𱾵��ļ�
# ~ result_json=client.asr(get_file_content('miao.wav'), 'wav', 16000, {
    # ~ 'lan': 'zh',
# ~ })
# ~ result = result_json['result'][0].replace("��", "")

############################################################################

# https://www.cnblogs.com/Vrapile/p/8421403.html
