class ReadCredentials(object):
    def __init__(self):
        pass

    @staticmethod
    def get(credentials_file_path):
        with open(credentials_file_path, 'r+') as cf:
            lines = cf.readlines()
            _, username = lines[0].strip().split(":")
            _, password = lines[1].strip().split(":")
            return username, password
