# models.py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    founding_year = Column(Integer)

    # Relationship: a company has many freebies
    freebies = relationship("Freebie", back_populates="company")

    # Will implement these later:
    # def devs(self): ...
    # def give_freebie(self, dev, item_name, value): ...
    # @classmethod
    # def oldest_company(cls, session): ...

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Relationship: a dev has many freebies
    freebies = relationship("Freebie", back_populates="dev")

    # Will implement these later:
    # def companies(self): ...
    # def received_one(self, item_name): ...
    # def give_away(self, dev, freebie): ...

class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    value = Column(Integer)

    # Foreign keys
    company_id = Column(Integer, ForeignKey('companies.id'))
    dev_id = Column(Integer, ForeignKey('devs.id'))

    # Relationships
    company = relationship("Company", back_populates="freebies")
    dev = relationship("Dev", back_populates="freebies")

    # Will implement this later:
    # def print_details(self): ...
