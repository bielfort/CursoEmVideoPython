 
def buscar_dados():
    requests = requests.get("https://www.receitaws.com.br/v1/cnpj/")
    print(requests.content)

