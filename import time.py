import time
print()
print("Olá bem-vindo a ouvidoria do ramonzin")
time.sleep(1)
from datetime import datetime, timedelta
agora = datetime.now()
hora = agora.hour
minuto = agora.minute
segundo = agora.second
data = agora.strftime("%d/%m/%y")
ocorrencia = []
opção = 88
opção = (input('''
--------------------------------------------------------
- encaminhando para o menu da nossa ouvidoria
- por favor, leia e prossiga conforme as instruções
- digite alguma coisa para prosseguir com o suporte
--------------------------------------------------------
- Digite: '''))

while opção != 5:
    print('''
-------------------------------------------------
- Digite - "1" para Listar Ocorrência
- Digite - "2" para Cadastrar nova ocorrência
- Digite - "3" para Remover Ocorrência
- Digite - "4" para Pesquisar Ocorrência
- Digite - "5" para Sair do Programa
-------------------------------------------------
- Escolha a sua opção: ''')
    print()
    opção = int(input("digite: "))
    if opção == 1:
        if len(ocorrencia) == 0:
            print("Você não tem nenhuma ocorrência registrada")
        else:
            for operação in ocorrencia:
                print("-",operação)
    elif opção == 2:
        print("Para Cadastrar uma nova ocorrência, digite abaixo.")
        nome_completo = input("digite seu nome completo: ")
        tipo = input("Qual seu tipo de chamado: ")
        novaocorrencia = input("Digite a Ocorrência: ")
        ocorrencia.append(novaocorrencia)
        print("Ocorrência registrada:", novaocorrencia)
        for i in range(len(ocorrencia)):
            print()
            print("Código:", i+1, "\nOcorrência:", ocorrencia[i],"\nSua ocorrencia foi registada com sucesso as:",hora, "Horas", minuto, "minutos", segundo, "segundos",", do dia", data)
    elif opção == 3:
        print("Para Exluir Ocorrencia, Digite o nome: ")
        fechar_ocorrencia = int(input("Excluir Ocorrencia: "))
        if fechar_ocorrencia in ocorrencia:    
            ocorrencia.pop(range(len(fechar_ocorrencia)))
            print("Ocorrencia excluida com sucesso.")
            print(ocorrencia)
        else:
            print("Ocorrencia não encontrada, tente novamente")
    elif opção == 4:
            print()
            print("Para pesquisar a sua ocorrência, digite abaixo o seu código, para prosseguir")
            codigo = int(input("Digite o código: "))
            if 1 <= codigo <= len(ocorrencia):
                opcodigo = ocorrencia[codigo-1]
                print("ocorrencia:",codigo)
                print(opcodigo)
            else:
                print("Codigo invalido, tente novamente.")
    elif opção != 5:
        print("sair") 
print("finalizado")


