# Maven API CLI
A cli tool that uses Maven's API to get info about Maven artifacts.

## Basic Requirements
* (Suggested) Python 3.9.6 version
* (Suggested) pip 21.1.3 version

## Installation
1. Put the project into an empty directory (working dir)
2. Create a Python virtual enviroment in the working dir and activate it
3. `pip install .`

To check installation run -> `mavenapicli <command>`\n

You should have the following output:
```
Usage: mavenapicli [OPTIONS] COMMAND [ARGS]...

  A CLI tool to perform basic operations with Maven API

Options:
  --help  Show this message and exit.

Commands:
  cmd_artifact_details  GET details about an artifact from Maven API
```

## Configuration
Modify `config.ini` to define:
* Max number of results to have making a request
* Log level

## Commands
* `cmd_artifact_detail` - Arguments: `ARTIFACT_ID` `GROUP_ID`
### Example
`mavenapicli cmd_artifact_details get-versions-dates maven-compiler-plugin org.apache.maven.plugins`

## Testing
Run -> `python3 -m unittest`
