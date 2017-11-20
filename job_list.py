
import logging
import json
import base64
import requests

log = logging.getLogger()
log.setLevel(logging.INFO)


def list(params):
    response = {
        "response_type": "in_channel",
        "text": "NOTHING"
    }

    config = json.loads(open("./config/jenkins-config.json").read())
    url = config['HOST'] + ':' + config['PORT'] + '/api/json'

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic " + base64.urlsafe_b64encode((config['USER'] + ':' + config['PASSWD']))
    }

    param = {'tree': 'jobs[name]'}

    jenkins_response = requests.get(url, headers=headers, params=param)

    if jenkins_response.status_code == 200:

        response['text'] = '--- \n'

        for job in jenkins_response.json()['jobs']:
            response['text'] += job['name']
            response['text'] += ' \n'
        response['text'] += '---'
    else:
        response['text'] = 'ERROR Request Jenkins'


    return response

