class Funcoes:
    
    #porcentagem de genero (M/F)
    def genero(self):
        arq = open("dados.txt", "r")
        linhas = arq.readlines()
        quantidade = int(linhas[0])
        feminino = 0

        for i in range(1, quantidade + 1, 1):
            pessoas = linhas[i].upper().split(",")
            if pessoas[0] == "F":
                feminino = feminino + 1

        porcentF = feminino / quantidade * 100
        porcentM = (quantidade - feminino) / quantidade * 100
        arq.close()
        result = f"Foi analisado um total de {porcentF:.2f}% participantes feminino "\
                 f"e {porcentM:.2f}% masculino."
        return result

    #porcentagem por idade (jovem adulto e idosos)
    def porcentagens(self):
        arq = open("dados.txt", "r")
        linhas = arq.readlines()
        quantidade = int(linhas[0])
        jovem = adulto = idoso = 0

        for i in range(1, quantidade + 1, 1):
            idade = linhas[i].split(",")
            valor = idade[1]
            if 0 < int(valor) < 19:
                jovem += 1
            elif 20 < int(valor) < 59:
                adulto += 1
            else:
                idoso += 1

        porcentJ = jovem / quantidade * 100
        porcentA = (quantidade - jovem - idoso) / quantidade * 100
        porcentI = (quantidade - jovem - adulto) / quantidade * 100

    #porcentagem de vacina ou placebo
        placebo = 0
        for i in range(1, quantidade + 1, 1):
            dose = linhas[i].upper().split(",")
            if dose[2] == "P":
                placebo += 1

        porcentP = placebo / quantidade * 100
        porcentV = (quantidade - placebo) / quantidade * 100

    #porcentagem de contágio
        contagiu = 0
        for i in range(1, quantidade + 1, 1):
            dose = linhas[i].upper().split(",")
            if dose[3] == "S":
                contagiu += 1

        porcentC = contagiu / quantidade * 100
        porcentNC = (quantidade - contagiu) / quantidade * 100
        arq.close()
        result = f"Total de {porcentJ:.2f}% participantes jovens, {porcentA:.2f}%" \
                 f" adultos e {porcentI:.2f}% idosos\n" \
                 f"Foram aplicadas {porcentV:.2f}% de vacina e {porcentP:.2f}% de placebo\n" \
                 f"{porcentC:.2f}% de participantes contrairam covid e " \
                 f"{porcentNC:.2f}% não contrairam"
        return result

    #porcentagem de eficácia geral
    def eficacia(self):
        arq = open("dados.txt", "r")
        linhas = arq.readlines()
        quantidade = int(linhas[0])
        a = 0
        b = 0
        for i in range(1, quantidade + 1, 1):
            pessoas = linhas[i].upper().split(",")
            if pessoas[2] == "V" and pessoas[3] == "S":
                b += 1
            elif pessoas[2] == "P" and pessoas[3] == "S":
                a += 1
        eficacia = 100 * (a-b)/a
        arq.close()
        result = f"A eficácia geral da vacina equivale a {eficacia:.2f}%"
        return result

    #porcentagem de eficacia por idade
    def eficaciaIdade(self):
        arq = open("dados.txt", "r")
        linhas = arq.readlines()
        quantidade = int(linhas[0]) 
        jovemA = jovemB = 0
        adultoA = adultoB = 0
        idosoA = idosoB = 0
        for i in range(1, quantidade + 1, 1):
            pessoas = linhas[i].split(",")
            if int(pessoas[1]) < 19:
                if pessoas[2] == "P" and pessoas[3] == "S":
                    jovemA += 1
                elif int(pessoas[1]) < 19:
                    if pessoas[2] == "V" and pessoas[3] == "S":
                        jovemB += 1
            elif 19 < int(pessoas[1]) < 59:
                if pessoas[2] == "P" and pessoas[3] == "S":
                    adultoA += 1
            elif 19 < int(pessoas[1]) < 59:
                if pessoas[2] == "V" and pessoas[3] == "S":
                    adultoB += 1
            else:
                if pessoas[2] == "P" and pessoas[3] == "S":
                    idosoA += 1
                elif pessoas[2] == "V" and pessoas[3] == "S":
                    idosoB += 1
        eficaciaJovem = 100 * (jovemA - jovemB) / jovemA
        eficaciaAdulto = 100 * (adultoA - adultoB) / adultoA
        eficaciaIdoso = 100 * (idosoA - idosoB) / idosoA
        arq.close()
        result = f"A eficácia da vacina para jovens é de {eficaciaJovem:.2f}%\n" \
                 f" Para adultos {eficaciaAdulto:.2f}%\n"\
                 f"Para idosos {eficaciaIdoso:.2f}%"
        return result

    #eficácia da vacina por gênero
    def eficaciaGenero(self):
        arq = open("dados.txt", "r")
        linhas = arq.readlines()
        quantidade = int(linhas[0])
        masculinoA = masculinoB = 0
        femininoA = femininoB = 0
        for i in range(1, quantidade + 1, 1):
            pessoas = linhas[i].split(",")
            if pessoas[0] == "M":
                if pessoas[2] == "P" and pessoas[3] == "S":
                    masculinoA += 1
                if pessoas[2] == "V" and pessoas[3] == "S":
                    masculinoB += 1
            else:
                if pessoas[0] == "F":
                    if pessoas[2] == "P" and pessoas[3] == "S":
                        femininoA += 1
                    if pessoas[2] == "V" and pessoas[3] == "S":
                        femininoB += 1

        eficaciaMasculina = 100 * (masculinoA - masculinoB) / masculinoA
        eficaciaFeminina = 100 * (femininoA - femininoB) / femininoA
        arq.close()
        result = f"A eficácia da vacina no gênero masculino equivale a {eficaciaMasculina:.2f}%.\n" \
                 f"A eficácia da vacina no gênero feminino equivale a {eficaciaFeminina:.2f}%."
        return result
