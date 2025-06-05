import json
from typing import Any
import requests


def send_request(url: str, response_type: str) -> Any: 
    query = requests.get(url, timeout=60)
    res = None 

    if response_type == 'status-code':
        res = query.status_code
    
    match response_type:
        case 'status-code':
            res = query.status_code
        case 'json':
            res = json.dumps(query.json(), indent=4)
        case 'html':
            res = query.text

    return res
