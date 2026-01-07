import requests

url = "https://www.google.com.br"
response = requests.get(url)
# print(response.status_code)
print(response)

# cria um arquivo na pasta de testes e gera o html da resposta da página chamada acima.
with open("testes/page.html", "w") as page:
    page.write(response.text)