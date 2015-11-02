from app.Resources.hub import *
from app import *

api.add_resource(HubListResource, '/hubs', endpoint='hubs')
api.add_resource(HubResource, '/hubs/<id>', endpoint='hub')
