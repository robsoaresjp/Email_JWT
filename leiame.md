# Jorge esse sistema criado, acredito eu que esteja completo e não está dificil de entender.


# O sistema abrange
- Perfilamento simples
- Login
- Recuperação de senha
- CRUD de usuário
- CRUD de produtos
- CRUD de fornecedores
- CRU de pedidos

# Fluxo de Informação
## Admin

O admin é responsável por:
- cadastrar usuários
- visualizar usuários
- editar usuários
- excluir usuários
- cadastrar produtos
- visualizar produtos
- editar produtos
- excluir produtos
- cadastrar fornecedores
- visualizar fornecedores
- editar fornecedores
- excluir fornecedores
- cadastrar pedidos
- visualizar pedidos
- editar pedidos
- excluir pedidos

## Usuário
O usuário é responsável por:
- visualizar produtos
- visualizar os próprios pedidos
- cadastrar pedidos


# Inicialização do sistema
Para inicializar o sistema, é necessário:
- Python 3.7 ou superior
- Banco SQL ou similar (caso queira usar sqlite3, apenas não altere o environment)

## Atualização
Lembre-se de atualizar o environment com as credenciais de sua preferência


## Execução
Para executar o sistema, use:
> flask run

ou:
> python application.py

Após rodar o sistema, faça uma requisição para qualquer URL, isso preenche a base de dados.
Na primeira requisição, as tabelas serão criadas automaticamente junto com as seeds de banco para inicializar o projeto.


# Testes
Para rodar os testes, use:
> pytest tests\\models tests\\resources tests\\helpers --disable-pytest-warnings -v
