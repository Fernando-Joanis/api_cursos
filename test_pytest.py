import requests


class TestCursos:
    url_base_cursos = 'http://127.0.0.1:8000/api/v2/cursos/'
    
    def test_get_cursos(self):
        cursos = requests.get(url=url_base_cursos)
        
        assert cursos.status_code == 200

    def test_get_curso(self):

        curso = requests.get(url=f'{url_base_cursos}5/')

        assert curso.status_code == 200
