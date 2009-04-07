#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM13.Core import IdentifiedObject
from CIM13 import Root



from enthought.traits.api import Instance, List, Enum, Str, Bool, Float
# <<< imports

# >>> imports

#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


OperationalLimitDirectionKind = Enum("absoluteValue", "low", "high")

#------------------------------------------------------------------------------
#  "OperationalLimit" class:
#------------------------------------------------------------------------------

class OperationalLimit(IdentifiedObject):
    """ A value associated with a specific kind of limit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    OperationalLimitType = Instance("CIM13.OperationalLimits.OperationalLimitType")

    OperationalLimitSet = Instance("CIM13.OperationalLimits.OperationalLimitSet")

    # Used to specify high/low and limit levels.
    type = Str

    #--------------------------------------------------------------------------
    #  Begin operationalLimit user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End operationalLimit user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BranchGroup" class:
#------------------------------------------------------------------------------

class BranchGroup(IdentifiedObject):
    """ A group of branch terminals whose directed flow summation is to be monitored. Abranch group need not form a cutset of the network.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    BranchGroupTerminal = List(Instance("CIM13.OperationalLimits.BranchGroupTerminal"))

    # Monitor the active power flow.
    monitorActivePower = Bool

    # The maximum active power flow.
    maximumActivePower = Float

    # Monitor the reactive power flow.
    monitorReactivePower = Bool

    # The minimum active power flow.
    minimumActivePower = Float

    # The maximum reactive power flow.
    maximumReactivePower = Float

    # The minimum reactive power flow.
    minimumReactivePower = Float

    #--------------------------------------------------------------------------
    #  Begin branchGroup user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End branchGroup user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OperationalLimitType" class:
#------------------------------------------------------------------------------

class OperationalLimitType(Root):
    """ A type of limit.  The meaning of a specific limit is described in this class.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    OperationalLimit = List(Instance("CIM13.OperationalLimits.OperationalLimit"))

    # The direction of the limit.
    direction = OperationalLimitDirectionKind

    # The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed.
    acceptableDuration = Float

    #--------------------------------------------------------------------------
    #  Begin operationalLimitType user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End operationalLimitType user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OperationalLimitSet" class:
#------------------------------------------------------------------------------

class OperationalLimitSet(IdentifiedObject):
    """ A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severiteis of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Terminal = Instance("CIM13.Core.Terminal")

    OperationalLimitValue = List(Instance("CIM13.OperationalLimits.OperationalLimit"))

    Equipment = Instance("CIM13.Core.Equipment")

    #--------------------------------------------------------------------------
    #  Begin operationalLimitSet user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End operationalLimitSet user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BranchGroupTerminal" class:
#------------------------------------------------------------------------------

class BranchGroupTerminal(Root):
    """ A specific directed terminal flow for a branch group.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    BranchGroup = Instance("CIM13.OperationalLimits.BranchGroup")

    Terminal = Instance("CIM13.Core.Terminal")

    # The flow into the terminal is summed if set true.   The flow out of the terminanl is summed if set false.
    positiveFlowIn = Bool

    #--------------------------------------------------------------------------
    #  Begin branchGroupTerminal user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End branchGroupTerminal user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ActivePowerLimit" class:
#------------------------------------------------------------------------------

class ActivePowerLimit(OperationalLimit):
    """ Limit on active power flow.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Value of active power limit.
    value = Float

    #--------------------------------------------------------------------------
    #  Begin activePowerLimit user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End activePowerLimit user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CurrentLimit" class:
#------------------------------------------------------------------------------

class CurrentLimit(OperationalLimit):
    """ Operational limit on current.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Limit on current flow.
    value = Float

    #--------------------------------------------------------------------------
    #  Begin currentLimit user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End currentLimit user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "VoltageLimit" class:
#------------------------------------------------------------------------------

class VoltageLimit(OperationalLimit):
    """ Operational limit applied to voltage.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Limit on voltage. High or low limit depends on the OperatoinalLimit.limitKind
    value = Float

    #--------------------------------------------------------------------------
    #  Begin voltageLimit user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End voltageLimit user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ApparentPowerLimit" class:
#------------------------------------------------------------------------------

class ApparentPowerLimit(OperationalLimit):
    """ Apparent power limit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The apparent power limit.
    value = Float

    #--------------------------------------------------------------------------
    #  Begin apparentPowerLimit user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End apparentPowerLimit user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
