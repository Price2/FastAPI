
from fastapi import Depends, HTTPException, APIRouter
from models import Category, CategoryInput, CategoryOutput
from db import get_session
from sqlmodel import Session, select
from fastapi.responses import JSONResponse





router = APIRouter(prefix="/api/categories")






@router.post("/categories", status_code=201)
def add_category( category: CategoryInput, session: Session = Depends(get_session)) -> JSONResponse :
    new_category = Category.from_orm(category)
    session.add(new_category)
    session.commit()
    session.refresh(new_category)
    return JSONResponse({"success": True, "results":{}}, status_code=201)



@router.get("/", status_code=201)
def get_categories(id:int|None=None ,name: str | None = None, 
                   session: Session = Depends(get_session)):
    
    query = select(Category)
    
    if id:
        query = query.where(Category.id == id)

    if name:
        query = query.where(Category.name == name)

    results = session.exec(query).all()

    return {"success": True, "results": results}


