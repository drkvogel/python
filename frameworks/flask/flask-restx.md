

>Flask-RESTX remains 100% compatible with Flask-RESTPlus’ API.

[How to set up a REST API in Flask in 5 steps - DEV Community ](https://dev.to/po5i/how-to-set-up-a-rest-api-in-flask-in-5-steps-5b7d)

[Scaling your project — Flask-RESTX 0.5.2.dev documentation ](https://flask-restx.readthedocs.io/en/latest/scaling.html#use-with-blueprints)
[Response marshalling — Flask-RESTX 0.5.2.dev documentation ](https://flask-restx.readthedocs.io/en/latest/marshalling.html)
>The idea of writing models is to use Flask-RESTX response marshalling, so no matter if our objects scale, the response will always be as we document it on our models. Flask-RESTX includes a lot of tools for this such as renaming attributes, complex, custom, and nested fields, and more.

[python - Flask-Restplus / route](https://stackoverflow.com/questions/32477878/flask-restplus-route)

[python - Returning rendered template with Flask-Restful shows HTML in browser](https://stackoverflow.com/questions/19315567/returning-rendered-template-with-flask-restful-shows-html-in-browser)



>The difference between the 2 different ways is, that:
>This one is "native" flask method, that you can use to wrap your functions with.
```py
@app.routing('/endpoint')
```
>This one is a part of the restful_flask package and it does the things in a different way than the native flask way.
```py
api.add_resource(CLASSNAME, endpoint)
```
>You can do the same stuff with both ways, but if you use the rest framework, then you should use the second method :)

```py
class CityModel():
    pass

class CitiesByNameAPI(Resource):
    def get(self, name_or_id):
        if name_or_id.isdigit():
            city = CityModel.find_by_id(name_or_id)
        else:
            city = CityModel.find_by_name(name_or_id)
        if city:
            return city.to_json(), 200
        return {'error': 'not found'}, 404

api.add_resource(CitiesByNameAPI, '/api/cities/<name_or_id>', endpoint = 'cities_by_name')
```
I guess the second form means you can put the classes somewhere else, (views.py?) and keep the routes in routes.py


do you have to make two classes - two Resources? - for each endpoint, single and plural?
In [Scaling your project — Flask-RESTX 0.5.2.dev documentation ](https://flask-restx.readthedocs.io/en/latest/scaling.html):
```py
@api.route('/')
class CatList(Resource):
    @api.doc('list_cats')
    @api.marshal_list_with(cat)
    def get(self):
        '''List all cats'''
        return CATS

@api.route('/<id>')
@api.param('id', 'The cat identifier')
@api.response(404, 'Cat not found')
class Cat(Resource):
    @api.doc('get_cat')
    @api.marshal_with(cat)
    def get(self, id):
        '''Fetch a cat given its identifier'''
        for cat in CATS:
            if cat['id'] == id:
                return cat
        api.abort(404)
```

[python - Combining multiple GET endpoints into a single resource](https://stackoverflow.com/questions/51967215/combining-multiple-get-endpoints-into-a-single-resource)
>Whole point of flask restfull is to separate resource from collections. I would suggest you to stay with creating one class for single resource (GET [one], PUT [update one], DELETE [remove one]) and other class for collection resource (GET [plural], POST [create new])

>The naming of your functions aside, you could probably do something like
```py
class Question(Resource):
    def get(self, user_id=0):
        if(user_id):
            return specific question
        return list of questions
```



[flask-restx or flask-restplus ns.doc](https://www.google.com/search?qie=UTF-8)
[python - How to document a flask-restplus response with list of strings](https://stackoverflow.com/questions/57332453/how-to-document-a-flask-restplus-response-with-list-of-strings)
[doc decorator](https://www.google.com/search?qie=UTF-8)
[Swagger documentation — Flask-RESTPlus 0.13.0 documentation ](https://flask-restplus.readthedocs.io/en/stable/swagger.html)
>The `api.doc()` decorator allows you to include additional information in the documentation. You can document a class or a method:
>The @api.response() decorator allows you to document the known responses and is a shortcut for @api.doc(responses='...').


Documenting the fields¶
Every Flask-Restplus field accepts optional arguments used to document the field:

required: a boolean indicating if the field is always set (default: False)
description: some details about the field (default: None)
example: an example to use when displaying (default: None)
...

my_fields = api.model('MyModel', {
    'name': fields.String(description='The name', required=True),
    'type': fields.String(description='The object type', enum=['A', 'B']),
    'age': fields.Integer(min=0),
})

[swagger - Why @api.doc decorator python flask restplus not update the changes I make?](https://stackoverflow.com/questions/54373759/why-api-doc-decorator-python-flask-restplus-not-update-the-changes-i-make)
[python - Working with flask restplus Namespace and blueprint](https://stackoverflow.com/questions/65243550/working-with-flask-restplus-namespace-and-blueprint)
[python - flask restful: how to document response body with fields.Dict()?](https://stackoverflow.com/questions/61376040/flask-restful-how-to-document-response-body-with-fields-dict)
