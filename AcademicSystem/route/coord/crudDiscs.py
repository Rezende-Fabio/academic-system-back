from flask import Blueprint, Response, request
import json

import AcademicSystem.model.dao.DisciplinaDao as DiscDao

crudDiscBlueprint = Blueprint('crudDiscs', __name__)

@crudDiscBlueprint.route("/disciplinas")
def ReadDiscs():
    BODY = { "mensagem": "Algo deu errado" }

    try:
        DATA = DiscDao.LerDisciplinas()
        
        if DATA:
            return Response(json.dumps(DATA), status=200, mimetype='application/json')
        
        return Response(json.dumps(BODY), status=404, mimetype='application/json')
    except:
        return Response(json.dumps(BODY), status=500, mimetype='application/json')
    

@crudDiscBlueprint.route("/disciplinas/<id>", methods=["GET"])
def ReadDiscsPerId(id):
    BODY = { "mensagem": "Algo deu errado" }

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

    # print(requestBody['id'])

    return requestBody['id']



