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



from enthought.traits.api import Instance, List, Property, Enum, Str, Bool, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
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

    OperationalLimitType = Instance("CIM13.OperationalLimits.OperationalLimitType",
        transient=True,
        opposite="OperationalLimit",
        editor=InstanceEditor(name="_OperationalLimitTypes"))

    _OperationalLimitTypes = Property( List(Instance("CIM.Root")) )

    def _get__OperationalLimitTypes(self):
        """ Property getter.
        """
        if self.ContainedBy is not None:
            return [element for element in self.ContainedBy.Contains \
                if isinstance(element, OperationalLimitType)]
        else:
            return []

    OperationalLimitSet = Instance("CIM13.OperationalLimits.OperationalLimitSet",
        transient=True,
        opposite="OperationalLimitValue",
        editor=InstanceEditor(name="_OperationalLimitSets"))

    _OperationalLimitSets = Property( List(Instance("CIM.Root")) )

    def _get__OperationalLimitSets(self):
        """ Property getter.
        """
        if self.ContainedBy is not None:
            return [element for element in self.ContainedBy.Contains \
                if isinstance(element, OperationalLimitSet)]
        else:
            return []

    # Used to specify high/low and limit levels.
    type = Str(desc="Used to specify high/low and limit levels.")

    #--------------------------------------------------------------------------
    #  Begin "OperationalLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "name", "localName", "description", "aliasName", "mRID", "pathName", "type",
                label="Attributes"),
            VGroup("ContainedBy", "ModelingAuthoritySet", "OperationalLimitType", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CIM13.OperationalLimits.OperationalLimit",
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

    BranchGroupTerminal = List(Instance("CIM13.OperationalLimits.BranchGroupTerminal"))

    # Monitor the active power flow.
    monitorActivePower = Bool(desc="Monitor the active power flow.")

    # The maximum active power flow.
    maximumActivePower = Float(desc="The maximum active power flow.")

    # Monitor the reactive power flow.
    monitorReactivePower = Bool(desc="Monitor the reactive power flow.")

    # The minimum active power flow.
    minimumActivePower = Float(desc="The minimum active power flow.")

    # The maximum reactive power flow.
    maximumReactivePower = Float(desc="The maximum reactive power flow.")

    # The minimum reactive power flow.
    minimumReactivePower = Float(desc="The minimum reactive power flow.")

    #--------------------------------------------------------------------------
    #  Begin "BranchGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "name", "localName", "description", "aliasName", "mRID", "pathName", "monitorActivePower", "maximumActivePower", "monitorReactivePower", "minimumActivePower", "maximumReactivePower", "minimumReactivePower",
                label="Attributes", columns=1),
            VGroup("ContainedBy", "ModelingAuthoritySet", "BranchGroupTerminal",
                label="References"),
            dock="tab"),
        id="CIM13.OperationalLimits.BranchGroup",
        title="BranchGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BranchGroup" user definitions:
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
    direction = OperationalLimitDirectionKind(desc="The direction of the limit.")

    # The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed.
    acceptableDuration = Float(desc="The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed.")

    #--------------------------------------------------------------------------
    #  Begin "OperationalLimitType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "direction", "acceptableDuration",
                label="Attributes"),
            VGroup("ContainedBy", "OperationalLimit",
                label="References"),
            dock="tab"),
        id="CIM13.OperationalLimits.OperationalLimitType",
        title="OperationalLimitType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OperationalLimitType" user definitions:
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

    Terminal = Instance("CIM13.Core.Terminal",
        transient=True,
        opposite="OperationalLimitSet",
        editor=InstanceEditor(name="_Terminals"))

    _Terminals = Property( List(Instance("CIM.Root")) )

    def _get__Terminals(self):
        """ Property getter.
        """
        if self.ContainedBy is not None:
            return [element for element in self.ContainedBy.Contains \
                if isinstance(element, Terminal)]
        else:
            return []

    OperationalLimitValue = List(Instance("CIM13.OperationalLimits.OperationalLimit"))

    Equipment = Instance("CIM13.Core.Equipment",
        transient=True,
        opposite="OperationalLimitSet",
        editor=InstanceEditor(name="_Equipments"))

    _Equipments = Property( List(Instance("CIM.Root")) )

    def _get__Equipments(self):
        """ Property getter.
        """
        if self.ContainedBy is not None:
            return [element for element in self.ContainedBy.Contains \
                if isinstance(element, Equipment)]
        else:
            return []

    #--------------------------------------------------------------------------
    #  Begin "OperationalLimitSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("ContainedBy", "ModelingAuthoritySet", "Terminal", "OperationalLimitValue", "Equipment",
                label="References"),
            dock="tab"),
        id="CIM13.OperationalLimits.OperationalLimitSet",
        title="OperationalLimitSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OperationalLimitSet" user definitions:
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

    BranchGroup = Instance("CIM13.OperationalLimits.BranchGroup",
        transient=True,
        opposite="BranchGroupTerminal",
        editor=InstanceEditor(name="_BranchGroups"))

    _BranchGroups = Property( List(Instance("CIM.Root")) )

    def _get__BranchGroups(self):
        """ Property getter.
        """
        if self.ContainedBy is not None:
            return [element for element in self.ContainedBy.Contains \
                if isinstance(element, BranchGroup)]
        else:
            return []

    Terminal = Instance("CIM13.Core.Terminal",
        transient=True,
        opposite="BranchGroupTerminal",
        editor=InstanceEditor(name="_Terminals"))

    _Terminals = Property( List(Instance("CIM.Root")) )

    def _get__Terminals(self):
        """ Property getter.
        """
        if self.ContainedBy is not None:
            return [element for element in self.ContainedBy.Contains \
                if isinstance(element, Terminal)]
        else:
            return []

    # The flow into the terminal is summed if set true.   The flow out of the terminanl is summed if set false.
    positiveFlowIn = Bool(desc="The flow into the terminal is summed if set true.   The flow out of the terminanl is summed if set false.")

    #--------------------------------------------------------------------------
    #  Begin "BranchGroupTerminal" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "positiveFlowIn",
                label="Attributes"),
            VGroup("ContainedBy", "BranchGroup", "Terminal",
                label="References"),
            dock="tab"),
        id="CIM13.OperationalLimits.BranchGroupTerminal",
        title="BranchGroupTerminal",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BranchGroupTerminal" user definitions:
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
    value = Float(desc="Value of active power limit.")

    #--------------------------------------------------------------------------
    #  Begin "ActivePowerLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "name", "localName", "description", "aliasName", "mRID", "pathName", "type", "value",
                label="Attributes"),
            VGroup("ContainedBy", "ModelingAuthoritySet", "OperationalLimitType", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CIM13.OperationalLimits.ActivePowerLimit",
        title="ActivePowerLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ActivePowerLimit" user definitions:
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
    value = Float(desc="Limit on current flow.")

    #--------------------------------------------------------------------------
    #  Begin "CurrentLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "name", "localName", "description", "aliasName", "mRID", "pathName", "type", "value",
                label="Attributes"),
            VGroup("ContainedBy", "ModelingAuthoritySet", "OperationalLimitType", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CIM13.OperationalLimits.CurrentLimit",
        title="CurrentLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CurrentLimit" user definitions:
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
    value = Float(desc="Limit on voltage. High or low limit depends on the OperatoinalLimit.limitKind")

    #--------------------------------------------------------------------------
    #  Begin "VoltageLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "name", "localName", "description", "aliasName", "mRID", "pathName", "type", "value",
                label="Attributes"),
            VGroup("ContainedBy", "ModelingAuthoritySet", "OperationalLimitType", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CIM13.OperationalLimits.VoltageLimit",
        title="VoltageLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "VoltageLimit" user definitions:
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
    value = Float(desc="The apparent power limit.")

    #--------------------------------------------------------------------------
    #  Begin "ApparentPowerLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "name", "localName", "description", "aliasName", "mRID", "pathName", "type", "value",
                label="Attributes"),
            VGroup("ContainedBy", "ModelingAuthoritySet", "OperationalLimitType", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CIM13.OperationalLimits.ApparentPowerLimit",
        title="ApparentPowerLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ApparentPowerLimit" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
