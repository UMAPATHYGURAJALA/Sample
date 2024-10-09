import base64


def encode_string(mystring):
    return base64.b64encode(mystring).decode("ascii")


def decode_string(mystring_bytes):
    return base64.b64decode(mystring_bytes).decode("ascii")
