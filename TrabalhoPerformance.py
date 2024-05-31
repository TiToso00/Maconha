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
