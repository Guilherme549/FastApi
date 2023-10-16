from model import Pessoa


class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open("pessoas.txt", "w") as arq:
            arq.write(pessoa.nome + "" + str(pessoa.idade) + "" + pessoa.cpf)

    @classmethod    
    def ler(cls):

        nome = "Guilherme"
        idade = 19
        cpf = 546546546

        return Pessoa(nome, idade, cpf)
    
p1 = Pessoa("Guilherme", 20, "123123131")
print(PessoaDal.ler().nome)   

