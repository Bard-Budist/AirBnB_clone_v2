#!/usr/bin/python3
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
        run("mkdir -p /data/web_static/releases/" + name)
        run(
            "tar -xzf /tmp/" +
            name + ".tgz -C /data/web_static/releases/"
            + name)
        run("rm /tmp/" + name + ".tgz")
        run("rm -rf /data/web_static/current")
        run(
            "ln -s /data/web_static/releases/"
            + name + " /data/web_static/current")
        print("New version deployed!")
        return True
    else:
        return False
