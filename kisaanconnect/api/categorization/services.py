from . import models

def getCategories():
    categories = models.Category.objects.all()
    jsonout = []
    for c in categories:
        d={}
        d['id']=c.id
        d['name']=c.name
        d['description']=c.description
        d['picture']=c.picture.url
        jsonout.append(d)
    return jsonout

def getSubcategories(categoryid):
    categories = models.Category.objects.filter(id=categoryid)
    if len(categories)==0:
        return -1
    subcategories = models.Subcategories.objects.filter(category = categories[0])
    if len(subcategories)==0:
        return -2
    jsonout = []
    for c in subcategories:
        d={}
        d['id']=c.id
        d['name']=c.name
        d['description']=c.description
        d['picture']=c.picture.url
        jsonout.append(d)
    return jsonout


    
