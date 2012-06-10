=======================================
Switches: Friendly Command Line Scripts
=======================================

A user-friendly way to define and process command line scripts.

Usage
=====

example.py::

    """Build commands with switches"""

    from switches import command, commandline


    @command
    def spam(argument1, argument2=None):
        """Print the arguments"""
        print argument1
        if argument2 is not None:
            print argument2


    @command
    def eggs(argument1=True, argument2=False):
        """Conditionally print the arguments"""
        if argument1:
            print 'argument1 is True'
        if argument2:
            print 'argument2 is True'


    if __name__ == '__main__':
        commandline(__doc__)

On the command line::

    $ python example.py --help
    usage: example.py [-h] {eggs,spam} ...

    Build commands with switches

    positional arguments:
      {eggs,spam}  commands
        eggs       Conditionally print the arguments
        spam       Print the arguments

    optional arguments:
      -h, --help   show this help message and exit

    $ python example.py spam --help
    usage: example.py spam [-h] [--argument2 ARGUMENT2] argument1

    positional arguments:
      argument1

    optional arguments:
      -h, --help            show this help message and exit
      --argument2 ARGUMENT2
                            The default value is "None".

    $ python example.py eggs --help
    usage: example.py eggs [-h] [--argument1 ARGUMENT1] [--argument2 ARGUMENT2]

    optional arguments:
      -h, --help            show this help message and exit
      --argument1 ARGUMENT1
                            The default value is "True".
      --argument2 ARGUMENT2
                            The default value is "False".

Full documentation can be found on `Read the Docs`_.

.. _Read the Docs: http://readthedocs.org/docs/switches/en/latest/

Installation
============

Installing Switches is easy::

    pip install switches

or download the source and run::

    python setup.py install
