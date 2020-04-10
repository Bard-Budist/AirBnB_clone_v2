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
        p1 = put(archive_path, "/tmp/")
        name = os.path.splitext(nameFile)[0]
        p2 = sudo("mkdir -p /data/web_static/releases/" + name)
        p3 = sudo(
            "tar -xzf /tmp/" +
            name + ".tgz -C /data/web_static/releases/"
            + name)
        p4 = sudo("rm /tmp/" + name + ".tgz")
        p5 = sudo(
            "mv -f /data/web_static/releases/"
            + name
            + "/web_static/* /data/web_static/releases/"
            + name)
        p6 = sudo(
            "rm -rf /data/web_static/releases/"
            + name
            + "/web_static")
        p7 = sudo("rm -rf /data/web_static/current")
        p8 = sudo(
            "ln -s /data/web_static/releases/"
            + name + " /data/web_static/current")
        print("New version deployed!")
        ops = [p1, p2, p3, p4, p5, p6, p7, p8]
        return True
    else:
        return False
