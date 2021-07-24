from unittest import TestCase, mock
from mavenapicli.services.service_mavenAPI import MavenAPI
from mavenapicli.classes.artifact import Artifact 


class TestRetrieveArtifactFullResponse(TestCase):
    def setUp(self) -> None:
        return_value = {'responseHeader': {'status': 0, 'QTime': 1, 'params': {'q': 'g:org.apache.maven.plugins AND a:maven-compiler-plugin', 'core': 'gav', 'indent': 'off', 'fl': 'id,g,a,v,p,ec,timestamp,tags', 'start': '', 'sort': 'score desc,timestamp desc,g asc,a asc,v desc', 'rows': '10', 'wt': 'json', 'version': '2.2'}}, 'response': {'numFound': 24, 'start': 0, 'docs': [{'id': 'org.apache.maven.plugins:maven-compiler-plugin:3.8.1', 'g': 'org.apache.maven.plugins', 'a': 'maven-compiler-plugin', 'v': '3.8.1', 'p': 'maven-plugin', 'timestamp': 1556456271000, 'ec': ['-javadoc.jar', '-sources.jar', '.jar', '.pom', '-source-release.zip'], 'tags': ['project', 'compile', 'your', 'compiler', 'used', 'plugin', 'sources']}, {'id': 'org.apache.maven.plugins:maven-compiler-plugin:3.8.0', 'g': 'org.apache.maven.plugins', 'a': 'maven-compiler-plugin', 'v': '3.8.0', 'p': 'maven-plugin', 'timestamp': 1532625277000, 'ec': ['-sources.jar', '-javadoc.jar', '.jar', '-source-release.zip', '.pom'], 'tags': ['project', 'compile', 'your', 'compiler', 'used', 'plugin', 'sources']}, {'id': 'org.apache.maven.plugins:maven-compiler-plugin:3.7.0', 'g': 'org.apache.maven.plugins', 'a': 'maven-compiler-plugin', 'v': '3.7.0', 'p': 'maven-plugin', 'timestamp': 1504271064000, 'ec': ['-sources.jar', '-javadoc.jar', '.jar', '.pom', '-source-release.zip'], 'tags': ['project', 'compile', 'your', 'compiler', 'used', 'plugin', 'sources']}, {'id': 'org.apache.maven.plugins:maven-compiler-plugin:3.6.2', 'g': 'org.apache.maven.plugins', 'a': 'maven-compiler-plugin', 'v': '3.6.2', 'p': 'maven-plugin', 'timestamp': 1501024740000, 'ec': ['-sources.jar', '-javadoc.jar', '.jar', '-source-release.zip', '.pom'], 'tags': ['project', 'compile', 'your', 'compiler', 'used', 'plugin', 'sources']}, {'id': 'org.apache.maven.plugins:maven-compiler-plugin:3.6.1', 'g': 'org.apache.maven.plugins', 'a': 'maven-compiler-plugin', 'v': '3.6.1', 'p': 'maven-plugin', 'timestamp': 1484306345000, 'ec': ['-sources.jar', '-javadoc.jar', '.jar', '.pom', '-source-release.zip'], 'tags': ['project', 'compile', 'your', 'compiler', 'used', 'plugin', 'sources']}, {'id': 'org.apache.maven.plugins:maven-compiler-plugin:3.6.0', 'g': 'org.apache.maven.plugins', 'a': 'maven-compiler-plugin', 'v': '3.6.0', 'p': 'maven-plugin', 'timestamp': 1477512731000, 'ec': ['-sources.jar', '-javadoc.jar', '.jar', '-source-release.zip', '.pom'], 'tags': ['project', 'compile', 'your', 'compiler', 'used', 'plugin', 'sources']}, {'id': 'org.apache.maven.plugins:maven-compiler-plugin:3.5.1', 'g': 'org.apache.maven.plugins', 'a': 'maven-compiler-plugin', 'v': '3.5.1', 'p': 'maven-plugin', 'timestamp': 1454785461000, 'ec': ['-sources.jar', '-javadoc.jar', '.jar', '-source-release.zip', '.pom'], 'tags': ['project', 'compile', 'your', 'compiler', 'used', 'plugin', 'sources']}, {'id': 'org.apache.maven.plugins:maven-compiler-plugin:3.5', 'g': 'org.apache.maven.plugins', 'a': 'maven-compiler-plugin', 'v': '3.5', 'p': 'maven-plugin', 'timestamp': 1452982713000, 'ec': ['-sources.jar', '-javadoc.jar', '.jar', '.pom', '-source-release.zip'], 'tags': ['project', 'compile', 'your', 'compiler', 'used', 'plugin', 'sources']}, {'id': 'org.apache.maven.plugins:maven-compiler-plugin:3.3', 'g': 'org.apache.maven.plugins', 'a': 'maven-compiler-plugin', 'v': '3.3', 'p': 'maven-plugin', 'timestamp': 1427135299000, 'ec': ['-sources.jar', '-javadoc.jar', '.jar', '.pom', '-source-release.zip'], 'tags': ['project', 'compile', 'your', 'compiler', 'used', 'plugin', 'sources']}, {'id': 'org.apache.maven.plugins:maven-compiler-plugin:3.2', 'g': 'org.apache.maven.plugins', 'a': 'maven-compiler-plugin', 'v': '3.2', 'p': 'maven-plugin', 'timestamp': 1412786601000, 'ec': ['-javadoc.jar', '-sources.jar', '.jar', '-source-release.zip', '.pom'], 'tags': ['project', 'compile', 'your', 'compiler', 'used', 'plugin', 'sources']}]}}
        self.patcher = mock.patch('mavenapicli.services.service_mavenAPI.MavenAPI.retrieve_artifact_full_response', return_value=return_value)
        self.patcher.start()


    
    def test_check_json_response_type(self):
        '''
        Check if the response is in JSON format
        '''
        maven_API = MavenAPI()
        #artifact = Artifact(artifact_id='artifact_id', group_id='group_id')
        actual_result = maven_API.retrieve_artifact_full_response()
        self.assertIsInstance(actual_result, dict)



    def test_check_json_response_structure(self):
        '''
        Check that the fields used in the JSON response are present
        '''
        maven_API = MavenAPI()
        #artifact = Artifact(artifact_id='artifact_id', group_id='group_id')
        actual_result = maven_API.retrieve_artifact_full_response()
        self.assertIsNotNone(actual_result['response']['numFound'])
        self.assertIsNotNone(actual_result['response']['docs'])


    def tearDown(self) -> None:
        self.patcher.stop()
