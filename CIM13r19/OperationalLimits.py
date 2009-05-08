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

from CIM13r19.Core import IdentifiedObject
from CIM13r19 import Element



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

    OperationalLimitType = Instance("CIM13r19.OperationalLimits.OperationalLimitType",
        transient=True,
        opposite="OperationalLimit",
        editor=InstanceEditor(name="_operationallimittypes"))

    def _get_operationallimittypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.OperationalLimits.OperationalLimitType" ]
        else:
            return []

    _operationallimittypes = Property(fget=_get_operationallimittypes)

    OperationalLimitSet = Instance("CIM13r19.OperationalLimits.OperationalLimitSet",
        transient=True,
        opposite="OperationalLimitValue",
        editor=InstanceEditor(name="_operationallimitsets"))

    def _get_operationallimitsets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.OperationalLimits.OperationalLimitSet" ]
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
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "type",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "OperationalLimitType", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CIM13r19.OperationalLimits.OperationalLimit",
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

    BranchGroupTerminal = List(Instance("CIM13r19.OperationalLimits.BranchGroupTerminal"))

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
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "monitorActivePower", "maximumActivePower", "monitorReactivePower", "minimumActivePower", "maximumReactivePower", "minimumReactivePower",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "BranchGroupTerminal",
                label="References"),
            dock="tab"),
        id="CIM13r19.OperationalLimits.BranchGroup",
        title="BranchGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BranchGroup" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OperationalLimitType" class:
#------------------------------------------------------------------------------

class OperationalLimitType(Element):
    """ A type of limit.  The meaning of a specific limit is described in this class.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    OperationalLimit = List(Instance("CIM13r19.OperationalLimits.OperationalLimit"))

    # The direction of the limit.
    direction = OperationalLimitDirectionKind(desc="The direction of the limit.")

    # The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed.
    acceptableDuration = Float(desc="The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed.")

    #--------------------------------------------------------------------------
    #  Begin "OperationalLimitType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("direction", "acceptableDuration",
                label="Attributes"),
            VGroup("Parent", "OperationalLimit",
                label="References"),
            dock="tab"),
        id="CIM13r19.OperationalLimits.OperationalLimitType",
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

    Terminal = Instance("CIM13r19.Core.Terminal",
        transient=True,
        opposite="OperationalLimitSet",
        editor=InstanceEditor(name="_terminals"))

    def _get_terminals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    OperationalLimitValue = List(Instance("CIM13r19.OperationalLimits.OperationalLimit"))

    Equipment = Instance("CIM13r19.Core.Equipment",
        transient=True,
        opposite="OperationalLimitSet",
        editor=InstanceEditor(name="_equipments"))

    def _get_equipments(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.Equipment" ]
        else:
            return []

    _equipments = Property(fget=_get_equipments)

    #--------------------------------------------------------------------------
    #  Begin "OperationalLimitSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Terminal", "OperationalLimitValue", "Equipment",
                label="References"),
            dock="tab"),
        id="CIM13r19.OperationalLimits.OperationalLimitSet",
        title="OperationalLimitSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OperationalLimitSet" user definitions:
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

    BranchGroup = Instance("CIM13r19.OperationalLimits.BranchGroup",
        transient=True,
        opposite="BranchGroupTerminal",
        editor=InstanceEditor(name="_branchgroups"))

    def _get_branchgroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.OperationalLimits.BranchGroup" ]
        else:
            return []

    _branchgroups = Property(fget=_get_branchgroups)

    Terminal = Instance("CIM13r19.Core.Terminal",
        transient=True,
        opposite="BranchGroupTerminal",
        editor=InstanceEditor(name="_terminals"))

    def _get_terminals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    # The flow into the terminal is summed if set true.   The flow out of the terminanl is summed if set false.
    positiveFlowIn = Bool(desc="The flow into the terminal is summed if set true.   The flow out of the terminanl is summed if set false.")

    #--------------------------------------------------------------------------
    #  Begin "BranchGroupTerminal" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("positiveFlowIn",
                label="Attributes"),
            VGroup("Parent", "BranchGroup", "Terminal",
                label="References"),
            dock="tab"),
        id="CIM13r19.OperationalLimits.BranchGroupTerminal",
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
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "type", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "OperationalLimitType", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CIM13r19.OperationalLimits.ActivePowerLimit",
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
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "type", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "OperationalLimitType", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CIM13r19.OperationalLimits.CurrentLimit",
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
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "type", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "OperationalLimitType", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CIM13r19.OperationalLimits.VoltageLimit",
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
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "type", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "OperationalLimitType", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CIM13r19.OperationalLimits.ApparentPowerLimit",
        title="ApparentPowerLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ApparentPowerLimit" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
