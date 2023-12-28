import hashlib

# Substitua 'sua_senha' pela senha que você deseja fazer o hash
senha = 'Mac@274341'

# Crie o objeto hash
hash_obj = hashlib.sha256(senha.encode())

# Gere o hash da senha
hash_senha = hash_obj.hexdigest()

print(f'A senha hash é: {hash_senha}')
