from sqlmodel import SQLModel, Field


class ProductBase(SQLModel):
    """
    Base Product Model
    """

    name: str
    price: float


class Product(ProductBase, table=True):
    """
    Product Model used for db
    """

    id: int = Field(default=None, primary_key=True)


class ProductCreate(ProductBase):
    """
    Product model for creating database
    """

    pass
