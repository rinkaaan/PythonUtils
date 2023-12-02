import os
import subprocess


def run_command(command, verbose=False):
    if verbose:
        run_command(command)
    else:
        subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def rename_at_root(root, old, new):
    os.rename(os.path.join(root, old), os.path.join(root, new))
