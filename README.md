# PowerOn

Sistema de academia em Python 3.10 ou superior, com menus no terminal.
Não requer bibliotecas externas.

Cadastre alunos e professores, depois modalidades e matrículas. O menu
principal também oferece faturamento por modalidade. Datas usam DD/MM/AAAA;
valores decimais aceitam ponto ou vírgula; altura é informada em metros.
Os submenus permitem cadastrar, buscar, listar, atualizar e excluir.
Na matrícula, a atualização altera apenas a quantidade de aulas. Para trocar
aluno ou modalidade, exclua a matrícula e cadastre uma nova.

## Organização

- `models/`: campos, validações e conversão entre objetos e dicionários.
- `structures/BST.py`: árvore binária em memória, com código e posição no arquivo.
- `persistence/repositorio.py`: leitura e gravação dos arquivos indexados.
- `services/`: regras, relacionamentos, vagas e faturamento.
- `views/`: entradas, menus e exibição dos registros.
- `main.py`: cria os quatro repositórios compartilhados e inicia os menus.

Os arquivos `data/alunos.txt`, `professores.txt`, `modalidades.txt` e
`matriculas.txt` são criados automaticamente junto ao projeto, independentemente
da pasta de execução. Cada linha tem um indicador (`1|` ativo ou `0|` excluído)
e os dados em JSON. A árvore é reconstruída ao iniciar o programa; consultas
usam a posição do registro encontrada no índice.

O total de alunos é controlado pelas inclusões e exclusões de matrículas.
Não é permitido excluir registros ainda utilizados por outras tabelas.
O faturamento considera as matrículas ativas e o valor atual da aula:
`soma(valor_aula × quantidade_aulas de cada matrícula)`. Não há histórico
de pagamentos. Cada matrícula conta como uma vaga, conforme o enunciado.
