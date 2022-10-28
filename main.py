import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
client = redis.Redis(connection_pool=pool)

finished = False
print('type exit to close the chat')

while not finished:
  client.set("mg", input())
  msg = client.get("mg")
  if msg == (b'exit'):
    #print(msg)
    finished = True
  else:
    print(msg)

client.close()
