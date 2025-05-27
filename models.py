from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    founding_year = Column(Integer)

    freebies = relationship("Freebie", back_populates="company")


class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    freebies = relationship("Freebie", back_populates="dev")


class Freebie(Base):
    __tablename__ = 'freebies'

    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    value = Column(Integer)

    company_id = Column(Integer, ForeignKey('companies.id'))
    dev_id = Column(Integer, ForeignKey('devs.id'))

    company = relationship("Company", back_populates="freebies")
    dev = relationship("Dev", back_populates="freebies")

    def print_details(self):
        print(f"{self.dev.name} owns a {self.item_name} from {self.company.name}")
