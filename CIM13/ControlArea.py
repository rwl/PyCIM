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

from CIM13 import Root
from CIM13.Core import PowerSystemResource



from enthought.traits.api import Instance, List, Enum, Float, Int, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


ControlAreaTypeKind = Enum("AGC", "Interchange", "Forecast")

#------------------------------------------------------------------------------
#  "ControlAreaGeneratingUnit" class:
#------------------------------------------------------------------------------

class ControlAreaGeneratingUnit(Root):
    """ A control area generating unit. This class is needed so that alternate control area definitions may include the same generating unit.   Note only one instance within a control area should reference a specific generating unit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    GeneratingUnit = Instance("CIM13.Generation.Production.GeneratingUnit",
        opposite="ControlAreaGeneratingUnit")

    AltGeneratingUnitMeas = List(Instance("CIM13.ControlArea.AltGeneratingUnitMeas"))

    ControlArea = Instance("CIM13.ControlArea.ControlArea",
        opposite="ControlAreaGeneratingUnit")

    #--------------------------------------------------------------------------
    #  Begin "ControlAreaGeneratingUnit" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("ContainedBy", "GeneratingUnit", "AltGeneratingUnitMeas", "ControlArea",
                label="References"),
            dock="tab"),
        id="CIM13.ControlArea.ControlAreaGeneratingUnit",
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

    BusNameMarker = List(Instance("CIM13.Topology.BusNameMarker"))

    EnergyArea = Instance("CIM13.LoadModel.EnergyArea",
        opposite="ControlArea")

    TopologicalNode = List(Instance("CIM13.Topology.TopologicalNode"))

    ControlAreaGeneratingUnit = List(Instance("CIM13.ControlArea.ControlAreaGeneratingUnit"))

    TieFlow = List(Instance("CIM13.ControlArea.TieFlow"))

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
            VGroup("URI", "name", "localName", "description", "aliasName", "mRID", "pathName", "type", "pTolerance", "netInterchange",
                label="Attributes"),
            VGroup("ContainedBy", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "BusNameMarker", "EnergyArea", "TopologicalNode", "ControlAreaGeneratingUnit", "TieFlow",
                label="References", columns=1),
            dock="tab"),
        id="CIM13.ControlArea.ControlArea",
        title="ControlArea",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ControlArea" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AltGeneratingUnitMeas" class:
#------------------------------------------------------------------------------

class AltGeneratingUnitMeas(Root):
    """ A prioritized measurement to be used for the generating unit in the control area specificaiton.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ControlAreaGeneratingUnit = Instance("CIM13.ControlArea.ControlAreaGeneratingUnit",
        opposite="AltGeneratingUnitMeas")

    AnalogValue = Instance("CIM13.Meas.AnalogValue",
        opposite="AltGeneratingUnit")

    # Priority of a measurement usage.   Lower numbers have first priority.
    priority = Int(desc="Priority of a measurement usage.   Lower numbers have first priority.")

    #--------------------------------------------------------------------------
    #  Begin "AltGeneratingUnitMeas" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "priority",
                label="Attributes"),
            VGroup("ContainedBy", "ControlAreaGeneratingUnit", "AnalogValue",
                label="References"),
            dock="tab"),
        id="CIM13.ControlArea.AltGeneratingUnitMeas",
        title="AltGeneratingUnitMeas",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AltGeneratingUnitMeas" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TieFlow" class:
#------------------------------------------------------------------------------

class TieFlow(Root):
    """ A flow specification in terms of location and direction for a control area.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A terminal may participate in zero, one, or two control areas as a tie flow.
    Terminal = Instance("CIM13.Core.Terminal",
        desc="A terminal may participate in zero, one, or two control areas as a tie flow.",
        opposite="TieFlow")

    AltTieMeas = List(Instance("CIM13.ControlArea.AltTieMeas"))

    ControlArea = Instance("CIM13.ControlArea.ControlArea",
        opposite="TieFlow")

    # The flow is positive into the terminal.  A flow is positive if it is an import into the control area.
    positiveFlowIn = Bool(desc="The flow is positive into the terminal.  A flow is positive if it is an import into the control area.")

    #--------------------------------------------------------------------------
    #  Begin "TieFlow" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "positiveFlowIn",
                label="Attributes"),
            VGroup("ContainedBy", "Terminal", "AltTieMeas", "ControlArea",
                label="References"),
            dock="tab"),
        id="CIM13.ControlArea.TieFlow",
        title="TieFlow",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TieFlow" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AltTieMeas" class:
#------------------------------------------------------------------------------

class AltTieMeas(Root):
    """ A prioritized measurement to be used for the tie flow as part of the control area specification.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    TieFlow = Instance("CIM13.ControlArea.TieFlow",
        opposite="AltTieMeas")

    AnalogValue = Instance("CIM13.Meas.AnalogValue",
        opposite="AltTieMeas")

    # Priority of a measurement usage.   Lower numbers have first priority.
    priority = Int(desc="Priority of a measurement usage.   Lower numbers have first priority.")

    #--------------------------------------------------------------------------
    #  Begin "AltTieMeas" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "priority",
                label="Attributes"),
            VGroup("ContainedBy", "TieFlow", "AnalogValue",
                label="References"),
            dock="tab"),
        id="CIM13.ControlArea.AltTieMeas",
        title="AltTieMeas",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AltTieMeas" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
