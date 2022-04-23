from server.target.models.jobs import Job


def get_job_by_id(id: int) -> Job:
    """
    Return single job has a same id
    """
    try:
        return Job.objects.get(id = id)
    except:
        return None

def get_jobs_based_on_job_seeker(id: int) -> Job:
    """
    Return list of jobs based on job seeker id
    """
    try:
        return Job.objects.filter(applied_users__in = [id])
    except:
        return None

def get_jobs_based_on_employer(id: int) -> Job:
    """
    Return list of jobs based on job seeker id
    """
    try:
        return Job.objects.filter(company__id = id)
    except:
        return None