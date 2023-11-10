url = "https://stackoverflow.com/questions/11731136/class-method-decorator-with-self-arguments/11731208#11731208"

def check_authorization(f):
    def wrapper(*args):
        print(args[0].url)
        return f(*args)
    return wrapper

class Client(object):
    def __init__(self, url):
        self.url = url

    @check_authorization
    def get(self):
        print('get')