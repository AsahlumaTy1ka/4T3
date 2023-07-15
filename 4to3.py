
import os
from time import sleep
try:
  from pydub import AudioSegment
  from colorama import Fore,Back,Style
  ###Colors
  red = Fore.RED
  grn = Fore.GREEN

except ModuleNotFoundError:
   print("{red}[{grn}+{red}]{grn} Installing requirements...")
   os.system("pip install colorama")
   os.system("pip install pydub")

def exi():
   logo()
   print(f"{red}[{grn}+{red}]{grn} Tool name : 4T3")
   print(f"{red}[{grn}+{red}]{grn} Coded by : Asahluma Ty1ka")
   print(f"{red}[{grn}+{red}]{grn} 4T3 : Tool made to convert mp4 to mp3")
   y = input('\nPress enter to continue...')
   logo()
   menu()
def menu():
   print(f"{red}[{grn}1{red}]{grn} Convert ")
   print(f"{red}[{grn}2{red}]{grn} About ")
   print(f"{red}[{grn}3{red}]{grn} Exit ")
   c = input(f"\n{red}[{grn}+{red}]{grn} Choice : ")
   if (c == "1"):
      main()
   elif (c == "2"):
      exi()
   elif (c == "3"):
      logo()
      print(f"{red}[{grn}+{red}]{grn} Thanks for using this tool...bye!{Style.RESET_ALL}")
      exit(1)
   else:
      print(f"{grn}[{red}!{grn}]{grn} Invalid choice!")
      sleep(2)
      menu()

def convert(mp4f,mp3f):
   try:
      audio = AudioSegment.from_file(mp4f,"mp4")
      audio.export(mp3f,format="mp3")
      print(f"{red}[{grn}+{red}]{grn} Converted Successfully!")
      sleep(2)
      print(f"{red}[{grn}+{red}] {grn}Saved as {mp3f}!{Style.RESET_ALL}")
   except Exception as e:
      print(f"{grn}[{red}!{grn}]{red} {e} {Style.RESET_ALL}")

def cdir(p):
   if os.path.isdir(p):
      return True
   else:
      return False

def main():
   try:
      songs_path = input(f"\n{red}[{grn}+{red}]{grn} Enter the songs folder/path name : {Style.RESET_ALL}")
      os.chdir(songs_path)
      songs_arr = os.listdir(songs_path)
      for i in range(0,len(songs_arr)):
         print(f"{red}[{grn}{i}{red}]{grn} {songs_arr[i]}")
   except FileNotFoundError:
      print(f"{grn}[{red}!{grn}] {red}Folder/Path does not exist!{Style.RESET_ALL}")
      exit(1)

   while True:
      try:
         ssong = int(input(f"{red}[{grn}+{red}]{grn} Select song to convert : "))
         print(f"{red}[{grn}+{red}]{grn} Selected {songs_arr[ssong]}")
         sleep(2)
         print(f"{red}[{grn}+{red}]{grn} Converting {songs_arr[ssong].split('.')[0]}")
         convert(songs_arr[ssong],f"{songs_arr[ssong].split('.')[0]}.mp3")
         break
      except Exception as e:
         print(f"{grn}[{red}!{grn}]{red} {e}{Style.RESET_ALL}")

def logo():
  # os.system("clear")
   print(grn+'''
 _  _ _______ ____  
| || |__   __|___ \ 
| || |_ | |    __) |
|__   _|| |   |__ < 
   | |  | |   ___) |
   |_|  |_|  |____/ 
                    '''+Style.RESET_ALL)
   print(f"{red}==================================")
   print(f"====={grn}[+]Tool by : TeekaY_X[+]{red}=====")
   print(f"====={grn}[+]Coded by: Asahluma[+]{red}=====")
   print(f"=================================={Style.RESET_ALL}\n")

if __name__ == '__main__':
   logo()
   menu()
