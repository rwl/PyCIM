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

""" The OperationalLimits package models a specification of limits associated with equipment and other operational entities.The OperationalLimits package models a specification of limits associated with equipment and other operational entities.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from UCTE.Core import IdentifiedObject
from UCTE.Domain import CurrentFlow
from UCTE.Domain import Voltage
from UCTE.Domain import Seconds



from enthought.traits.api import Instance, List, Property, Enum
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


OperationalLimitDirectionKind = Enum("high", "absoluteValue", "low")

#------------------------------------------------------------------------------
#  "OperationalLimit" class:
#------------------------------------------------------------------------------

class OperationalLimit(IdentifiedObject):
    """ A value associated with a specific kind of limit.A value associated with a specific kind of limit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The limit set to which the limit values belong.The limit set to which the limit values belong.
    OperationalLimitSet = Instance("UCTE.OperationalLimits.OperationalLimitSet", allow_none=False,
        desc="The limit set to which the limit values belong.The limit set to which the limit values belong.",
        transient=True,
        opposite="OperationalLimitValue",
        editor=InstanceEditor(name="_operationallimitsets"))

    def _get_operationallimitsets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.OperationalLimits.OperationalLimitSet" ]
        else:
            return []

    _operationallimitsets = Property(fget=_get_operationallimitsets)

    # The limit type associated with this limit.The limit type associated with this limit.
    OperationalLimitType = Instance("UCTE.OperationalLimits.OperationalLimitType", allow_none=False,
        desc="The limit type associated with this limit.The limit type associated with this limit.",
        transient=True,
        opposite="OperationalLimit",
        editor=InstanceEditor(name="_operationallimittypes"))

    def _get_operationallimittypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.OperationalLimits.OperationalLimitType" ]
        else:
            return []

    _operationallimittypes = Property(fget=_get_operationallimittypes)

    #--------------------------------------------------------------------------
    #  Begin "OperationalLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "description", "name", "aliasName",
                label="Attributes"),
            VGroup("Model", "OperationalLimitSet", "OperationalLimitType",
                label="References"),
            dock="tab"),
        id="UCTE.OperationalLimits.OperationalLimit",
        title="OperationalLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OperationalLimit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "OperationalLimitSet" class:
#------------------------------------------------------------------------------

class OperationalLimitSet(IdentifiedObject):
    """ A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severiteis of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.A set of limits associated with equipmnet.  Sets of limits might apply to a specific temperature, or season for example. A set of limits may contain may different severiteis of limit levels that would apply to the same equipment.   The set may contain limits of different types such as apparent power and current limits or high and low voltage limits  that are logically applied together as a set.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The terminal specifically associated to this operational limit set.  If no terminal is associated, all terminals of the equipment are implied.For UCTE profile, the terminal associated with the limit is always required, and thus there is no need to exchange the associated Equipment which can always be derived from the terminal.The terminal specifically associated to this operational limit set.  If no terminal is associated, all terminals of the equipment are implied.For UCTE profile, the terminal associated with the limit is always required, and thus there is no need to exchange the associated Equipment which can always be derived from the terminal.
    Terminal = Instance("UCTE.Core.Terminal", allow_none=False,
        desc="The terminal specifically associated to this operational limit set.  If no terminal is associated, all terminals of the equipment are implied.For UCTE profile, the terminal associated with the limit is always required, and thus there is no need to exchange the associated Equipment which can always be derived from the terminal.The terminal specifically associated to this operational limit set.  If no terminal is associated, all terminals of the equipment are implied.For UCTE profile, the terminal associated with the limit is always required, and thus there is no need to exchange the associated Equipment which can always be derived from the terminal.",
        transient=True,
        opposite="OperationalLimitSet",
        editor=InstanceEditor(name="_terminals"))

    def _get_terminals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    # Values of equipment limits.Values of equipment limits.
    OperationalLimitValue = List(Instance("UCTE.OperationalLimits.OperationalLimit"),
        desc="Values of equipment limits.Values of equipment limits.")

    #--------------------------------------------------------------------------
    #  Begin "OperationalLimitSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "description", "name", "aliasName",
                label="Attributes"),
            VGroup("Model", "Terminal", "OperationalLimitValue",
                label="References"),
            dock="tab"),
        id="UCTE.OperationalLimits.OperationalLimitSet",
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
    """ A type of limit.  The meaning of a specific limit is described in this class.A type of limit.  The meaning of a specific limit is described in this class.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The operational limits associated with this type of limit.The operational limits associated with this type of limit.
    OperationalLimit = List(Instance("UCTE.OperationalLimits.OperationalLimit"),
        desc="The operational limits associated with this type of limit.The operational limits associated with this type of limit.")

    # The direction of the limit.The direction of the limit.
    direction = OperationalLimitDirectionKind(desc="The direction of the limit.The direction of the limit.")

    # The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed.The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed.
    acceptableDuration = Seconds(desc="The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed.The nominal acceptable duration of the limit.  Limits are commonly expressed in terms of the a time limit for which the limit is normally acceptable.   The actual acceptable duration of a specific limit may depend on other local factors such as temperature or wind speed.")

    #--------------------------------------------------------------------------
    #  Begin "OperationalLimitType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "description", "name", "aliasName", "direction", "acceptableDuration",
                label="Attributes"),
            VGroup("Model", "OperationalLimit",
                label="References"),
            dock="tab"),
        id="UCTE.OperationalLimits.OperationalLimitType",
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
    """ Operational limit on current.Operational limit on current.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Limit on current flow.Limit on current flow.
    value = CurrentFlow(desc="Limit on current flow.Limit on current flow.")

    #--------------------------------------------------------------------------
    #  Begin "CurrentLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "description", "name", "aliasName", "value",
                label="Attributes"),
            VGroup("Model", "OperationalLimitSet", "OperationalLimitType",
                label="References"),
            dock="tab"),
        id="UCTE.OperationalLimits.CurrentLimit",
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
    """ Operational limit applied to voltage.Operational limit applied to voltage.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Limit on voltage. High or low limit depends on the OperatoinalLimit.limitKindLimit on voltage. High or low limit depends on the OperatoinalLimit.limitKind
    value = Voltage(desc="Limit on voltage. High or low limit depends on the OperatoinalLimit.limitKindLimit on voltage. High or low limit depends on the OperatoinalLimit.limitKind")

    #--------------------------------------------------------------------------
    #  Begin "VoltageLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "description", "name", "aliasName", "value",
                label="Attributes"),
            VGroup("Model", "OperationalLimitSet", "OperationalLimitType",
                label="References"),
            dock="tab"),
        id="UCTE.OperationalLimits.VoltageLimit",
        title="VoltageLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "VoltageLimit" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
