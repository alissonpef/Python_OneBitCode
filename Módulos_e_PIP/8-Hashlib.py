import hashlib

# 1 - Todas as opções de algoritmos disponíveis
print(hashlib.algorithms_available) 

# 2 - Algoritmos disponível de acordo com o SO
print(hashlib.algorithms_guaranteed) 

# 3 - Criptografia de textos com Sha256
algorithm = hashlib.sha256()
print(algorithm.digest()) # Hash que é usado para criptografia do algoritmo
sha = hashlib.sha256()
message = "A melhor forma de prever o futuro é criá-lo".encode()
sha.update(message)
print(sha.hexdigest())

# 4 - Criptografia de textos com MD5
md5 = hashlib.md5()
md5.update(message)
print(md5.hexdigest())