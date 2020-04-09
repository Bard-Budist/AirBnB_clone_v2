#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os.path


def do_pack():
    """dawdawd"""
    now = datetime.now()
    string = now.strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    name_file = "web_static_" + string + ".tgz"
    local("tar -cvzf versions/" + name_file + " web_static")
    if os.path.isfile("versions/" + name_file):
        print("web_static packed: {} -> {}".format(
            "versions/" + name_file,
            os.path.getsize("versions/" + name_file)
        ))
    else:
        return None
