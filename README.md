# Conversor de Nomes de Arquivos

## Descrição

Este projeto apresenta um script em Python para automatizar a cópia e a renomeação sequencial de arquivos armazenados em uma pasta.

O programa lê todos os arquivos presentes na pasta de origem, ordena-os pelo nome atual e cria cópias em uma nova pasta, atribuindo nomes padronizados em sequência.

Exemplo:

```text
whatzap Image1.jpg -> Foto_Nomes_Empresas_1.jpg
whatzap Image2.jpg -> Foto_Nomes_Empresas_2.jpg
whatzap Image3.jpg -> Foto_Nomes_Empresas_3.jpg
```

O projeto também inclui:

* Leitura automática dos arquivos de uma pasta
* Ordenação dos arquivos pelo nome atual
* Criação automática da pasta de destino
* Renomeação sequencial
* Preservação da extensão original dos arquivos
* Cópia dos arquivos sem alterar os originais
* Preservação dos metadados dos arquivos por meio de `shutil.copy2`

---

# Estrutura do Projeto

```text
Converter_Nomes_Arquivos/
│
├── Data/
│   ├── arquivo_1.jpg
│   ├── arquivo_2.jpg
│   └── arquivo_3.jpg
│
├── Data_Convertidos/
│   ├── Foto_Nomes_Empresas_1.jpg
│   ├── Foto_Nomes_Empresas_2.jpg
│   └── Foto_Nomes_Empresas_3.jpg
│
├── converter_nomes.py
└── README.md
```

---

# Funcionamento

## 1. Definição das Pastas

A pasta de origem contém os arquivos que serão processados:

```python
pasta_origem = Path(r"/workspaces/Converter_Nomes_Arquivos/Data")
```

A pasta de destino recebe as cópias renomeadas:

```python
pasta_destino = Path(r"/workspaces/Converter_Nomes_Arquivos/Data_Convertidos")
```

---

## 2. Criação da Pasta de Destino

Caso a pasta `Data_Convertidos` ainda não exista, ela será criada automaticamente:

```python
pasta_destino.mkdir(parents=True, exist_ok=True)
```

O parâmetro `exist_ok=True` evita erros caso a pasta já tenha sido criada anteriormente.

---

## 3. Leitura dos Arquivos

O script percorre a pasta de origem e seleciona apenas arquivos:

```python
arquivos = [
    arquivo
    for arquivo in pasta_origem.iterdir()
    if arquivo.is_file()
]
```

Pastas ou outros diretórios internos não são incluídos no processamento.

---

## 4. Ordenação

Antes da renomeação, os arquivos são ordenados pelo nome atual:

```python
arquivos.sort()
```

Dessa forma, a numeração é aplicada seguindo a ordem alfabética dos nomes dos arquivos.

---

# Renomeação dos Arquivos

Os arquivos são numerados a partir de `1` utilizando `enumerate`:

```python
for numero, arquivo in enumerate(arquivos, start=1):
```

O novo nome é criado com o seguinte padrão:

```python
novo_nome = f"Foto_Nomes_Empresas_{numero}{arquivo.suffix}"
```

Exemplo de saída:

```text
Foto_Nomes_Empresas_1.jpg
Foto_Nomes_Empresas_2.jpg
Foto_Nomes_Empresas_3.png
```

A extensão original é preservada através de:

```python
arquivo.suffix
```

---

# Cópia dos Arquivos

Os arquivos originais não são renomeados ou removidos.

O script cria cópias dentro da pasta `Data_Convertidos` utilizando:

```python
shutil.copy2(arquivo, novo_caminho)
```

O método `copy2` também tenta preservar metadados do arquivo, como datas de modificação.

---

# Como Executar

## 1. Clone o repositório

```bash
git clone https://github.com/ArthurF36/Converter_Nomes_Arquivos.git
```

Entre na pasta do projeto:

```bash
cd Converter_Nomes_Arquivos
```

Execute o script:

```bash
python converter_nomes.py
```
---

## 2. Adicione os arquivos

Coloque os arquivos que deseja processar dentro da pasta:

```text
Data/
```

---

## 3. Verifique os caminhos

Caso o projeto esteja em outro diretório, altere os caminhos definidos no script:

```python
pasta_origem = Path(r"/workspaces/Converter_Nomes_Arquivos/Data")
pasta_destino = Path(r"/workspaces/Converter_Nomes_Arquivos/Data_Convertidos")
```

---

## 4. Execute o script

```bash
python converter_nomes.py
```

Ao final da execução, o terminal exibirá as alterações realizadas:

```text
whatzap Image1.jpg -> Foto_Nomes_Empresas_1.jpg
whatzap Image2.jpg -> Foto_Nomes_Empresas_2.jpg
whatzap Image3.jpg -> Foto_Nomes_Empresas_3.jpg

Conversão concluída!
Arquivos salvos em: /workspaces/Converter_Nomes_Arquivos/Data_Convertidos
```

---

# Dependências

O projeto utiliza apenas módulos da biblioteca padrão do Python:

* `pathlib`
* `shutil`

Por esse motivo, não é necessário instalar bibliotecas externas com `pip`.

---

# Requisitos

* Python 3.8 ou superior
* Uma pasta `Data` contendo os arquivos que serão processados

---

# Resultados Esperados

O projeto permite:

* automatizar a padronização dos nomes de arquivos;
* organizar arquivos em sequência numérica;
* preservar os arquivos originais;
* criar automaticamente uma pasta separada para os arquivos convertidos;
* manter a extensão original de cada arquivo;
* reduzir o trabalho manual de renomeação de grandes quantidades de arquivos.

---

# Tecnologias Utilizadas

* Python
* pathlib
* shutil

---

# Observações

A ordenação atual é feita com base no nome dos arquivos:

```python
arquivos.sort()
```

Portanto, a sequência final depende da ordem alfabética dos nomes originais.

Caso existam arquivos com nomes como:

```text
Imagem1.jpg
Imagem2.jpg
Imagem10.jpg
```

a ordenação alfabética pode ser diferente da ordenação numérica esperada.

---

# Autor

Projeto desenvolvido para automatizar a organização, cópia e padronização sequencial de nomes de arquivos utilizando Python.
