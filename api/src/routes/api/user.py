from typing import Any, List
import email
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
import schemas
    
router = APIRouter(
    prefix="/user", 
    tags=["User"]
    )

@router.post("/{id}", response_model=schemas.UserOut)
async def createUser(id: int, userIn: schemas.UserIn = Body()):
    user = userIn.dict()
    return {"id":id, "isActive":True, "isSuperUser":False, **user}
