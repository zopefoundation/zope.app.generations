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

# BBB imports
from zope.generations.interfaces import (
    GenerationTooHigh, GenerationTooLow, UnableToEvolve,
    ISchemaManager, IInstallableSchemaManager)
from zope.generations.generations import (
    generations_key, SchemaManager, Context, findManagers, PersistentDict,
    EVOLVE, EVOLVENOT, EVOLVEMINIMUM, evolve, evolveSubscriber,
    evolveNotSubscriber, evolveMinimumSubscriber)
