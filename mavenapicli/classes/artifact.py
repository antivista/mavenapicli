class Artifact:
    '''
        A class to represent a Maven artifact
    '''
    def __init__(self, artifact_id, group_id, version_date_map={}):
        '''
        Parameters
        ----------
        artifact_id -> str
        group_id -> str
        version_date_map -> dict<str: str>
            keys are the versions, values are the dates
        '''
        self.artifact_id = artifact_id
        self.group_id = group_id
        self.version_date_map = version_date_map
