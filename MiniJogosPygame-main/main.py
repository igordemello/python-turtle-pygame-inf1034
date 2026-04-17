from pygame import *
from pygame.locals import QUIT
from botao import Botao
import sys
import random


init()
SCREEN = display.set_mode((1280,720))
display.set_caption('Games')

def gamefont(size):
    return font.Font('assets\Gameplay.ttf',size)

def helvfont(size):
    return font.Font('assets\Helvetica.ttf',size)





def inicio_menu():
    while True:
        MENU_MOUSE_POS = mouse.get_pos()

        SCREEN.fill('#80043a')

        menutexto = gamefont(50).render("Selecione o jogo",True,'#f39708')
        menutextorect = menutexto.get_rect(center=(640, 100))
        SCREEN.blit(menutexto, menutextorect)

        botao_forca = Botao(image=None, pos=(640, 250), text_input="Jogo da forca", font=gamefont(35), base_color="#157E85", hovering_color="White")
        botao_PPT = Botao(image=None, pos=(640, 350), text_input="Pedra, papel e tesoura", font=gamefont(35), base_color="#157E85", hovering_color="White")
        botao_calc = Botao(image=None, pos=(640, 450), text_input="Calculadora", font=gamefont(35), base_color="#157E85", hovering_color="White")
        botao_adivinhacao = Botao(image=None, pos=(640, 550), text_input="Jogo de adivinhacao", font=gamefont(35), base_color="#157E85", hovering_color="White")

        for button in [botao_forca, botao_PPT, botao_calc, botao_adivinhacao]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)


        for ev in event.get():
            if ev.type == QUIT:
                quit()
                sys.exit()
            if ev.type == MOUSEBUTTONDOWN:
                if botao_forca.checkForInput(MENU_MOUSE_POS):
                    play_forca()
                if botao_PPT.checkForInput(MENU_MOUSE_POS):
                    play_PPT()
                if botao_calc.checkForInput(MENU_MOUSE_POS):
                    play_calc()
                if botao_adivinhacao.checkForInput(MENU_MOUSE_POS):
                    play_adivinhacao()


        display.update()
    



def processar_entrada_letra(tecla):
    if len(tecla) == 1 and tecla.isalpha():
        return True
    else:
        return False


