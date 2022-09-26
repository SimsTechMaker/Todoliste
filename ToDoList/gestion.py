from . import model

def commit():
    model.db.session.commit()
    

def add_theme(nom_theme):
    model.db.session.add(model.Theme_tache(nom_theme))
    commit()

def add_tache (descrip, id_theme, prio =0):
    th = model.Tache(descrip,prio)
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
    # ! FAIRE LA LOGIQUE POUR LA MAJ DE LA PRIORISATION 
    model.db.session.query(model.Tache).filter_by(id=id_tache).update({"description":valeur})
    commit()

def get_theme(id_theme):
    #theme = model.db.session.query(model.Theme_tache).filter_by(id=id_theme)
    #theme.filter_by(id=id_theme)
    return model.db.session.query(model.Theme_tache.nom_theme).filter_by(id=id_theme)[0]

def get_tache(id_tache):
    
    return model.db.session.query(model.Tache).filter_by(id=id_tache)
    
add_theme("Menage")

add_tache("faire la lessive",2,65)

add_theme("Coder")
add_tache("faire du pythion",3,25)

add_theme("Vie")
add_tache("diva avec les combie",4,258)
add_tache("diva avec ma nga",4,550)
add_tache("diva avec tout le monde",4,687)
print("iiiiiiiiicicic")
g =get_theme(1)
gt =get_tache(1)
print(g[0])

print(gt[0])
 