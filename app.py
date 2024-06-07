from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session
import schemas
import models

models.Base.metadata.create_all(bind=models.engine)

app = FastAPI()

@app.post("/phonepost", response_model=schemas.PhoneBase)
async def create_product(pro :schemas.PhoneBase,  db: Session=Depends(models.get_db)):
    new_pro = models.ForPhone(**pro.dict())
    db.add(new_pro)
    db.commit()
    db.refresh(new_pro)
    return new_pro

@app.put("/phoneget", response_model=schemas.PhoneBase)
async def phone_put(phone_id: int, pro: schemas.PhoneBase, db: Session = Depends(models.get_db)):
    phone = db.query(models.ForPhone).filter(models.ForPhone.id == phone_id).first()
    if phone is None:
        raise HTTPException(status_code=404, detail="sorry phone not found")
    for key, value in pro.dict().items():
        setattr(phone, key, value)
    db.commit()
    db.refresh(phone)
    return phone

@app.delete("/phone/{phone_id}")
async def phone_del(phone_id: int, db: Session = Depends(models.get_db)):
    del_phone = db.query(models.ForPhone).filter(models.ForPhone.id == phone_id).first()
    if del_phone is None:
        raise HTTPException(status_code=404, detail="sorry phone not found")
    db.delete(del_phone)
    db.commit()
    return f"Deleted Successfully - ID - {phone_id}"


@app.get("/phoneget", response_model=list[schemas.PhoneBase])
async def phone_get(db:Session= Depends(models.get_db)):
    getting = db.query(models.ForPhone).all()
    return getting

@app.get("/phoneget/{phone_id}", response_model=schemas.PhoneBase)
async def Get_By_Id(phone_id : int, db: Session= Depends(models.get_db)):
    get_id = db.query(models.ForPhone).filter(models.ForPhone.id == phone_id).first()
    if get_id is None:
        raise HTTPException(status_code=404, detail="sorry product not found")
    return get_id



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port= 5000)