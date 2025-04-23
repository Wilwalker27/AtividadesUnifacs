# Este é um simples sistema de CRUD em Python.


usuarios = [] # armazena os usuários cadastrados
  
def cadastrar_usuario(): # função para cadastrar um novo usuário
    
    print("\n--- Cadastro de Usuário ---")
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    idade = input("Digite a idade: ")
    
    # Cria um dicionário com as informações do usuário
    usuario = {"nome": nome, "email": email, "idade": idade}
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def listar_usuarios(): # função para listar todos os usuários cadastrados
    
    print("\n--- Lista de Usuários ---")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for i, usuario in enumerate(usuarios, start=1):
            print(f"{i}. Nome: {usuario['nome']}, E-mail: {usuario['email']}, Idade: {usuario['idade']}")

def buscar_usuario(): # função para buscar um usuário pelo nome
    
    print("\n--- Busca de Usuário ---")
    nome_busca = input("Digite o nome do usuário que deseja buscar: ")
    for usuario in usuarios:
        if usuario["nome"].lower() == nome_busca.lower():
            print(f"Usuário encontrado: Nome: {usuario['nome']}, E-mail: {usuario['email']}, Idade: {usuario['idade']}")
            return
    print("Usuário não encontrado.")

def exibir_menu(): # função para exibir o menu principal
    
    print("\n--- Menu ---")
    print("1. Cadastrar Usuário")
    print("2. Listar Usuários")
    print("3. Buscar Usuário")
    print("4. Sair")

def main(): # função principal que executa o programa
    print("\n Bem-vindo ao sistema de cadastro de usuários!")
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            buscar_usuario()
        elif opcao == "4":
            print("Saindo da aplicação. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa a aplicação
if __name__ == "__main__":
    main()



# Obrigado por me permitirem participar do processo de seleção, espero conseguir.
# Link do Repositório: https://github.com/Wilwalker27/Crud_Simples