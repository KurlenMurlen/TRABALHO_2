import random
#santo deus prof mari oq eu não penei pra aprender a usar import random certinho.. me fez cair aos prantos

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "jogos", "desenvolvimento"]
    return random.choice(palavras)

#eu coloquei um número limitado de palavras que a forca pode usar, pq fazer um programa que randomiza a palavra dentro dum banco de dados 
#gigantesco está fora do meu leque

def exibir_palavra(palavra, letras_corretas):
    for letra in palavra:
        if letra in letras_corretas:
            print(letra, end=' ')
        else:
            print('_', end=' ')
    print()

def jogar_forca():
    palavra_secreta = escolher_palavra()
    letras_corretas = []
    tentativas_restantes = 6

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra secreta.")

    while tentativas_restantes > 0:
        exibir_palavra(palavra_secreta, letras_corretas)
        print("Tentativas restantes:", tentativas_restantes)

        palpite = input("Informe uma letra: ").lower()

        if palpite in letras_corretas:
            print("Você já tentou essa letra. Tente novamente.")
            continue

        if palpite in palavra_secreta:
            letras_corretas.append(palpite)
            acertos = [letra for letra in palavra_secreta if letra == palpite]
            print("Letra correta! A letra", palpite, "aparece na palavra", len(acertos), "vezes.")
        else:
            print("Letra incorreta! Tente novamente.")
            tentativas_restantes -= 1

        if len(letras_corretas) == len(set(palavra_secreta)):
            print("Parabéns! Você adivinhou a palavra secreta:", palavra_secreta)
            break

    if tentativas_restantes == 0:
        print("Você perdeu! A palavra secreta era:", palavra_secreta)

jogar_forca()

#eu escrevi o programa no VSCode, oque eu achei engraçado no entanto é que eu posso manualmente descontar a quantidade de tentativas simplesmente 
#ao clicar no botão para iniciar o programa. 

#obs: eu decidi ser menos misericordioso que o seu exemplo e decidi dar apenas 6 tentativas, como se fosse a cabeça, o torax, ambos braços e ambas pernas.

#Obrigado prof! Tchauuuu e até a próxima.
