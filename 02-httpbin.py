import requests

# url = "https://httpbin.org/get"
url = "https://httpbin.org/post"
data  = {
    "pessoa":{
        "nome":"Joao",
        "idade":30
    }
}

# response = requests.get(url)
response = requests.post(url, json=data)
print(response)

with open("testes/httpbin_response.html", "w") as page:
    page.write(response.request.url)
    page.write("\n\n")
    page.write(response.status_code.__str__())
    page.write("\n\n")
    page.write(response.text)
