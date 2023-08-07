# nuclea-python-finance
## O Projeto:
Construiremos uma aplicação em Python que ofereça um menu com 5 opções ao usuário. **As Opções são as seguintes**:  

**1 - Cliente**:  

- Essa opção irá oferecer ao usuário a opção de realizar um CRUD com o Cliente. Deve ser exibido as seguintes opções:  
	- Cadastrar Cliente:  
  		> Os campos necessários para cadastrar um cliente são: ID, Nome, CPF, RG, Data Nascimento, CEP, Logradouro, ~~Complemento~~, Bairro, Cidade, Estado e ~~Número residência~~ **Status**.
 
		> Os campos do cliente devem ser validados com as validações construídas durante as aulas (**Nome**, CPF, ~~RG~~, CEP e DATA).
	- Consultar Cliente;
	- Atualizar Cliente;
	- Deletar Cliente (**deleção virtual**);  
> ~~O cliente deve ser construído seguindo o modelo do script que foi passado no repositório do GitHub.~~

**2 - Ordem**:  
- A ordem no sistema representa uma ordem de compra de uma ação. Ao selecionar essa opção deve ser exibido ao usuário a opção de:
	- Cadastrar ordem de compra:
		> Os campos necessários para cadastrar uma ordem são: ID, Nome, Ticket, Valor Compra, Quantidade Compra, Data Compra e ID do Cliente.
 	- **Deletar ação (deleção bruta que quebra o sistema caso executada)**;
  
**3 - Realizar análise da carteira**:
- A opção de análise irá exibir ao usuário um gráfico utilizando a biblioteca Matplotlib contendo as informações das ações cadastradas no banco de dados de determinado usuário. Essa determinação deve ocorrer através da solicitação do CPF do Cliente.

**4 - Imprimir relatório da carteira ou Consultar relatório da ação**:
- Essa opção permite  duas possibilidades:
	- Executar o arquivo(relatorio) para imprimir relatório pegando as ações do cliente que estão armazenadas dentro do banco de dados. Dessa forma será necessário solicitar o CPF do cliente e consultar as ações atreladas a ele e então criar um arquivo informando o relatório de cada ação. O nome desse arquivo deve ser solicitado ao cliente e deve ter a extensão txt.
	- Oferecer ao cliente uma opção para consultar dados de qualquer ação, para que ele possa se informar sobre o seu status atual.
 
**5 - Sair**:
- Opção sair irá encerrar a aplicação.


Obs.:
> Todas as opções do menu devem perguntar ao usuário se ele deseja voltar ao menu principal ou sair da aplicação.
> 
> O código deve ser escrito utilizando os princípios ensinados em aula da orientação a objetos.
> 
> O código deve conter testes unitários para testar a aplicação.
> 
> O projeto deve ser entregue no dia 07/08/2023 até às 19:00 para o email danielgundimvieira@hotmail.com  
	- No email deve ser informado:  
		- Nome do aluno;  
		- Link do repositório no Github;  
		- O repositório deve estar público.  
