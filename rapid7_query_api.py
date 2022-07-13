import requests
import json
import time

def continue_request(req):
    if 'links' in req.json():
        continue_url = req.json()['links'][0]['href']
        new_response = make_request(continue_url)
        handle_response(new_response)


def handle_response(resp):
    response = resp
    print(response.status_code)
    if response.status_code == 200:
        print(json.dumps(resp.json(), indent=4))
        return
    if response.status_code == 202:
        continue_request(resp)
        return
    if response.status_code > 202:
        print('Error status code ' + str(response.status_code))
        return

def make_request(provided_url=None):
    headers = {'x-api-key': ''}

    url = "https://us.rest.logs.insight.rapid7.com/query/"
    if provided_url:
        url = provided_url
    req = requests.get(url, headers=headers)
    return req


def print_query():
    req = make_request()
    handle_response(req)

def start():
    print_query()


if __name__ == '__main__':
    start()