def play_forca():
    PALAVRAS = ['mouse','teclado','monitor', 'cadeira', 'computador','mousepad']
    # PALAVRAS = ['fone de ouvido', 'pc gamer']
    erros = 0
    mododetentativa = 'letra'
    palavra_secreta = PALAVRAS[random.randint(0,len(PALAVRAS)-1)]
    letras_erradas = []
    entrada_palavra = ''

    x_inicial_forca = 400
    estado_forca = 'andamento'
    
    palavra_mascarada = {}
    for i, letra in enumerate(palavra_secreta):
        if letra == ' ':
            palavra_mascarada[i] = ' '
        else:
            palavra_mascarada[i] = '_'

    # print(palavra_secreta)
    # print(palavra_mascarada)

    while True:
        FORCA_MOUSE_POS = mouse.get_pos()

        SCREEN.fill('black')

        tituloforca = gamefont(50).render("Jogo da forca",True,'#f39708')
        tituloforcarect = tituloforca.get_rect(center=(640, 100))
        SCREEN.blit(tituloforca, tituloforcarect)

        botao_voltarmenu = Botao(image=None, pos=(100, 100), text_input="Voltar", font=gamefont(20), base_color="#850701", hovering_color="White")

        #condição de vitoria ou derrota:
        if erros > 6 : estado_forca = 'derrota'
        elif all(val != '_' for val in palavra_mascarada.values()):
            estado_forca = 'vitoria'

        if estado_forca == 'andamento':
            titulomodo = gamefont(15).render("Alterne o modo de chute:",True,'#FFFFFF')
            titulomodorect = titulomodo.get_rect(center=(1000, 175))
            SCREEN.blit(titulomodo, titulomodorect)

            if mododetentativa=='letra': 
                botao_letra = Botao(image=None, pos=(950, 200), text_input="Letra", font=gamefont(15), base_color="#53EB5D", hovering_color="#53EB5D")
                botao_palavra = Botao(image=None, pos=(1050, 200), text_input="Palavra", font=gamefont(15), base_color="#FFFFFF", hovering_color="#53EB5D")
            elif mododetentativa=='palavra':
                botao_letra = Botao(image=None, pos=(950, 200), text_input="Letra", font=gamefont(15), base_color="#FFFFFF", hovering_color="#53EB5D")
                botao_palavra = Botao(image=None, pos=(1050, 200), text_input="Palavra", font=gamefont(15), base_color="#53EB5D", hovering_color="#53EB5D")

            SCREEN.blit(image.load(f'assets/bonecoforca/{erros}erros.png'), (100, 250))

            if mododetentativa == 'palavra':
                texto_palpite = gamefont(15).render(f"Palpite: {entrada_palavra}", True, '#FFFFFF')
                SCREEN.blit(texto_palpite, (925, 250))

            x_atual = x_inicial_forca
            for letra_errada in letras_erradas:
                box2 = gamefont(15).render(letra_errada, True, '#FFFFFF')
                SCREEN.blit(box2, (x_atual, 175))
                x_atual += box2.get_width() + 10 

            for i in palavra_mascarada:
                box = gamefont(35).render(palavra_mascarada[i],True,'#FFFFFF')
                SCREEN.blit(box,((x_inicial_forca+((i)*50)),500))


            
            for button in [botao_voltarmenu, botao_letra, botao_palavra]:
                    button.changeColor(FORCA_MOUSE_POS)
                    button.update(SCREEN)

            for ev in event.get():
                if ev.type == QUIT:
                    quit()
                    sys.exit()
                if ev.type == MOUSEBUTTONDOWN:
                    if botao_voltarmenu.checkForInput(FORCA_MOUSE_POS):
                        inicio_menu()
                    if botao_letra.checkForInput(FORCA_MOUSE_POS):
                        mododetentativa = 'letra'
                    if botao_palavra.checkForInput(FORCA_MOUSE_POS):
                        mododetentativa = 'palavra'
                

                if ev.type == KEYDOWN:
                    tecla = key.name(ev.key).lower()

                    if mododetentativa == 'letra':
                        if processar_entrada_letra(tecla):
                            if tecla in palavra_secreta:
                                for i, letra in enumerate(palavra_secreta):
                                    if letra == tecla:
                                        palavra_mascarada[i] = tecla
                            else:
                                if tecla not in letras_erradas:
                                    erros += 1
                                    letras_erradas.append(tecla)

                    elif mododetentativa == 'palavra':
                        if tecla == 'return':
                            if entrada_palavra == palavra_secreta:
                                for i, letra in enumerate(palavra_secreta):
                                    palavra_mascarada[i] = letra
                            else:
                                if entrada_palavra not in letras_erradas:
                                    erros += 1
                                    letras_erradas.append(entrada_palavra)
                            entrada_palavra = ''
                        elif tecla == 'backspace':
                            entrada_palavra = entrada_palavra[:-1]
                        elif tecla == 'space':
                            entrada_palavra += ' '
                        elif len(tecla) == 1 and tecla.isalpha():
                            entrada_palavra += tecla
                            
                    

        elif estado_forca == 'derrota':
            tituloforcaderrota = gamefont(50).render("Voce perdeu!",True,'#FFFFFF')
            tituloforcaderrotarect = tituloforcaderrota.get_rect(center=(640, 300))
            SCREEN.blit(tituloforcaderrota, tituloforcaderrotarect)

            botao_voltarmenu = Botao(image=None, pos=(540, 400), text_input="Voltar", font=gamefont(25), base_color="#850701", hovering_color="White")
            botao_reiniciar = Botao(image=None, pos=(740, 400), text_input="Reiniciar", font=gamefont(25), base_color="#53EB5D", hovering_color="White")

            for button in [botao_voltarmenu, botao_reiniciar]:
                    button.changeColor(FORCA_MOUSE_POS)
                    button.update(SCREEN)

            for ev in event.get():
                if ev.type == QUIT:
                    quit()
                    sys.exit()
                if ev.type == MOUSEBUTTONDOWN:
                    if botao_voltarmenu.checkForInput(FORCA_MOUSE_POS):
                        inicio_menu()
                    if botao_reiniciar.checkForInput(FORCA_MOUSE_POS):
                        play_forca()
        elif estado_forca == 'vitoria':
            tituloforcavitoria = gamefont(50).render("Voce ganhou!",True,'#FFFFFF')
            tituloforcavitoriarect = tituloforcavitoria.get_rect(center=(640, 300))
            SCREEN.blit(tituloforcavitoria, tituloforcavitoriarect)

            exibirpalavrasecreta = gamefont(30).render(f"A palavra era: {palavra_secreta}",True,'#FFFFFF')
            exibirpalavrasecretarect = exibirpalavrasecreta.get_rect(center=(640, 400))
            SCREEN.blit(exibirpalavrasecreta, exibirpalavrasecretarect)

            botao_voltarmenu = Botao(image=None, pos=(540, 500), text_input="Voltar", font=gamefont(25), base_color="#850701", hovering_color="White")
            botao_reiniciar = Botao(image=None, pos=(740, 500), text_input="Reiniciar", font=gamefont(25), base_color="#53EB5D", hovering_color="White")

            for button in [botao_voltarmenu, botao_reiniciar]:
                    button.changeColor(FORCA_MOUSE_POS)
                    button.update(SCREEN)

            for ev in event.get():
                if ev.type == QUIT:
                    quit()
                    sys.exit()
                if ev.type == MOUSEBUTTONDOWN:
                    if botao_voltarmenu.checkForInput(FORCA_MOUSE_POS):
                        inicio_menu()
                    if botao_reiniciar.checkForInput(FORCA_MOUSE_POS):
                        play_forca()

        display.update()

