import hashlib


def gerar_hash(texto):
    hash_obj = hashlib.sha256(texto.encode())
    return hash_obj.hexdigest()


texto = "Teste"

print(gerar_hash(texto))
