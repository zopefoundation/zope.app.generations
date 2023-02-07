##############################################################################
#
# Copyright (c) 2004 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Support for application database generations."""

from zope.generations.generations import EVOLVE
from zope.generations.generations import EVOLVEMINIMUM
from zope.generations.generations import EVOLVENOT
from zope.generations.generations import Context
from zope.generations.generations import PersistentDict
from zope.generations.generations import SchemaManager
from zope.generations.generations import evolve
from zope.generations.generations import evolveMinimumSubscriber
from zope.generations.generations import evolveNotSubscriber
from zope.generations.generations import evolveSubscriber
from zope.generations.generations import findManagers
from zope.generations.generations import generations_key
# BBB imports
from zope.generations.interfaces import GenerationTooHigh
from zope.generations.interfaces import GenerationTooLow
from zope.generations.interfaces import IInstallableSchemaManager
from zope.generations.interfaces import ISchemaManager
from zope.generations.interfaces import UnableToEvolve
