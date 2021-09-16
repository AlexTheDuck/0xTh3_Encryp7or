#/usr/bin/python3
import secrets
import os
import sys
sys.stdout.write("\033[0;32m")
print("Welcome to 0xTh3_Encryp7or, a python utillity to encrypt files with AES" + "\n" + "Code made by 0x37.Credits in credits.txt")

print("Awaiting input...")
file = input("File name:")
print("Input recieved")

print('Loading source of entropy...')
key = secrets.token_urlsafe(256)

print("Encrypting...")
os.system("pyAesCrypt -p %s -e %s "%(key, file))
os.system("shred -fzu %s" %file) 
print("Encryption completed")

answer = input("Do you want to export the key?(if no they will be discarded)y/n: ") 
if answer == "y": 
      fp = open('%s.key'%file, 'w')
      fp.write(key)
      fp.close()
elif answer == "n": 
      del key
print("=======End of script=======")