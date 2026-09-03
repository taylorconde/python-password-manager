# Password Manager — Projeto de Estudo

Um gerenciador de senhas simples, desenvolvido em Python como projeto de estudo e aprendizado.

O objetivo principal deste projeto é praticar a construção de uma aplicação desktop, organização de código, geração de senhas e fundamentos de criptografia aplicada.

> **Aviso:** este projeto ainda está em desenvolvimento e tem finalidade educacional. Não o utilize para proteger senhas reais sem antes realizar uma revisão completa de segurança.

## Tecnologias utilizadas

- **Python 3** — linguagem principal do projeto.
- **Tkinter** — criação da interface gráfica desktop.
- **Fernet**, da biblioteca `cryptography` — criptografia simétrica autenticada.
- **PBKDF2-HMAC-SHA256** — derivação de uma chave criptográfica a partir da senha mestra.
- **Pyperclip** — cópia da senha gerada para a área de transferência.
- **CSV/texto estruturado** — armazenamento local dos registros no arquivo `data.csv`.

## Como funciona

1. O usuário informa uma senha mestra.
2. A aplicação cria ou carrega um salt local no arquivo `.salt`.
3. A senha mestra e o salt são usados pelo PBKDF2-HMAC-SHA256 para derivar a chave de criptografia.
4. A senha cadastrada é criptografada com Fernet antes de ser salva.
5. Os dados são armazenados localmente, associados ao site e ao e-mail/usuário informado.

A senha mestra não é salva pelo programa. Sem ela e sem o respectivo `.salt`, os registros criptografados não podem ser recuperados pela aplicação.

## Funcionalidades atuais

- Login com senha mestra.
- Geração de senhas fortes aleatórias.
- Cópia automática da senha gerada para a área de transferência.
- Validação básica de e-mail e tamanho mínimo da senha.
- Criptografia das senhas antes do armazenamento.
- Interface gráfica para cadastrar site, e-mail/usuário e senha.
- Teste independente de criptografia e descriptografia em `test_encrypt.py`.

## Próxima funcionalidade

Uma das próximas etapas será implementar a **busca de senhas**:

- localizar um registro pelo nome do site;
- descriptografar o valor armazenado usando a chave derivada da senha mestra;
- exibir o resultado somente quando solicitado pelo usuário;
- permitir copiar a senha recuperada para a área de transferência.

## O que estou aprendendo

Este projeto está sendo usado para praticar:

- criação de interfaces gráficas com Tkinter;
- separação entre interface, regras de negócio e serviço de criptografia;
- uso de classes e injeção simples de callbacks;
- geração segura de valores aleatórios;
- derivação de chaves criptográficas;
- criptografia e descriptografia de dados;
- validação de entradas do usuário;
- leitura e escrita de arquivos;
- uso de Git para acompanhar a evolução do código.

## Como executar

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install cryptography pyperclip six
```

Execute a aplicação:

```bash
python main.py
```

Para executar o teste de criptografia:

```bash
python test_encrypt.py
```

## Estrutura do projeto

```text
day_29/
├── encryption_service.py   # Derivação de chave e criptografia Fernet
├── main.py                 # Fluxo principal da aplicação
├── password.py             # Geração de senhas aleatórias
├── service_interface.py    # Interfaces de login e cadastro
├── test_encrypt.py         # Teste de criptografia/descriptografia
├── logo.png                # Imagem da interface
└── README.md               # Documentação do projeto
```

## Melhorias futuras

- Implementar busca e recuperação de senhas.
- Separar o armazenamento em uma estrutura mais robusta.
- Melhorar o tratamento de erros de descriptografia.
- Adicionar edição e exclusão de registros.
- Evitar exibir senhas em texto aberto nas caixas de confirmação.
- Remover valores de teste fixos e revisar permissões dos arquivos locais.
- Adicionar testes automatizados para os principais fluxos.

## Status

🚧 Projeto em desenvolvimento — criado para estudo, prática e aprendizado contínuo.
