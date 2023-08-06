from cryptography.fernet import Fernet
import rsa

def Decryption():

    private_key = open('private_key.key','rb')
    prikey = private_key.read()
    prkey=rsa.PrivateKey.load_pkcs1(prikey)

    #read the encrypted file
    encrypted_key = open ('Encryptedkey',"rb")
    ekey= encrypted_key.read()

    #decrypt the data
    dkey = rsa.decrypt(ekey,prkey)

    ciper = Fernet(dkey)

    encrypted_data  = open('EncryptedFiles','rb')
    edata = encrypted_data.read()

    decrypted_data = ciper.decrypt(edata)

    print(decrypted_data.decode())
    