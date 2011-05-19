# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

"""The OperationalLimits package models a specification of limits associated with equipment and other operational entities.
"""

from CIM15.IEC61970.OperationalLimits.ApparentPowerLimit import ApparentPowerLimit
from CIM15.IEC61970.OperationalLimits.ActivePowerLimit import ActivePowerLimit
from CIM15.IEC61970.OperationalLimits.OperationalLimitType import OperationalLimitType
from CIM15.IEC61970.OperationalLimits.BranchGroup import BranchGroup
from CIM15.IEC61970.OperationalLimits.OperationalLimitSet import OperationalLimitSet
from CIM15.IEC61970.OperationalLimits.ActivePowerLimitSet import ActivePowerLimitSet
from CIM15.IEC61970.OperationalLimits.CurrentLimit import CurrentLimit
from CIM15.IEC61970.OperationalLimits.CurrentLimitSet import CurrentLimitSet
from CIM15.IEC61970.OperationalLimits.ApparentPowerLimitSet import ApparentPowerLimitSet
from CIM15.IEC61970.OperationalLimits.BranchGroupTerminal import BranchGroupTerminal
from CIM15.IEC61970.OperationalLimits.VoltageLimitSet import VoltageLimitSet
from CIM15.IEC61970.OperationalLimits.VoltageLimit import VoltageLimit
from CIM15.IEC61970.OperationalLimits.OperationalLimit import OperationalLimit

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15#OperationalLimits"
nsPrefix = "cimOperationalLimits"


class OperationalLimitDirectionKind(str):
    """Values are: low, high, absoluteValue
    """
    pass
