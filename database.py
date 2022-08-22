import redis


def connect_to_redis():
    redis_con  = redis.Redis("127.0.0.1", 6379, db=0)
    return (redis_con)
