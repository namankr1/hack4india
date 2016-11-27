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
    subcategories = models.Subcategory.objects.filter(category = categories[0])
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

def addCategories(name,description):
    category = models.Category(name = name, description = description)
    category.save()
    return 1;
def addSubCategories(name,description,categoryid):
	category = models.Category.objects.filter(id=categoryid)
	if len(category)==0:
		return -1
	subcategory = models.Subcategory(name = name, description = description, category = category[0])
	subcategories.save()
	return 1
