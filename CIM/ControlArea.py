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

""" The ControlArea package models area specifications which can be used for a variety of purposes.  The package as a whole models potentially overlapping control area specifications for the purpose of actual generation control, load forecast area load capture, or powerflow based analysis.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM import Element
from CIM.Core import PowerSystemResource
from CIM.Domain import ActivePower



from enthought.traits.api import Instance, List, Property, Enum, Int, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# The type of control area.
ControlAreaTypeKind = Enum("AGC", "Interchange", "Forecast", desc="The type of control area.")

#------------------------------------------------------------------------------
#  "AltTieMeas" class:
#------------------------------------------------------------------------------

class AltTieMeas(Element):
    """ A prioritized measurement to be used for the tie flow as part of the control area specification.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The tie flow of the alternate measurements.
    TieFlow = Instance("CIM.ControlArea.TieFlow",
        desc="The tie flow of the alternate measurements.",
        transient=True,
        opposite="AltTieMeas",
        editor=InstanceEditor(name="_tieflows"))

    def _get_tieflows(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.ControlArea.TieFlow" ]
        else:
            return []

    _tieflows = Property(fget=_get_tieflows)

    # The specific analog value used as a source.
    AnalogValue = Instance("CIM.Meas.AnalogValue",
        desc="The specific analog value used as a source.",
        transient=True,
        opposite="AltTieMeas",
        editor=InstanceEditor(name="_analogvalues"))

    def _get_analogvalues(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Meas.AnalogValue" ]
        else:
            return []

    _analogvalues = Property(fget=_get_analogvalues)

    # Priority of a measurement usage.   Lower numbers have first priority.
    priority = Int(desc="Priority of a measurement usage.   Lower numbers have first priority.")

    #--------------------------------------------------------------------------
    #  Begin "AltTieMeas" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "priority",
                label="Attributes"),
            VGroup("TieFlow", "AnalogValue",
                label="References"),
            dock="tab"),
        id="CIM.ControlArea.AltTieMeas",
        title="AltTieMeas",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AltTieMeas" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AltGeneratingUnitMeas" class:
#------------------------------------------------------------------------------

