#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CookingAPI.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    #This currently does use sqlite!

    #TODO make functions to interact with db (perchance adaptable)
    '''
    translate previous endpoints here
    Fix getRandom endpoint
    implement new ones
    Docker?
    Presentation/service/data layer
    Classes for objects?
    /recipes
    /add/get/update/delete/getRandom
    Keep track of order of steps? option to move around?
    method to convert list elements
    Query string!
    adjust portion quantities through get instead of FE?
    '''


if __name__ == '__main__':
    main()
