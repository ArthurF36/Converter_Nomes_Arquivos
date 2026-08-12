from pathlib import Path
import shutil

# Raiz do projeto
BASE_DIR = Path(__file__).resolve().parent

# Pastas dentro da raiz do projeto
pasta_origem = BASE_DIR / "Data"
pasta_destino = BASE_DIR / "Data_Convertidos"

# Cria a pasta de destino caso ela não exista
pasta_destino.mkdir(parents=True, exist_ok=True)

# Lista os arquivos da pasta de origem
arquivos = [
    arquivo
    for arquivo in pasta_origem.iterdir()
    if arquivo.is_file()
]

# Ordena pelo nome atual
arquivos.sort()

# Copia os arquivos para a nova pasta, renomeando em sequência
for numero, arquivo in enumerate(arquivos, start=1):
    novo_nome = f"Foto_Nomes_Empresas_{numero}{arquivo.suffix}"

    novo_caminho = pasta_destino / novo_nome

    shutil.copy2(arquivo, novo_caminho)

    print(f"{arquivo.name} -> {novo_nome}")

print("\nConversão concluída!")
print(f"Arquivos salvos em: {pasta_destino}")