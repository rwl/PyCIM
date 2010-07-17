#------------------------------------------------------------------------------
# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------

""" The OperationalLimits package models a specification of limits associated with equipment and other operational entities.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.Core import IdentifiedObject
from CIM import Element
from CIM.Domain import CurrentFlow
from CIM.Domain import ActivePower
from CIM.Domain import ReactivePower
from CIM.Domain import ApparentPower
from CIM.Domain import Voltage
from CIM.Domain import Seconds



from enthought.traits.api import Instance, List, Property, Enum, Str, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# The direction of an operational limit.
OperationalLimitDirectionKind = Enum("high", "low", "absoluteValue", desc="The direction of an operational limit.")

#------------------------------------------------------------------------------
#  "OperationalLimit" class:
#------------------------------------------------------------------------------

class OperationalLimit(IdentifiedObject):
    """ A value associated with a specific kind of limit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The limit type associated with this limit.
    OperationalLimitType = Instance("CIM.OperationalLimits.OperationalLimitType",
        desc="The limit type associated with this limit.",
        transient=True,
        opposite="OperationalLimit",
        editor=InstanceEditor(name="_operationallimittypes"))

    def _get_operationallimittypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.OperationalLimits.OperationalLimitType" ]
        else:
            return []

    _operationallimittypes = Property(fget=_get_operationallimittypes)

    # The limit set to which the limit values belong.
    OperationalLimitSet = Instance("CIM.OperationalLimits.OperationalLimitSet",
        desc="The limit set to which the limit values belong.",
        transient=True,
        opposite="OperationalLimitValue",
        editor=InstanceEditor(name="_operationallimitsets"))

    def _get_operationallimitsets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.OperationalLimits.OperationalLimitSet" ]
        else:
            return []

    _operationallimitsets = Property(fget=_get_operationallimitsets)

    # Used to specify high/low and limit levels.
    type = Str(desc="Used to specify high/low and limit levels.")

    #--------------------------------------------------------------------------
    #  Begin "OperationalLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "type",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperationalLimitType", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CIM.OperationalLimits.OperationalLimit",
        title="OperationalLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OperationalLimit" user definitions:
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

    # The directed branch group terminals to be summed.
    BranchGroupTerminal = List(Instance("CIM.OperationalLimits.BranchGroupTerminal"),
        desc="The directed branch group terminals to be summed.")

    # The minimum active power flow.
    minimumActivePower = ActivePower(desc="The minimum active power flow.")

    # The minimum reactive power flow.
    minimumReactivePower = ReactivePower(desc="The minimum reactive power flow.")

    # Monitor the reactive power flow.
    monitorReactivePower = Bool(desc="Monitor the reactive power flow.")

    # Monitor the active power flow.
    monitorActivePower = Bool(desc="Monitor the active power flow.")

    # The maximum reactive power flow.
    maximumReactivePower = ReactivePower(desc="The maximum reactive power flow.")

    # The maximum active power flow.
    maximumActivePower = ActivePower(desc="The maximum active power flow.")

    #--------------------------------------------------------------------------
    #  Begin "BranchGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "minimumActivePower", "minimumReactivePower", "monitorReactivePower", "monitorActivePower", "maximumReactivePower", "maximumActivePower",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "BranchGroupTerminal",
                label="References"),
            dock="tab"),
        id="CIM.OperationalLimits.BranchGroup",
        title="BranchGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BranchGroup" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BranchGroupTerminal" class:
#------------------------------------------------------------------------------

