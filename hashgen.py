import hashlib

text = input("Enter the text to convert into hash: ")
options = int(input('''## HASH Generator ##
                    Choose one option:
                    1) MD5
                    2) SHA1
                    3) SHA256
                    4) SHA512
                    '''))
if options == 1:
    result = hashlib.md5(text.encode('utf-8'))
    print("The generated hash is: ", result.hexdigest())

elif options == 2:
    result = hashlib.sha1(text.encode('utf-8'))
    print("The generated hash is: ", result.hexdigest())

elif options == 3:
    result = hashlib.sha256(text.encode('utf-8'))
    print("The generated hash is: ", result.hexdigest())

elif options == 4:
    result = hashlib.sha512(text.encode('utf-8'))
    print("The generated hash is: ", result.hexdigest())

else:
    print("Invalid option")
