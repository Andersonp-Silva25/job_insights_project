from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    files_reader = read(path)
    max_salary = 0
    for file in files_reader:
        salary = file["max_salary"]
        if salary != '' and salary != 'invalid':
            if int(salary) > max_salary:
                max_salary = int(salary)
                str(salary)
    return max_salary


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    files_reader = read(path)
    min_salary = get_max_salary(path)
    for file in files_reader:
        salary = file["min_salary"]
        if salary != '' and salary != 'invalid':
            if int(salary) < min_salary:
                min_salary = int(salary)
                str(salary)
    return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        converted_salary = int(salary)
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        if min_salary > max_salary:
            raise ValueError('min_salary cannot be bigger than max_salary')
    except (KeyError, TypeError, ValueError):
        raise ValueError('Values are empty, or not numeric')
    return max_salary >= converted_salary >= min_salary


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    validating_work_salaries = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                validating_work_salaries.append(job)
        except ValueError:
            print("Invalid Job")
    return validating_work_salaries
