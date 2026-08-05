import hashlib

from config import SECRET



message = '{"KS_ID":27,"KR_ID":49,"method":"getRouteArrivalToStop"}'

text_bytes = (message + SECRET).encode("utf-8")
hash_object = hashlib.sha1(text_bytes)
authKEY = str(hash_object.hexdigest())

