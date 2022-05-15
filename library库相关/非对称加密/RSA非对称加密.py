import rsa
import base64

password = 'password'
print('加密前 :%s' % password)

y = base64.b64encode(password.encode())
print('base64 加密后  :%s' % y)

with open("pemData/public.pem", "rb") as x:
    f = x.read()
    print("从文件读取公钥 : %s" % f)
    f = rsa.PublicKey.load_pkcs1(f)  # load 公钥
    print("rsa 格式处理 公钥 : %s" % f)

with open("pemData/private.pem", "rb") as x:
    e = x.read()
    print("从文件读取私钥 : %s" % e)
    e = rsa.PrivateKey.load_pkcs1(e)  # load 私钥

cipher_text = rsa.encrypt(y, f)  # 使用公钥加密
print('cipher_text:%s' % cipher_text)

msg = base64.b64encode(cipher_text).decode()
print('msg:%s' % msg)

crypto = base64.b64decode(msg)
print('crypto:%s' % crypto)

text = rsa.decrypt(crypto, e).decode()  # 使用私钥解密
print('text:%s' % text)

password = base64.b64decode(text).decode()
print('password:%s' % password)
