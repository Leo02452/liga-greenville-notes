<h1 align="center">Liga Greenville Notes</h1>

## Índice

- [Descrição](#page_facing_up-descrição)
- [Próximos passos](#construction-próximos-passos)
- [Habilidades desenvolvidas](#bulb-habilidades-desenvolvidas)
- [Funcionalidades](#sparkles-funcionalidades)
- [Ferramentas](#hammer_and_wrench-ferramentas)
- [Como usar a aplicação](#computer-como-usar-a-aplicação)
- [Autor](#memo-autor)


## :page_facing_up: Descrição

Projeto desenvolvido em Python e Flask para automatizar o registro de notas da Liga Greenville, liga amadora de FIFA da qual faço parte.

O fluxo consiste em o usuário fazer upload das fotos e o programa junta as fotos do mesmo time, inverte a cor, usa o pytesseract pra extrair os dados e os dispõe em inputs e dropdowns pro usuário corrigir. Após correções o usuário registra cada jogo individualmente direto em uma planilha e em um CSV de backup.

## :construction: Próximos passos
<details>
  <summary><strong>Ver mais</strong></summary>

- [ ] Fazer deploy da aplicação
</details>


## :bulb: Habilidades desenvolvidas
<details>
  <summary><strong>Ver mais</strong></summary>

- Criar aplicação única do zero

- Criar aplicação com Flask

- Utilizar Jinja2

- Utilizar Python

- Utilizar Pytesseract

</details>


## :sparkles: Funcionalidades
<details>
  <summary><strong>Ver mais</strong></summary>

:heavy_check_mark: Fazer upload de fotos dos jogos

:heavy_check_mark: Corrigir dados de jogadores

:heavy_check_mark: Salvar jogo direto na planilha

:heavy_check_mark: Salvar jogo em CSV
</details>


## :hammer_and_wrench: Ferramentas
<details>
  <summary><strong>Ver mais</strong></summary>

* [Python](https://www.python.org/py) para desenvolver
* [Pytesseract](https://pypi.org/project/pytesseract/) para extrair dados das imagens
* [Pillow](https://pypi.org/project/Pillow/) para lidar com imagens, como combinação de duas imagens e inversão de cores
* [Flask](https://flask.palletsprojects.com/en/2.3.x/) para desenvolver aplicação web
* [Gspread](https://docs.gspread.org/en/latest/) para fazer integração com Google Planilhas
</details>


## :computer: Como usar a aplicação
<details>
  <summary><strong>Pré-requisitos</strong></summary>

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

- [Python](https://www.python.org/py)
- [Git](https://git-scm.com)
</details>

<details>
  <summary><strong>Executar o projeto</strong></summary>
1 - Clone esse repositório para sua máquina com o seguinte comando:

```
 git clone git@github.com:Leo02452/liga-greenville-notes.git
```

2 - Entre na pasta criada:

```
 cd liga-greenville-notes
```

3 - Crie um ambiente virtual se quiser:

```
 python3 -m venv .venv && source .venv/bin/activate
```

4 - Instale as dependências:

```
 python3 -m pip install -r requirements.txt
```

5 - Execute a aplicação:

```
 export FLASK_APP=app/app.py && flask run --reload
```

6 - Acesse em seu navegador o endereço `127.0.0.1:5000` 
</details>


## :memo: Autor

Desenvolvido por Leonardo Araujo

Email: leonardo_02452@hotmail.com

Github: https://github.com/Leo02452

LinkedIn: https://www.linkedin.com/in/leo02452/

---