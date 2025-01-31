AH='result'
AG='www.google.com'
AF='en-US,en;q=0.9,fr;q=0.8'
AE='gzip, deflate'
AD='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
AC='Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'
AB='max-age=0'
AA='keep-alive'
A9='referer'
A8='Accept-Language'
A7='Accept-Encoding'
A6='Accept'
A5='User-Agent'
A4='Upgrade-Insecure-Requests'
A3='Cache-Control'
A2='Connection'
A1='Task Complete Press Enter to return to the main menu...'
A0='All in One BY TEAM ANON FORCE'
y='\x1b[0;36m'
x=' ---> '
w='\x1b[1;32m'
v='ns2.'
u='ns1.'
t='cpcontacts.'
s='mail.'
r='cpcalendars.'
q='webdisk.'
p='cpanel.'
o='ftp.'
n='webmail.'
m='Grabbed.txt'
l='utf-8'
k='1'
j='\x1b[1;31mThread: '
c='/'
b='clear'
a='ignore'
X='\n'
W='www.'
V='cls'
U='nt'
T=True
S=str
Q='r'
O='https://'
N='http://'
M=int
F='a'
E=''
C=input
B=open
A=print
import sys as P,requests as G,re as K,ctypes,threading,socket,os as D,warnings as AI
from multiprocessing.dummy import Pool as Y
from pathlib import Path
from colorama import Fore as H,init
AI.filterwarnings(a,category=G.packages.urllib3.exceptions.InsecureRequestWarning)
init(autoreset=T)
R=H.RED
Z=H.GREEN
AJ=H.WHITE
z=H.CYAN
L="\x1b[0;36m\n         _____ ___  ______   _____  _____ \n        |_   _/ _ \\ |  ___| |____ ||  _  |\n          | |/ /_\\ \\| |_        / /| |/' |\n          | ||  _  ||  _|       \\ \\|  /| |\n          | || | | || |     .___/ /\\ |_/ /\n          \\_/\\_| |_/\\_|     \\____(_)\\___/ \n\n              \x1b[1;32m [CODED BY: Professor6T9] \n               https://t.me/teamanonforce\n               \x1b[0;31mversion: \x1b[0;33m0.1"
def J():D.system(V if D.name==U else b)
if D.name==U:ctypes.windll.kernel32.SetConsoleTitleW(A0)
else:P.stdout.write(A0)
def AK():J();A(L);A('\n        \x1b[0;36m Reverse IP Private [3 API]\n        \n        \x1b[1;32mNote: Lower Threads Better Results  \n        ');D=C('\x1b[1;31mEnter list ip : ');E=M(C(j));F=B(D,mode=Q,errors=a).read().splitlines();G=Y(E);G.map(AO,F);C('TASK COMPLETED')
def AL():
	J();A(L);A('\n        \x1b[0;36m Domain To IP\n        \n        \x1b[1;32mNote: Recomended Threads 300 \n        ');G.urllib3.disable_warnings();H=C('\x1b[1;31mEnter list Domains : ')
	try:
		with B(H,Q)as I:S=[A.strip()for A in I if A.strip()]
	except FileNotFoundError:A('File not found:',H);P.exit(1)
	T=M(C(j))
	def U(site):
		A=site
		if A.startswith(N):A=A.replace(N,E)
		elif A.startswith(O):A=A.replace(O,E)
		if W in A:A=A.replace(W,E)
		A=A.rstrip()
		if A.split(c):A=A.split(c)[0]
		while A[-1]==c:B=K.compile('(.*)/');C=K.findall(B,A);A=C[0]
		return A
	def V(url):
		G=' --> {}[DomainNotwork]';D=' -| ';C=url
		try:
			H=U(C)
			try:E=socket.gethostbyname(H);A(D+C+' --> {}[{}]'.format(Z,E));B('IPs.txt',F).write(E+X)
			except:A(D+C+G.format(R))
		except:A(D+C+G.format(R))
	D=Y(T);D.map(V,S);D.close();D.join();C(A1)
