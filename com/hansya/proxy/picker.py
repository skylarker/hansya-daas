import random

from com.hansya.model.proxy import Proxy
from com.hansya.util.credentials.read_credentials import ReadCredentials
from com.hansya.util.proxy.construct_url import ConstructURL
from com.hansya.util.proxy.read_proxies import ReadProxies


class Picker(object):
    def __init__(self):
        self.proxies = list()
        self.setup()

    def setup(self):
        username, password = ReadCredentials.get(
                "/Users/arunprasathshankar/Desktop/hansya-daas/com/hansya/data/credentials/credentials")
        id_ = 0
        for ip in ReadProxies.read(
                "/Users/arunprasathshankar/Desktop/hansya-daas/com/hansya/data/proxies/proxies"):
            proxy = Proxy()
            proxy.ip = ip
            proxy.port = 6060
            proxy.username = username
            proxy.password = password
            id_ += 1
            self.proxies.append({'id': id_, 'url': {'http': ConstructURL.construct(proxy)}})

    def get_random_proxy(self):
        return random.choice(self.proxies)
