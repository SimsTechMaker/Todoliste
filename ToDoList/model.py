from flask_sqlalchemy import SQLAlchemy, BaseQuery
from .route import app
 
db = SQLAlchemy(app)
 
class Theme_tache(db.Model):
    __tablename__ = "Theme_tache"
    id = db.Column(db.Integer, primary_key=True)
    nom_theme = db.Column(db.String(50), nullable=False)

    tache = db.relationship("Tache",
                            backref = db.backref("Theme-tache", cascade='all, delete')
                            )
    
    def __init__(self, nom_theme) -> None:
        self.nom_theme = nom_theme
    def __str__(self) -> str:
        return self.nom_theme

class Tache(db.Model):
    __tablename__ = "Tache"
    id = db.Column(db.Integer, primary_key= True)
    theme_key = db.Column(db.Integer, db.ForeignKey("Theme_tache.id"))
    description = db.Column(db.String(500), nullable = False)
    priorite = db.Column(db.Integer)
    
    
    def __init__(self, description,prirorite=0) -> None:
        print(prirorite)
        self.description = description
        self.priorite = prirorite
    def __str__(self) -> str:
        return self.description
    
def init_db():
    db.drop_all()
    db.create_all()
    theme_init = Theme_tache("Defaut")
    db.session.add(theme_init)
    db.session.commit()
    
    tache_init = Tache("Bonjour ici nous sommes a l'initialisation de la tache")
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
    tache_init.theme_key = theme_init.id
    db.session.add(tache_init)
    db.session.commit()

init_db()
