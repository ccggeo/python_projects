import socket

TARGET = ""
def is_connected():
  try:
    host = socket.gethostbyname(TARGET)
    s = socket.create_connection((host, 22), 2)
    return True
  except:
     pass
  return False
print is_connected()








