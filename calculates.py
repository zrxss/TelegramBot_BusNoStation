import hashlib

from config import SECRET, KR_ID, KS_ID



message = f'{{"KS_ID":{KS_ID},"KR_ID":{KR_ID},"method":"getRouteArrivalToStop"}}'

text_bytes = (message + SECRET).encode("utf-8")
hash_object = hashlib.sha1(text_bytes)
authKEY = str(hash_object.hexdigest())

