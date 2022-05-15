import Crypto.PublicKey.RSA

with open("pemData/a.pem", "rb") as x:
    xx = Crypto.PublicKey.RSA.importKey(x.read())

b = xx.publickey().exportKey()  # 生成公钥
with open("pemData/b.pem", "wb") as x:
    x.write(b)

a = xx.exportKey("DER")  # 生成 DER 格式的证书
with open("pemData/a.der", "wb") as x:
    x.write(a)
