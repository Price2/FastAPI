from sqlmodel import SQLModel, Field, Relationship



class ProductInput(SQLModel):
    name: str
    price: int
    quantity: int
    imgURL: str | None
    category_id : int



class Product (ProductInput, table=True):
    id: int | None = Field(default=None, primary_key=True)
    category_id : int = Field(foreign_key="category.id")
    category : "Category" = Relationship(back_populates="categories")



class ProductOutPut(ProductInput):
    id: int


class CategoryInput(SQLModel):
    name: str

class Category (CategoryInput, table=True):
    id: int | None = Field(default=None, primary_key=True)
    categories: list[Product] = Relationship(back_populates="category")

class CategoryOutput(CategoryInput):
    id: int
    categories: list[ProductOutPut] = []