#!/usr/bin/env python3
"""Distribute an archive to your webservers."""


from fabric.api import env, put, run
import os


env.hosts = ['52.3.244.39', '100.26.244.124']


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
    run(f"mkdir -p /data/web_static/releases/{dirName}")
    archiveName = archive_path.split('/')[1]
    run(f"tar -xzf /tmp/{archiveName} -C /data/web_static/releases/{dirName}/")
    run(f"rm /tmp/{archiveName}")
    run(f"mv /data/web_static/releases/{dirName}/web_static/*"
        f" /data/web_static/releases/{dirName}/")
    run(f"rm -rf /data/web_static/releases/{dirName}/web_static")
    run("rm -rf /data/web_static/current")
    run(f"ln -s /data/web_static/releases/{dirName}/ /data/web_static/current")
    return True