def AM():
	J()
	def D(i):
		try:
			C=i.split('.')
			for E in range(0,255):D='{0}.{1}.{2}.{3}'.format(C[0],C[1],C[2],S(E));A(D);B('ip_ranged.txt',F).write(D+X)
		except:pass
	A(L);E=C('\x1b[0;32mEnter ip : ');G=B(E,Q,errors=a).read().splitlines();H=Y(100);H.map(D,G);C(A1)
def AN():
	J();A(L);A('\n        \x1b[0;36m CMS Checker\n        \n        \x1b[1;32mNote: Recommended Threads 300 \n        ')
	try:U=C('\x1b[1;31mSite Lists: ');V=Path(__file__).with_name(U);W=[A.strip()for A in V.open(Q).readlines()]
	except IndexError:H=S(P.argv[0]).split('\\');exit('\n\x1b[1;31m  [!] Enter <'+H[len(H)-1]+'> <your list.txt>')
	X=M(C(j))
	def I(site):
		A=site
		if A.startswith(N):A=A.replace(N,E)
		elif A.startswith(O):A=A.replace(O,E)
		else:0
		B=K.compile('(.*)/')
		while K.findall(B,A):C=K.findall(B,A);A=C[0]
		return A
	def a(url):
		M='[!]';L='/\n';K='WordPress.txt';J=' --> {}[WordPress]';H='\x1b[0;32m[!]';C=url;E={A2:AA,A3:AB,A4:k,A5:AC,A6:AD,A7:AE,A8:AF,A9:AG}
		try:
			C=N+I(C);D=G.get(C+'/wp-includes/css/buttons.css',headers=E,allow_redirects=T,timeout=15)
			if'WordPress-style Buttons'in D.content.decode(l):A(H+C+J.format(Z));B(K,F).write(C+L)
			else:
				C=O+I(C);D=G.get(C+c,headers=E,allow_redirects=T,verify=False,timeout=15)
				if'wp-'in D.content.decode(l):A(H+C+J.format(Z));B(K,F).write(C+L)
				else:A(M+C+' --> {}[Other CMS]'.format(R))
		except G.exceptions.RequestException:A(M+C+' --> {}[Domain Not Reachable]'.format(R))
	D=Y(X);D.map(a,W);D.close();D.join();C('\n [!] {}Task Finished Press Enter to return to the main menu...'.format(z))
def AO(ip):AQ(ip);AR(ip);AS(ip)
AP='unknown'
def AQ(ip):
	try:
		H='https://rapiddns.io/s/'+ip+'?full=1&down=1#result';I=G.get(H,timeout=10000).text;J=K.findall('<td>(?!\\-)(?:[a-zA-Z\\d\\-]{0,62}[a-zA-Z\\d]\\.){1,126}(?!\\d+)[a-zA-Z]{1,63}</td>',I)[3:]
		with B(m,F)as L:
			for D in J:
				C=D.lower()
				if AH not in C and'total'not in C:
					if not C.startswith(n)and not C.startswith(o)and not C.startswith(p)and not C.startswith(q)and not C.startswith(r)and not C.startswith(s)and not C.startswith(t)and not C.startswith(u)and not C.startswith(v):D=D.replace(W,E);D=D.replace('<td>',E);D=D.replace('</td>',E);A('\x1b[1;31m[REVIP_API_1]: '+w+ip+x+y+D);L.write(D+X)
	except:pass
def AR(ip):
	try:
		H='https://api.webscan.cc/?action=query&ip='+ip;I=G.get(H,timeout=10000).text;J=K.findall('"domain": "(.*?)",',I)[3:]
		with B(m,F)as L:
			for D in J:
				C=D.lower()
				if AH not in C and'total'not in C:
					if not C.startswith(n)and not C.startswith(o)and not C.startswith(p)and not C.startswith(q)and not C.startswith(r)and not C.startswith(s)and not C.startswith(t)and not C.startswith(u)and not C.startswith(v):D=D.replace(W,E);A('\x1b[1;31m[REVIP_API_2]: '+w+ip+x+y+D);L.write(D+X)
	except:pass
