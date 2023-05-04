#!/usr/bin/python3
"""Generate .tgz archive."""


from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generate .tgz using web_static's content."""
    if not os.path.exists("versions"):
        local("mkdir versions")
    ts = datetime.utcnow().strftime('%Y%m%d%H%M%S')
    fileName = "web_static_{}.tgz".format(ts)
    local("tar -cvzf versions/{} web_static".format(fileName))
    archiveFilePath = "versions/{}".format(fileName)
    if os.path.exists(archiveFilePath):
        return archiveFilePath
    return None
