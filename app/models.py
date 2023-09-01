# import os
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine, MetaData
# from sqlalchemy_utils import database_exists, create_database
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import Column, Integer, String
# from datetime import datetime

# main_dir = os.path.dirname(os.path.dirname(__file__))

# db_path = os.path.join(main_dir, "db", "prova.db")
# url = f"sqlite:///{db_path}"

# engine = create_engine(url, connect_args={"check_same_thread": False})
# Base = declarative_base()
# Session = sessionmaker(engine)
# session = Session()
# meta = MetaData()


# # Clases
# class Plantilla(Base):
#     __tablename__ = ("PLANTILLA",)
#     id = Column(Integer(), primary_key=True)
#     plantilla_id = Column(String())


# if not database_exists(engine.url):
#     # create_database(engine.url)
#     Base.metadata.create_all(engine)
# else:
#     # Connect the database if exists.
#     engine.connect()
