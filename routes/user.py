from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.user import userEntity,usersEntity
from models.user import User
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT 

user = APIRouter()

@user.get('/users')
def find_all_users():
    return usersEntity(conn.local.user.find())

@user.post('/user')
def create_user(user: User):
    new_user = dict(user)
    del new_user["id"]
    
    id =conn.local.user.insert_one(new_user).inserted_id
    
    user = conn.local.user.find_one({"_id":id})
    return userEntity(user)

@user.get('/user/{dni}')
def find_user(dni:str):
    return userEntity(conn.local.user.find_one(
        {"dni": dni }))

@user.put('/user/{id}')
def update_user(id :str, user: User):
    userEntity(conn.local.user.find_one_and_update(
        {"_id": ObjectId(id)},{"$set":dict(user)}))
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))

@user.delete('/user/{dni}')
def delete_user(dni:str):
    userEntity(conn.local.user.find_one_and_delete(
        {"dni": dni}))
    return Response(status_code=HTTP_204_NO_CONTENT)
