# alfred-launchctl

A simple Alfred Workflow for managing `launchd` jobs.

- [alfred-launchctl](#alfred-launchctl)
	- [What does this workflow do?](#what-does-this-workflow-do)
	- [Demo](#demo)
	- [Install](#install)
## What does this workflow do?

- Get a list of `*.plist` files in `~/Library/LaunchAgents` and let you choose one to act on;
- Let you choose a `launchctl` to run on the selected plist file;
- Display a notification after running the command.

## Demo

https://user-images.githubusercontent.com/45612704/164894524-0bcd2546-73c4-4238-a2ef-e69c61c42de0.mp4

## Install
- Step 1: `brew install python@3.10`, or point the python path in the workflow to your python3 installation.
- Step 2: Download the latest workflow release [here](https://github.com/tddschn/alfred-launchctl/releases/download/1.0.0/launchctl.alfredworkflow) and open it.

Enjoy!

## Usage
- The default keyword trigger is `laup`
- Press <kbd>shift</kbd> on the plist for preview
- Supported launchctl actions: `'load', 'unload', 'reload', 'start', 'stop', 'restart', 'enable', 'disable'`, where `reload` = `unload` + `load` and `restart` = `reload` + `start`.
    `
