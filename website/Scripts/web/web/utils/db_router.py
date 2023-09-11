from random import random


class MysqlRouter(object):

    def db_for_read(self, model, **hints):

        return 'shop_slave2'

    def db_for_write(self, model, **hints):

        return 'default'

