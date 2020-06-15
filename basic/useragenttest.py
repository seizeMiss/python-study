from fake_useragent import UserAgent
import tempfile

if __name__ == '__main__':

    a = tempfile.gettempdir()
    print(a)

    ua = UserAgent(verify_ssl=False)
    for i in range(3):
        print(ua.random)