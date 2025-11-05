# Compilador básico em Python
# Linguagem simples com:
# - expressões: +, -, *, /
# - variáveis e atribuições: x = 5 + 3
# - comando print: print(x)
# Agora com entrada interativa!

import re

# 1. Analisador Léxico (Lexer)
def lexer(codigo):
    tokens = re.findall(r'[A-Za-z_]\w*|\d+|[=+\-*/()]', codigo)
    return tokens

# 2. Avaliador de Expressões
variaveis = {}

def avaliar_expressao(expr):
    try:
        return eval(expr, {}, variaveis)
    except Exception as e:
        print("Erro na expressão:", e)

# 3. Compilador / Interpretador
def executar(codigo):
    linhas = codigo.splitlines()
    for linha in linhas:
        linha = linha.strip()
        if not linha:
            continue
        # Comando print
        if linha.startswith("print(") and linha.endswith(")"):
            expr = linha[6:-1]
            valor = avaliar_expressao(expr)
            print(valor)
        # Atribuição
        elif "=" in linha:
            nome, expr = linha.split("=", 1)
            nome = nome.strip()
            expr = expr.strip()
            valor = avaliar_expressao(expr)
            variaveis[nome] = valor
        else:
            print("Comando desconhecido:", linha)

# 4. Entrada interativa
if __name__ == "__main__":
    print("=== Compilador Básico em Python ===")
    print("Digite seu código abaixo (digite 'fim' para executar):\n")

    linhas = []
    while True:
        linha = input(">>> ")
        if linha.lower() == "fim":
            break
        linhas.append(linha)

    codigo = "\n".join(linhas)
    print("\n--- Executando código ---\n")
    executar(codigo)
