from AcademicSystem.route.CriaBanco import crairBancoBlueprint

def resgister_blueprint(app):
    app.register_blueprint(crairBancoBlueprint)