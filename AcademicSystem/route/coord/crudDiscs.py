from flask import Blueprint, Response, request
import json

import AcademicSystem.model.dao.DisciplinaDao as DiscDao

BODY = { "mensagem": "Algo deu errado" }
crudDiscBlueprint = Blueprint('crudDiscs', __name__)

@crudDiscBlueprint.route("/disciplinas")
def ReadDiscs():
    try:
        DATA = DiscDao.LerDisciplinas()
        
        if DATA:
            return Response(json.dumps(DATA), status=200, mimetype='application/json')
        
        return Response(json.dumps(BODY), status=404, mimetype='application/json')
    except:
        return Response(json.dumps(BODY), status=500, mimetype='application/json')
    

@crudDiscBlueprint.route("/disciplinas/<id>", methods=["GET"])
def ReadDiscsPerId(id):
    try:
        DATA = DiscDao.LerDisciplinasPorID(id)

        if DATA:
            return Response(json.dumps(DATA), status=200, mimetype='application/json')
        
        return Response(json.dumps(BODY), status=404, mimetype='application/json')
    except:
        return Response(json.dumps(BODY), status=500, mimetype='application/json')


@crudDiscBlueprint.route('/addDisciplina', methods=["POST"])
def AddNewDisc():
    requestBody = request.get_json()

    try:
        DATA = DiscDao.CadastrarDisciplina(requestBody['sigla'], requestBody['nomeDisc'], requestBody['preReq1'], requestBody['preReq2'], requestBody['ativo'] ,requestBody['idCurso'])

        if DATA:
            resp = {
                "sigla": requestBody['sigla'], 
                "nomeDisc": requestBody['nomeDisc'], 
                "preReq1": requestBody['preReq1'], 
                "preReq2": requestBody['preReq2'],
                "ativo": requestBody['ativo'],
                "idCurso": requestBody['idCurso']
            }

            return Response(json.dumps(resp), status=200, mimetype='application/json')
        
        return Response(json.dumps(BODY), status=404, mimetype='application/json')

    except:
        return Response(json.dumps(BODY), status=500, mimetype='application/json')
    