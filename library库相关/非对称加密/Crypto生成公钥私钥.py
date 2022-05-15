import Crypto.PublicKey.RSA
import Crypto.Random

x = Crypto.PublicKey.RSA.generate(2048)
a = x.exportKey("PEM")  # 生成私钥
b = x.publickey().exportKey()  # 生成公钥
with open("pemData/a.pem", "wb") as x:
    x.write(a)
with open("pemData/b.pem", "wb") as x:
    x.write(b)

y = Crypto.PublicKey.RSA.generate(2048, Crypto.Random.new().read)  # 使用 Crypto.Random.new().read 伪随机数生成器
c = y.exportKey()  # 生成私钥
d = y.publickey().exportKey()  # 生成公钥
with open("pemData/c.pem", "wb") as x:
    x.write(c)
with open("pemData/d.pem", "wb") as x:
    x.write(d)
