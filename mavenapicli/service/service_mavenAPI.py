import requests
import urllib
import mavenapicli.utils.utils as utils


class MavenAPI:
    '''
    A service used to make requests to the Maven's API
    '''
    def __init__(self):
        self.base_url = 'https://search.maven.org/'


    def retrieve_artifact_full_response(self, artifact):
        '''
        Retrieve all the details of a specified artifact and return them as JSON
        '''
        api_endpoint = self.base_url + 'solrsearch/select'
        params = {'q': 'g:' + artifact.group_id + ' AND a:' + artifact.artifact_id, \
            'core': 'gav', 'rows': '10', 'wt': 'json'}
        params = urllib.parse.urlencode(params)
        response = requests.get(api_endpoint, params=params) 
        json_response = response.json()
        return json_response


    def get_artifact_version_date_map(self, artifact):
        '''
        Retrieve all the details of a specified artifact
        Returns a dict having as keys the versions and as values the dates

        Parameters
        ----------
        artifact -> Artifact
            it must have not None values for group_id and artifact_id
        '''
        artifact_details = self.retrieve_artifact_full_response(artifact=artifact)
        artifacts = artifact_details['response']['docs']
        artifact_version_date_map = {}
        for artifact in artifacts:
            ymd_date = utils.from_time_in_millis_to_ymd_date(timestamp_in_millis=artifact['timestamp'])
            artifact_version_date_map[artifact['v']] = ymd_date

        return artifact_version_date_map
