import os

restaurantes = [{'nome':'Praça','categoria':'Japonesa','ativo':False},
                {'nome':'Pizza Suprema','categoria':'Italiana','ativo':True},
                {'nome':'Sushi Bar','categoria': 'Japonesa','ativo':True}]

def voltar_ao_menu():
    input ('\nDigite uma tecla para voltar para as opções: ')
    main()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '=' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def exibir_nome_do_programa():
    print('\n🆂🅰🅱🅾🆁 🅴🆇🅿🆁🅴🆂🆂\n')

def casdastrar_restaurante():
    ''' Essa função é responsavel por cadastrar um novo restaurante'''
    exibir_subtitulo('Cadastrado de Restaurante: \n')
    nome_do_restaurante = input('Digite o nome do restaurando para cadastro: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante ={'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado.')
    voltar_ao_menu()

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Alterna estado do Restaurante')
    print('4. Sair')

def finalizar_app():
    exibir_subtitulo('Finalizando o app...\n')

def opcao_invalidada():
    print ('Opção invalida')
    voltar_ao_menu()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes: \n')
    
    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status\n'}')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome'] 
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu()

def alterna_estado_restaurante():
    exibir_subtitulo('Alterando status restaurante: ')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterna o status (ativo)|(desativado):')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')

    voltar_ao_menu()
    
def escolher_opcao(): 
    try:   
        opcao_escolhida = int(input('\nEscolha uma opção: '))

        if opcao_escolhida == 1:
            casdastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterna_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            print('Opção inválida! Tente novamente.\n')
            escolher_opcao()
    except ValueError:
        print('Entrada inválida! Por favor, insira um número.\n')
        escolher_opcao()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()