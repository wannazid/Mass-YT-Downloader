#mass yt download using python3
#by : wannazid
import os
import pafy
from colorama import Fore, Back, Style
def main():
    hijau = Fore.GREEN
    merah = Fore.RED
    cyan = Fore.CYAN
    tai = Fore.YELLOW
    biru = Fore.BLUE
    batas = Style.RESET_ALL
    
    linux = 'clear'
    windows = 'cls'
    os.system([linux,windows][os.name == 'nt'])
    banner = '        X×× M a s s Y T D o n w l o a d ××X'
    by = '        By : Wan5550'
    git = '        Github : github.com/wannazid'
    print(f'{cyan}{banner}')
    print(f'{cyan}{by}')
    print(f'{cyan}{git}')
    print(batas)
    url  = input("[#] List Link Youtube >  ")
    open_url = open(url,'r').read().splitlines()
    for link in open_url:
    	try:
    		ekse = pafy.new(link)
    		print(f'{hijau}[+] {link}{tai} Judul : {ekse.title}')
    		print(cyan)
    		print('[!] Download > ')
    		dl = ekse.getbest()
    		dl.download()
    		print(batas)
    	except:
    		print(f'{hijau}[#] {link} : {merah}Error')
    		print(batas)
if __name__ == '__main__':
			mainmenu = True
			while mainmenu == True:
				main()
				back = input("[!] Succes Download, Kembali Ke Home? (y/n) > ")
				if back.lower() == 'y':
					mainmenu = True
				else:
					mainmenu = False
			
		