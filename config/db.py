from sqlalchemy import create_engine, MetaData

engine = create_engine("sqlite:///backend.db", echo=True)
meta_data = MetaData()

