import click
from mavenapicli.services.service_mavenAPI import MavenAPI 
from mavenapicli.classes.artifact import Artifact 


@click.group()
def cli():
    '''
    GET details about an artifact from Maven API endpoint
    '''
    pass


@click.command()
@click.argument('artifact_id')
@click.argument('group_id')
def get_versions_dates(artifact_id, group_id):
    '''
    GET numbers of version and the related release dates of an artifact.

    Arguments
    ----------
    ARTIFACT_ID is the artifact's id 
    GROUP_ID is the group id where the artifact belongs to
    '''
    maven_API = MavenAPI()
    artifact = Artifact(artifact_id=artifact_id, group_id=group_id)
    artifact_version_date_map = maven_API.get_artifact_version_date_map(artifact=artifact)
    if artifact_version_date_map == {}:
        click.echo('This artifact has not versions, it may not exist or there is a typo in the ARTIFACT_ID or/and GROUP_ID passed.')
    else:        
        artifact.version_date_map = artifact_version_date_map
        click.echo(f'Artifact versions and related dates -> {artifact.__dict__}')


cli.add_command(get_versions_dates)
