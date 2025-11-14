r'''
   a   b   c
1 [ ]-[ ]-[ ]
   | \ | / |
2 [ ]-[ ]-[ ]
   | / | \ |
3 [ ]-[ ]-[ ]

'''

#nao esquecer de meter comentarios em tudo oq for sitio
# 'deverão incluir a assinatura das funções definidas, comentários 
# para o utilizador (docstring) e comentários para o programador'

# ---------- TAD posicao ----------

#construtor
def cria_posicao(c,l):
    if 'a' <= c <= 'c' and 0 < l < 4:
        return (c,l)
    else:
        raise ValueError("cria_posicao: argumentos invalidos")
    
def cria_copia_posicao(p):
    return p

#seletores
def obter_pos_c(p):
    return p[0]

def obter_pos_l(p):
    return p[1]

#reconhecedor
def eh_posicao(arg):
    return type(arg) is tuple and len(arg) == 2 and 'a' <= arg[0] <= 'c' and 0 < arg[1] < 4

#teste
def posicoes_iguais(p1, p2):
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2

#transformador
def posicao_para_str(p):
    return str(p[0]) + str(p[1])

#funcao de alto nivel
def obter_posicoes_adjacentes(p):
    c = p[0]
    l = p[1]
    adj_pos = []
    pos_e = chr(ord(c) - 1)
    if 'a' <= pos_e < c:
        adj_pos.append(cria_posicao(pos_e, l))
    pos_e = chr(ord(c) + 1)
    if c < pos_e <= 'c':
        adj_pos.append(cria_posicao(pos_e, l))
    pos_e = l - 1
    if 0 < pos_e < l:
        adj_pos.append(cria_posicao(c, pos_e))
    if l < pos_e < 4:
        adj_pos.append(cria_posicao(c, pos_e))
    return tuple(adj_pos)


# ---------- TAD peca ----------

#construtor
def cria_peca(s):
    if s == 'X' or s == 'O' or s == ' ':
        return (s)
    else:
        raise ValueError("cria_peca: argumento invalido")

def cria_copia_peca(j):
    return j

#reconhecedor
def eh_peca(arg):
    return type(arg) is str and (arg == 'X' or arg == 'O' or arg == ' ')

#teste
def pecas_iguais(j1, j2):
    return eh_peca(j1) and eh_peca(j2) and j1 == j2

#transformador
def peca_para_str(j):
    return "'[" + j + "]'"

#funcao de alto nivel
def peca_para_inteiro(j):
    if j == 'X':
        return 1
    if j == 'O':
        return -1
    return 0


