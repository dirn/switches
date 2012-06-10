switches 0.1.0
==============

Switches providers a user-friendly way to create command line scripts using
Python.

.. toctree::
   :maxdepth: 2

Usage
-----

To designate a function as a possible command::

    @command
    def function():
        """This function does stuff"""
        pass

This will create a command accessible through::

    $ python script.py function

Switches will create a command called ``function``. It's docstring will be used
to generate the help text associated with the command.

If function is defined with arguments, these will be added to the command as
either positional or optional arguments, depending on whether or not the
argument takes a default value::

    @command
    def function(positional, optional='default'):
        """This function does stuff"""
        pass

In this instance, Switches will create a command called ``function`` that has
one positional argument and one optional argument. The optional argument,
``optional``, can be given a value by adding ``--optional 'value'`` to the call
to ``function``. If no value is given, the default, ``default`` will be used::

    $ python script.py function 'value1' --optional 'value2'

Once all of the commands have been defined, the rest is as simple as::

    commandline('Description of the script')

This will tell Switches to process the command line and run the appropriate
command. A description for the script can be passed to ``commandline`` to help
users who call the script with just the ``--help`` option.
