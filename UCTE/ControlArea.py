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

""" The ControlArea package models area specifications which can be used for a variety of purposes.  The package as a whole models potentially overlapping control area specifications for the purpose of actual generation control, load forecast area load capture, or powerflow based analysis.The ControlArea package models area specifications which can be used for a variety of purposes.  The package as a whole models potentially overlapping control area specifications for the purpose of actual generation control, load forecast area load capture, or powerflow based analysis.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from UCTE.Core import IdentifiedObject
from UCTE import Element
from UCTE.Domain import ActivePower



from enthought.traits.api import Instance, List, Property, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "ControlArea" class:
#------------------------------------------------------------------------------

class ControlArea(IdentifiedObject):
    """ A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The topological nodes included in the control area.The topological nodes included in the control area.
    TopologicalNode = List(Instance("UCTE.Topology.TopologicalNode"),
        desc="The topological nodes included in the control area.The topological nodes included in the control area.")

    # The tie flows associated with the control area.The tie flows associated with the control area.
    TieFlow = List(Instance("UCTE.ControlArea.TieFlow"),
        desc="The tie flows associated with the control area.The tie flows associated with the control area.")

    # The generating unit specificaitons for the control area.The generating unit specificaitons for the control area.
    ControlAreaGeneratingUnit = List(Instance("UCTE.ControlArea.ControlAreaGeneratingUnit"),
        desc="The generating unit specificaitons for the control area.The generating unit specificaitons for the control area.")

    # Active power net interchange toleranceActive power net interchange tolerance
    pTolerance = ActivePower(desc="Active power net interchange toleranceActive power net interchange tolerance")

    # The specified positive net interchange into the control area.The specified positive net interchange into the control area.
    netInterchange = ActivePower(desc="The specified positive net interchange into the control area.The specified positive net interchange into the control area.")

    #--------------------------------------------------------------------------
    #  Begin "ControlArea" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "description", "name", "aliasName", "pTolerance", "netInterchange",
                label="Attributes"),
            VGroup("Model", "TopologicalNode", "TieFlow", "ControlAreaGeneratingUnit",
                label="References"),
            dock="tab"),
        id="UCTE.ControlArea.ControlArea",
        title="ControlArea",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ControlArea" user definitions:
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
    ControlArea = Instance("UCTE.ControlArea.ControlArea", allow_none=False,
        desc="The parent control area for the generating unit specifications.The parent control area for the generating unit specifications.",
        transient=True,
        opposite="ControlAreaGeneratingUnit",
        editor=InstanceEditor(name="_controlareas"))

    def _get_controlareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.ControlArea.ControlArea" ]
        else:
            return []

    _controlareas = Property(fget=_get_controlareas)

    # The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.
    GeneratingUnit = Instance("UCTE.Generation.Production.GeneratingUnit", allow_none=False,
        desc="The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.",
        transient=True,
        opposite="ControlAreaGeneratingUnit",
        editor=InstanceEditor(name="_generatingunits"))

    def _get_generatingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Generation.Production.GeneratingUnit" ]
        else:
            return []

    _generatingunits = Property(fget=_get_generatingunits)

    #--------------------------------------------------------------------------
    #  Begin "ControlAreaGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model", "ControlArea", "GeneratingUnit",
                label="References"),
            dock="tab"),
        id="UCTE.ControlArea.ControlAreaGeneratingUnit",
        title="ControlAreaGeneratingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ControlAreaGeneratingUnit" user definitions:
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
    ControlArea = Instance("UCTE.ControlArea.ControlArea", allow_none=False,
        desc="The control area of the tie flows.The control area of the tie flows.",
        transient=True,
        opposite="TieFlow",
        editor=InstanceEditor(name="_controlareas"))

    def _get_controlareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.ControlArea.ControlArea" ]
        else:
            return []

    _controlareas = Property(fget=_get_controlareas)

    # The terminal to which this tie flow belongs.The terminal to which this tie flow belongs.
    Terminal = Instance("UCTE.Core.Terminal", allow_none=False,
        desc="The terminal to which this tie flow belongs.The terminal to which this tie flow belongs.",
        transient=True,
        opposite="TieFlow",
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

    # The flow is positive into the terminal.  A flow is positive if it is an import into the control area.The power flow is positive into the Terminal of the ConductingEquipment.The flow is positive into the terminal.  A flow is positive if it is an import into the control area.The power flow is positive into the Terminal of the ConductingEquipment.
    positiveFlowIn = Bool(desc="The flow is positive into the terminal.  A flow is positive if it is an import into the control area.The power flow is positive into the Terminal of the ConductingEquipment.The flow is positive into the terminal.  A flow is positive if it is an import into the control area.The power flow is positive into the Terminal of the ConductingEquipment.")

    #--------------------------------------------------------------------------
    #  Begin "TieFlow" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "positiveFlowIn",
                label="Attributes"),
            VGroup("Model", "ControlArea", "Terminal",
                label="References"),
            dock="tab"),
        id="UCTE.ControlArea.TieFlow",
        title="TieFlow",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TieFlow" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
