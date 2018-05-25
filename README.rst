irc-notifier
=============================

A small app which sends a message on IRC when certain signals are received.
This is an example Django app intended to demonstrate building basic edX
extensions for a workshop at the Open edX convention of 2018.

Overview
--------

This is built from the `edx cookiecutter-django-app <https://github.com/edx/cookiecutter-django-app>`_.
The application specific code is in the ``irc_notifier`` directory.

* `apps.py <irc_notifier/apps.py>`_ contains the application configuration.
* `signals.py <irc_notifier/signals.py>`_ contains the signal handler configuration.
* `tasks.py <irc_notifier/tasks.py>`_ contain the tasks that are run on receipt of signals.

Copyrights
----------

Created by OpenCraft.

Copyright (c) 2018 OpenCraft GmbH. See included LICENSE.txt file for usage rights.
