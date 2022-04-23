#!/usr/bin/env python3

import subprocess
import os

plist_path = os.getenv('plist_path', '')
command = os.getenv('command', '')


def main() -> None:
    if command == 'load':
        subprocess.call(['launchctl', 'load', plist_path])
    elif command == 'unload':
        subprocess.call(['launchctl', 'unload', plist_path])
    elif command == 'reload':
        subprocess.call(['launchctl', 'unload', plist_path])
        subprocess.call(['launchctl', 'load', plist_path])
    elif command == 'start':
        subprocess.call(['launchctl', 'start', plist_path])
    elif command == 'stop':
        subprocess.call(['launchctl', 'stop', plist_path])
    elif command == 'restart':
        subprocess.call(['launchctl', 'unload', plist_path])
        subprocess.call(['launchctl', 'load', plist_path])
        subprocess.call(['launchctl', 'start', plist_path])
    elif command == 'enable':
        subprocess.call(['launchctl', 'enable', plist_path])
    elif command == 'disable':
        subprocess.call(['launchctl', 'disable', plist_path])
    print(f'launchctl {command} {plist_path}')


if __name__ == '__main__':
    main()
