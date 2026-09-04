# Password Manager

Aplicação desktop em Python para estudo de interface gráfica com Tkinter, geração de senhas e criptografia básica de credenciais.

> **Aviso:** este projeto tem finalidade educacional. Não use para armazenar senhas reais sem revisar segurança, persistência e tratamento de erros.

## Visão geral

O projeto usa uma senha mestra para derivar uma chave com `PBKDF2HMAC` e criptografar senhas com `Fernet` antes de salvar os dados localmente.

Fluxo atual da aplicação:

1. O usuário faz login com uma senha mestra.
2. A aplicação cria ou reutiliza um `salt` salvo em `.salt`.
3. A chave criptográfica é derivada a partir da senha mestra.
4. As senhas cadastradas são criptografadas antes de serem gravadas em `data.csv`.
5. A interface permite gerar, salvar e buscar credenciais.

## Tecnologias

- `Python 3`
- `Tkinter`
- `cryptography`
- `pyperclip`
- `six`

## Funcionalidades

- Login com senha mestra.
- Geração de senha forte aleatória.
- Cópia automática da senha gerada para a área de transferência.
- Validação simples de e-mail e tamanho mínimo de senha.
- Criptografia de senhas antes do armazenamento local.
- Cadastro de site, e-mail/usuário e senha.
- Busca de credenciais salvas pelo nome do site.
- Tratamento de erro quando a senha mestra não consegue descriptografar um registro.
- Teste isolado do serviço de criptografia em `test_encrypt.py`.

## Estrutura

```text
day_29/
├── encryption_service.py   # Derivação de chave, salt e criptografia
├── main.py                 # Regras principais da aplicação
├── password.py             # Geração de senhas
├── service_interface.py    # Telas de login e cadastro
├── test_encrypt.py         # Teste manual do serviço de criptografia
├── logo.png                # Logo exibida na interface
└── README.md               # Documentação
```

## Como executar

```bash
python -m venv .venv
source .venv/bin/activate
pip install cryptography pyperclip six
python main.py
```

Para testar a criptografia separadamente:

```bash
python test_encrypt.py
```

## Pontos de aprendizado

- Construção de interface desktop com Tkinter.
- Separação entre interface e lógica da aplicação.
- Geração aleatória de senhas.
- Derivação de chave com `PBKDF2HMAC`.
- Criptografia e descriptografia com `Fernet`.
- Leitura e escrita de arquivos locais.
- Versionamento com Git.

## Limitações atuais

- Os dados são armazenados em `data.csv`, sem estrutura robusta ou controle de concorrência.
- O projeto ainda não possui suíte de testes automatizados.
- As validações ainda são básicas.
- A aplicação precisa de revisão de segurança antes de qualquer uso real.

## Próximos passos

- Melhorar a busca para lidar com maiúsculas/minúsculas e múltiplos registros do mesmo site.
- Adicionar edição e remoção de credenciais.
- Melhorar persistência e organização dos dados.
- Cobrir os fluxos principais com testes automatizados.
