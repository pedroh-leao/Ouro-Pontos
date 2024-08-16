# Ouro-Pontos
<p> Para iniciar, instale o virtualenv </p>

```
pip install virtualenv
```

<p> Dentro da pasta Ouro-Pontos, execute o seguinte comando para inciar o ambiente virtual: </p>

```
source venv/bin/activate
```

<p>No ambiente virtual, instale as dependências necessárias:</p>

```
pip install -r requirements.txt
```

<p>Dentro do ambiente virtual, para executar o servidor, há duas opções:</p>

```
python3 ouro_pontos.py
```

```
export FLASK_APP=app
export FLASK_ENV=development
flask --debug run
```

<p>Para desconectar do ambiente virtual basta executar:</p>

```
deactivate
```