def btnCalc(fcor, cor, hcor,tam,pos,txt):
        return Botao(image=transform.scale((image.load(f'assets/calc/botao{fcor}.png')), (tam,tam)), pos=(pos), text_input=txt, font=helvfont(tam-20), base_color=cor, hovering_color=hcor)


def play_calc():

    
    pos_inicial_x = 550
    pos_inicial_y = 400
    espaco_x = 60
    espaco_y = 60

    expressao = ''
    operando1 = ''
    operador = ''
    operando2 = ''
    resultado = ''
    memoria = ''
    estado_resultado = False


    while True:

        

        CALC_MOUSE_POS = mouse.get_pos()

        SCREEN.fill('black')

        tituloforca = gamefont(50).render("Calculadora",True,'#f39708')
        tituloforcarect = tituloforca.get_rect(center=(640, 100))
        SCREEN.blit(tituloforca, tituloforcarect)

        botao_voltarmenu = Botao(image=None, pos=(100, 100), text_input="Voltar", font=gamefont(20), base_color="#850701", hovering_color="White")

        botao_ac = btnCalc('cinza','White', '#d9d9d9', 50, (pos_inicial_x, pos_inicial_y), 'C')
        botao_porc = btnCalc('cinza','White', '#d9d9d9', 50, (pos_inicial_x + espaco_x, pos_inicial_y), '%')
        botao_maismenos = btnCalc('cinza','White', '#d9d9d9', 50, (pos_inicial_x + 2 * espaco_x, pos_inicial_y), '+/-')
        botao_div = btnCalc('laranja','White', '#d9d9d9', 50, (pos_inicial_x + 3 * espaco_x, pos_inicial_y), '÷')

        botao_7 = btnCalc('cinzaesc','White', '#d9d9d9', 50, (pos_inicial_x, pos_inicial_y + espaco_y), '7')
        botao_8 = btnCalc('cinzaesc','White', '#d9d9d9', 50, (pos_inicial_x + espaco_x, pos_inicial_y + espaco_y), '8')
        botao_9 = btnCalc('cinzaesc','White', '#d9d9d9', 50, (pos_inicial_x + 2 * espaco_x, pos_inicial_y + espaco_y), '9')
        botao_mult = btnCalc('laranja', 'White', '#e88c44', 50, (pos_inicial_x + 3 * espaco_x, pos_inicial_y + espaco_y), 'x')

        botao_4 = btnCalc('cinzaesc','White', '#d9d9d9', 50, (pos_inicial_x, pos_inicial_y + 2 * espaco_y), '4')
        botao_5 = btnCalc('cinzaesc','White', '#d9d9d9', 50, (pos_inicial_x + espaco_x, pos_inicial_y + 2 * espaco_y), '5')
        botao_6 = btnCalc('cinzaesc','White', '#d9d9d9', 50, (pos_inicial_x + 2 * espaco_x, pos_inicial_y + 2 * espaco_y), '6')
        botao_menos = btnCalc('laranja', 'White', '#e88c44', 50, (pos_inicial_x + 3 * espaco_x, pos_inicial_y + 2 * espaco_y), '-')

        botao_1 = btnCalc('cinzaesc','White', '#d9d9d9', 50, (pos_inicial_x, pos_inicial_y + 3 * espaco_y), '1')
        botao_2 = btnCalc('cinzaesc','White', '#d9d9d9', 50, (pos_inicial_x + espaco_x, pos_inicial_y + 3 * espaco_y), '2')
        botao_3 = btnCalc('cinzaesc','White', '#d9d9d9', 50, (pos_inicial_x + 2 * espaco_x, pos_inicial_y + 3 * espaco_y), '3')
        botao_mais = btnCalc('laranja', 'White', '#e88c44', 50, (pos_inicial_x + 3 * espaco_x, pos_inicial_y + 3 * espaco_y), '+')

        botao_0 = btnCalc('cinzaesc','White', '#d9d9d9', 50, (pos_inicial_x + espaco_x, pos_inicial_y + 4 * espaco_y), '0')
        botao_virgula = btnCalc('cinzaesc','White', '#d9d9d9', 50, (pos_inicial_x + 2 * espaco_x, pos_inicial_y + 4 * espaco_y), '.')
        botao_igual = btnCalc('laranja', 'White', '#e88c44', 50, (pos_inicial_x + 3 * espaco_x, pos_inicial_y + 4 * espaco_y), '=')


        botoes_calc = [
            botao_ac, botao_porc, botao_maismenos, botao_div,
            botao_7, botao_8, botao_9, botao_mult,
            botao_4, botao_5, botao_6, botao_menos,
            botao_1, botao_2, botao_3, botao_mais,
            botao_0, botao_virgula, botao_igual
        ]

        for button in [botao_voltarmenu]:
                button.changeColor(CALC_MOUSE_POS)
                button.update(SCREEN)

        for button in botoes_calc:
                button.changeColor(CALC_MOUSE_POS)
                button.update(SCREEN)

        for ev in event.get():
            if ev.type == QUIT:
                quit()
                sys.exit()
            if ev.type == MOUSEBUTTONDOWN:
                if botao_voltarmenu.checkForInput(CALC_MOUSE_POS):
                    inicio_menu()

                for botao in botoes_calc:
                    if botao.checkForInput(CALC_MOUSE_POS):
                        entrada = botao.text_input
                        

                        if entrada == 'C':
                            operando1 = ''
                            operador = ''
                            operando2 = ''
                            resultado = ''
                            memoria = ''
                            estado_resultado = False

                        elif entrada == '%':
                            if operando2:
                                try:
                                    op1 = float(operando1.replace(',', '.') if operando1 else memoria)
                                    op2 = float(operando2.replace(',', '.'))

                                    porcento = str(op1 * (op2 / 100))
                                    operando2 = porcento
                                except:
                                    resultado = 'Erro'
                                    estado_resultado = True

                        elif entrada == '=':
                            if operando1 and operador and operando2:
                                try:
                                    op1 = float(operando1.replace(',', '.'))
                                    op2 = float(operando2.replace(',', '.'))

                                    if operador == '+':
                                        resultado = str(op1 + op2)
                                    elif operador == '-':
                                        resultado = str(op1 - op2)
                                    elif operador == 'x':
                                        resultado = str(op1 * op2)
                                    elif operador == '÷':
                                        resultado = str(op1 / op2 if op2 != 0 else 'Erro')

                                    memoria = resultado
                                    estado_resultado = True

                                    
                                    operando1 = ''
                                    operador = ''
                                    operando2 = ''
                                except:
                                    resultado = 'Erro'
                                    estado_resultado = True

                        elif entrada in ['+', '-', 'x', '÷']:
                            if estado_resultado and memoria:
                                operando1 = memoria
                                estado_resultado = False

                            if operando1 and not operador:
                                operador = entrada

                        elif entrada == '+/-':
                            if operador == '' and operando1:
                                if operando1.startswith('-'):
                                    operando1 = operando1[1:]
                                else:
                                    operando1 = '-' + operando1
                            elif operador and operando2:
                                if operando2.startswith('-'):
                                    operando2 = operando2[1:]
                                else:
                                    operando2 = '-' + operando2
                            elif estado_resultado and resultado:
                                if memoria.startswith('-'):
                                    memoria = memoria[1:]
                                else:
                                    memoria = '-' + memoria
                                resultado = memoria

                        else:
                            if estado_resultado:
                                operando1 = ''
                                operador = ''
                                operando2 = ''
                                resultado = ''
                                estado_resultado = False

                            if not operador:
                                operando1 += entrada
                            else:
                                operando2 += entrada



        

        if estado_resultado and resultado:
            mostrar = resultado
        elif operando2:
            mostrar = operando2
        elif operador:
            mostrar = operador
        elif operando1:
            mostrar = operando1
        elif memoria:
            mostrar = memoria
        else:
            mostrar = ''

        texto_expressao = helvfont(35).render(mostrar, True, 'white')
        texto_rect = texto_expressao.get_rect(center=(640,300))
        SCREEN.blit(texto_expressao, texto_rect)

        display.update()


