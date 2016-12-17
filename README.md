# Python Manage

Biblioteca para criação de ferramentas de linhas de comando e shell interativo para programas em Python de forma não invasiva, não é preciso alterar nada no código, apenas no `manage.yml`

## Grupy SP - Mercado Livre - 15 de Dezembro de 2016

## Como usar:

1. Clone

```bash
git clone https://github.com/rochacbruno/manage_example_grupy
cd manage_example_grupy
```

2. Instale as dependencias

> recomendado usar virtualenv

Instale o manage
```bash
pip install manage
```

instale dependencias adicionais/opcionais usadas no exemplo de código `program.py`

```bash
pip install pyfiglet
pip install pillow
pip install ipython

# ou

pip install -r requirements.txt
```

Use:

```bash
$ manage --help

$ manage shell

$ manage image rotate logo-grupy.png 45
$ manage image to_bw path_to_image.jpg
$ manage utils say_hi --name=Bruno
```

Customize:

> edite o arquivo `manage.yml` para adicionar mais opções e comandos.
