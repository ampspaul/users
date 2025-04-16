from database import get_db_connection
from schema import User, UserResponse

#createUser
def createUser(user:User):
    conn =get_db_connection()
    cursor= conn.cursor()
    cursor.execute("INSERT INTO users (name,email) VALUES (?,?)",(user.name,user.email))
    conn.commit()
    user_id= cursor.lastrowid
    return UserResponse(id=user_id, name=user.name,email=user.email)
    

def listUsers():
    conn =get_db_connection()
    cursor= conn.cursor()
    cursor.execute("SELECT id,name,email from users")
    rows = cursor.fetchall()
    conn.close()
    return [ UserResponse(
        id=row["id"],
        name=row["name"],
        email=row["email"])
     for row in rows]
    
def getUser(userId):
    conn =get_db_connection()
    cursor =conn.cursor()
    cursor.execute("SELECT id,name, email from users where id=?",userId)
    row = cursor.fetchone()
    conn.close()
    return UserResponse(id=row["id"],name=row["Name"],email=row["email"])

    
def deteteUser(userId):
     conn = get_db_connection()
     cursor = conn.cursor()
     cursor.execute("DELETE FROM users where id=?",userId)
     conn.commit()
     conn.close()