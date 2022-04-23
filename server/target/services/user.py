from server.target.models.user import Employer, User, JobSeeker


def get_user_by_email_for_login(email: str) -> User:
    """Return user who have the same email"""
    try:
        return User.objects.get(email=email)
    except:
        return None

def get_user_by_id(id: int) -> User:
    """Return user who have the same id"""
    try:
        return User.objects.get(id=id)
    except:
        return None

def get_job_seeker_by_id(id: int) -> JobSeeker:
    """Return job seeker who have the same id"""
    try:
        return JobSeeker.objects.get(id=id)
    except:
        return None

def get_employer_by_id(id: int) -> Employer:
    """Return employer who have the same id"""
    try:
        return Employer.objects.get(id=id)
    except:
        return None

def get_employer_by_email(email: str) -> Employer:
    """Return employer who have the same id"""
    try:
        return Employer.objects.get(email=email)
    except:
        return None
