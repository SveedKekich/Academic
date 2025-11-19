# Student Management Python Project

Layers:
- PL: Console UI (pl_console.py)
- BLL: Business Logic (bll.py)
- DAL: CSV File IO (dal.py)

Testing:
- pytest
- pytest-cov

Install dependencies:
    pip install -r requirements.txt

Run tests:
    pytest --cov=project --cov-report=term-missing
