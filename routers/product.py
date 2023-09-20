from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.exc import IntegrityError  # Import the IntegrityError class
from db import get_session
from models import Product, ProductInput, ProductOutPut
from sqlmodel import Session, select
from fastapi.responses import JSONResponse
import traceback


router = APIRouter(prefix="/api/products")



@router.get("/")
def get_products(name: str | None = None, price : int | None = None,
                 quantity : int | None = None, category_id: int | None = None ,session: Session = Depends(get_session)):
    query = select(Product)
    if name:
        query = query.where(Product.name == name)
    if price:
        query = query.where(Product.price == price)
    if quantity:
        query = query.where(Product.quantity == quantity)
    if category_id:
        query = query.where(Product.category_id == category_id)
    result = session.exec(query).all()
    return {"success": True, "results": result}



@router.get("/{id}")
def product_by_id(id: int, session: Session = Depends(get_session)) -> dict:
    product = session.get(Product, id)
    print(f"product retrieved: {product}")
    if product:
        return {'success': True, 'results': product}
    else:

        raise HTTPException(status_code=404, detail={"success": False, "results": {}, "message": f"No product with id={id}"})


@router.post("/", response_model=Product)
def create_product(product: ProductInput, session: Session = Depends(get_session)):
    new_prod = Product.from_orm(product)
    try:
        session.add(new_prod)
        session.commit()
        session.refresh(new_prod)
    except Exception as error:
        raise HTTPException(status_code=400, detail={"success":False, "results": {}, "message": f"An Error occured while creating product, check your configuration"})
    return JSONResponse({"success": True, "results": {}}, status_code=201)



@router.put("/{id}")
def update_product( id:int ,productInp: ProductInput, session: Session = Depends(get_session)):

    product = session.get(Product, id)

    if product:
        product.name = productInp.name
        product.price = productInp.price
        product.quantity = productInp.quantity
        product.imgURL = productInp.imgURL
        product.category_id = productInp.category_id
        try:
            session.commit()
            session.refresh(product)
            print(f"Product? {product}")
            return {"success": True, "results": product}
        except:
            raise HTTPException(status_code=400, detail={"success": False, "results": {} ,"message": f"Error updating product, please check your configuration"})
    raise HTTPException(status_code=404, detail={"success": False, "results": {} ,"message": f"No product with id={id}"})