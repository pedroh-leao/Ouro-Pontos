import config
import app

if __name__ == '__main__':
    configuration = config.Config()
    ouro_pontos = app.create_app(configuration)

    ouro_pontos.run(debug=True, host='0.0.0.0', port=5000)