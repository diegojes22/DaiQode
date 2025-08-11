import os

def getScriptPath():
    return str(os.path.dirname(os.path.abspath(__file__)))

def getProjectPath():
    return str(os.path.dirname(getScriptPath()))