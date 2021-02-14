import sys
import requests
import time
from .export_json import jsonToCsv


# When the status code (429) occurs, sleep 60 then retry the request.
# When the status code (500) occurs, raise the exception system exit.
def getOffers(api_endpoint: str, auth_token: str, retyable: bool = True, sleep: int = 60, timeout: int = 2) -> dict:
    while True:
        try:
            r = requests.get(api_endpoint, headers={
                "Authorization": "Bearer " + auth_token}, timeout=timeout)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as e:
            if r.status_code == 429:
                if retyable == True:
                    time.sleep(sleep)
            elif r.status_code == 500:
                raise SystemExit(e)
            else:
                raise e
        except Exception as e:
            raise e
        if not retyable:
            return None


def exportOffersToCsv(offers: dict, filename: str = 'offers.csv') -> bool:
    try:
        rows = offers['rows']
        jsonToCsv(rows, filename=filename)
        return True
    except Exception as e:
        raise e
