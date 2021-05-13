from datetime import datetime

dict = {}
index_dict = 0
ctrl_loop_principal = True
ctrl_cadastro = True

while ctrl_loop_principal:
    #Cadastro de Dados
    if ctrl_cadastro:
        nome_cliente = input("Digite nome do cliente: ")
        nome_anuncio = input("Digite nome do anúncio: ")
        investimento = int(input("Digite valor do investimento: R$ "))
        data_inicio = datetime.strptime(input("Digite a data de início (ex. 12/12/2012): "), "%d/%m/%Y")
        data_termino = datetime.strptime(input("Digite a data de término (ex. 30/12/2012): "), "%d/%m/%Y")

        #Cálculo de indicadores
        dias = data_termino - data_inicio
        vis_original = (investimento * dias.days) * 30
        cliques = (vis_original / 100) * 12
        compart_clique = (cliques / 20) * 3

        if compart_clique > 4:
            compart_clique = 4

        vis_compart = compart_clique * 40
        total = vis_compart + vis_original

        #Inserção dos dados no dicionário
        dict[index_dict] = {"nome_cliente": nome_cliente, "nome_anuncio": nome_anuncio
            , "investimento": investimento, "data_inicio": data_inicio, "data_fim": data_termino
            , "vis_total": round(total), "compart_total": round(compart_clique), "cliques_total": round(cliques)}

        index_dict += 1

    if int(input("\nDeseja imprimir relatório? 1 - Sim | 2 - Não ")) == 1:
        if int(input("1 - Por Nome do Cliente | 2 - Por Período ")) == 1:
            print("\n")
            cliente_pesquisa = input("Digite nome do cliente: ")
            for index, cadastro in dict.items():
                if cadastro['nome_cliente'] == cliente_pesquisa:
                    print("\n")
                    print(f"Nome do Cliente: {cadastro['nome_cliente']}")
                    print(f"Nome do Anúncio: {cadastro['nome_anuncio']}")
                    print(f"Visualizações: {cadastro['vis_total']}")
                    print(f"Compartilhamentos: {cadastro['compart_total']}")
                    print(f"Cliques: {cadastro['cliques_total']}")
                    print(f"Período: {cadastro['data_inicio']} até {cadastro['data_fim']}")
        else:
            print("\n")
            inicio = datetime.strptime(input("Digite a data inicial (ex. 12/12/2012): "), "%d/%m/%Y")
            fim = datetime.strptime(input("Digite a data final (ex. 12/12/2012): "), "%d/%m/%Y")
            for index, cadastro in dict.items():
                if cadastro['data_inicio'] == inicio and cadastro['data_fim'] == fim:
                    print("\n")
                    print(f"Nome do Cliente: {cadastro['nome_cliente']}")
                    print(f"Nome do Anúncio: {cadastro['nome_anuncio']}")
                    print(f"Visualizações: {cadastro['vis_total']}")
                    print(f"Compartilhamentos: {cadastro['compart_total']}")
                    print(f"Cliques: {cadastro['cliques_total']}")
                    print(f"Período: {cadastro['data_inicio']} até {cadastro['data_fim']}")

    if int(input("\nDeseja realizar outro cadastro?"
                 "1 - Sim | 2 - Não ")) == 1:
        ctrl_cadastro = True
    else:
        ctrl_cadastro = False

    if ctrl_cadastro == False:
        if int(input("\nDeseja finalizar programa? 1 - Sim | 2 - Não ")) == 2:
            ctrl_loop_principal = True

    print("\n\n")