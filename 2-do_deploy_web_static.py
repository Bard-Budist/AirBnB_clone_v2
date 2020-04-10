#!/usr/bin/python3
"""dawdawd"""
from fabric.api import *
import os.path

env.hosts = [
    "34.74.131.254",
    "18.215.154.76"
]


def do_deploy(archive_path):
    """Deploy"""
    if os.path.exists(archive_path):
        nameFile = archive_path.split('/')[1]
        put(archive_path, "/tmp/")
        name = os.path.splitext(nameFile)[0]
        sudo("mkdir -p /data/web_static/releases/" + name)
        sudo(
            "tar -xzf /tmp/" +
            name + ".tgz -C /data/web_static/releases/"
            + name)
        sudo("rm /tmp/" + name + ".tgz")
        sudo(
            "mv -f /data/web_static/releases/"
            + name
            + "/web_static/* /data/web_static/releases/"
            + name)
        sudo(
            "rm -rf /data/web_static/releases/"
            + name
            + "/web_static")
        sudo("rm -rf /data/web_static/current")
        sudo(
            "ln -s /data/web_static/releases/"
            + name + " /data/web_static/current")
        print("New version deployed!")
        return True
    else:
        return False
