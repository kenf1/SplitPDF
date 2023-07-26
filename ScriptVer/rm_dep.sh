#!bin/bash

echo "Script to remove dependencies for auto-py-to-exe"
python3 -m pip uninstall whichcraft bottle altgraph zope.interface zope.event pyinstaller-hooks-contrib macholib greenlet future pyinstaller gevent gevent-websocket bottle-websocket Eel auto-py-to-exe
echo "Completed"