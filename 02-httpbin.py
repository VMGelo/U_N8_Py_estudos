import requests

# url = "https://httpbin.org/get"
url = "https://httpbin.org/post"
data  = {
    "pessoa":{
        "nome":"Joao",
        "profissao":"professor"
    }
}
params ={
    "dataIni":"2025-01-01",
    "dataFim":"2025-12-31"
}

# response = requests.get(url)
response = requests.post(url, json=data, params=params)
print(response.request.url)
print(response.text)

#with open("testes/httpbin_response.html", "w") as page:
#    page.write(response.request.url)
#    page.write("\n\n")
#    page.write(response.status_code.__str__())
#    page.write("\n\n")
#    page.write(response.text)
