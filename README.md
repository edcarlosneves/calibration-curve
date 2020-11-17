# Calirabration Curve
Projeto em Django para a construção de curvas de calibração
para aplicação em Química Analítica.

## Tecnologias usadas no projeto
- Python
- Django
- Scipy
- Numpy
- Bootstrap
- Matplotlib

## Para usar localmente

### Via pip (Ubuntu e derivados)
- Clone o repositório
```
git clone https://github.com/edcarlosneves/calibration-curve.git
```
- Entrar na pasta do projeto
```
cd calibration-curve
```
- Criar uma virtualenv
```
vituenv -p python3 .venv
```
- Ativar a virtualenv
```
source .venv/bin/activate
```
- Instalar as dependências do projeto via pip
```
pip install -r requirements.txt
```
- Executar o projeto
```
python manage.py runserver
```
- Abrir a aplicação no Browser
```
http://localhost:8000
```
### Via Docker+Docker Compose
- Certifique-se que tem o Docker + Docker Compose instalados
```
docker -v
```
```
docker-compose -v
```

- Clone o repositório
```
git clone https://github.com/edcarlosneves/calibration-curve.git
```
- Entrar na pasta do projeto
```
cd calibration-curve
```
- Executar o seguinte comando
```
docker-compose up --build
```
- Abrir a aplicação no Browser
```
http://localhost:8000
```
## Contribuindo
Pull requests são bem-vindos. Para mudanças importantes, abra uma issue e informe o que você gostaria de mudar.