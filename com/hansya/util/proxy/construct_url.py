class ConstructURL(object):
    def __init__(self):
        pass

    @staticmethod
    def construct(proxy):
        auth_string = "http://%s:%s@%s:%s" % (proxy.username,
                                              proxy.password,
                                              proxy.ip,
                                              proxy.port)
        return auth_string
