import base64

def encodeString(mystring):
  return base64.b64encode(mystring).decode("ascii")

def decodeString(mystring_bytes):
  return base64.b64decode(mystring).decode("ascii")



