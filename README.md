# Python Manage

## Grupy SP - Mercado Livre - 15 Dezembro de 2016

## Como usar:

1. Clone

```bash
git clone https://github.com/rochacbruno/manage_example_grupy
cd manage_example_grupy
```

2. Instale as dependencias

> recomendado usar virtualenv

```bash
pip install manage
pip install pyfiglet
pip install ipython

# ou

pip install -r requirements.txt
```

Use:

```bash
$ manage --help

$ manage image rotate logo-grupy.png 45
$ manage image to_bw path_to_image.jpg
$ manage utils say_hi --name=Bruno
```

Customize:

> edite o arquivo `manage.yml` para adicionar mais opções e comandos.
