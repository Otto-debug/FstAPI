from fastapi import FastAPI, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from . import models, schemas, database, utils, auth

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter_by(username=user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail='Username already exists')
    new_user = models.User(
        username=user.username,
        name=user.name,
        password_hash=utils.hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.reset(new_user)
    return {'msg': 'User registered'}

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter_by(username=user.username).first()
    if not db_user or not utils.verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = auth.create_access_token({"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}

@app.post('/connect-telegram')
def connect_telegram(data: schemas.TelegramConnect, authorization: str = Header(...), db: Session = Depends(get_db)):
    token = authorization.split(" ")[1]
    payload = auth.decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    username = payload["sub"]
    user = db.query(models.User).filter_by(username=username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.telegram_id = data.telegram_id
    db.commit()
    return {"msg": "Telegram ID connected"}
