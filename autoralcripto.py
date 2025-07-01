import random
import string

def Cria_wordlist():
    caracteres = string.ascii_letters + string.digits + '!@#$%¨&*()_+-=[]{}`^~;:,.<>?/|\\' + 'áàâãéèêíìóòôõúùçÁÀÂÃÉÈÊÍÌÓÒÔÕÚÙÇ'
    lista = list(caracteres)
    Embaralha_wordlist = ''.join(random.sample(lista, len(lista)))
    return Embaralha_wordlist

def Criptografia (texto, E_wordlist):
    chave = len(texto)
    resultado = ''
    for L in texto: 
        if L in E_wordlist:
            posicao = E_wordlist.index(L)
            nova_posicao = (posicao + chave) % len(E_wordlist)
            resultado += E_wordlist[nova_posicao]
        else:
            resultado += L
    return resultado

def Decriptografia (Palavra_Criptografada, wordlist):
    chave = len(Palavra_Criptografada)
    resultado = ''
    for L in Palavra_Criptografada: 
        if L in     wordlist:
            posicao = wordlist.index(L)
            nova_posicao = (posicao - chave) % len(wordlist)
            resultado += wordlist[nova_posicao]
        else:
            resultado += L
    return resultado


def main():
    palavra = input('Insira a palavra : ')
    Wordlist = Cria_wordlist()
    Palavra_Criptografada = Criptografia(palavra, Wordlist)
    Palavra_Decriptografada = Decriptografia(Palavra_Criptografada, Wordlist)  
    print(f'Wordlist usada : {Wordlist}')
    print(f'Palavra criptografada : {Palavra_Criptografada}')
    print(f'Palavara Decifrada : {Palavra_Decriptografada}')

if __name__ == "__main__":
    main()

