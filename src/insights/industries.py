from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them.

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    files_reader = read(path)
    unique_industry = set()
    for file in files_reader:
        industries = file["industry"]
        if industries != '':
            unique_industry.add(industries)
    return unique_industry


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    filter_industry = [
        job_type for job_type in jobs if job_type['industry'] == industry
    ]
    return filter_industry
