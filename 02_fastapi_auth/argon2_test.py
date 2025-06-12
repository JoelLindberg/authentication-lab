from argon2 import PasswordHasher

ph = PasswordHasher()

hash = ph.hash("correct horse battery staple")
print(hash)

ph.verify(hash, "correct horse battery staple")
ph.check_needs_rehash(hash)
ph.verify(hash, "Tr0ub4dor&3")
