# Freebie Tracker

A Freebie Tracker app using SQLAlchemy to track developer freebies  from companies.

Setup

1. Clone the repo
   ```bash
   git clone <your-github-url> freebie-tracker
   cd freebie-tracker
   ```

2. Install dependencies
   ```bash
   pipenv install
   pipenv shell
   ```

3. Run migrations
   ```bash
   alembic upgrade head
   ```

4. Seed the database
   ```bash
   python seed.py
   ```

5. Open the debug shell
   ```bash
   python debug.py
   ```

 Usage

Inside the debug shell you can run:

```python
# List all companies
session.query(Company).all()

# See Enock’s freebies
enock = session.query(Dev).filter_by(name="Enock").first()
enock.freebies

# Give a new freebie
google = session.query(Company).filter_by(name="Google").first()
fb = google.give_freebie(enock, "Sticker", 5)
session.add(fb)
session.commit()

# Print freebie details
print(fb.print_details())
```

 Files

- `models.py` – SQLAlchemy models and methods  
- `migrations/` – Alembic migration scripts  
- `seed.py` – Populate sample data  
- `debug.py` – IPython session for testing  

