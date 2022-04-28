


data = b'vol:412'

print(data,type(data))

skk = data.decode('utf-8','ignore')

print(skk)
shengy = data.decode()[0:-3]
print(shengy)
shengy = data.decode()[4:]
print(shengy,int(shengy))