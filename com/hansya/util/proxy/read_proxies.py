class ReadProxies(object):
    def __init__(self):
        pass

    @staticmethod
    def read(proxies_file_path):
        with open(proxies_file_path, 'r+') as pf:
            for proxy in pf.readlines():
                proxy = proxy.strip()
                yield proxy
