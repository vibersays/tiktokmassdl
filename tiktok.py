import requests,json,wget
print('OK')
def palupila(kode,urut):
    try:
        url = 'http://api.areltiyan.xyz/tiktokwm?link='+kode
        r = requests.get(url,verify=False).json()
        print (r['status'])
        a = (r['no_watermark_link'])
        file_name = 'oke.mp4'
        wget.download(a,file_name)
        print ('\33[32m Success '+str(urut)+' \33[39m')
    except:
        print('Gagal= ',kode)
        pass
print ('Tiktok Mass Download Thx to : \33[96mArel Tiyan\33[39m ')
list_kode = input("List url tiktoknya ngab : ")
read_kode = open(list_kode,"r") 
urut = 0
for kode in read_kode:
    urut +=1
    kode = kode.strip()
    palupila(kode,urut)
