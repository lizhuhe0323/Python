import redis

redis_config = {
    "host": "127.0.0.1",
    "port": 6379
}
# redis连接对象
redis_conn = redis.Redis(**redis_config)
redis_conn.set("name","ping")
print (redis_conn.get("name"))

# redis连接池
redis_pool = redis.ConnectionPool(**redis_config)
r = redis.Redis(connection_pool=redis_pool)
r.set('name','qiang')
print (r.get('name'))