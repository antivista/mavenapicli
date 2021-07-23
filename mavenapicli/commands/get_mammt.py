import click
import requests
import urllib
from mavenapicli.service.service_mavenAPI import Artifact
from mavenapicli.service.service_mavenAPI import MavenAPI 
#import mavenapicli.service.service_artifact as svc_artifact

@click.group()
def cli():
    '''mammt HERE'''
    pass

@click.command()
@click.argument('name1')
@click.argument('name2')
def pat_t(name1, name2):
    '''pat t'''
    click.echo(f"uffa {name1} e {name2}")
    pass


@click.command()
@click.argument('artifact_id')
@click.argument('group_id')
def frat_t(artifact_id, group_id):
    '''frat t'''
    maven_API = MavenAPI()
    artifact = Artifact(artifact_id=artifact_id, \
        group_id=group_id)
    maven_API.get_artifact_versions(artifact=artifact)
    click.echo(f"uffa2 {artifact_id} e {group_id}")
    pass


cli.add_command(frat_t)
cli.add_command(pat_t)

'''
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
        payload = {'q': 'g:' + artifact.artifact_id + ' AND a:' + artifact.group_id, \
            'core': 'gav', 'rows': '10', 'wt': 'json'}
        print(payload)
        payload = urllib.parse.urlencode(payload)
        response = requests.get(api_endpoint, params=payload) 
        print(response.status_code)     # To print http response code  
        print(response.text)
'''        