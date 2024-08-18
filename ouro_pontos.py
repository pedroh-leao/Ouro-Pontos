import app

if __name__ == '__main__':
    ouro_pontos = app.create_app()
    ouro_pontos.run(debug=True, host='0.0.0.0', port=5000)