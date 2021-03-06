#!/usr/bin/env python

# Sourced, with some modification, from
# https://github.com/seb-m/pyinotify/blob/master/python2/examples/autocompile.py

import subprocess
import sys
import pyinotify

class OnWriteHandler(pyinotify.ProcessEvent):
    def my_init(self, cwd, extension, cmd):
        self.cwd = cwd
        self.extensions = extension.split(',')
        self.cmd = cmd

    def _run_cmd(self):
        print('==> Modification detected')
        #subprocess.call(self.cmd.split(' '), cwd=self.cwd)
        subprocess.call(self.cmd, cwd=self.cwd, shell=True)

    def process_IN_MODIFY(self, event):
        if all(not event.pathname.endswith(ext) for ext in self.extensions):
            return
        self._run_cmd()

    def process_IN_CREATE(self, event):
        self.process_IN_MODIFY(event)

    def process_IN_DELETE(self, event):
        self.process_IN_MODIFY(event)

    def process_IN_MOVED_TO(self, event):
        self.process_IN_MODIFY(event)

    def process_IN_MOVED_FROM(self, event):
        self.process_IN_MODIFY(event)

def auto_compile(path, extension, cmd):
    wm = pyinotify.WatchManager()
    handler = OnWriteHandler(cwd=path, extension=extension, cmd=cmd)
    notifier = pyinotify.Notifier(wm, default_proc_fun=handler)
    wm.add_watch(path, pyinotify.ALL_EVENTS, rec=True, auto_add=True)
    print('==> Start monitoring {} (type c^c to exit)'.format(path))
    notifier.loop()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Command line error: missing argument(s).", file=sys.stderr)
        sys.exit(1)

    # Required arguments
    path = sys.argv[1]
    extension = sys.argv[2]

    # Optional argument
    cmd = 'make'
    if len(sys.argv) == 4:
        cmd = sys.argv[3]

    # Blocks monitoring
    auto_compile(path, extension, cmd)
