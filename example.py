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
