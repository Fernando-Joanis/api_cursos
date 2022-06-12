import requests


# Get avaliacoes

avaliacoes = requests.get('http://127.0.0.1:8000/api/v2/avaliacoes/')

print(avaliacoes.status_code)
print(avaliacoes.json())


cursos = requests.get('http://127.0.0.1:8000/api/v2/cursos/')

print(cursos.status_code)
