from app.extensions import db

class PontoTuristico(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(150))
    descricao = db.Column(db.Text)
    longitude = db.Column(db.String(50))
    latitude = db.Column(db.String(50))

    def __repr__(self) -> str:
        return f"id:{{{self.id}}} - nome:{{{self.nome}}} - descrição:{{{self.descricao}}} - latitude:{{{self.latitude}}} - longitude:{{{self.longitude}}}"