def AS(ip):
	H='Domains'
	try:
		I='http://de-datacenter.xreverselabs.my.id:1337/reverse-ip?apikey='+AP+'&ip='+ip;J=G.get(I,timeout=10000).text;L=K.findall('"(.*?)"',J)[3:]
		with B(m,F)as M:
			for D in L:
				C=D.lower()
				if'status'not in C and'success'not in C and H not in C:
					if not C.startswith(n)and not C.startswith(o)and not C.startswith(p)and not C.startswith(q)and not C.startswith(r)and not C.startswith(s)and not C.startswith(t)and not C.startswith(u)and not C.startswith(v):D=D.replace(W,E);D=D.replace(H,E);A('\x1b[1;31m[REVIP_API_3]: '+w+ip+x+y+D);M.write(D+X)
	except:pass
def d(directory):
	A=directory
	if not D.path.exists(A):D.makedirs(A)
d('Date_Grabbed')
def J():D.system(V if D.name==U else b)
def Af():D.system(V if D.name==U else b)
def AT(year,month,day,result_list):
	B=f"{year}-{month:02d}-{day:02d}";D=f"http://files.xz.com/{B}.txt"
	try:
		C=G.get(D);C.raise_for_status();E=C.text.splitlines()
		for F in E:result_list.append(F)
		A(f"Successfully collected website list for {B}")
	except G.RequestException as H:A(f"Failed to collect website list for {B}. Error: {H}")
import os as D,sys as P,threading,requests as G,concurrent.futures
from colorama import Fore as H,Style as e,init
init(autoreset=T)
f=0
I=0
AU=0
g=0
h=0
i=0
AV=0
AW=0
AX=0
R=H.RED
Ag=H.BLUE
z=H.CYAN
AJ=H.WHITE
Ah=H.YELLOW
Z=H.GREEN
Ai=e.DIM
Aj=e.NORMAL
Ak=e.BRIGHT
def d(directory):
	A=directory
	if not D.path.exists(A):D.makedirs(A)
d('Shell')
def AY():
	try:
		if D.name==U:D.system(V)
		else:D.system(b)
	except:pass
def J():AY()
def __init__():D.system(V);G.urllib3.disable_warnings()
def AZ(site):
	A=site
	if A.startswith(N)or A.startswith(O):return A.replace(N,E).replace(O,E)
	else:return A
def Aa(domain):
	H='Shell/random.txt';C=domain;global f,I,AU,g,h,i,AV,AW,AX
	try:
		C=AZ(C.strip());J={A2:AA,A3:AB,A4:k,A5:AC,A6:AD,A7:AE,A8:AF,A9:AG}
		for D in B('configs.txt',Q,encoding=l).readlines():
			D=D.strip();K=f"https://{C}/{D}";E=G.get(f"https://{C}/{D}",K,headers=J,verify=False,timeout=30).text
			if'No route found for "'not in S(E)and'Apache2'not in S(E)and'ErrorException'not in S(E):
				if'>public_html'in E:B('Shell/shell.txt',F).write(f"http://{C}/{D}\n");I=I+1;A(f"[x] http://{C}/{D} -->[0;32m[Shell Found]");break
				elif'<span>Upload file:'in E:B(H,F).write(f"http://{C}/{D}\n");I=I+1;A(f"[x] http://{C}/{D} -->[0;32m[Shell Found]");break
				elif'type="submit" id="_upl" value="Upload">'in E:B('Shell/Uploader.txt',F).write(f"http://{C}/{D}\n");I=I+1;A(f"[x] http://{C}/{D}  -->[0;32m[Shell Found]");break
				elif'Leaf PHPMailer'in E or'>alexusMailer 2.0<'in E:B('Shell/Mailer.txt',F).write(f"http://{C}/{D}\n");h=h+1;A(f"[x] http://{C}/{D}  -->[0;32m[Mailer Found]");break
				elif'method=post>Password:'in E or'<input type=password name=pass'in E:B('Shell/password.txt',F).write(f"http://{C}/{D}\n");g=g+1;A(f"[x] http://{C}/{D}  -->[0;32m[Shell Found]");break
				elif'name="uploader" id="uploader">'in E:B(H,F).write(f"http://{C}/{D}\n");I=I+1;A(f"[x] http://{C}/{D}  -->[0;32m[Shell Found]");break
				elif'Upload File : <input'in E:B(H,F).write(f"http://{C}/{D}\n");I=I+1;A(f"[x] http://{C}/{D}  -->[0;32m[Shell Found]");break
				else:A(f"[x] http://{C}/{D}  -->[0;31m[Shell Not Found]");f=f+1
	except:i=i+1;pass
