import requests
import urllib

class Artifact:
    def __init__(self, artifact_id, group_id):
        self.artifact_id = artifact_id
        self.group_id = group_id


class MavenAPI:
    def __init__(self):
        self.base_url = 'https://search.maven.org/'

    def get_artifact_versions(self, artifact):
        api_endpoint = self.base_url + 'solrsearch/select'
        print('artifact_id', artifact.artifact_id)
        payload = {'q': 'g:' + artifact.group_id + ' AND a:' + artifact.artifact_id, \
            'core': 'gav', 'rows': '10', 'wt': 'json'}
        payload = urllib.parse.urlencode(payload)
        print(payload)
        response = requests.get(api_endpoint, params=payload) 
        print('URL ->', response.url)
        print(response.status_code)     # To print http response code  
        print(response.text)
