from AcademicSystem.route.CriaBanco import criarBancoBlueprint
from AcademicSystem.route.coord.crudDiscs import crudDiscBlueprint
from AcademicSystem.route.aluno.RealizarInscricao import realizarInscricaoBlue

def resgister_blueprint(app):
    app.register_blueprint(criarBancoBlueprint)
    app.register_blueprint(crudDiscBlueprint)
    app.register_blueprint(realizarInscricaoBlue)