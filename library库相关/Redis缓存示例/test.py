import redis


client = redis.StrictRedis(host='localhost', port=6379, db=0)
client.delete('HookMouse')
client.delete('HookKey')
client.hdel('Hash案例键',"author","Alice","date","2022-10-01") # 删除指定字段

client.delete('id1')
client.delete('name')
client.delete('colors')



client.lpush("HookMouse", "")  # 增 # 从左端插入元素
client.lpush("HookKey", "")  # 增 # 从左端插入元素










