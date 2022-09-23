
def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "lastname": item["lastname"],
        "dni": item["dni"],
        "email": item["email"],
        "password": item["password"]
        
    }
    
def usersEntity(entity) -> list:
    return [userEntity(i) for i in entity]