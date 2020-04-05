from flask_restful import Resource, reqparse
from models.store import StoreModel


class Store(Resource):

    def get(Self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message" : "store not found"}


    def post(self, name):
        if StoreModel.find_by_name(name):
            return {"message" : f"a store with name {name} exists"}, 400

        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {"message" : "an error occured while inserting item"}, 500

        return store.json(), 201


    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {"message" : "store deleted"}
        return {"message" : "store not exists"}, 400


class StoreList(Resource):
    def get(self):
        return {"stores" : [store.json() for store in StoreModel.query.all()]}
