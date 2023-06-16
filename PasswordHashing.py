import hashlib

pw = b"P@ssword_1234"  #converting string to byte type

print(hashlib.md5(pw).hexdigest()) #md5 is one of the hashing algo
print(hashlib.sha256(pw).hexdigest())
print(hashlib.blake2b(pw).hexdigest())
