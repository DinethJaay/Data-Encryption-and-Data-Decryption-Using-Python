import encryptionData
import decryptionData
import createKey


class App:
    @staticmethod
    def KeyGeneration():
        createKey.KeyGeneration()

    @staticmethod
    def DataEncrypt(message):
        encryptionData.Encryption(message)
    
    @staticmethod
    def DataDecrypt():
        decryptionData.Decryption()


#create Key
App.KeyGeneration()

#Encryption
message = input("Please enter the msg")
App.DataEncrypt(message)
 
#Decrption
App.DataDecrypt()