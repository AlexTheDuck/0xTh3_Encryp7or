#/usr/bin/python3
import secrets
import os
import sys
sys.stdout.write("\033[0;32m")
print("Welcome to 0xTh3_Encryp7or, a python utillity to encrypt files with AES" + "\n" + "Code made by 0x37.Credits in credits.txt")

print("Awaiting input...")
file = input("Encrypted file name:")
print("Input recieved")

print("Awaiting input...")
key_nm = input("key file name:")
print("Input recieved")

print("Reading source of entropy...")
key_o = open(key_nm , "r")
key = key_o.read()

print("Decrypting...")
os.system("pyAesCrypt -p %s -d %s "%(key, file))
os.system("shred -fzu %s" %file) 
print("Decryption completed")
answer = input("Do you want to keep the key?(if no it will be shredded)y/n: ") 
if answer == "n": 
      os.system("shred -fzu %s"%key_nm)
print("=======End of script=======")