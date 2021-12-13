from config import *
from modelo import Pessoa
from modelo import Disciplina
from modelo import EstudanteDaDisciplina
from flask import jsonify
from flask import request
import flask

@app.route("/")
def inicio():
    return flask.render_template('inicio.html')  #ir direto pra ação na página home


@app.route("/listarPessoasJson")
def listarPessoasJson():
    pessoasBD = db.session.query(Pessoa).all()
    pessoasJson = []
    for x in pessoasBD:
        pessoasJson.append(x.json())
    resposta = jsonify(pessoasJson)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/incluirPessoas", methods=['post']) 
def incluirPessoas(): 
   resposta = jsonify({"resultado": "Criado com sucesso", "detalhes": "ok"}) 
   dadosnovapessoa = request.get_json()
   try: 
    novapessoa = Pessoa(**dadosnovapessoa) 
    db.session.add(novapessoa)
    db.session.commit() 
   except Exception as e:
    resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
   resposta.headers.add("Access-Control-Allow-Origin", "*") 
   return resposta 

@app.route("/incluirDisciplinas", methods=['post']) 
def incluirDisciplinas(): 
   resposta = jsonify({"resultado": "Criado com sucesso", "detalhes": "ok"}) 
   dadosnovadisciplina = request.get_json()
   try: 
    novadisciplina = Disciplina(**dadosnovadisciplina) 
    db.session.add(novadisciplina)
    db.session.commit() 
   except Exception as e:
    resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
   resposta.headers.add("Access-Control-Allow-Origin", "*") 
   return resposta 

@app.route("/listarDisciplinasJson")
def listarDisciplinasJson():
    disciplinaBD = db.session.query(Disciplina).all()
    disciplinaJson = []
    for x in disciplinaBD:
        disciplinaJson.append(x.json())
    resposta = jsonify(disciplinaJson)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listarEstudantesDisciplinasJson")
def listarEstudantesDisciplinasJson():
    rstudanteDaDisciplinaBD = db.session.query(EstudanteDaDisciplina).all()
    rstudanteDaDisciplinaJson = []
    for x in rstudanteDaDisciplinaBD:
        rstudanteDaDisciplinaJson.append(x.json())
    resposta = jsonify(rstudanteDaDisciplinaJson)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/incluirEstudanteDisciplina", methods=['post']) 
def incluirEstudanteDisciplina(): 
   resposta = jsonify({"resultado": "Criado com sucesso", "detalhes": "ok"}) 
   dadosnovoestudantedisciplina = request.get_json()   
   try: 
    novoestudantedisciplina = EstudanteDaDisciplina(**dadosnovoestudantedisciplina) 
    novoestudantedisciplina.pessoa = encontrarPessoa(novoestudantedisciplina.pessoaId)
    novoestudantedisciplina.disciplina = encontrarDisciplina(novoestudantedisciplina.disciplinaId)    
    db.session.add(novoestudantedisciplina)
    db.session.commit() 
   except Exception as e:
    resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
   resposta.headers.add("Access-Control-Allow-Origin", "*") 
   return resposta 

def encontrarPessoa(pessoaId):    
    return Pessoa.query.get(pessoaId)

def encontrarDisciplina(disciplinaId):    
    return Disciplina.query.get(disciplinaId)

@app.route("/script.js")#rota para carregar o js
def javascriptcarros():
    return flask.render_template('script.js')  

# iniciar o servidor web(endereço http://localhost:5000/ ou ver no terminal)
app.run(debug=True)    