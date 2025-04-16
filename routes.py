from fastapi import APIRouter, HTTPException
from schema import User
from typing import List
from database import get_db_connection
from schema import User, UserResponse
from services.users import createUser,listUsers,getUser,deteteUser

router = APIRouter()
print("Router....")
router.add_api_route("/user",createUser,response_model=UserResponse,methods=["POST"])
router.add_api_route("/users",listUsers,response_model=List[UserResponse],methods=["GET"])
router.add_api_route("/users/{userId}",getUser,response_model=UserResponse,methods=["GET"])
router.add_api_route("/users/{userId}",deteteUser,methods=["DELETE"])




