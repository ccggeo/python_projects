import socket


def connection():
    input =  raw_input("site to check: ")
    try:
        host = socket.gethostbyname(input)
        socket.create_connection((host, 80), 2)
        return True

    except:
        pass
    return False


print(connection())
