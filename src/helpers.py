import simplejson as json
from datetime import datetime
import yaml


def check_validation(sec_number, password, data):
    for i in data:
        if i.get("account_password") == password and i.get("social_security_number") == sec_number:
            return i
    return {"err": "There was no such account with provided password and SSN"}


def create_conf(path, sub_directory):
    if path:
        with open(path, 'r') as stream:
            try:
                parsed_yaml = yaml.safe_load(stream)
                return parsed_yaml.get(sub_directory) if sub_directory is not None else parsed_yaml
            except yaml.YAMLError as exc:
                print(exc)
    print("Path was not provided")
    return None


def convert_to_json(data):
    data = json.dumps(data, use_decimal=True, default=convert_datetime_to_string)
    return json.loads(str(data).replace("'", '"'))


def convert_datetime_to_string(o):
    if isinstance(o, datetime):
        return o.__str__()


def from_json_to_tuple(data):
    return tuple(data.values())
