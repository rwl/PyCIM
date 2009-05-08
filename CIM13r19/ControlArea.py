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

from CIM13r19 import Element
from CIM13r19.Core import PowerSystemResource



from enthought.traits.api import Instance, List, Property, Enum, Float, Int, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


ControlAreaTypeKind = Enum("AGC", "Interchange", "Forecast")

#------------------------------------------------------------------------------
#  "ControlAreaGeneratingUnit" class:
#------------------------------------------------------------------------------

class ControlAreaGeneratingUnit(Element):
    """ A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GeneratingUnit = Instance("CIM13r19.Generation.Production.GeneratingUnit",
        transient=True,
        opposite="ControlAreaGeneratingUnit",
        editor=InstanceEditor(name="_generatingunits"))

    def _get_generatingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Generation.Production.GeneratingUnit" ]
        else:
            return []

    _generatingunits = Property(fget=_get_generatingunits)

    AltGeneratingUnitMeas = List(Instance("CIM13r19.ControlArea.AltGeneratingUnitMeas"))

    ControlArea = Instance("CIM13r19.ControlArea.ControlArea",
        transient=True,
        opposite="ControlAreaGeneratingUnit",
        editor=InstanceEditor(name="_controlareas"))

    def _get_controlareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.ControlArea.ControlArea" ]
        else:
            return []

    _controlareas = Property(fget=_get_controlareas)

    #--------------------------------------------------------------------------
    #  Begin "ControlAreaGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("Parent", "GeneratingUnit", "AltGeneratingUnitMeas", "ControlArea",
                label="References"),
            dock="tab"),
        id="CIM13r19.ControlArea.ControlAreaGeneratingUnit",
        title="ControlAreaGeneratingUnit",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ControlAreaGeneratingUnit" user definitions:
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

    BusNameMarker = List(Instance("CIM13r19.Topology.BusNameMarker"))

    EnergyArea = Instance("CIM13r19.LoadModel.EnergyArea",
        transient=True,
        opposite="ControlArea",
        editor=InstanceEditor(name="_energyareas"))

    def _get_energyareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.LoadModel.EnergyArea" ]
        else:
            return []

    _energyareas = Property(fget=_get_energyareas)

    TopologicalNode = List(Instance("CIM13r19.Topology.TopologicalNode"))

    ControlAreaGeneratingUnit = List(Instance("CIM13r19.ControlArea.ControlAreaGeneratingUnit"))

    TieFlow = List(Instance("CIM13r19.ControlArea.TieFlow"))

    # The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes.
    type = ControlAreaTypeKind(desc="The type of control area defintion used to determine if this is used for automatic generation control, for planning interchange control, or other purposes.")

    # Active power net interchange tolerance
    pTolerance = Float(desc="Active power net interchange tolerance")

    # The specified positive net interchange into the control area.
    netInterchange = Float(desc="The specified positive net interchange into the control area.")

    #--------------------------------------------------------------------------
    #  Begin "ControlArea" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "type", "pTolerance", "netInterchange",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "BusNameMarker", "EnergyArea", "TopologicalNode", "ControlAreaGeneratingUnit", "TieFlow",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.ControlArea.ControlArea",
        title="ControlArea",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ControlArea" user definitions:
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

    ControlAreaGeneratingUnit = Instance("CIM13r19.ControlArea.ControlAreaGeneratingUnit",
        transient=True,
        opposite="AltGeneratingUnitMeas",
        editor=InstanceEditor(name="_controlareageneratingunits"))

    def _get_controlareageneratingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.ControlArea.ControlAreaGeneratingUnit" ]
        else:
            return []

    _controlareageneratingunits = Property(fget=_get_controlareageneratingunits)

    AnalogValue = Instance("CIM13r19.Meas.AnalogValue",
        transient=True,
        opposite="AltGeneratingUnit",
        editor=InstanceEditor(name="_analogvalues"))

    def _get_analogvalues(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.AnalogValue" ]
        else:
            return []

    _analogvalues = Property(fget=_get_analogvalues)

    # Priority of a measurement usage.   Lower numbers have first priority.
    priority = Int(desc="Priority of a measurement usage.   Lower numbers have first priority.")

    #--------------------------------------------------------------------------
    #  Begin "AltGeneratingUnitMeas" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("priority",
                label="Attributes"),
            VGroup("Parent", "ControlAreaGeneratingUnit", "AnalogValue",
                label="References"),
            dock="tab"),
        id="CIM13r19.ControlArea.AltGeneratingUnitMeas",
        title="AltGeneratingUnitMeas",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AltGeneratingUnitMeas" user definitions:
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

    # A terminal may participate in zero, one, or two control areas as a tie flow.
    Terminal = Instance("CIM13r19.Core.Terminal",
        desc="A terminal may participate in zero, one, or two control areas as a tie flow.",
        transient=True,
        opposite="TieFlow",
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

    AltTieMeas = List(Instance("CIM13r19.ControlArea.AltTieMeas"))

    ControlArea = Instance("CIM13r19.ControlArea.ControlArea",
        transient=True,
        opposite="TieFlow",
        editor=InstanceEditor(name="_controlareas"))

    def _get_controlareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.ControlArea.ControlArea" ]
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
            VGroup("positiveFlowIn",
                label="Attributes"),
            VGroup("Parent", "Terminal", "AltTieMeas", "ControlArea",
                label="References"),
            dock="tab"),
        id="CIM13r19.ControlArea.TieFlow",
        title="TieFlow",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TieFlow" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AltTieMeas" class:
#------------------------------------------------------------------------------

class AltTieMeas(Element):
    """ A prioritized measurement to be used for the tie flow as part of the control area specification.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    TieFlow = Instance("CIM13r19.ControlArea.TieFlow",
        transient=True,
        opposite="AltTieMeas",
        editor=InstanceEditor(name="_tieflows"))

    def _get_tieflows(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.ControlArea.TieFlow" ]
        else:
            return []

    _tieflows = Property(fget=_get_tieflows)

    AnalogValue = Instance("CIM13r19.Meas.AnalogValue",
        transient=True,
        opposite="AltTieMeas",
        editor=InstanceEditor(name="_analogvalues"))

    def _get_analogvalues(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Meas.AnalogValue" ]
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
            VGroup("priority",
                label="Attributes"),
            VGroup("Parent", "TieFlow", "AnalogValue",
                label="References"),
            dock="tab"),
        id="CIM13r19.ControlArea.AltTieMeas",
        title="AltTieMeas",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AltTieMeas" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
