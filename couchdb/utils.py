from typing import List
from requests import Session


def get_uuids(url: str, session: Session, count: int = 10) -> List[str]:
    """
    Generate list of uuids that may be used as documents' _id fields
    :param session:
    :param url:
    :param count: Count of uuids that should be returned
    :return: List of uuids
    """
    uuids_url = url + f"_uuids?{count=}"
    response = session.get(uuids_url)
    return response.json()["uuids"]