def play_PPT():
    def verificar_resultado(jogador, maquina):
        if jogador == maquina:
            return "Empate"
        elif (jogador == "pedra" and maquina == "tesoura") or (jogador == "papel" and maquina == "pedra") or (jogador == "tesoura" and maquina == "papel"):
            return "Vitória"
        else:
            return "Derrota"


    opcoes = ['pedra', 'papel', 'tesoura']
    placar = [0,0]
    txt_resultado = ''
    jogador = ''
    maquina = ''

    tam_img = (100,100)
    imgpedra = transform.scale((image.load(f'assets/ppt/pedra.png')), tam_img)
    imgpapel = transform.scale((image.load(f'assets/ppt/papel.png')), tam_img)
    imgtesoura = transform.scale((image.load(f'assets/ppt/tesoura.png')), tam_img)

    while True:
        PPT_MOUSE_POS = mouse.get_pos()

        SCREEN.fill('black')

        tituloforca = gamefont(50).render("Pedra, papel e tesoura",True,'#f39708')
        tituloforcarect = tituloforca.get_rect(center=(640, 100))
        SCREEN.blit(tituloforca, tituloforcarect)

        botao_voltarmenu = Botao(image=None, pos=(100, 100), text_input="Voltar", font=gamefont(20), base_color="#850701", hovering_color="White")

        botao_reiniciar = Botao(image=None, pos=(1150, 100), text_input="Reiniciar", font=gamefont(20), base_color="#FFFFFF", hovering_color="#53EB5D")

        btn_x = 550
        btn_y = 600
        btnPedra = Botao(image=imgpedra, pos=(btn_x,btn_y), text_input="", font=gamefont(20), base_color="#00000000", hovering_color="White", value="pedra")  
        btnPapel = Botao(image=imgpapel, pos=(btn_x+100,btn_y), text_input="", font=gamefont(20), base_color="#00000000", hovering_color="White", value="papel")  
        btnTesoura = Botao(image=imgtesoura, pos=(btn_x+200,btn_y), text_input="", font=gamefont(20), base_color="#00000000", hovering_color="White", value="tesoura")  

        botoes_ppt = [btnPedra, btnPapel, btnTesoura]

        for button in [botao_voltarmenu, botao_reiniciar]:
                button.changeColor(PPT_MOUSE_POS)
                button.update(SCREEN)
        for button in botoes_ppt:
                button.changeColor(PPT_MOUSE_POS)
                button.update(SCREEN)

        for ev in event.get():
            if ev.type == QUIT:
                quit()
                sys.exit()
            if ev.type == MOUSEBUTTONDOWN:
                if botao_voltarmenu.checkForInput(PPT_MOUSE_POS):
                    inicio_menu()

                if botao_reiniciar.checkForInput(PPT_MOUSE_POS):
                    placar = [0,0]
                    txt_resultado = ''
                    jogador = ''
                    maquina = ''

                for botao in botoes_ppt:
                    if botao.checkForInput(PPT_MOUSE_POS):
                        jogador = botao.value

                        maquina = opcoes[random.randint(0,2)]

                        resultado = verificar_resultado(jogador,maquina)

                        if resultado == "Empate":
                            txt_resultado = "Empate"
                        elif resultado == "Derrota":
                            txt_resultado = "Derrota"
                            placar[1] += 1
                        else:
                            txt_resultado = "Vitoria"
                            placar[0] += 1

        placarppt = gamefont(25).render(f"Jogador: {placar[0]} x Maquina: {placar[1]}",True,'White')
        placarpptrect = placarppt.get_rect(center=(640, 200))
        SCREEN.blit(placarppt, placarpptrect)

        result = gamefont(15).render(txt_resultado,True,'White')
        resultrect = result.get_rect(center=(640, 250))
        SCREEN.blit(result, resultrect)

        if jogador == "pedra":
            SCREEN.blit(imgpedra, (500, 350))
        elif jogador == "papel":
            SCREEN.blit(imgpapel, (500, 350))
        elif jogador == "tesoura":
            SCREEN.blit(imgtesoura, (500, 350))

        if maquina == "pedra":
            SCREEN.blit(imgpedra, (700, 350))
        elif maquina == "papel":
            SCREEN.blit(imgpapel, (700, 350))
        elif maquina == "tesoura":
            SCREEN.blit(imgtesoura, (700, 350))


        display.update()

