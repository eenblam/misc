# PyAutotest
Inspired by [Building robust software in Python using unit tests](https://www.youtube.com/watch?v=Qw2vczm4m2c).
I didn't want to bother with fswatch,
and I found [a similar script](https://github.com/seb-m/pyinotify/blob/master/python2/examples/autocompile.py)
in the pyinotify wiki.

With the included Makefile, you can just run `make dev_test`,
and your tests will execute whenever you make an edit! Better for the early stages of a TDD project.

Note that you can add more than just `.py` files. `autotest.py ~/path/to/project .py,.js,.html "clear && make tests"`
will run your test suite whenever you create, delete, or edit a file with a .py, .js, or.html extension.
