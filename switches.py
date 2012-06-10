# -*- coding: utf-8 -*-

""" Friendly Command Line Scripts """

import argparse
from functools import wraps
import inspect


_ACTIONS = {}
__POSITIONAL_ARGUMENT = '!@**PE**@!'  # Hopefully this won't be a real default


def command(f):
    """Context manager to define a command
    """
    @wraps(f)
    def wrapper():
        f()
    _ACTIONS[f.__name__] = f
    return wrapper


def commandline(description=''):
    """Process the command line
    """
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawTextHelpFormatter,
    )

    commands = parser.add_subparsers(dest='command', help='commands')

    # Loop through all of the actions registered through the decorator
    for action in _ACTIONS:
        # Get the list of arguments and default values
        # - args will be a list containing all arguments
        # - defaults will be a tuple containing all default values for keyword
        #   arguments, positional arguments will not be included
        args, _, _, defaults = inspect.getargspec(_ACTIONS[action])
        help_text = _ACTIONS[action].__doc__

        command = commands.add_parser(action, help=help_text)

        # Track the total number of arguments, positional arguments, and
        # keyword arguments. The three separate values are needed to account
        # for positional arguments not being included in defaults.
        number_of_arguments = len(args)
        number_of_keyword_arguments = len(defaults) if defaults else 0
        number_of_positional_arguments = number_of_arguments - number_of_keyword_arguments

        # If there are more arguments than there are positional arguments,
        # there are keyword arguments. These translate into optional arguments
        # on the command line. In order to reduce the amount of code needed to
        # determine whether an argument is positional or optional, pad the
        # front of the defaults tuple with enough placeholder values to make
        # the length of the arguments list and the default tuple the same. The
        # placeholder value used is a string that will hopefully never be set
        # as an actual default value.
        if number_of_arguments > number_of_positional_arguments:
            defaults = (__POSITIONAL_ARGUMENT,) * number_of_positional_arguments + defaults

        for i in xrange(0, number_of_arguments):
            arg = args[i]
            default = defaults[i] if defaults else __POSITIONAL_ARGUMENT
            help = ''

            # Optional arguments are denoted by placing '--' in front of the
            # argument name. It's also a good idea to include the default value
            # in the help text.
            if default != __POSITIONAL_ARGUMENT:
                arg = '--{0}'.format(arg)
                help = 'The default value is "{0}".'.format(default)

            command.add_argument(arg, default=default, help=help)

    # Run the parser. It returns a Namespace object containing the command and
    # any arguments passed in. In order to handle it nicely, convert the object
    # to a dictionary, pop the command, and pass the rest of the arguments to
    # the action as name parameters.
    args = parser.parse_args()
    vargs = vars(args)
    command = vargs.pop('command')
    _ACTIONS[command](**vargs)