def Ab():
	try:D=P.argv[1];E=P.argv[2];F=B(D).read().splitlines()
	except:
		try:D=C('\x1b[1;33mList :');F=B(D,Q,errors=a).read().splitlines()
		except:A('\x1b[0;31mList not found!')
		try:E=C('\x1b[1;33mThreads :')
		except:A('\x1b[0;31mWrong thread number!')
	try:
		with concurrent.futures.ThreadPoolExecutor(M(E))as G:G.map(Aa,F)
	except Exception as H:A(H)
def Ac(banner):J();A(banner);Ab();C('Press Enter to return to the main menu...')
def Ad():
	global L
	while T:
		J();A(L);A(E);A('\x1b[1;33m1. Domain to IP');A('\x1b[1;33m2. Range IPs');A('\x1b[1;33m3. Reverse IP \x1b[1;32m[Private 3 api]');A('\x1b[1;33m4. CMS Checker');A('\x1b[1;33m5. Grab Domains By Date \x1b[1;32m[Best For WP-Brute]');A('\x1b[1;33m6. Shell Finder \x1b[1;32m[Add Path On config.txt]');A('\x1b[0;31m7. Exit');A('\x1b[1;34m8. More Options will Be added soon.');A(E);B=C('\x1b[0;32mEnter your choice: ')
		if B==k:AL()
		elif B=='2':AM()
		elif B=='3':AK()
		elif B=='4':AN()
		elif B=='5':Ae()
		elif B=='6':Ac(L)
		elif B=='7':A('\x1b[0;32mExiting the program. Goodbye!');break
		else:A('\x1b[0;31mInvalid choice. Please enter a number from 1 to 7.')
def Ae():
	J();A(L);A('\x1b[0;35mWebsite Grabber by Date [Best For WP-Bruteforce ]\n');A('\x1b[1;33mExample Usage:\n             Year: 2024\n             Month: 01\n             Date: 01\n             Number of dates to collect:30\n             \n             \x1b[0;31mNote: Wait for result until all successful attempt');G=M(C('\x1b[1;31mEnter year: '));H=M(C('\x1b[1;31mEnter month: '));I=M(C('\x1b[1;31mEnter day: '));O=M(C('\x1b[0;31mNumber of dates to collect:'));K=[];N=[]
	for F in range(O):D=[];E=threading.Thread(target=AT,args=(G,H,I+F,D));N.append(E);K.append(D);E.start()
	for E in N:E.join()
	for(F,D)in enumerate(K):
		P=f"{G}-{H:02d}-{I+F:02d}";Q=f"grabbed_{P}.txt"
		with B(f"Date_Grabbed/{Q}",'w')as R:
			for S in D:R.write(f"{S}\n")
	C('Website lists collected successfully and saved date-wise!')
if __name__=='__main__':Ad()