# -*- coding: utf-8 -*-
"""
EXERCÍCIO DE BUSCA AO TESOURO - CRIPTOGRAFIA XOR (CHAVE DE 8 DÍGITOS)
Objetivo: Encontrar a chave numérica de 8 dígitos para descriptografar o arquivo secreto
"""

# Função para criptografar um arquivo usando operação XOR com chave numérica de 8 dígitos.
def criptografar_arquivo(arquivo_entrada, arquivo_saida, chave):
    """
    Criptografa um arquivo usando operação XOR com chave numérica de 8 dígitos.
    A chave será convertida para bytes e repetida ciclicamente durante o XOR.
    """
    with open(arquivo_entrada, 'rb') as f:
        dados = f.read()
    
    # Converte a chave para string com zeros à esquerda e transforma em bytes
    chave_bytes = str(chave).zfill(8).encode()  # Agora usando 8 dígitos
    
    # Aplica operação XOR usando a chave estendida
    dados_cripto = xor_bytes(dados, chave_bytes)
    
    with open(arquivo_saida, 'wb') as f:
        f.write(dados_cripto)

def xor_bytes(dados, chave):
    """
    Aplica XOR entre cada byte dos dados e a chave repetida.
    Mesma função para criptografar e descriptografar.
    """
    return bytes([dado ^ chave[i % len(chave)] for i, dado in enumerate(dados)])


def carregar_arquivo_criptografado(nome_arquivo):
    """Retorna o arquivo"""
    with open(nome_arquivo, 'rb') as f:
        return f.read()

def tentar_descriptografia(dados_cripto, chave_tentativa):
    """
    Tenta descriptografar com uma chave de 8 dígitos.
    Retorna None se a decodificação UTF-8 falhar (chave inválida)
    """
    try:
        chave_bytes = str(chave_tentativa).zfill(8).encode()  # 8 dígitos
        dados_decripto = xor_bytes(dados_cripto, chave_bytes)
        return dados_decripto.decode('utf-8')
    except UnicodeDecodeError:
        return None

def main():
    print('Iniciando busca ao tesouro...')

    
    

if __name__ == '__main__':
    main()

"""
PRINCIPAIS ALTERAÇÕES E DESAFIOS:
1. A chave agora tem 8 dígitos (100 milhões de combinações possíveis)
2. Aumento exponencial na complexidade do brute force
3. Necessidade de otimização e trabalho em equipe eficiente

ESTRATÉGIAS SUGERIDAS:
1. Divisão de tarefas:
   - Dividir o intervalo 0-99999999 entre os membros do grupo
   - Ex: Cada membro testa 12.500.000 chaves (100M / 8 pessoas)


"""