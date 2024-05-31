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

        print("\nResumo:")
        print("Total de posições de memórias acessadas:", len(posicoes_memoria_acessar))
        print("Total de hits:", hits)
        print("Total de misses:", misses)
        print("Taxa de cache hit:", hits / len(posicoes_memoria_acessar))


# Teste de Mapeamento Direto
print("Mapeamento Direto:")
cache_direto = CacheMapeamentoDireto(5)
posicoes_memoria_acessar_1 = [0, 1, 2, 3, 1, 4, 5, 6]
cache_direto.mapeamento_direto(posicoes_memoria_acessar_1)
print("\n")

posicoes_memoria_acessar_2 = [0, 1, 2, 2, 22, 32, 42, 20, 1, 10, 11, 12, 13]
cache_direto.mapeamento_direto(posicoes_memoria_acessar_2)
print("\n")

posicoes_memoria_acessar_3 = [1, 6, 1, 11, 1, 16, 1, 21, 1, 26]
cache_direto.mapeamento_direto(posicoes_memoria_acessar_3)

# Endereços que sempre mapeiam para a mesma posição na cache
print("\nConfiguração com Mesma Posição na Cache:")
posicoes_memoria_acessar_mesma_posicao = [0, 5, 10, 15, 20, 25]
cache_direto.mapeamento_direto(posicoes_memoria_acessar_mesma_posicao)

class CacheMapeamentoAssociativoConjunto:
    def __init__(self, tamanho_cache, tamanho_conjunto):
        self.tamanho_cache = tamanho_cache
        self.tamanho_conjunto = tamanho_conjunto
        self.cache = [[] for _ in range(tamanho_cache // tamanho_conjunto)]
        self.lru_counter = 0

    def inicializar_cache(self):
        self.cache = [[] for _ in range(self.tamanho_cache // self.tamanho_conjunto)]
        self.lru_counter = 0

    def imprimir_cache(self):
        print("Tamanho da Cache:", self.tamanho_cache)
        print("Tamanho do Conjunto:", self.tamanho_conjunto)
        print("Conjuntos - Conteúdo")
        for conjunto, conteudo in enumerate(self.cache):
            print(f"Conjunto {conjunto}:", conteudo)

    def mapeamento_associativo_conjunto(self, posicoes_memoria_acessar):
        hits = 0  # Contador de hits para esta execução
        misses = 0  # Contador de misses para esta execução

        print("Inicializando Cache...")
        self.inicializar_cache()
        print("Situação inicial da memória cache:")
        self.imprimir_cache()
        print("\nRealizando mapeamento associativo por conjunto...")

        for pos_memoria in posicoes_memoria_acessar:
            conjunto = pos_memoria % (self.tamanho_cache // self.tamanho_conjunto)
            found = False
            for i, bloco in enumerate(self.cache[conjunto]):
                if bloco[0] == pos_memoria:  # Verifica se o endereço está no conjunto
                    hits += 1
                    print(f"Hit: Acessando endereço {pos_memoria}")
                    bloco[1] = self.lru_counter  # Atualiza o contador LRU
                    found = True
                    break
            if not found:
                misses += 1
                print(f"Miss: Acessando endereço {pos_memoria}")
                if len(self.cache[conjunto]) < self.tamanho_conjunto:
                    self.cache[conjunto].append([pos_memoria, self.lru_counter])  # Adiciona novo bloco ao conjunto
                else:
                    # Encontra o bloco LRU no conjunto e o substitui
                    lru_index = min(range(len(self.cache[conjunto])), key=lambda x: self.cache[conjunto][x][1])
                    self.cache[conjunto][lru_index] = [pos_memoria, self.lru_counter]
            self.lru_counter += 1

            print("Memória cache atualizada:")
            self.imprimir_cache()

        print("\nResumo:")
        print("Total de posições de memórias acessadas:", len(posicoes_memoria_acessar))
        print("Total de hits:", hits)
        print("Total de misses:", misses)
        print("Taxa de cache hit:", hits / len(posicoes_memoria_acessar))

        # Teste de Mapeamento Associativo por Conjunto
print("Mapeamento Associativo por Conjunto com 4 blocos por conjunto:")
cache_conjunto_4 = CacheMapeamentoAssociativoConjunto(16, 4)
posicoes_memoria_acessar_4 = [0, 1, 2, 3, 4, 5, 6, 7]
cache_conjunto_4.mapeamento_associativo_conjunto(posicoes_memoria_acessar_4)
print("\n")

print("Mapeamento Associativo por Conjunto com 8 blocos por conjunto:")
cache_conjunto_8 = CacheMapeamentoAssociativoConjunto(16, 8)
posicoes_memoria_acessar_8 = [0, 1, 2, 3, 4, 5, 6, 7]
cache_conjunto_8.mapeamento_associativo_conjunto(posicoes_memoria_acessar_8)

