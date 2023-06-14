from AcademicSystem.route.CriaBanco import criarBancoBlueprint

def resgister_blueprint(app):
    app.register_blueprint(criarBancoBlueprint)