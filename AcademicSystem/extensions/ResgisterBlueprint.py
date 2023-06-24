from AcademicSystem.route.CriaBanco import criarBancoBlueprint
from AcademicSystem.route.coord.crudDiscs import crudDiscBlueprint

def resgister_blueprint(app):
    app.register_blueprint(criarBancoBlueprint)
    app.register_blueprint(crudDiscBlueprint)