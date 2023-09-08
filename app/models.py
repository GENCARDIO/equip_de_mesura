import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Table
from datetime import datetime

main_dir = os.path.dirname(os.path.dirname(__file__))

db_path = os.path.join(main_dir, "app", "db", "fitxes_tecniques.db")
url = f"sqlite:///{db_path}"

engine = create_engine(url, connect_args={"check_same_thread": False})
Base = declarative_base()
Session = sessionmaker(engine)
session = Session()
meta = MetaData()


# Clases
class Fitxes(Base):
    __tablename__ = ("fitxes_tecniques")
    codi_aux = Column(String(), primary_key=True)
    codi_cgc = Column(String())
    descripcio = Column(String())
    fabricant = Column(String())
    ref_fabricant = Column(String())
    serial_number = Column(String())
    model = Column(String())
    emp_subministradora = Column(String())
    data_alta = Column(String())
    condicions_equip = Column(String())
    data_baixa = Column(String())
    situacio_contractual = Column(String())
    preu = Column(String())
    tipus = Column(String())
    amplada = Column(String())
    alçada = Column(String())
    profunditat = Column(String())
    pes = Column(String())
    condicions_ambientals = Column(String())
    humitat = Column(String())
    presa_aigua = Column(String())
    sai = Column(String())
    cont_comercial = Column(String())
    cont_tecnic = Column(String())
    observacions = Column(String())


if not database_exists(engine.url):
    # create_database(engine.url)
    Base.metadata.create_all(engine)
else:
    # Connect the database if exists.
    engine.connect()
