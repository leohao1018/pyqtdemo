#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author leo hao
# os windows 7
import redis

# pool = redis.ConnectionPool(host='10.138.60.43', port=6379, db=14, password='123456')
# r = redis.Redis(connection_pool=pool)


class RedisQueue(object):
    """Simple Queue with Redis Backend"""

    def __init__(self, name, namespace='queue', **redis_kwargs):
        """The default connection parameters are: host='localhost', port=6379, db=0"""
        self.__db = redis.Redis(**redis_kwargs)
        self.key = '%s:%s' % (namespace, name)

    def qsize(self):
        """Return the approximate size of the queue."""
        return self.__db.llen(self.key)

    def empty(self):
        """Return True if the queue is empty, False otherwise."""
        return self.qsize() == 0

    def put(self, item):
        """Put item into the queue."""
        self.__db.rpush(self.key, item)

    def get(self, block=True, timeout=None):
        """Remove and return an item from the queue.

        If optional args block is true and timeout is None (the default), block
        if necessary until an item is available."""
        if block:
            item = self.__db.blpop(self.key, timeout=timeout)
        else:
            item = self.__db.lpop(self.key)

        if item:
            item = item[1]
        return item

    def get_nowait(self):
        """Equivalent to get(False)."""
        return self.get(False)

q = RedisQueue('test2', host='10.138.60.43', port=6379, db=14, password='123456')


if __name__ == '__main__':
    # pipe = r.pipeline()
    # pipe.set('foo', 'bar')
    # pipe.get('bing')
    # pipe.execute()
    #
    # pipe.set('foo', 'bar').sadd('faz', 'baz').incr('auto_number').execute()
    q.put('hello world 1')



