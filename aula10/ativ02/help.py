import hashlib, json
senha = "123"
hash = hashlib.sha256(senha.encode()).hexdigest()
print(hash)

