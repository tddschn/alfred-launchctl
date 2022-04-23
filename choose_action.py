#!/usr/bin/env python3
"""choose a launchctl action"""

from workflow import Workflow3, ICON_WARNING, ICON_WEB, PasswordNotFound
import os
from choose_plist import get_query

commands = [
    'load', 'unload', 'reload', 'start', 'stop', 'restart', 'enable', 'disable'
]


def main(wf: Workflow3) -> None:
    query = get_query(wf)
    plist_path = os.getenv('plist_path', '')
    global commands
    if query:
        commands = wf.filter(query, commands, key=lambda x: x, min_score=20)

    for command in commands:
        wf.add_item(
            command,
            f'launchctl {command} {plist_path}',
            arg=command,
            valid=True,
        )
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow3()
    wf.run(main)
