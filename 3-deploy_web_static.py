#!/usr/bin/python3
"""Generate .tgz archive."""


from fabric.api import local, env, put, run
from datetime import datetime
import os


env.hosts = ['52.3.244.39', '100.26.244.124']


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


def do_deploy(archive_path):
    """
    Distribute an archive to your web servers.

    args:
        archive_path: path to the archive file
    Returns:
        True if success, false otherwise

    """
    if not os.path.exists(archive_path):
        return False
    put(archive_path, "/tmp")
    dirName = archive_path.split('/')[1].split('.')[0]
    run("mkdir -p /data/web_static/releases/{}".format(dirName))
    archiveName = archive_path.split('/')[1]
    run("tar -xzf /tmp/{} -C"
        " /data/web_static/releases/{}/".format(archiveName, dirName))
    run("rm /tmp/{}".format(archiveName))
    run("mv /data/web_static/releases/{}/web_static/*"
        " /data/web_static/releases/{}/".format(dirName, dirName))
    run("rm -rf /data/web_static/releases/{}/web_static".format(dirName))
    run("rm -rf /data/web_static/current")
    run("ln -s /data/web_static/releases/{}/"
        " /data/web_static/current".format(dirName))
    return True


def deploy():
    """Create and distributes an archive to your web servers."""
    archiveFilePath = do_pack()
    if not archiveFilePath:
        return False
    return do_deploy(archiveFilePath)
