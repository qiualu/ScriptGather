
import rsa

# 创建密钥对
def resKey():
    (pubkey, privkey) = rsa.newkeys(512) # 生成公钥、私钥
    return (pubkey, privkey) # 生成公钥、私钥


# rsa加密
def rsaEncrypt(str,pubkey):
    # 明文编码格式
    content = str.encode("utf-8")
    # 公钥加密
    crypto = rsa.encrypt(content, pubkey)
    return crypto


# rsa解密
def rsaDecrypt(str, pk):
    # 私钥解密
    content = rsa.decrypt(str, pk)
    con = content.decode("utf-8")
    return con


if __name__ == "__main__":
    pubkey, privkey = resKey()  # # 生成公钥、私钥
    print("公钥:\n%s\n私钥:\n%s" % (pubkey, privkey))

    data = "hello wolrd 5512"
    print("   加密前密文 : ", data)


    str = rsaEncrypt(data,pubkey)  # 公钥 加密
    # print("加密后密文：\n%s" % str)
    print("   加密后密文 : ",str)

    content = rsaDecrypt(str, privkey) # 私钥 解密
    print("   解密后明文： %s" % content)








