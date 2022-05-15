import rsa

f, e = rsa.newkeys(1024)  # 生成公钥、私钥

e = e.save_pkcs1()  # 保存为 .pem 格式
with open("pemData/private.pem", "wb") as x:  # 保存私钥
    x.write(e)
f = f.save_pkcs1()  # 保存为 .pem 格式
with open("pemData/public.pem", "wb") as x:  # 保存公钥
    x.write(f)
