#!/usr/bin/env python3

import logging
from pathlib import Path
import sys

# Workflow3 supports Alfred 3's new features. The `Workflow` class
# is also compatible with Alfred 2.
from workflow import Workflow3, ICON_WARNING, ICON_WEB, PasswordNotFound, ICON_INFO
from workflow.background import run_in_background, is_running
import plistlib, argparse


def get_plist_paths(
    plist_dir: Path | str = Path('~/Library/LaunchAgents').expanduser(),
) -> list[Path]:
    """
    Get a list of plist paths in a given directory.
    """
    plist_dir = Path(plist_dir).expanduser()
    return [p for p in plist_dir.glob('*.plist') if p.exists()]


def plist_path_to_label(plist_path: Path) -> str:
    """
    Get the label from the plist file
    """
    plist = plistlib.loads(plist_path.read_bytes())
    return plist['Label']


def get_query(wf) -> str | None:
    if len(wf.args):
        query = wf.args[0]
    else:
        query = None
    return query


def main(wf: Workflow3):
    # logger, query, plistdir
    logger = wf.logger
    logger.setLevel(logging.INFO)

    cache_name = 'plist_paths'
    plist_paths: list[Path] | None = wf.cached_data(
        cache_name, get_plist_paths, max_age=2
    )

    # # filtering
    query = get_query(wf)
    if query and plist_paths:
        plist_paths = wf.filter(query, plist_paths, key=lambda x: x.name, min_score=20)

    # if got 0 results
    if not plist_paths:
        wf.add_item('No matching plist file found', icon=ICON_WARNING)
        wf.send_feedback()
        return 0

    for plist_path in plist_paths:
        wf.add_item(
            plist_path_to_label(plist_path),
            plist_path.name,
            quicklookurl=plist_path.as_uri(),
            arg=str(plist_path),
            valid=True,
        )

    wf.send_feedback()


if __name__ == '__main__':
    # Create a global `Workflow3` object
    wf = Workflow3()
    # Call your entry function via `Workflow3.run()` to enable its
    # helper functions, like exception catching, ARGV normalization,
    # magic arguments etc.
    sys.exit(wf.run(main))
