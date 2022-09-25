from . import model

def commit():
    model.db.session.commit()
    

def add_theme(nom_theme):
    model.db.session.add(model.Theme_tache(nom_theme))
    commit()

def add_tache (descrip, id_theme):
    th = model.Tache(descrip)
    th.theme_key = id_theme
    model.db.session.add(th)
    commit()
    
def drop_theme(id_theme):
    model.db.session.query(model.Theme_tache).filter_by(id= id_theme).delete()
    commit()

def drop_tache(id_tache):
    model.db.session.query(model.Tache).filter_by(id= id_tache).delete()
    commit()

def update_theme(id_theme, valeur):
    model.db.session.query(model.Theme_tache).filter_by(id=id_theme).update({"nom_theme":valeur})
    commit()
    
def update_tache(id_tache, valeur):
    model.db.session.query(model.Tache).filter_by(id=id_tache).update({"description":valeur})
    commit()


    