def processar_entrada_num(tecla):
    if len(tecla) <=4 and tecla.isnumeric():
        return True
    else:
        return False



def play_adivinhacao():
    modo_jogo = None
    palpite = ""
    numero_secreto = random.randint(1, 1023)
    tentativas = 0
    feedback = None
    min_computador = 1
    max_computador = 1023
    palpite_computador = None
    estado_jogo = 'andamento' 

    btn_maior = Botao(image=None, pos=(500, 350), text_input="Meu numero e maior", font=gamefont(15), base_color="#53EB5D", hovering_color="White")
    btn_menor = Botao(image=None, pos=(800, 350), text_input="Meu numero e menor", font=gamefont(15), base_color="#53EB5D", hovering_color="White")
    btn_acertou = Botao(image=None, pos=(650, 420), text_input="acertou!", font=gamefont(15), base_color="#53EB5D", hovering_color="White")

    while True:
        ADV_MOUSE_POS = mouse.get_pos()
        SCREEN.fill('black')


        titulo = gamefont(50).render("Jogo de Adivinhacao", True, '#f39708')
        SCREEN.blit(titulo, titulo.get_rect(center=(640, 100)))


        botao_voltarmenu = Botao(image=None, pos=(100, 100), text_input="Voltar", font=gamefont(20), base_color="#850701", hovering_color="White")
        botao_reiniciar = Botao(image=None, pos=(1150, 100), text_input="Reiniciar", font=gamefont(20), base_color="#FFFFFF", hovering_color="#53EB5D")


        cor_jogador = "#53EB5D" if modo_jogo == 'jogador' else "#FFFFFF"
        cor_maquina = "#53EB5D" if modo_jogo == 'maquina' else "#FFFFFF"

        titulomodo = gamefont(15).render("Quem sera o adivinhador?",True,'#FFFFFF')
        titulomodorect = titulomodo.get_rect(center=(640, 175))
        SCREEN.blit(titulomodo, titulomodorect)
        
        botao_jogador = Botao(image=None, pos=(600, 200), text_input="Jogador", font=gamefont(15), base_color=cor_jogador, hovering_color="#53EB5D")
        botao_maquina = Botao(image=None, pos=(700, 200), text_input="Maquina", font=gamefont(15), base_color=cor_maquina, hovering_color="#53EB5D")


        if modo_jogo == 'jogador':
            palpite_texto = gamefont(25).render(f"Seu palpite: {palpite}", True, 'White')
            SCREEN.blit(palpite_texto, (400, 250))
            

            if feedback is not None:
                feedback_text = ""
                if feedback == 1:
                    feedback_text = "Muito baixo! Tente um numero maior"
                elif feedback == -1:
                    feedback_text = "Muito alto! Tente um numero menor"
                elif feedback == 0:
                    feedback_text = f"Acertou em {tentativas} tentativas!"
                    estado_jogo = 'vitoria'
                
                feedback_render = gamefont(20).render(feedback_text, True, '#53EB5D')
                SCREEN.blit(feedback_render, (400, 300))
                
        elif modo_jogo == 'maquina':
            if palpite_computador is None:
                if min_computador > max_computador:
                    estado_jogo = 'trapaca'
                    mensagem_trapaca = gamefont(20).render("Voce trapaceou! Nao ha numero possivel com as dicas dadas.", True, '#FF0000')
                    SCREEN.blit(mensagem_trapaca, (300, 300))
                else:
                    palpite_computador = (min_computador + max_computador) // 2 
                    tentativas += 1
            
            if estado_jogo != 'trapaca':
                palpite_texto = gamefont(25).render(f"O computador chuta: {palpite_computador}", True, 'White')
                SCREEN.blit(palpite_texto, (400, 250))
            
            
            if estado_jogo == 'andamento':
                btn_maior.changeColor(ADV_MOUSE_POS)
                btn_menor.changeColor(ADV_MOUSE_POS)
                btn_acertou.changeColor(ADV_MOUSE_POS)
                
                btn_maior.update(SCREEN)
                btn_menor.update(SCREEN)
                btn_acertou.update(SCREEN)


        if estado_jogo == 'vitoria':
            mensagem = f"Parabens! Voce acertou em {tentativas} tentativas!" if modo_jogo == 'jogador' else f"O computador acertou em {tentativas} tentativas!"
            
            resultado_texto = gamefont(30).render(mensagem, True, '#53EB5D')
            SCREEN.blit(resultado_texto, resultado_texto.get_rect(center=(640, 350)))
            
            botao_reiniciar = Botao(image=None, pos=(640, 450), text_input="Jogar Novamente", 
                                  font=gamefont(25), base_color="#53EB5D", hovering_color="White")
            botao_reiniciar.changeColor(ADV_MOUSE_POS)
            botao_reiniciar.update(SCREEN)


        for button in [botao_voltarmenu, botao_jogador, botao_maquina, botao_reiniciar]:
            button.changeColor(ADV_MOUSE_POS)
            button.update(SCREEN)


        for ev in event.get():
            if ev.type == QUIT:
                quit()
                sys.exit()

            if ev.type == MOUSEBUTTONDOWN:
                if botao_voltarmenu.checkForInput(ADV_MOUSE_POS):
                    inicio_menu()

                if botao_reiniciar.checkForInput(ADV_MOUSE_POS):
                    modo_jogo = None
                    palpite = ""
                    numero_secreto = random.randint(1, 1023)
                    tentativas = 0
                    feedback = None
                    min_computador = 1
                    max_computador = 1023
                    palpite_computador = None
                    estado_jogo = 'andamento'

                if botao_jogador.checkForInput(ADV_MOUSE_POS) and estado_jogo == 'andamento':
                    modo_jogo = 'jogador'
                    numero_secreto = random.randint(1, 1023)
                    tentativas = 0
                    palpite = ""
                    
                if botao_maquina.checkForInput(ADV_MOUSE_POS) and estado_jogo == 'andamento':
                    modo_jogo = 'maquina'
                    min_computador = 1
                    max_computador = 1023
                    tentativas = 0
                    palpite_computador = None
                    

                if modo_jogo == 'maquina' and estado_jogo == 'andamento':
                    if btn_maior.checkForInput(ADV_MOUSE_POS):
                        min_computador = palpite_computador + 1
                        palpite_computador = None
                    elif btn_menor.checkForInput(ADV_MOUSE_POS):
                        max_computador = palpite_computador - 1
                        palpite_computador = None
                    elif btn_acertou.checkForInput(ADV_MOUSE_POS):
                        estado_jogo = 'vitoria'


            if ev.type == KEYDOWN and modo_jogo == 'jogador' and estado_jogo == 'andamento':
                tecla = key.name(ev.key).lower()
                
                if tecla == 'return' and palpite:
                    try:
                        palpite_num = int(palpite)
                        tentativas += 1
                        
                        if palpite_num < numero_secreto:
                            feedback = 1
                        elif palpite_num > numero_secreto:
                            feedback = -1
                        else:
                            feedback = 0
                            estado_jogo = 'vitoria'
                            
                        palpite = ""
                    except ValueError:
                        pass
                elif tecla == 'backspace':
                    palpite = palpite[:-1]
                elif tecla.isdigit() and len(palpite) < 4:
                    palpite += tecla

        display.update()


inicio_menu()