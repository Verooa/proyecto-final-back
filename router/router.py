from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy import select, update
from model.products import products
from config.db import engine
from schema.product_schema import ProductSchema, ProductInput

router = APIRouter()

@router.get("/api/products/{product_id}", response_model=ProductSchema, response_class=JSONResponse)
def get_product(product_id: int):
    with engine.connect() as conn:
        result = conn.execute(select(products).where(products.c.id == product_id)).first()
        if result:
            return result
        else:
            raise HTTPException(status_code=404, detail="Product not found")

@router.post("/api/products", response_model=ProductSchema, response_class=JSONResponse)
def create_product(product: ProductInput):
    with engine.connect() as conn:
        new_product = product.dict()
        result = conn.execute(products.insert().values(**new_product))
        conn.commit()  
        return {**new_product, "id": result.inserted_primary_key[0]}

@router.put("/api/products/{product_id}", response_model=ProductSchema, response_class=JSONResponse)
def update_product(product_id: int, product: ProductInput):
    with engine.connect() as conn:
        updated = conn.execute(
            products.update()
            .where(products.c.id == product_id)
            .values(
                name=product.name,
                description=product.description,
                price=product.price,
                stock=product.stock,
                category=product.category,
            )
        )
        conn.commit()  
        if updated.rowcount == 1:
            updated_product = conn.execute(select(products).where(products.c.id == product_id)).first()
            return updated_product
        else:
            raise HTTPException(status_code=404, detail="Product not found")

@router.delete("/api/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
    with engine.connect() as conn:
        deleted = conn.execute(products.delete().where(products.c.id == product_id))
        conn.commit()  
        if deleted.rowcount == 1:
            return
        else:
            raise HTTPException(status_code=404, detail="Product not found")
