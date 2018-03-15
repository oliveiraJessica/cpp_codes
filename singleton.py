def singleton(myClass):
    instances = {}
    def getInstace(*args, **kwargs):
        if myClass not in instances:
            instances[myClass] = myClass(*args, **kwargs)
        return instances[myClass]
    return getInstace

@singleton
class TestClass(object):
    pass

x = TestClass()
