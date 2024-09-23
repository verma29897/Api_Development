from fastapi import FastAPI,status,HTTPException
from  pydantic import BaseModel
from database import SessionLocal
import models
app=FastAPI()

db=SessionLocal()
class ourModel(BaseModel):
    class config:
        orm_mode=True

class Person(BaseModel):
    id:int
    first_name:str
    last_name:str
    isMale:bool
    
@app.get('/',response_model=list[Person],status_code=status.HTTP_200_OK)
def all_person():
    data=db.query(models.Person).all()
    return data

@app.get('/get_person/{person_id}',response_model=Person,status_code=status.HTTP_200_OK)
def getdata(person_id:int):
    data=db.query(models.Person).filter(models.Person.id == person_id).first()
    if data is not None:
        return data
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Person not found')

    
@app.post("/addpersoninfo",response_model=Person,status_code=status.HTTP_201_CREATED)
def addpersoninfo(person:Person):
    newperson=models.Person(
        id=person.id,
        first_name=person.first_name,
        last_name=person.last_name,
        isMale=person.isMale
        )
    find_person=db.query(models.Person).filter(models.Person.id==person.id).first()
    if find_person is not  None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="Person already exists")
        
    
    db.add(newperson)
    db.commit()
    return newperson

@app.put("/update_person/{person_id}",response_model=Person,status_code=status.HTTP_202_ACCEPTED)
def addpersoninfo(person_id:int,person:Person):
    find_person=db.query(models.Person).filter(models.Person.id==person_id).first()
    if find_person is not None:
        find_person.id=person.id
        find_person.first_name=person.first_name
        find_person.last_name=person.last_name
        find_person.isMale=person.isMale
        db.commit()
        return find_person
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Person not exist")
    
@app.delete("/delete_person/{person_id}",response_model=Person,status_code=200)
def  delete_person(person_id:int):
    find_person=db.query(models.Person).filter(models.Person.id==person_id).first()
    if  find_person is not None:
        db.delete(find_person)
        db.commit()
        return find_person
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Person not exist")

