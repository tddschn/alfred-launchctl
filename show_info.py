#!/usr/bin/env python3
"""show info about a plist file"""

import logging
from pathlib import Path
import sys
from typing import Any

# Workflow3 supports Alfred 3's new features. The `Workflow` class
# is also compatible with Alfred 2.
from workflow import Workflow3, ICON_WARNING, ICON_WEB, PasswordNotFound, ICON_INFO, Variables
from workflow.background import run_in_background, is_running
import plistlib, argparse, os


def main(wf: Workflow3):
    plist_path = os.getenv('plist_path', '')
    d: dict[str, Any] = plistlib.loads(Path(plist_path).read_bytes())
    for k, v in d.items():
        if isinstance(v, list):
            v = ' '.join(v)
        v = str(v)
        wf.add_item(k, v, valid=True, arg=v)
    wf.send_feedback()


if __name__ == '__main__':
    # Create a global `Workflow3` object
    wf = Workflow3()
    # Call your entry function via `Workflow3.run()` to enable its
    # helper functions, like exception catching, ARGV normalization,
    # magic arguments etc.
    sys.exit(wf.run(main))