class BranchGroupTerminal(Element):
    """ A specific directed terminal flow for a branch group.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The terminal to be summed.
    Terminal = Instance("CIM.Core.Terminal",
        desc="The terminal to be summed.",
        transient=True,
        opposite="BranchGroupTerminal",
        editor=InstanceEditor(name="_terminals"))

    def _get_terminals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    # The branch group to which the directed branch group terminals belong.
    BranchGroup = Instance("CIM.OperationalLimits.BranchGroup",
        desc="The branch group to which the directed branch group terminals belong.",
        transient=True,
        opposite="BranchGroupTerminal",
        editor=InstanceEditor(name="_branchgroups"))

    def _get_branchgroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.OperationalLimits.BranchGroup" ]
        else:
            return []

    _branchgroups = Property(fget=_get_branchgroups)

    # The flow into the terminal is summed if set true.   The flow out of the terminanl is summed if set false.
    positiveFlowIn = Bool(desc="The flow into the terminal is summed if set true.   The flow out of the terminanl is summed if set false.")

    #--------------------------------------------------------------------------
    #  Begin "BranchGroupTerminal" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "positiveFlowIn",
                label="Attributes"),
            VGroup("Terminal", "BranchGroup",
                label="References"),
            dock="tab"),
        id="CIM.OperationalLimits.BranchGroupTerminal",
        title="BranchGroupTerminal",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BranchGroupTerminal" user definitions:
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

    # The equpment to which the limit set applies.
    Equipment = Instance("CIM.Core.Equipment",
        desc="The equpment to which the limit set applies.",
        transient=True,
        opposite="OperationalLimitSet",
        editor=InstanceEditor(name="_equipments"))

    def _get_equipments(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Core.Equipment" ]
        else:
            return []

    _equipments = Property(fget=_get_equipments)

    # The terminal specifically associated to this operational limit set.  If no terminal is associated, all terminals of the equipment are implied.
    Terminal = Instance("CIM.Core.Terminal",
        desc="The terminal specifically associated to this operational limit set.  If no terminal is associated, all terminals of the equipment are implied.",
        transient=True,
        opposite="OperationalLimitSet",
        editor=InstanceEditor(name="_terminals"))

    def _get_terminals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    # Values of equipment limits.
    OperationalLimitValue = List(Instance("CIM.OperationalLimits.OperationalLimit"),
        desc="Values of equipment limits.")

    #--------------------------------------------------------------------------
    #  Begin "OperationalLimitSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "Equipment", "Terminal", "OperationalLimitValue",
                label="References"),
            dock="tab"),
        id="CIM.OperationalLimits.OperationalLimitSet",
        title="OperationalLimitSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OperationalLimitSet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OperationalLimitType" class:
#------------------------------------------------------------------------------

class OperationalLimitType(IdentifiedObject):
    """ A type of limit.  The meaning of a specific limit is described in this class.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The operational limits associated with this type of limit.
    OperationalLimit = List(Instance("CIM.OperationalLimits.OperationalLimit"),
        desc="The operational limits associated with this type of limit.")

    # The direction of the limit.
    direction = OperationalLimitDirectionKind(desc="The direction of the limit.")

    # The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed.
    acceptableDuration = Seconds(desc="The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed.")

    #--------------------------------------------------------------------------
    #  Begin "OperationalLimitType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "direction", "acceptableDuration",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperationalLimit",
                label="References"),
            dock="tab"),
        id="CIM.OperationalLimits.OperationalLimitType",
        title="OperationalLimitType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OperationalLimitType" user definitions:
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
    value = CurrentFlow(desc="Limit on current flow.")

    #--------------------------------------------------------------------------
    #  Begin "CurrentLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "type", "value",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperationalLimitType", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CIM.OperationalLimits.CurrentLimit",
        title="CurrentLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CurrentLimit" user definitions:
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
    value = ApparentPower(desc="The apparent power limit.")

    #--------------------------------------------------------------------------
    #  Begin "ApparentPowerLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "type", "value",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperationalLimitType", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CIM.OperationalLimits.ApparentPowerLimit",
        title="ApparentPowerLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ApparentPowerLimit" user definitions:
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
    value = Voltage(desc="Limit on voltage. High or low limit depends on the OperatoinalLimit.limitKind")

    #--------------------------------------------------------------------------
    #  Begin "VoltageLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "type", "value",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperationalLimitType", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CIM.OperationalLimits.VoltageLimit",
        title="VoltageLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "VoltageLimit" user definitions:
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
    value = ActivePower(desc="Value of active power limit.")

    #--------------------------------------------------------------------------
    #  Begin "ActivePowerLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "type", "value",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperationalLimitType", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CIM.OperationalLimits.ActivePowerLimit",
        title="ActivePowerLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ActivePowerLimit" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
