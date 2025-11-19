# Student Management Python Project

Layers:
- PL: Console UI (pl_console.py)
- BLL: Business Logic (bll.py)
- DAL: CSV File IO (dal.py)

Testing:
- pytest
- pytest-cov
- 100% coverage required for Student logic

Install dependencies:
    pip install -r requirements.txt

Run tests:
    pytest --cov=project --cov-report=term-missing

CSV example:
last_name,first_name,course,student_id,gender,residence
Ivanenko,Olena,1,ST001,F,1.102
Petrov,Andriy,2,ST002,M,Kyiv
