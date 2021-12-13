from config import *

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    cpf = db.Column(db.String(254))
    email = db.Column(db.String(254))

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cpf": self.cpf,
        }

# pra mostrar de modo entendivel no print
    def __str__(self):
        return str(self.id)+"- "+ self.nome + ", " +\
            self.cpf + ", " + self.email

class Disciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    cargaHoraria = db.Column(db.Integer)
    ementa = db.Column(db.String(254))

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "cargaHoraria": self.cargaHoraria,
            "ementa": self.ementa
        }

# pra mostrar de modo entendivel no print
    def __str__(self):
        return str(self.id)+"- "+ self.nome + ", " +\
            self.cargaHoraria + ", " + self.ementa

class EstudanteDaDisciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    semestre = db.Column(db.Integer)
    mediaFinal = db.Column(db.String(254))
    frequencia = db.Column(db.Integer)#em porcentagem
    pessoaId = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=True) 
    pessoa = db.relationship("Pessoa")
    disciplinaId = db.Column(db.Integer, db.ForeignKey(Disciplina.id), nullable=True) 
    disciplina = db.relationship("Disciplina")

    def json(self):
        return {
            "id": self.id,
            "semestre": self.semestre,
            "mediaFinal": self.mediaFinal,
            "frequencia": self.frequencia,
            "pessoaId": self.pessoaId,
            "pessoa": self.pessoa.json(),
            "disciplinaId": self.disciplinaId,
            "disciplina": self.disciplina.json()
        }

# pra mostrar de modo entendivel no print
    def __str__(self):
        return str(self.id)+"- "+ self.semestre + ", " +\
            self.mediaFinal + ", " + self.frequencia+", "+ self.pessoa.json()+", "+ self.disciplina.json()

# teste com valores fixos    
if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    #criar e adicionar pessoas
    pessoa1 = Pessoa(nome = "Joao", cpf = "123123123", email = "joao@yahoo.com")
    pessoa2 = Pessoa(nome = "Paulo", cpf = "123124124", email = "paulinho@gmail.com")
    pessoa3 = Pessoa(nome = "Claudio", cpf = "32141515", email = "CLAUDIO@hotmail.com")
    db.session.add(pessoa1)
    db.session.add(pessoa2)
    db.session.add(pessoa3)

     #criar e adicionar disciplinas
    disciplina1 = Disciplina(nome = "Python", cargaHoraria = "30", ementa = "python web")
    disciplina2 = Disciplina(nome = "PDSII", cargaHoraria = "60", ementa = "Trabalho final")
    db.session.add(disciplina1)
    db.session.add(disciplina2)


     #criar e adicionar Estudantes de disciplinas
    disciplinaestudante = EstudanteDaDisciplina(semestre = "6", mediaFinal = "10", frequencia = 100, pessoaId=1,pessoa=pessoa1, disciplinaId=1,disciplina=disciplina1)
    db.session.add(disciplinaestudante)
    #enviar modificações ativas na sessão pro bd
    db.session.commit()
