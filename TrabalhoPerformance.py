class CacheMapeamentoDireto:
    def __init__(self, tamanho_cache):
        self.tamanho_cache = tamanho_cache
        self.cache = [-1] * tamanho_cache

    def inicializar_cache(self):
        self.cache = [-1] * self.tamanho_cache

    def imprimir_cache(self):
        print("Tamanho da Cache:", self.tamanho_cache)
        print("Posição - Memória")
        for posicao, memoria in enumerate(self.cache):
            print(posicao, "-", memoria)

    def mapeamento_direto(self, posicoes_memoria_acessar):
        hits = 0  # Contador de hits para esta execução
        misses = 0  # Contador de misses para esta execução

        print("Inicializando Cache...")
        self.inicializar_cache()
        print("Situação inicial da memória cache:")
        self.imprimir_cache()
        print("\nRealizando mapeamento direto...")

        for pos_memoria in posicoes_memoria_acessar:
            posicao_cache = pos_memoria % self.tamanho_cache
            if self.cache[posicao_cache] == pos_memoria:
                hits += 1
                print(f"Hit: Acessando endereço {pos_memoria}")
            else:
                self.cache[posicao_cache] = pos_memoria
                misses += 1
                print(f"Miss: Acessando endereço {pos_memoria}")
            print("Memória cache atualizada:")
            self.imprimir_cache()
            print("\n")

        print("\nResumo:")
        print("Total de posições de memórias acessadas:", len(posicoes_memoria_acessar))
        print("Total de hits:", hits)
        print("Total de misses:", misses)
        print("Taxa de cache hit:", hits / len(posicoes_memoria_acessar))



        
class CacheAssociativoPorConjunto:
    def __init__(self, tamanho_cache, tamanho_conjunto):
        self.tamanho_cache = tamanho_cache
        self.tamanho_conjunto = tamanho_conjunto
        self.num_conjuntos = tamanho_cache // tamanho_conjunto
        self.cache = [[-1] * tamanho_conjunto for _ in range(self.num_conjuntos)]
        self.lru = [0] * self.num_conjuntos  # Inicializa LRU para cada conjunto como 0
        self.hits = 0
        self.misses = 0

    def acessar_endereco(self, endereco):
        conjunto_index = (endereco // self.tamanho_conjunto) % self.num_conjuntos
        conjunto = self.cache[conjunto_index]

        if endereco in conjunto:
            self.hits += 1
            print(f"Hit: Acessando endereço {endereco}")
        else:
            self.misses += 1
            if -1 in conjunto:
                # Ainda há espaço no conjunto, adiciona o bloco
                index = conjunto.index(-1)
                conjunto[index] = endereco
            else:
                # O conjunto está cheio, substitui usando LRU
                lru_index = self.lru[conjunto_index]
                conjunto[lru_index] = endereco

            print(f"Miss: Acessando endereço {endereco}")

        self.atualizar_lru(conjunto_index, endereco)
        self.imprimir_cache()

    def atualizar_lru(self, conjunto_index, endereco):
        conjunto = self.cache[conjunto_index]
        if -1 not in conjunto:
            # O conjunto está cheio, atualiza o LRU
            if endereco in conjunto:
                self.lru[conjunto_index] = conjunto.index(endereco)
            else:
                # Encontra o bloco mais antigo no conjunto
                self.lru[conjunto_index] = conjunto.index(min(conjunto))

    def imprimir_cache(self):
        print("Estado atual da cache:")
        for i, conjunto in enumerate(self.cache):
            lru_index = self.lru[i]
            for pos, bloco in enumerate(conjunto):
                if pos == lru_index and -1 not in conjunto:
                    print(f"Conjunto {i} - Bloco {pos}: {bloco} (LRU)")
                else:
                    print(f"Conjunto {i} - Bloco {pos}: {bloco}")
        print()

    def imprimir_hits_misses(self):
        print("Resumo:")
        print(f"Hits: {self.hits}")
        print(f"Misses: {self.misses}")


# Teste de Mapeamento Direto
print("Mapeamento Direto:")
cache_direto = CacheMapeamentoDireto(5)

print("Exemplo 4")
posicoes_memoria_acessar = [0, 19, 2, 1, 23, 4, 17, 6]
cache_direto.mapeamento_direto(posicoes_memoria_acessar)
print("\n")

print("Exemplo 5a")
posicoes_memoria_acessar_1 = [0, 1, 2, 3, 1, 4, 5, 6]
cache_direto.mapeamento_direto(posicoes_memoria_acessar_1)
print("\n")
print("Exemplo 5a")
posicoes_memoria_acessar_2 = [0, 1, 2, 2, 22, 32, 42, 20, 1, 10, 11, 12, 13]
cache_direto.mapeamento_direto(posicoes_memoria_acessar_2)
print("\n")
print("Exemplo 5b")
posicoes_memoria_acessar_3 = [1, 6, 1, 11, 1, 16, 1, 21, 1, 26]
cache_direto.mapeamento_direto(posicoes_memoria_acessar_3)
print("\n")

# Endereços que sempre mapeiam para a mesma posição na cache
print("\nConfiguração com Mesma Posição na Cache (5c):")
posicoes_memoria_acessar_mesma_posicao = [0, 5, 10, 15, 20, 25]
cache_direto.mapeamento_direto(posicoes_memoria_acessar_mesma_posicao)

print("Mapeamento Associativo por Conjunto (6a):")
tamanho_cache = 16
tamanho_conjunto = 4
cache = CacheAssociativoPorConjunto(tamanho_cache, tamanho_conjunto)
posicoes_memoria_acessar_1 = [0, 1, 19, 23, 2, 7, 52, 5, 7, 8, 19, 10, 11, 21, 13, 19, 5]
for endereco in posicoes_memoria_acessar_1:
    cache.acessar_endereco(endereco)
cache.imprimir_hits_misses()
print("\n")

print("\n Outro exemplo (6a):")

tamanho_conjunto = 8
cache = CacheAssociativoPorConjunto(tamanho_cache, tamanho_conjunto)
posicoes_memoria_acessar_2 = [0, 4, 2, 8, 7, 24, 6, 9, 34, 23, 5, 11, 18, 13, 44, 15, 6]
for endereco in posicoes_memoria_acessar_2:
    cache.acessar_endereco(endereco)
cache.imprimir_hits_misses()
print("\n")

# Exemplo 6b
print("Mapeamento Direto (6b):")
cache_direto=CacheMapeamentoDireto(8)
posicoes_memoria_acessar_1 = [2,8,3,22,16,1,28,7,15,44,5,1,]
cache_direto.mapeamento_direto(posicoes_memoria_acessar_1)
print("\n")

print("Mapeamento Associativo por Conjunto (6b):")
tamanho_cache = 8
tamanho_conjunto = 2
cache = CacheAssociativoPorConjunto(tamanho_cache, tamanho_conjunto)

posicoes_memoria_acessar_1 = [2,8,3,22,16,1,28,7,15,44,5,1,]
for endereco in posicoes_memoria_acessar_1:
    cache.acessar_endereco(endereco)
cache.imprimir_hits_misses()
