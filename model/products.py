from sqlalchemy import Table, Column, Integer, String, Float
from config.db import engine, meta_data

products = Table("products", meta_data,
                 Column("id", Integer, primary_key=True),
                 Column("name", String(120), nullable=False),
                 Column("description", String(120), nullable=False),
                 Column("price", Float, nullable=False),
                 Column("stock", Integer, nullable=False),
                 Column("category", String(50), nullable=False))

meta_data.create_all(engine)