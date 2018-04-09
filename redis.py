import redis

redis_config = {
    "host": "172.16.43.129",
    "port": 6379
}
# redis连接对象
redis_conn = redis.Redis(**redis_config)
redis_conn.set("name","ping")
print (redis_conn.get("name"))

# redis连接池
redis_pool = redis.ConnectPool(**redis_config)
r = redis.Redis(connection_pool=redis_pool)
r.set('name','qiang')
print (r.get('name'))