from flask import Flask, request
from src.flask_db import novoUsuario

app = Flask("API de cadastro")

@app.route("/", methods=["GET"])
def saudacao():
    return {"msg":"Bem-Vindo ao meu servidor"}

@app.route("/cadastro-do-usuario", methods=["POST"])
def cadastro():
    body = request.get_json()
    
    if("nome" not in body):
        return Resposta(400, "O nome é obrigatorio")

    if("cpf" not in body):
        return Resposta(400, "O cpf é obrigatorio")
    
    elif("email" not in body):
        return Resposta(400, "O email é obrigatorio")

    elif("senha" not in body):
        return Resposta(400, "O senha é obrigatorio")

    usuario = novoUsuario(body["nome"], body["cpf"], body["email"], body["senha"])

    print(body)

    return Resposta(200, "Usuario criado", "user" ,usuario), body

def Resposta(status, mensagem, nome=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome and conteudo):
        response[nome] = conteudo
    
    return response
app.run()

if __name__ == "__main__":
    app.run(debug=True)