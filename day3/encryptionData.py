import rsa
from cryptography.fernet import Fernet


def Encryption(message):
   
    #open the message key
    skey =open('message.key','rb')
    key=skey.read()
    
    #create chipher
    chipher = Fernet(key)
    
    
    #write encrypt data
    encrypt_data =chipher.encrypt(bytes(message,'utf-8'))
    edata = open("EncryptedFiles","wb")
    edata.write(encrypt_data)
    
    public_key= open('public_key.key','rb')
    pubKey=public_key.read()
    
    #encrypt the data
    pukey= rsa.PublicKey.load_pkcs1(pubKey)
    encrypt_data = rsa.encrypt(key,pukey)
    
    #write encrypt data
    edata = open("Encryptedkey","wb")
    edata.write(encrypt_data)
