#importe de uma classe para agilizar e diminuir codigos para criações Tkinter, feita pelo professor Adjailson
from Tkfull import Janela
#importe das funções necessárias para as opções do combobox
from codigo import Funcoes

class menu_interface:
    mensagem_dados = [["dados vacinação covid-19"]]
    #itens do combobox
    opcoes = [['Escolha os dados que deseja obter:',
               ("gênero",
                "idade, tipo de dose, contágio",
                "eficácia da vacina",
                "eficácia da vacina por idade",
                "eficácia da vacina por gênero")]]
    #botão executar
    botoes = [["*Executar"]]
    #Label vazia onde ficará o resultado
    resultado = [[""]]
    cadastro = [["Cadastro de pessoas"]]
    genero = [['Sexo:', ("F", "M")]]
    idade = [['Idade:', input]]
    dose = [['Tipo de dose:V-vacina/P-placebo:', ("V", "P")]]
    contagio = [["Foi contaminado:", ("S", "N")]]
    cadastrar = [["*Cadastrar"]]
    confirmacao = [[""]]

    #estilização
    estilo_dados = {"bg": "#3EB595", "font": ("Cooper Black", 14)}
    estilo_mensagem = {"font": ("verdana", 12)}
    estilo_combobox = {"font": ("verdana", 10)}
    estilo_resultado = {"font": ("verdana", 10)}
    estilo_cadastro = {"bg": "#3EB595", "font": ("Cooper Black", 14)}

    def __init__(self):
        self.classe = Janela()
        self.classe.icone("dados.png")
        self.classe.titulo("Análise de dados vacinação contra covid")

        #para gerar os campos na tela
        self.classe.gerar(self.mensagem_dados)
        self.classe.gerar(self.opcoes)
        self.classe.gerar(self.botoes)
        self.classe.gerar(self.resultado)
        self.classe.gerar(self.cadastro)
        self.classe.gerar(self.genero)
        self.classe.gerar(self.idade)
        self.classe.gerar(self.dose)
        self.classe.gerar(self.contagio)
        self.classe.gerar(self.cadastrar)
        self.classe.gerar(self.confirmacao)

        #parar aplicar estilos
        self.classe.setEstilo(1, self.estilo_dados)
        self.classe.setEstilo(2, self.estilo_mensagem)
        self.classe.setEstilo(3, self.estilo_combobox)
        self.classe.setEstilo(5, self.estilo_resultado)
        self.classe.setEstilo(6, self.estilo_cadastro)

        #para aplicar eventos
        self.classe.setEvento(4, self.verDados)
        self.classe.setEvento(15, self.ad_pessoa)
        self.classe.start()

    #gera a integração das funções do arquivo "codigo.py" para dentro das opções do combobox
    def verDados(self):
        obj = Funcoes()
        
        escolha = self.classe.getTexto(3)
        #para cada condição nova a resposta antiga é apagada
        self.classe.apagarTexto(5, 1)
        if(escolha == "gênero"):
            self.classe.setTexto(5, obj.genero())
        elif(escolha == "idade, tipo de dose, contágio"):
            self.classe.setTexto(5, obj.porcentagens())
        elif (escolha == "eficácia da vacina"):
            self.classe.setTexto(5, obj.eficacia())
        elif(escolha == "eficácia da vacina por idade"):
            self.classe.setTexto(5, obj.eficaciaIdade())
        else:
            self.classe.setTexto(5, obj.eficaciaGenero())

    #função que adiciona novas pessoas ao arquivo "dados.txt"
    def ad_pessoa(self):
        obj = Funcoes
        arq2 = open("dados.txt", "r")
        linhas = arq2.readlines()
        qtd = int(linhas[0]) + 1
        linhas[0] = str(qtd) + "\n"
        arq2.close()
        arq = open("dados.txt", "w")
        pessoa = self.classe.getTexto(8) + "," + self.classe.getTexto(10)
        pessoa += "," + self.classe.getTexto(12) + "," + self.classe.getTexto(14) + ",\n"
            
        linhas.append(pessoa)
        for l in linhas:
            arq.writelines(str(l))

        arq.close()
        self.classe.mensagem("Cadastro realizado com sucesso!")

menu_interface()
