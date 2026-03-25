from datetime import datetime

def is_overdue(deadline):
    if not deadline:
        return False
    try:
        due_date = datetime.strptime(deadline, "%Y-%m-%d")
        return datetime.now() > due_date
    except:
        return False