class AltGeneratingUnitMeas(Element):
    """ A prioritized measurement to be used for the generating unit in the control area specificaiton.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The specific analog value used as a source.
    AnalogValue = Instance("CIM.Meas.AnalogValue",
        desc="The specific analog value used as a source.",
        transient=True,
        opposite="AltGeneratingUnit",
        editor=InstanceEditor(name="_analogvalues"))

    def _get_analogvalues(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Meas.AnalogValue" ]
        else:
            return []

    _analogvalues = Property(fget=_get_analogvalues)

    # The control aread generating unit to which the prioritized measurement assignment is applied.
    ControlAreaGeneratingUnit = Instance("CIM.ControlArea.ControlAreaGeneratingUnit",
        desc="The control aread generating unit to which the prioritized measurement assignment is applied.",
        transient=True,
        opposite="AltGeneratingUnitMeas",
        editor=InstanceEditor(name="_controlareageneratingunits"))

    def _get_controlareageneratingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.ControlArea.ControlAreaGeneratingUnit" ]
        else:
            return []

    _controlareageneratingunits = Property(fget=_get_controlareageneratingunits)

    # Priority of a measurement usage.   Lower numbers have first priority.
    priority = Int(desc="Priority of a measurement usage.   Lower numbers have first priority.")

    #--------------------------------------------------------------------------
    #  Begin "AltGeneratingUnitMeas" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "priority",
                label="Attributes"),
            VGroup("AnalogValue", "ControlAreaGeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM.ControlArea.AltGeneratingUnitMeas",
        title="AltGeneratingUnitMeas",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AltGeneratingUnitMeas" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ControlArea" class:
#------------------------------------------------------------------------------

class ControlArea(PowerSystemResource):
    """ A <b>control area </b>is a grouping of <b>generating units</b> and/or loads and a cutset of tie lines (as <b>terminals</b>) which may be used for a variety of purposes including automatic generation control, powerflow solution area interchange control specification, and input to load forecasting.   Note that any number of overlapping control area specifications can be superimposed on the physical model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The energy area that is forecast from this control area specification.
    EnergyArea = Instance("CIM.LoadModel.EnergyArea",
        desc="The energy area that is forecast from this control area specification.",
        transient=True,
        opposite="ControlArea",
        editor=InstanceEditor(name="_energyareas"))

    def _get_energyareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.LoadModel.EnergyArea" ]
        else:
            return []

    _energyareas = Property(fget=_get_energyareas)

    # The tie flows associated with the control area.
    TieFlow = List(Instance("CIM.ControlArea.TieFlow"),
        desc="The tie flows associated with the control area.")

    # The generating unit specificaitons for the control area.
    ControlAreaGeneratingUnit = List(Instance("CIM.ControlArea.ControlAreaGeneratingUnit"),
        desc="The generating unit specificaitons for the control area.")

    # BusNameMarker objects that belong to the control area.
    BusNameMarker = List(Instance("CIM.Topology.BusNameMarker"),
        desc="BusNameMarker objects that belong to the control area.")

    # The topological nodes included in the control area.
    TopologicalNode = List(Instance("CIM.Topology.TopologicalNode"),
        desc="The topological nodes included in the control area.")

    # The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes.
    type = ControlAreaTypeKind(desc="The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes.")

    # Active power net interchange tolerance
    pTolerance = ActivePower(desc="Active power net interchange tolerance")

    # The specified positive net interchange into the control area.
    netInterchange = ActivePower(desc="The specified positive net interchange into the control area.")

    #--------------------------------------------------------------------------
    #  Begin "ControlArea" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "type", "pTolerance", "netInterchange",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "EnergyArea", "TieFlow", "ControlAreaGeneratingUnit", "BusNameMarker", "TopologicalNode",
                label="References", columns=1),
            dock="tab"),
        id="CIM.ControlArea.ControlArea",
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
    """ A flow specification in terms of location and direction for a control area.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The primary and alternate tie flow measurements associated with the tie flow.
    AltTieMeas = List(Instance("CIM.ControlArea.AltTieMeas"),
        desc="The primary and alternate tie flow measurements associated with the tie flow.")

    # The terminal to which this tie flow belongs.
    Terminal = Instance("CIM.Core.Terminal",
        desc="The terminal to which this tie flow belongs.",
        transient=True,
        opposite="TieFlow",
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

    # The control area of the tie flows.
    ControlArea = Instance("CIM.ControlArea.ControlArea",
        desc="The control area of the tie flows.",
        transient=True,
        opposite="TieFlow",
        editor=InstanceEditor(name="_controlareas"))

    def _get_controlareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.ControlArea.ControlArea" ]
        else:
            return []

    _controlareas = Property(fget=_get_controlareas)

    # The flow is positive into the terminal.  A flow is positive if it is an import into the control area.
    positiveFlowIn = Bool(desc="The flow is positive into the terminal.  A flow is positive if it is an import into the control area.")

    #--------------------------------------------------------------------------
    #  Begin "TieFlow" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "positiveFlowIn",
                label="Attributes"),
            VGroup("AltTieMeas", "Terminal", "ControlArea",
                label="References"),
            dock="tab"),
        id="CIM.ControlArea.TieFlow",
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
    """ A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The link to prioritized measurements for this GeneratingUnit.
    AltGeneratingUnitMeas = List(Instance("CIM.ControlArea.AltGeneratingUnitMeas"),
        desc="The link to prioritized measurements for this GeneratingUnit.")

    # The parent control area for the generating unit specifications.
    ControlArea = Instance("CIM.ControlArea.ControlArea",
        desc="The parent control area for the generating unit specifications.",
        transient=True,
        opposite="ControlAreaGeneratingUnit",
        editor=InstanceEditor(name="_controlareas"))

    def _get_controlareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.ControlArea.ControlArea" ]
        else:
            return []

    _controlareas = Property(fget=_get_controlareas)

    # The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.
    GeneratingUnit = Instance("CIM.Generation.Production.GeneratingUnit",
        desc="The generating unit specified for this control area.  Note that a control area should include a GeneratingUnit only once.",
        transient=True,
        opposite="ControlAreaGeneratingUnit",
        editor=InstanceEditor(name="_generatingunits"))

    def _get_generatingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Generation.Production.GeneratingUnit" ]
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
            VGroup("AltGeneratingUnitMeas", "ControlArea", "GeneratingUnit",
                label="References"),
            dock="tab"),
        id="CIM.ControlArea.ControlAreaGeneratingUnit",
        title="ControlAreaGeneratingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ControlAreaGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
