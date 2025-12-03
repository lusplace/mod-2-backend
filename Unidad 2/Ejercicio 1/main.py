from dotenv import load_dotenv
import os

load_dotenv()

STATE_KEY = "spotify_auth_state"
CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
URI = os.environ["SPOTFY_URI"]
REDIRECT_URI = URI + "/callback"

HOST = os.environ["MYSQL_HOST"]
ROOT_USER = os.environ["MYSQL_ROOT_USER"]
ROOT_PW = os.environ["MYSQL_ROOT_PASSWORD"]
DB = os.environ["MYSQL_DATABASE"]
DB_PORT = os.environ["MYSQL_PORT"]
DB_NAME = os.environ["MYSQL_DATABASE"]

from typing import Annotated

from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select

#USERS
class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    mail : str = Field(index=True)
    full_name : str | None = Field(index=True)
    user_disabled : bool = True

    def __init__(self, id, username, mail, full_name, user_disabled = True):
        self.id = id
        self.username = username
        self.mail = mail 
        self.full_name = full_name
        self.user_disabled = user_disabled
    #pw: str

class UserBase(BaseModel):
    username : str
    mail : str
    full_name : str | None

class UserUpdate(BaseModel):
    username: str | None
    mail : str | None
    full_name : str | None
    user_disabled : bool | None

#DB CONNECTION

import mysql.connector

db_conn = None

def get_connection(db = db_conn, 
        host: str = HOST, 
        port: int = DB_PORT, 
        user: str = ROOT_USER, 
        password: str = ROOT_PW, 
        database: str = DB_NAME):
    if db is None:
        db = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
    return db

def __exit__(self):
    if  db_conn is not None:
        db_conn.close()

#APP
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()

@app.on_event("startup")
def on_startup():
    db_conn = get_connection()
    sql = '''
        CREATE TABLE IF NOT EXISTS users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            mail VARCHAR(255) NOT NULL,
            full_name VARCHAR(255),
            user_disabled BOOLEAN NOT NULL DEFAULT 1
    );'''
    db_conn.cursor().execute(sql)
    db_conn.commit()
    db_conn.close()


#CREATE
@app.post("/users/add")
async def add_user(user: UserBase):

    user_dict = user.dict()
    username = user_dict['username']
    mail = user_dict['mail']
    full_name = user_dict['full_name']
    
    db_conn = get_connection()

    sql = "INSERT INTO users (username, mail, full_name) VALUES (%s, %s, %s)"
    val = (username, mail, full_name)

    db_conn.cursor().execute(sql, val)

    db_conn.commit()

    return JSONResponse(content=f"User {username} inserted successfully", status_code=201)

#READ
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    if user_id < 0: 
        return JSONResponse(content=f"Wrong Request", status_code=403)   
    db_conn = get_connection()
    sql = f"SELECT * FROM users WHERE user_id = {user_id}"

    cursor = db_conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()

    if not result:
        raise HTTPException(status_code=200, detail="User not found")
    db_conn.close()
    return JSONResponse(content=result, status_code=200)

@app.get("/users")
async def get_users():
   
    db_conn = get_connection()
    sql = f"SELECT * FROM users"

    cursor = db_conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    
    if not result:
        raise HTTPException(status_code=404, detail="Users not found")
    db_conn.close()
    return JSONResponse(content=result, status_code=200)

#UPDATE
##PUT
@app.put("/users/update/{user_id}")
async def add_user(user: UserUpdate, user_id : int):
    if user_id < 0: 
        return JSONResponse(content=f"Wrong Request", status_code=403)
    user_dict = user.dict()

    username = user_dict['username']
    mail = user_dict['mail']
    full_name = user_dict['full_name']
    user_disabled = user_dict['user_disabled']
    
    if (not username or len(username) == 0) or (not mail or len(mail) == 0) or (user_disabled is None):
        return JSONResponse(content=f"username, mail and user_disabled cannot be null", status_code=422)

    db_conn = get_connection()

    sql = f'''UPDATE users SET username = "{username}", mail="{mail}", full_name="{full_name}", user_disabled={user_disabled}
        WHERE user_id = {user_id}'''
    print(sql)
    db_conn.cursor().execute(sql)

    db_conn.commit()

    return JSONResponse(content=f"User {username} updated successfully", status_code=201)

##PATCH
@app.patch("/users/partial-update/{user_id}")
async def add_user(user: UserUpdate, user_id : int):
    if user_id < 0: 
        return JSONResponse(content=f"Wrong Request", status_code=403)
    user_dict = user.dict()

    username = user_dict['username']
    mail = user_dict['mail']
    full_name = user_dict['full_name']
    user_disabled = user_dict['user_disabled']
    
    keyValPairs = ""
    if(username is not None and len(username) > 0):
        keyValPairs += f"username = '{username}', " 
    if(mail is not None and len(mail) > 0):
        keyValPairs += f"mail = '{mail}', " 
    if(full_name is not None and len(full_name) > 0):
        keyValPairs += f"full_name = '{full_name}', " 
    if(user_disabled is not None):
        keyValPairs += f"user_disabled = {user_disabled}  " 
    if len(keyValPairs) > 2:
        keyValPairs = keyValPairs[:len(keyValPairs)-2]

    if len(keyValPairs) < 3:
        return JSONResponse(content=f"username, mail and user_disabled cannot be null", status_code=422)

    db_conn = get_connection()

    sql = f"UPDATE users SET {keyValPairs} WHERE user_id = {user_id}"
    print(sql)
    db_conn.cursor().execute(sql)

    db_conn.commit()

    return JSONResponse(content=f"User {username} updated successfully", status_code=201)

#DELETE
@app.delete("/users/delete/{user_id}")
async def get_user(user_id: int):
    if user_id < 0: 
        return JSONResponse(content=f"Wrong Request", status_code=403)
   
    db_conn = get_connection()
    sql = f"DELETE FROM users WHERE user_id = {user_id}"

    cursor = db_conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    db_conn.commit()
    db_conn.close()
    return JSONResponse(f"user with id {user_id} deleted", status_code=200)
