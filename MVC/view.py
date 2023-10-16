from controller import PessoaController


while True:
    decisao = int(
        input(
            "Digite 1 para salvar um pessoa ou digite 2 para ver a pessoa salvar e 3 para sair: "
        )
    )
    if decisao == 3:
        print("Finalizado")
        break
    if decisao == 1:
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        cpf = input("Digite seu cpf: ")

        if PessoaController.Cadastrar(nome, idade, cpf):
            print("Usuario cadastrado com sucesso")
        else:
            print("valores invalidos")
