from proxypool.api import app
from proxypool.schedule import Schedule
from aiohttp.errors import ClientResponseError

def main():
    try:
        s = Schedule()
        s.run()
        app.run()

    except ClientResponseError as c:
        print(c)
        pass



if __name__ == '__main__':
    main()

