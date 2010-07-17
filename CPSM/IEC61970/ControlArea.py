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

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CPSM.IEC61970.Core import PowerSystemResource
from CPSM import Element
from CPSM.IEC61970.Domain import ActivePower



from enthought.traits.api import Instance, List, Property, Enum, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


ControlAreaTypeKind = Enum("Forecast", "Interchange", "AGC")

#------------------------------------------------------------------------------
#  "ControlArea" class:
#------------------------------------------------------------------------------

class ControlArea(PowerSystemResource):
    """ A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The generating unit specificaitons for the control area.The generating unit specificaitons for the control area.
    ControlAreaGeneratingUnit = List(Instance("CPSM.IEC61970.ControlArea.ControlAreaGeneratingUnit"),
        desc="The generating unit specificaitons for the control area.The generating unit specificaitons for the control area.")

    # The energy area that is forecast from this control area specification.The energy area that is forecast from this control area specification.
    EnergyArea = Instance("CPSM.IEC61970.LoadModel.EnergyArea", allow_none=False,
        desc="The energy area that is forecast from this control area specification.The energy area that is forecast from this control area specification.",
        transient=True,
        opposite="ControlArea",
        editor=InstanceEditor(name="_energyareas"))

    def _get_energyareas(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.LoadModel.EnergyArea" ]
        else:
            return []

    _energyareas = Property(fget=_get_energyareas)

    # The tie flows associated with the control area.The tie flows associated with the control area.
    TieFlow = List(Instance("CPSM.IEC61970.ControlArea.TieFlow"),
        desc="The tie flows associated with the control area.The tie flows associated with the control area.")

    # The specified positive net interchange into the control area.The specified positive net interchange into the control area.
    netInterchange = ActivePower(desc="The specified positive net interchange into the control area.The specified positive net interchange into the control area.")

    # The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes.The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes.
    type = ControlAreaTypeKind(desc="The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes.The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes.")

    #--------------------------------------------------------------------------
    #  Begin "ControlArea" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "netInterchange", "type",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "ControlAreaGeneratingUnit", "EnergyArea", "TieFlow",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.ControlArea.ControlArea",
        title="ControlArea",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ControlArea" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TieFlow" class:
#------------------------------------------------------------------------------

class TieFlow(Element):
    """ A flow specification in terms of location and direction for a control area.A flow specification in terms of location and direction for a control area.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The control area of the tie flows.The control area of the tie flows.
    ControlArea = Instance("CPSM.IEC61970.ControlArea.ControlArea", allow_none=False,
        desc="The control area of the tie flows.The control area of the tie flows.",
        transient=True,
        opposite="TieFlow",
        editor=InstanceEditor(name="_controlareas"))

    def _get_controlareas(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.ControlArea.ControlArea" ]
        else:
            return []

    _controlareas = Property(fget=_get_controlareas)

    # The flow is positive into the terminal.  A flow is positive if it is an import into the control area.The flow is positive into the terminal.  A flow is positive if it is an import into the control area.
    positiveFlowIn = Bool(desc="The flow is positive into the terminal.  A flow is positive if it is an import into the control area.The flow is positive into the terminal.  A flow is positive if it is an import into the control area.")

    #--------------------------------------------------------------------------
    #  Begin "TieFlow" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "positiveFlowIn",
                label="Attributes"),
            VGroup("Model", "ControlArea",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.ControlArea.TieFlow",
        title="TieFlow",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TieFlow" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ControlAreaGeneratingUnit" class:
#------------------------------------------------------------------------------

class ControlAreaGeneratingUnit(Element):
    """ A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The parent control area for the generating unit specifications.The parent control area for the generating unit specifications.
    ControlArea = Instance("CPSM.IEC61970.ControlArea.ControlArea", allow_none=False,
        desc="The parent control area for the generating unit specifications.The parent control area for the generating unit specifications.",
        transient=True,
        opposite="ControlAreaGeneratingUnit",
        editor=InstanceEditor(name="_controlareas"))

    def _get_controlareas(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.ControlArea.ControlArea" ]
        else:
            return []

    _controlareas = Property(fget=_get_controlareas)

    # The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.
    GeneratingUnit = Instance("CPSM.IEC61970.Generation.Production.GeneratingUnit", allow_none=False,
        desc="The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.",
        transient=True,
        opposite="ControlAreaGeneratingUnit",
        editor=InstanceEditor(name="_generatingunits"))

    def _get_generatingunits(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Generation.Production.GeneratingUnit" ]
        else:
            return []

    _generatingunits = Property(fget=_get_generatingunits)

    #--------------------------------------------------------------------------
    #  Begin "ControlAreaGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            VGroup("Model", "ControlArea", "GeneratingUnit",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.ControlArea.ControlAreaGeneratingUnit",
        title="ControlAreaGeneratingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ControlAreaGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
