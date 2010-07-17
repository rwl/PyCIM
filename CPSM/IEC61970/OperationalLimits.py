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

""" The specificatoin of limits associated with equipment and other operational entities.The specificatoin of limits associated with equipment and other operational entities.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CPSM.IEC61970.Core import IdentifiedObject
from CPSM.IEC61970.Domain import ActivePower
from CPSM.IEC61970.Domain import ApparentPower
from CPSM.IEC61970.Domain import Voltage
from CPSM.IEC61970.Domain import CurrentFlow



from enthought.traits.api import Instance, List, Property, Str
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


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
    OperationalLimitSet = Instance("CPSM.IEC61970.OperationalLimits.OperationalLimitSet", allow_none=False,
        desc="The limit set to which the limit values belong.The limit set to which the limit values belong.",
        transient=True,
        opposite="OperationalLimitValue",
        editor=InstanceEditor(name="_operationallimitsets"))

    def _get_operationallimitsets(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.OperationalLimits.OperationalLimitSet" ]
        else:
            return []

    _operationallimitsets = Property(fget=_get_operationallimitsets)

    # Used to specify high/low and limit levels.Used to specify high/low and limit levels.
    type = Str(desc="Used to specify high/low and limit levels.Used to specify high/low and limit levels.")

    #--------------------------------------------------------------------------
    #  Begin "OperationalLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "type",
                label="Attributes"),
            VGroup("Model", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.OperationalLimits.OperationalLimit",
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
    """ A set of limits associated with equipmnet.A set of limits associated with equipmnet.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The equpment to which the limit set applies.The equpment to which the limit set applies.
    Equipment = Instance("CPSM.IEC61970.Core.Equipment", allow_none=False,
        desc="The equpment to which the limit set applies.The equpment to which the limit set applies.",
        transient=True,
        opposite="OperationalLimitSet",
        editor=InstanceEditor(name="_equipments"))

    def _get_equipments(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Core.Equipment" ]
        else:
            return []

    _equipments = Property(fget=_get_equipments)

    # Values of equipment limits.Values of equipment limits.
    OperationalLimitValue = List(Instance("CPSM.IEC61970.OperationalLimits.OperationalLimit"),
        desc="Values of equipment limits.Values of equipment limits.")

    #--------------------------------------------------------------------------
    #  Begin "OperationalLimitSet" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Equipment", "OperationalLimitValue",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.OperationalLimits.OperationalLimitSet",
        title="OperationalLimitSet",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "OperationalLimitSet" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ActivePowerLimit" class:
#------------------------------------------------------------------------------

class ActivePowerLimit(OperationalLimit):
    """ Limit on active power flow.Limit on active power flow.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Value of active power limit.Value of active power limit.
    value = ActivePower(desc="Value of active power limit.Value of active power limit.")

    #--------------------------------------------------------------------------
    #  Begin "ActivePowerLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "type", "value",
                label="Attributes"),
            VGroup("Model", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.OperationalLimits.ActivePowerLimit",
        title="ActivePowerLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ActivePowerLimit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ApparentPowerLimit" class:
#------------------------------------------------------------------------------

class ApparentPowerLimit(OperationalLimit):
    """ Apparent power limit.Apparent power limit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The apparent power limit.The apparent power limit.
    value = ApparentPower(desc="The apparent power limit.The apparent power limit.")

    #--------------------------------------------------------------------------
    #  Begin "ApparentPowerLimit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "type", "value",
                label="Attributes"),
            VGroup("Model", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.OperationalLimits.ApparentPowerLimit",
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
            VGroup("UUID", "pathName", "description", "aliasName", "name", "type", "value",
                label="Attributes"),
            VGroup("Model", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.OperationalLimits.VoltageLimit",
        title="VoltageLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "VoltageLimit" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CurrentLimit" class:
#------------------------------------------------------------------------------

class CurrentLimit(OperationalLimit):
    """ OIoeratuibak kimit on current.OIoeratuibak kimit on current.
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
            VGroup("UUID", "pathName", "description", "aliasName", "name", "type", "value",
                label="Attributes"),
            VGroup("Model", "OperationalLimitSet",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.OperationalLimits.CurrentLimit",
        title="CurrentLimit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CurrentLimit" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
