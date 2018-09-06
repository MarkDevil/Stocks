# coding = utf-8


import redis


class RedisPool(object):

    def __init__(self):

        pass

    def getRedis(self):
        pool = redis.ConnectionPool(host='localhost', port=6379)
        r = redis.Redis(connection_pool= pool)
        return r



