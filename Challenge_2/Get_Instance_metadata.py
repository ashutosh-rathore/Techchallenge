import requests
import json

instance_metadata_url = 'http://169.254.169.254/latest/'


def metadata_dict(md_url, md_list):
    md_output = {}
    for i in md_list:
        next_url = md_url + i
        req = requests.get(next_url)
        txt = req.text
        if i[-1] == "/":
            split_list_values = req.text.splitlines()
            md_output[i[:-1]] = metadata_dict(next_url, split_list_values)
        elif check_json(txt):
            md_output[i] = json.loads(txt)
        else:
            md_output[i] = txt
    return md_output


def get_instance_metadata():
    path = ["meta-data/"]
    result = metadata_dict(instance_metadata_url, path)
    return result


def get_instance_metadata_json():
    metadata = get_instance_metadata()
    metadata_json = json.dumps(metadata, indent=4, sort_keys=True)
    return metadata_json


def check_json(thisjson):
    try:
        json.loads(thisjson)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    print(get_instance_metadata_json())