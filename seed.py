# seed.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Company, Dev, Freebie

# Connect to the SQLite database
engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)
session = Session()

# Clear out existing data 
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()
session.commit()

#  Create sample companies
google = Company(name="Google", founding_year=1998)
microsoft = Company(name="Microsoft", founding_year=1975)
dukakit = Company(name="Dukakit", founding_year=2015)

# Create sample devs
enock = Dev(name="Enock")
zawadi = Dev(name="zawadi")
charlie = Dev(name="Charlie")

# Add companies and devs to the session
session.add_all([google, microsoft,dukakit, enock, zawadi, charlie])
session.commit()

# 5. Create sample freebies
f1 = Freebie(item_name="T-shirt", value=25, company=google, dev=enock)
f2 = Freebie(item_name="Sticker Pack", value=5, company=microsoft, dev=zawadi)
f3 = Freebie(item_name="Mug", value=15, company=dukakit, dev=charlie)
f4 = Freebie(item_name="Hoodie", value=50, company=google, dev=zawadi)
f5 = Freebie(item_name="Notebook", value=10, company=microsoft, dev=enock)

session.add_all([f1, f2, f3, f4, f5])
session.commit()

print("✅  Database with  Companies, Devs, and Freebies!")
 