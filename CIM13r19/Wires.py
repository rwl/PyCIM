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

from CIM13r19.Core import RegularIntervalSchedule
from CIM13r19.Core import ConductingEquipment
from CIM13r19.Core import IdentifiedObject
from CIM13r19.Core import PowerSystemResource
from CIM13r19.Core import EquipmentContainer
from CIM13r19.Core import Equipment
from CIM13r19 import Element
from CIM13r19.Core import Curve
from CIM13r19.Core import PhaseCode



from enthought.traits.api import Instance, List, Property, Enum, Float, Bool, Int, Str
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


WindingConnection = Enum("D", "Z", "Y")

TransformerCoolingType = Str

SVCControlMode = Enum("voltage", "reactivePower", "off")

TransformerControlMode = Enum("volt", "off", "local", "reactive", "active")

SynchronousMachineOperatingMode = Enum("generator", "condenser")

RegulatingControlModeKind = Enum("reactivePower", "currentFlow", "fixed", "activePower", "voltage")

WindingType = Enum("quaternary", "tertiary", "primary", "secondary")

CoolantType = Enum("hydrogenGas", "water", "air")

SynchronousMachineType = Enum("generator_or_condenser", "condenser", "generator")

TapChangerKind = Enum("voltageControl", "fixed", "phaseControl", "voltageAndPhaseControl")

#------------------------------------------------------------------------------
#  "RegulationSchedule" class:
#------------------------------------------------------------------------------

class RegulationSchedule(RegularIntervalSchedule):
    """ A pre-established pattern over time for a controlled variable, e.g., busbar voltage.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    RegulatingControl = List(Instance("CIM13r19.Wires.RegulatingControl"))

    # A VoltageControlZone may have a  voltage regulation schedule.
    VoltageControlZones = List(Instance("CIM13r19.Wires.VoltageControlZone"),
        desc="A VoltageControlZone may have a  voltage regulation schedule.")

    # Line drop resistance.
    lineDropR = Float(desc="Line drop resistance.")

    # Flag to indicate that line drop compensation is to be applied
    lineDropCompensation = Bool(desc="Flag to indicate that line drop compensation is to be applied")

    # Line drop reactance.
    lineDropX = Float(desc="Line drop reactance.")

    #--------------------------------------------------------------------------
    #  Begin "RegulationSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "value2Unit", "startTime", "value2Multiplier", "value1Unit", "value1Multiplier", "timeStep", "endTime", "lineDropR", "lineDropCompensation", "lineDropX",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "RegulatingControl", "VoltageControlZones",
                label="References"),
            dock="tab"),
        id="CIM13r19.Wires.RegulationSchedule",
        title="RegulationSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegulationSchedule" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TransformerWinding" class:
#------------------------------------------------------------------------------

class TransformerWinding(ConductingEquipment):
    """ A winding is associated with each defined terminal of a transformer (or phase shifter).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The winding to which the test was conducted
    To_WindingTest = List(Instance("CIM13r19.Wires.WindingTest"),
        desc="The winding to which the test was conducted")

    # The winding from which the test was conducted
    From_WindingTest = List(Instance("CIM13r19.Wires.WindingTest"),
        desc="The winding from which the test was conducted")

    # A transformer winding may have tap changers, separately for voltage and phase angle.  If a TransformerWinding does not have an associated TapChanger, the winding is assumed to be fixed tap.
    TapChangers = List(Instance("CIM13r19.Wires.TapChanger"),
        desc="A transformer winding may have tap changers, separately for voltage and phase angle.  If a TransformerWinding does not have an associated TapChanger, the winding is assumed to be fixed tap.")

    # A transformer has windings
    MemberOf_PowerTransformer = Instance("CIM13r19.Wires.PowerTransformer",
        desc="A transformer has windings",
        transient=True,
        opposite="Contains_TransformerWindings",
        editor=InstanceEditor(name="_powertransformers"))

    def _get_powertransformers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.PowerTransformer" ]
        else:
            return []

    _powertransformers = Property(fget=_get_powertransformers)

    # The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.
    ratedU = Float(desc="The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.")

    # Ground resistance path through connected grounding transformer.
    rground = Float(desc="Ground resistance path through connected grounding transformer.")

    # Zero sequence magnetizing branch susceptance.
    b0 = Float(desc="Zero sequence magnetizing branch susceptance.")

    # Positive sequence series resistance of the winding.
    r = Float(desc="Positive sequence series resistance of the winding.")

    # Ground reactance path through connected grounding transformer.
    xground = Float(desc="Ground reactance path through connected grounding transformer.")

    # Magnetizing branch susceptance (B mag).
    b = Float(desc="Magnetizing branch susceptance (B mag).")

    # Zero sequence series resistance of the winding.
    r0 = Float(desc="Zero sequence series resistance of the winding.")

    # Set if the winding is grounded.
    grounded = Bool(desc="Set if the winding is grounded.")

    # Apparent power that the winding can carry for a short period of time.
    shortTermS = Float(desc="Apparent power that the winding can carry for a short period of time.")

    # The normal apparent power rating for the winding
    ratedS = Float(desc="The normal apparent power rating for the winding")

    # Positive sequence series reactance of the winding.
    x = Float(desc="Positive sequence series reactance of the winding.")

    # The type of winding.
    windingType = WindingType(desc="The type of winding.")

    # The apparent power that the winding can carry  under emergency conditions.
    emergencyS = Float(desc="The apparent power that the winding can carry  under emergency conditions.")

    # Basic insulation level voltage rating
    insulationU = Float(desc="Basic insulation level voltage rating")

    # Magnetizing branch conductance (G mag).
    g = Float(desc="Magnetizing branch conductance (G mag).")

    # Zero sequence magnetizing branch conductance.
    g0 = Float(desc="Zero sequence magnetizing branch conductance.")

    # Zero sequence series reactance of the winding.
    x0 = Float(desc="Zero sequence series reactance of the winding.")

    # The type of connection of the winding.
    connectionType = WindingConnection(desc="The type of connection of the winding.")

    #--------------------------------------------------------------------------
    #  Begin "TransformerWinding" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "ratedU", "rground", "b0", "r", "xground", "b", "r0", "grounded", "shortTermS", "ratedS", "x", "windingType", "emergencyS", "insulationU", "g", "g0", "x0", "connectionType",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "To_WindingTest", "From_WindingTest", "TapChangers", "MemberOf_PowerTransformer",
                label="References", columns=2),
            dock="tab"),
        id="CIM13r19.Wires.TransformerWinding",
        title="TransformerWinding",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TransformerWinding" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EnergySource" class:
#------------------------------------------------------------------------------

class EnergySource(ConductingEquipment):
    """ A generic equivalent for an energy supplier on a transmission or distribution voltage level.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Zero sequence Thevenin resistance.
    r0 = Float(desc="Zero sequence Thevenin resistance.")

    # Phase-to-phase nominal voltage.
    nominalVoltage = Float(desc="Phase-to-phase nominal voltage.")

    # Positive sequence Thevenin resistance.
    r = Float(desc="Positive sequence Thevenin resistance.")

    # Phase-to-phase open circuit voltage magnitude.
    voltageMagnitude = Float(desc="Phase-to-phase open circuit voltage magnitude.")

    # Positive sequence Thevenin reactance.
    x = Float(desc="Positive sequence Thevenin reactance.")

    # Phase angle of a-phase open circuit.
    voltageAngle = Float(desc="Phase angle of a-phase open circuit.")

    # Negative sequence Thevenin resistance.
    rn = Float(desc="Negative sequence Thevenin resistance.")

    # High voltage source load
    activePower = Float(desc="High voltage source load")

    # Negative sequence Thevenin reactance.
    xn = Float(desc="Negative sequence Thevenin reactance.")

    # Zero sequence Thevenin reactance.
    x0 = Float(desc="Zero sequence Thevenin reactance.")

    #--------------------------------------------------------------------------
    #  Begin "EnergySource" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "r0", "nominalVoltage", "r", "voltageMagnitude", "x", "voltageAngle", "rn", "activePower", "xn", "x0",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.EnergySource",
        title="EnergySource",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EnergySource" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SeriesCompensator" class:
#------------------------------------------------------------------------------

class SeriesCompensator(ConductingEquipment):
    """ A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Positive sequence reactance.
    x = Float(desc="Positive sequence reactance.")

    # Positive sequence resistance.
    r = Float(desc="Positive sequence resistance.")

    #--------------------------------------------------------------------------
    #  Begin "SeriesCompensator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "x", "r",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.SeriesCompensator",
        title="SeriesCompensator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SeriesCompensator" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WireType" class:
#------------------------------------------------------------------------------

class WireType(IdentifiedObject):
    """ Wire conductor (per IEEE specs). A specific type of wire or combination of wires, not insulated from each other, suitable for carrying electrical current.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A WireType is mounted at a specified place in a WireArrangement.
    WireArrangements = List(Instance("CIM13r19.Wires.WireArrangement"),
        desc="A WireType is mounted at a specified place in a WireArrangement.")

    # Number of conductor strands in the (symmetrical) bundle (1-12)
    phaseConductorCount = Int(desc="Number of conductor strands in the (symmetrical) bundle (1-12)")

    # Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor.
    gMR = Float(desc="Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor.")

    # Distance between conductor strands in a (symmetrical) bundle.
    phaseConductorSpacing = Float(desc="Distance between conductor strands in a (symmetrical) bundle.")

    # Current carrying capacity of a wire or cable under stated thermal conditions
    ratedCurrent = Float(desc="Current carrying capacity of a wire or cable under stated thermal conditions")

    # The radius of the conductor
    radius = Float(desc="The radius of the conductor")

    # The resistance per unit length of the conductor
    resistance = Float(desc="The resistance per unit length of the conductor")

    #--------------------------------------------------------------------------
    #  Begin "WireType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "phaseConductorCount", "gMR", "phaseConductorSpacing", "ratedCurrent", "radius", "resistance",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "WireArrangements",
                label="References"),
            dock="tab"),
        id="CIM13r19.Wires.WireType",
        title="WireType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WireType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "VoltageControlZone" class:
#------------------------------------------------------------------------------

class VoltageControlZone(PowerSystemResource):
    """ An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A VoltageControlZone may have a  voltage regulation schedule.
    RegulationSchedule = Instance("CIM13r19.Wires.RegulationSchedule",
        desc="A VoltageControlZone may have a  voltage regulation schedule.",
        transient=True,
        opposite="VoltageControlZones",
        editor=InstanceEditor(name="_regulationschedules"))

    def _get_regulationschedules(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.RegulationSchedule" ]
        else:
            return []

    _regulationschedules = Property(fget=_get_regulationschedules)

    # A VoltageControlZone is controlled by a designated BusbarSection.
    BusbarSection = Instance("CIM13r19.Wires.BusbarSection",
        desc="A VoltageControlZone is controlled by a designated BusbarSection.",
        transient=True,
        opposite="VoltageControlZone",
        editor=InstanceEditor(name="_busbarsections"))

    def _get_busbarsections(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.BusbarSection" ]
        else:
            return []

    _busbarsections = Property(fget=_get_busbarsections)

    #--------------------------------------------------------------------------
    #  Begin "VoltageControlZone" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "RegulationSchedule", "BusbarSection",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.VoltageControlZone",
        title="VoltageControlZone",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "VoltageControlZone" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RegulatingCondEq" class:
#------------------------------------------------------------------------------

class RegulatingCondEq(ConductingEquipment):
    """ RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    RegulatingControl = Instance("CIM13r19.Wires.RegulatingControl",
        transient=True,
        opposite="RegulatingCondEq",
        editor=InstanceEditor(name="_regulatingcontrols"))

    def _get_regulatingcontrols(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.RegulatingControl" ]
        else:
            return []

    _regulatingcontrols = Property(fget=_get_regulatingcontrols)

    # The association gives the control output that is used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuators.
    Controls = List(Instance("CIM13r19.Meas.Control"),
        desc="The association gives the control output that is used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuators.")

    #--------------------------------------------------------------------------
    #  Begin "RegulatingCondEq" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "RegulatingControl", "Controls",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.RegulatingCondEq",
        title="RegulatingCondEq",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegulatingCondEq" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Conductor" class:
#------------------------------------------------------------------------------

class Conductor(ConductingEquipment):
    """ Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Sections of conductor are physically described by a conductor type
    ConductorType = Instance("CIM13r19.Wires.ConductorType",
        desc="Sections of conductor are physically described by a conductor type",
        transient=True,
        opposite="Conductors",
        editor=InstanceEditor(name="_conductortypes"))

    def _get_conductortypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.ConductorType" ]
        else:
            return []

    _conductortypes = Property(fget=_get_conductortypes)

    # Zero sequence series resistance of the entire line section.
    r0 = Float(desc="Zero sequence series resistance of the entire line section.")

    # Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
    g0ch = Float(desc="Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.")

    # Segment length for calculating line section capabilities
    length = Float(desc="Segment length for calculating line section capabilities")

    # Positive sequence series reactance of the entire line section.
    x = Float(desc="Positive sequence series reactance of the entire line section.")

    # Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
    gch = Float(desc="Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.")

    # Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
    b0ch = Float(desc="Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.")

    # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
    bch = Float(desc="Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.")

    # Zero sequence series reactance of the entire line section.
    x0 = Float(desc="Zero sequence series reactance of the entire line section.")

    # Positive sequence series resistance of the entire line section.
    r = Float(desc="Positive sequence series resistance of the entire line section.")

    #--------------------------------------------------------------------------
    #  Begin "Conductor" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "r0", "g0ch", "length", "x", "gch", "b0ch", "bch", "x0", "r",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "ConductorType",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.Conductor",
        title="Conductor",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Conductor" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Line" class:
#------------------------------------------------------------------------------

class Line(EquipmentContainer):
    """ A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A Line can be contained by a SubGeographical Region.
    Region = Instance("CIM13r19.Core.SubGeographicalRegion",
        desc="A Line can be contained by a SubGeographical Region.",
        transient=True,
        opposite="Lines",
        editor=InstanceEditor(name="_subgeographicalregions"))

    def _get_subgeographicalregions(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.SubGeographicalRegion" ]
        else:
            return []

    _subgeographicalregions = Property(fget=_get_subgeographicalregions)

    #--------------------------------------------------------------------------
    #  Begin "Line" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "TopologicalNode", "ConnectivityNodes", "Contains_Equipments", "Region",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.Line",
        title="Line",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Line" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Ground" class:
#------------------------------------------------------------------------------

class Ground(ConductingEquipment):
    """ A common point for connecting grounded conducting equipment such as shunt capacitors. The power system model can have more than one ground.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "Ground" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.Ground",
        title="Ground",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Ground" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TapChanger" class:
#------------------------------------------------------------------------------

class TapChanger(PowerSystemResource):
    """ Mechanism for changing transformer winding tap positions.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A transformer winding may have tap changers, separately for voltage and phase angle.  If a TransformerWinding does not have an associated TapChanger, the winding is assumed to be fixed tap.
    TransformerWinding = Instance("CIM13r19.Wires.TransformerWinding",
        desc="A transformer winding may have tap changers, separately for voltage and phase angle.  If a TransformerWinding does not have an associated TapChanger, the winding is assumed to be fixed tap.",
        transient=True,
        opposite="TapChangers",
        editor=InstanceEditor(name="_transformerwindings"))

    def _get_transformerwindings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.TransformerWinding" ]
        else:
            return []

    _transformerwindings = Property(fget=_get_transformerwindings)

    RegulatingControl = Instance("CIM13r19.Wires.RegulatingControl",
        transient=True,
        opposite="TapChanger",
        editor=InstanceEditor(name="_regulatingcontrols"))

    def _get_regulatingcontrols(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.RegulatingControl" ]
        else:
            return []

    _regulatingcontrols = Property(fget=_get_regulatingcontrols)

    # The neutral tap step position for this winding.
    neutralStep = Int(desc="The neutral tap step position for this winding.")

    # Lowest possible tap step position, retard from neutral
    lowStep = Int(desc="Lowest possible tap step position, retard from neutral")

    # For an LTC, the tap changer control mode.
    tculControlMode = TransformerControlMode(desc="For an LTC, the tap changer control mode.")

    # Voltage at which the winding operates at the neutral tap setting.
    neutralU = Float(desc="Voltage at which the winding operates at the neutral tap setting.")

    # The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.
    normalStep = Int(desc="The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.")

    # Highest possible tap step position, advance from neutral
    highStep = Int(desc="Highest possible tap step position, advance from neutral")

    # The type of tap changer. Indicates the ability of the transformer to perform various regulation tasks. The tap changer must be also be associated wtih a RegulationControl object before any regulation is possible.
    type = TapChangerKind(desc="The type of tap changer. Indicates the ability of the transformer to perform various regulation tasks. The tap changer must be also be associated wtih a RegulationControl object before any regulation is possible.")

    # Tap step increment, in per cent of nominal voltage, per step position.
    stepVoltageIncrement = Float(desc="Tap step increment, in per cent of nominal voltage, per step position.")

    # For an LTC, the delay for subsequent tap changer operation (second and later step changes)
    subsequentDelay = Float(desc="For an LTC, the delay for subsequent tap changer operation (second and later step changes)")

    # For an LTC, the delay for initial tap changer operation (first step change)
    initialDelay = Float(desc="For an LTC, the delay for initial tap changer operation (first step change)")

    # Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer).
    stepPhaseShiftIncrement = Float(desc="Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer).")

    #--------------------------------------------------------------------------
    #  Begin "TapChanger" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "neutralStep", "lowStep", "tculControlMode", "neutralU", "normalStep", "highStep", "type", "stepVoltageIncrement", "subsequentDelay", "initialDelay", "stepPhaseShiftIncrement",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "TransformerWinding", "RegulatingControl",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.TapChanger",
        title="TapChanger",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TapChanger" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CompositeSwitch" class:
#------------------------------------------------------------------------------

class CompositeSwitch(Equipment):
    """ A model of a set of individual Switches normally enclosed within the same cabinet and possibly with interlocks that restrict the combination of switch positions. These are typically found in medium voltage distribution networks.  A CompositeSwitch could represent a Ring-Main-Unit (RMU), or pad-mounted switchgear, with primitive internal devices such as an internal bus-bar plus 3 or 4 internal switches each of which may individually be open or closed. A CompositeSwitch and a set of contained Switches can also be used to represent a multi-position switch e.g. a switch that can connect a circuit to Ground, Open or Busbar.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Switches = List(Instance("CIM13r19.Wires.Switch"))

    # An alphanumeric code that can be used as a reference to extar information such as the description of the interlocking scheme if any
    compositeSwitchType = Str(desc="An alphanumeric code that can be used as a reference to extar information such as the description of the interlocking scheme if any")

    #--------------------------------------------------------------------------
    #  Begin "CompositeSwitch" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "compositeSwitchType",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Switches",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.CompositeSwitch",
        title="CompositeSwitch",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CompositeSwitch" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WireArrangement" class:
#------------------------------------------------------------------------------

class WireArrangement(IdentifiedObject):
    """ Identification, spacing and configuration of the wires of a ConductorType, with reference to their type.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A ConductorType is made up of wires that can be configured in several ways.
    ConductorType = Instance("CIM13r19.Wires.ConductorType",
        desc="A ConductorType is made up of wires that can be configured in several ways.",
        transient=True,
        opposite="WireArrangements",
        editor=InstanceEditor(name="_conductortypes"))

    def _get_conductortypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.ConductorType" ]
        else:
            return []

    _conductortypes = Property(fget=_get_conductortypes)

    # A WireType is mounted at a specified place in a WireArrangement.
    WireType = Instance("CIM13r19.Wires.WireType",
        desc="A WireType is mounted at a specified place in a WireArrangement.",
        transient=True,
        opposite="WireArrangements",
        editor=InstanceEditor(name="_wiretypes"))

    def _get_wiretypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.WireType" ]
        else:
            return []

    _wiretypes = Property(fget=_get_wiretypes)

    # Mounting point where wire One is mounted.
    mountingPointX = Int(desc="Mounting point where wire One is mounted.")

    # Mounting point where wire One is mounted.
    mountingPointY = Int(desc="Mounting point where wire One is mounted.")

    #--------------------------------------------------------------------------
    #  Begin "WireArrangement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "mountingPointX", "mountingPointY",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ConductorType", "WireType",
                label="References"),
            dock="tab"),
        id="CIM13r19.Wires.WireArrangement",
        title="WireArrangement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WireArrangement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PowerTransformer" class:
#------------------------------------------------------------------------------

class PowerTransformer(Equipment):
    """ An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A transformer has windings
    Contains_TransformerWindings = List(Instance("CIM13r19.Wires.TransformerWinding"),
        desc="A transformer has windings")

    # A transformer may have a heat exchanger
    HeatExchanger = Instance("CIM13r19.Wires.HeatExchanger",
        desc="A transformer may have a heat exchanger",
        transient=True,
        opposite="PowerTransformer",
        editor=InstanceEditor(name="_heatexchangers"))

    def _get_heatexchangers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.HeatExchanger" ]
        else:
            return []

    _heatexchangers = Property(fget=_get_heatexchangers)

    # Type of transformer cooling
    transfCoolingType = TransformerCoolingType(desc="Type of transformer cooling")

    # Describes the phases carried by a power transformer.
    phases = PhaseCode(desc="Describes the phases carried by a power transformer.")

    # Core shunt magnetizing susceptance in the saturation region.
    bmagSat = Float(desc="Core shunt magnetizing susceptance in the saturation region.")

    # Core magnetizing saturation curve knee flux level.
    magSatFlux = Float(desc="Core magnetizing saturation curve knee flux level.")

    # The reference voltage at which the magnetizing saturation measurements were made
    magBaseU = Float(desc="The reference voltage at which the magnetizing saturation measurements were made")

    #--------------------------------------------------------------------------
    #  Begin "PowerTransformer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "transfCoolingType", "phases", "bmagSat", "magSatFlux", "magBaseU",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Contains_TransformerWindings", "HeatExchanger",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.PowerTransformer",
        title="PowerTransformer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PowerTransformer" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MutualCoupling" class:
#------------------------------------------------------------------------------

class MutualCoupling(Element):
    """ This class represents the zero sequence line mutual coupling.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    First_ACLineSegment = Instance("CIM13r19.Wires.ACLineSegment",
        transient=True,
        opposite="HasFirst_MutualCoupling",
        editor=InstanceEditor(name="_aclinesegments"))

    def _get_aclinesegments(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.ACLineSegment" ]
        else:
            return []

    _aclinesegments = Property(fget=_get_aclinesegments)

    Second_ACLineSegment = Instance("CIM13r19.Wires.ACLineSegment",
        transient=True,
        opposite="HasSecond_MutualCoupling",
        editor=InstanceEditor(name="_aclinesegments"))

    def _get_aclinesegments(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.ACLineSegment" ]
        else:
            return []

    _aclinesegments = Property(fget=_get_aclinesegments)

    # Zero sequence branch-to-branch mutual impedance coupling, reactance
    x0 = Float(desc="Zero sequence branch-to-branch mutual impedance coupling, reactance")

    # Distance from the second line's from bus to end of coupled region
    distance22 = Float(desc="Distance from the second line's from bus to end of coupled region")

    # Distance from the first line's from bus to start of coupled region
    distance11 = Float(desc="Distance from the first line's from bus to start of coupled region")

    # Distance from the first line's from bus to end of coupled region
    distance12 = Float(desc="Distance from the first line's from bus to end of coupled region")

    # Zero sequence branch-to-branch mutual impedance coupling, resistance
    r0 = Float(desc="Zero sequence branch-to-branch mutual impedance coupling, resistance")

    # Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section.
    b0ch = Float(desc="Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section.")

    # Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section.
    g0ch = Float(desc="Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section.")

    # Distance from the second line's from bus to start of coupled region
    distance21 = Float(desc="Distance from the second line's from bus to start of coupled region")

    #--------------------------------------------------------------------------
    #  Begin "MutualCoupling" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("x0", "distance22", "distance11", "distance12", "r0", "b0ch", "g0ch", "distance21",
                label="Attributes"),
            VGroup("Parent", "First_ACLineSegment", "Second_ACLineSegment",
                label="References"),
            dock="tab"),
        id="CIM13r19.Wires.MutualCoupling",
        title="MutualCoupling",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MutualCoupling" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RectifierInverter" class:
#------------------------------------------------------------------------------

class RectifierInverter(ConductingEquipment):
    """ Bi-directional AC-DC conversion equipment that can be used to control DC current, DC voltage, DC power flow, or firing angle.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Rectifier/inverter primary base voltage
    ratedU = Float(desc="Rectifier/inverter primary base voltage")

    # Operating mode for the converter.
    operatingMode = Str(desc="Operating mode for the converter.")

    # Frequency on the AC side.
    frequency = Float(desc="Frequency on the AC side.")

    # The maximum voltage on the DC side at which the converter should operate.
    maxU = Float(desc="The maximum voltage on the DC side at which the converter should operate.")

    # Commutating resistance.
    commutatingResistance = Float(desc="Commutating resistance.")

    # The minimum active power on the DC side at which the converter should operate.
    minP = Float(desc="The minimum active power on the DC side at which the converter should operate.")

    # Number of bridges
    bridges = Int(desc="Number of bridges")

    # Commutating reactance at AC bus frequency.
    commutatingReactance = Float(desc="Commutating reactance at AC bus frequency.")

    # The maximum active power on the DC side at which the fconverter should operate.
    maxP = Float(desc="The maximum active power on the DC side at which the fconverter should operate.")

    # Minimum compounded DC voltage
    minCompoundVoltage = Float(desc="Minimum compounded DC voltage")

    # Compounding resistance.
    compoundResistance = Float(desc="Compounding resistance.")

    # The minimum voltage on the DC side at which the converter should operate.
    minU = Float(desc="The minimum voltage on the DC side at which the converter should operate.")

    #--------------------------------------------------------------------------
    #  Begin "RectifierInverter" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "ratedU", "operatingMode", "frequency", "maxU", "commutatingResistance", "minP", "bridges", "commutatingReactance", "maxP", "minCompoundVoltage", "compoundResistance", "minU",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.RectifierInverter",
        title="RectifierInverter",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RectifierInverter" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "HeatExchanger" class:
#------------------------------------------------------------------------------

class HeatExchanger(Equipment):
    """ Equipment for the cooling of electrical equipment and the extraction of heat
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A transformer may have a heat exchanger
    PowerTransformer = Instance("CIM13r19.Wires.PowerTransformer",
        desc="A transformer may have a heat exchanger",
        transient=True,
        opposite="HeatExchanger",
        editor=InstanceEditor(name="_powertransformers"))

    def _get_powertransformers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.PowerTransformer" ]
        else:
            return []

    _powertransformers = Property(fget=_get_powertransformers)

    #--------------------------------------------------------------------------
    #  Begin "HeatExchanger" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "PowerTransformer",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.HeatExchanger",
        title="HeatExchanger",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HeatExchanger" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EnergyConsumer" class:
#------------------------------------------------------------------------------

class EnergyConsumer(ConductingEquipment):
    """ Generic user of energy - a  point of consumption on the power system model
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # An energy consumer is assigned to a power cut zone
    PowerCutZone = Instance("CIM13r19.LoadModel.PowerCutZone",
        desc="An energy consumer is assigned to a power cut zone",
        transient=True,
        opposite="EnergyConsumers",
        editor=InstanceEditor(name="_powercutzones"))

    def _get_powercutzones(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.LoadModel.PowerCutZone" ]
        else:
            return []

    _powercutzones = Property(fget=_get_powercutzones)

    LoadResponse = Instance("CIM13r19.LoadModel.LoadResponseCharacteristic",
        transient=True,
        opposite="EnergyConsumer",
        editor=InstanceEditor(name="_loadresponsecharacteristics"))

    def _get_loadresponsecharacteristics(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.LoadModel.LoadResponseCharacteristic" ]
        else:
            return []

    _loadresponsecharacteristics = Property(fget=_get_loadresponsecharacteristics)

    # Number of individual customers represented by this Demand
    customerCount = Int(desc="Number of individual customers represented by this Demand")

    # Reactive power of the load that is a fixed quantity.
    qfixed = Float(desc="Reactive power of the load that is a fixed quantity.")

    # Active power of the load that is a fixed quantity.
    pfixed = Float(desc="Active power of the load that is a fixed quantity.")

    # Fixed reactive power as per cent of load group fixed reactive power.
    qfixedPct = Float(desc="Fixed reactive power as per cent of load group fixed reactive power.")

    # Fixed active power as per cent of load group fixed active power
    pfixedPct = Float(desc="Fixed active power as per cent of load group fixed active power")

    #--------------------------------------------------------------------------
    #  Begin "EnergyConsumer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "customerCount", "qfixed", "pfixed", "qfixedPct", "pfixedPct",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "PowerCutZone", "LoadResponse",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.EnergyConsumer",
        title="EnergyConsumer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EnergyConsumer" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Switch" class:
#------------------------------------------------------------------------------

class Switch(ConductingEquipment):
    """ A generic device designed to close, or open, or both, one or more electric circuits.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A switch may be operated by many schedules.
    SwitchingOperations = List(Instance("CIM13r19.Outage.SwitchingOperation"),
        desc="A switch may be operated by many schedules.")

    CompositeSwitch = Instance("CIM13r19.Wires.CompositeSwitch",
        transient=True,
        opposite="Switches",
        editor=InstanceEditor(name="_compositeswitchs"))

    def _get_compositeswitchs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.CompositeSwitch" ]
        else:
            return []

    _compositeswitchs = Property(fget=_get_compositeswitchs)

    # Branch is retained in a bus branch model.
    retained = Bool(desc="Branch is retained in a bus branch model.")

    # The date and time when the switch was last switched on.
    switchOnDate = Str(desc="The date and time when the switch was last switched on.")

    # The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.
    normalOpen = Bool(desc="The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.")

    # The switch on count since the switch was last reset or initialized.
    switchOnCount = Int(desc="The switch on count since the switch was last reset or initialized.")

    #--------------------------------------------------------------------------
    #  Begin "Switch" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "retained", "switchOnDate", "normalOpen", "switchOnCount",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "SwitchingOperations", "CompositeSwitch",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.Switch",
        title="Switch",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Switch" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RegulatingControl" class:
#------------------------------------------------------------------------------

class RegulatingControl(PowerSystemResource):
    """ Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    RegulatingCondEq = List(Instance("CIM13r19.Wires.RegulatingCondEq"))

    TapChanger = List(Instance("CIM13r19.Wires.TapChanger"))

    Terminal = Instance("CIM13r19.Core.Terminal",
        transient=True,
        opposite="RegulatingControl",
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

    RegulationSchedule = Instance("CIM13r19.Wires.RegulationSchedule",
        transient=True,
        opposite="RegulatingControl",
        editor=InstanceEditor(name="_regulationschedules"))

    def _get_regulationschedules(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.RegulationSchedule" ]
        else:
            return []

    _regulationschedules = Property(fget=_get_regulationschedules)

    # The target value specified for case input.   This value can be used for the target value wihout the use of schedules. The value has the units appropriate to the mode attribute.
    targetValue = Float(desc="The target value specified for case input.   This value can be used for the target value wihout the use of schedules. The value has the units appropriate to the mode attribute.")

    # The regulation is performed in a discrete mode.
    discrete = Bool(desc="The regulation is performed in a discrete mode.")

    # This is the case input target range.   This performs the same function as the value2 attribute on the regulation schedule in the case that schedules are not used.   The units of those appropriate for the mode.
    targetRange = Float(desc="This is the case input target range.   This performs the same function as the value2 attribute on the regulation schedule in the case that schedules are not used.   The units of those appropriate for the mode.")

    # The regulating control mode presently available.  This specifications allows for determining the kind of regualation without need for obtaining the units from a schedule.
    mode = RegulatingControlModeKind(desc="The regulating control mode presently available.  This specifications allows for determining the kind of regualation without need for obtaining the units from a schedule.")

    #--------------------------------------------------------------------------
    #  Begin "RegulatingControl" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "targetValue", "discrete", "targetRange", "mode",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "RegulatingCondEq", "TapChanger", "Terminal", "RegulationSchedule",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.RegulatingControl",
        title="RegulatingControl",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegulatingControl" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Connector" class:
#------------------------------------------------------------------------------

class Connector(ConductingEquipment):
    """ A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation and are modelled with a single logical terminal.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "Connector" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.Connector",
        title="Connector",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Connector" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "WindingTest" class:
#------------------------------------------------------------------------------

class WindingTest(IdentifiedObject):
    """ Physical winding test data for the winding/tap pairs of a transformer (or phase shifter). This test data can be used to derive other attributes of specific transformer or phase shifter models.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The winding to which the test was conducted
    To_TransformerWinding = Instance("CIM13r19.Wires.TransformerWinding",
        desc="The winding to which the test was conducted",
        transient=True,
        opposite="To_WindingTest",
        editor=InstanceEditor(name="_transformerwindings"))

    def _get_transformerwindings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.TransformerWinding" ]
        else:
            return []

    _transformerwindings = Property(fget=_get_transformerwindings)

    # The winding from which the test was conducted
    From_TransformerWinding = Instance("CIM13r19.Wires.TransformerWinding",
        desc="The winding from which the test was conducted",
        transient=True,
        opposite="From_WindingTest",
        editor=InstanceEditor(name="_transformerwindings"))

    def _get_transformerwindings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.TransformerWinding" ]
        else:
            return []

    _transformerwindings = Property(fget=_get_transformerwindings)

    # The load loss kW ('to' winding short-circuited) from the test report.
    loadLoss = Float(desc="The load loss kW ('to' winding short-circuited) from the test report.")

    # The tap step number for the 'to' winding of the test pair.
    toTapStep = Int(desc="The tap step number for the 'to' winding of the test pair.")

    # The tap step number for the 'from' winding of the test pair.
    fromTapStep = Int(desc="The tap step number for the 'from' winding of the test pair.")

    # The no load loss kW 'to' winding open-circuited) from the test report.
    noLoadLoss = Float(desc="The no load loss kW 'to' winding open-circuited) from the test report.")

    # The voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
    voltage = Float(desc="The voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.")

    # The phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
    phaseShift = Float(desc="The phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.")

    # The leakage impedance measured at the 'from' winding  with the 'to' winding short-circuited and all other windings open-circuited.  Leakage impedance is expressed in units based on the apparent power and voltage ratings of the 'from' winding.
    leakageImpedance = Float(desc="The leakage impedance measured at the 'from' winding  with the 'to' winding short-circuited and all other windings open-circuited.  Leakage impedance is expressed in units based on the apparent power and voltage ratings of the 'from' winding.")

    # The exciting current on open-circuit test, expressed as a percentage of rated current, at nominal voltage
    excitingCurrent = Float(desc="The exciting current on open-circuit test, expressed as a percentage of rated current, at nominal voltage")

    #--------------------------------------------------------------------------
    #  Begin "WindingTest" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "loadLoss", "toTapStep", "fromTapStep", "noLoadLoss", "voltage", "phaseShift", "leakageImpedance", "excitingCurrent",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "To_TransformerWinding", "From_TransformerWinding",
                label="References"),
            dock="tab"),
        id="CIM13r19.Wires.WindingTest",
        title="WindingTest",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WindingTest" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ConductorType" class:
#------------------------------------------------------------------------------

class ConductorType(IdentifiedObject):
    """ Wire or cable conductor (per IEEE specs). A specific type of wire or combination of wires not insulated from one another, suitable for carrying electric current. It may be bare or insulated.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Sections of conductor are physically described by a conductor type
    Conductors = List(Instance("CIM13r19.Wires.Conductor"),
        desc="Sections of conductor are physically described by a conductor type")

    # A ConductorType is made up of wires that can be configured in several ways.
    WireArrangements = List(Instance("CIM13r19.Wires.WireArrangement"),
        desc="A ConductorType is made up of wires that can be configured in several ways.")

    # Reactance of the sheath for cable conductors.
    sheathReactance = Float(desc="Reactance of the sheath for cable conductors.")

    # Resistance of the sheath for cable conductors.
    sheathResistance = Float(desc="Resistance of the sheath for cable conductors.")

    #--------------------------------------------------------------------------
    #  Begin "ConductorType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "sheathReactance", "sheathResistance",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Conductors", "WireArrangements",
                label="References"),
            dock="tab"),
        id="CIM13r19.Wires.ConductorType",
        title="ConductorType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConductorType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Plant" class:
#------------------------------------------------------------------------------

class Plant(EquipmentContainer):
    """ A Plant is a collection of equipment for purposes of generation.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "Plant" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "TopologicalNode", "ConnectivityNodes", "Contains_Equipments",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.Plant",
        title="Plant",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Plant" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ReactiveCapabilityCurve" class:
#------------------------------------------------------------------------------

class ReactiveCapabilityCurve(Curve):
    """ Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    SynchronousMachines = List(Instance("CIM13r19.Wires.SynchronousMachine"))

    # Defines the default MVArCapabilityCurve for use by a SynchronousMachine.
    InitiallyUsedBySynchronousMachine = List(Instance("CIM13r19.Wires.SynchronousMachine"),
        desc="Defines the default MVArCapabilityCurve for use by a SynchronousMachine.")

    # The machine's coolant temperature (e.g., ambient air or stator circulating water).
    coolantTemperature = Float(desc="The machine's coolant temperature (e.g., ambient air or stator circulating water).")

    # The hydrogen coolant pressure
    hydrogenPressure = Float(desc="The hydrogen coolant pressure")

    #--------------------------------------------------------------------------
    #  Begin "ReactiveCapabilityCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "y1Unit", "curveStyle", "y2Multiplier", "y2Unit", "y1Multiplier", "xMultiplier", "xUnit", "coolantTemperature", "hydrogenPressure",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveScheduleDatas", "SynchronousMachines", "InitiallyUsedBySynchronousMachine",
                label="References"),
            dock="tab"),
        id="CIM13r19.Wires.ReactiveCapabilityCurve",
        title="ReactiveCapabilityCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ReactiveCapabilityCurve" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GroundDisconnector" class:
#------------------------------------------------------------------------------

class GroundDisconnector(Switch):
    """ A manually operated or motor operated mechanical switching device used for isolating a circuit or equipment from Ground.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "GroundDisconnector" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "retained", "switchOnDate", "normalOpen", "switchOnCount",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "SwitchingOperations", "CompositeSwitch",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.GroundDisconnector",
        title="GroundDisconnector",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GroundDisconnector" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "FrequencyConverter" class:
#------------------------------------------------------------------------------

class FrequencyConverter(RegulatingCondEq):
    """ A device to convert from one frequency to another (e.g., frequency F1 to F2) comprises a pair of FrequencyConverter instances. One converts from F1 to DC, the other converts the DC to F2.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The maximum active power on the DC side at which the frequence converter should operate.
    maxP = Float(desc="The maximum active power on the DC side at which the frequence converter should operate.")

    # Frequency on the AC side.
    frequency = Float(desc="Frequency on the AC side.")

    # The minimum voltage on the DC side at which the frequency converter should operate.
    minU = Float(desc="The minimum voltage on the DC side at which the frequency converter should operate.")

    # The minimum active power on the DC side at which the frequence converter should operate.
    minP = Float(desc="The minimum active power on the DC side at which the frequence converter should operate.")

    # Operating mode for the frequency converter
    operatingMode = Str(desc="Operating mode for the frequency converter")

    # The maximum voltage on the DC side at which the frequency converter should operate.
    maxU = Float(desc="The maximum voltage on the DC side at which the frequency converter should operate.")

    #--------------------------------------------------------------------------
    #  Begin "FrequencyConverter" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "maxP", "frequency", "minU", "minP", "operatingMode", "maxU",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "RegulatingControl", "Controls",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.FrequencyConverter",
        title="FrequencyConverter",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FrequencyConverter" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ProtectedSwitch" class:
#------------------------------------------------------------------------------

class ProtectedSwitch(Switch):
    """ A ProtectedSwitch is a switching device that can be operated by ProtectionEquipment.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Circuit breakers may be operated by protection relays.
    OperatedBy_ProtectionEquipments = List(Instance("CIM13r19.Protection.ProtectionEquipment"),
        desc="Circuit breakers may be operated by protection relays.")

    # A breaker may have zero or more automatic reclosures after a trip occurs.
    RecloseSequences = List(Instance("CIM13r19.Protection.RecloseSequence"),
        desc="A breaker may have zero or more automatic reclosures after a trip occurs.")

    #--------------------------------------------------------------------------
    #  Begin "ProtectedSwitch" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "retained", "switchOnDate", "normalOpen", "switchOnCount",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "SwitchingOperations", "CompositeSwitch", "OperatedBy_ProtectionEquipments", "RecloseSequences",
                label="References", columns=2),
            dock="tab"),
        id="CIM13r19.Wires.ProtectedSwitch",
        title="ProtectedSwitch",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ProtectedSwitch" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Jumper" class:
#------------------------------------------------------------------------------

class Jumper(Switch):
    """ A short section of conductor with negligible impedance which can be manually removed and replaced if the circuit is de-energized. Note that zero-impedance branches can be modelled by an ACLineSegment with a zero impedance ConductorType
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "Jumper" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "retained", "switchOnDate", "normalOpen", "switchOnCount",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "SwitchingOperations", "CompositeSwitch",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.Jumper",
        title="Jumper",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Jumper" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DCLineSegment" class:
#------------------------------------------------------------------------------

class DCLineSegment(Conductor):
    """ A wire or combination of wires not insulated from one another, with consistent electrical characteristics, used to carry direct current between points in the DC region of the power system.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Inductance of the DC line segment.
    dcSegmentInductance = Float(desc="Inductance of the DC line segment.")

    # Resistance of the DC line segment.
    dcSegmentResistance = Float(desc="Resistance of the DC line segment.")

    #--------------------------------------------------------------------------
    #  Begin "DCLineSegment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "r0", "g0ch", "length", "x", "gch", "b0ch", "bch", "x0", "r", "dcSegmentInductance", "dcSegmentResistance",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "ConductorType",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.DCLineSegment",
        title="DCLineSegment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DCLineSegment" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "BusbarSection" class:
#------------------------------------------------------------------------------

class BusbarSection(Connector):
    """ A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A VoltageControlZone is controlled by a designated BusbarSection.
    VoltageControlZone = Instance("CIM13r19.Wires.VoltageControlZone",
        desc="A VoltageControlZone is controlled by a designated BusbarSection.",
        transient=True,
        opposite="BusbarSection",
        editor=InstanceEditor(name="_voltagecontrolzones"))

    def _get_voltagecontrolzones(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.VoltageControlZone" ]
        else:
            return []

    _voltagecontrolzones = Property(fget=_get_voltagecontrolzones)

    #--------------------------------------------------------------------------
    #  Begin "BusbarSection" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "VoltageControlZone",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.BusbarSection",
        title="BusbarSection",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BusbarSection" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ACLineSegment" class:
#------------------------------------------------------------------------------

class ACLineSegment(Conductor):
    """ A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    HasFirst_MutualCoupling = List(Instance("CIM13r19.Wires.MutualCoupling"))

    HasSecond_MutualCoupling = List(Instance("CIM13r19.Wires.MutualCoupling"))

    #--------------------------------------------------------------------------
    #  Begin "ACLineSegment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "r0", "g0ch", "length", "x", "gch", "b0ch", "bch", "x0", "r",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "ConductorType", "HasFirst_MutualCoupling", "HasSecond_MutualCoupling",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.ACLineSegment",
        title="ACLineSegment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ACLineSegment" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ShuntCompensator" class:
#------------------------------------------------------------------------------

class ShuntCompensator(RegulatingCondEq):
    """ A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The date and time when the capacitor bank was last switched on.
    switchOnDate = Str(desc="The date and time when the capacitor bank was last switched on.")

    # The maximum voltage at which the capacitor bank should operate.
    maxU = Float(desc="The maximum voltage at which the capacitor bank should operate.")

    # Time delay required for the device to be connected or disconnected by automatic voltage regulation (AVR).
    aVRDelay = Float(desc="Time delay required for the device to be connected or disconnected by automatic voltage regulation (AVR).")

    # For a capacitor bank, the maximum number of sections that may be switched in.
    maximumSections = Int(desc="For a capacitor bank, the maximum number of sections that may be switched in.")

    # For a capacitor bank, the admittance of each switchable section. Calculated using the reactive power per section and corrected for network voltage.
    yPerSection = Float(desc="For a capacitor bank, the admittance of each switchable section. Calculated using the reactive power per section and corrected for network voltage.")

    # Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive power.
    voltageSensitivity = Float(desc="Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive power.")

    # The switch on count since the capacitor count was last reset or initialized.
    switchOnCount = Int(desc="The switch on count since the capacitor count was last reset or initialized.")

    # For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).
    normalSections = Int(desc="For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).")

    # Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive.
    nomQ = Float(desc="Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive.")

    # For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.
    reactivePerSection = Float(desc="For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.")

    # Zero sequence shunt (charging) conductance per section
    g0PerSection = Float(desc="Zero sequence shunt (charging) conductance per section")

    # The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.
    nomU = Float(desc="The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.")

    # The minimum voltage at which the capacitor bank should operate.
    minU = Float(desc="The minimum voltage at which the capacitor bank should operate.")

    # Zero sequence shunt (charging) susceptance per section
    b0PerSection = Float(desc="Zero sequence shunt (charging) susceptance per section")

    #--------------------------------------------------------------------------
    #  Begin "ShuntCompensator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "switchOnDate", "maxU", "aVRDelay", "maximumSections", "yPerSection", "voltageSensitivity", "switchOnCount", "normalSections", "nomQ", "reactivePerSection", "g0PerSection", "nomU", "minU", "b0PerSection",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "RegulatingControl", "Controls",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.ShuntCompensator",
        title="ShuntCompensator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ShuntCompensator" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Fuse" class:
#------------------------------------------------------------------------------

class Fuse(Switch):
    """ An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Fault interrupting current rating.
    ampRating = Float(desc="Fault interrupting current rating.")

    #--------------------------------------------------------------------------
    #  Begin "Fuse" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "retained", "switchOnDate", "normalOpen", "switchOnCount", "ampRating",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "SwitchingOperations", "CompositeSwitch",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.Fuse",
        title="Fuse",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Fuse" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SynchronousMachine" class:
#------------------------------------------------------------------------------

class SynchronousMachine(RegulatingCondEq):
    """ An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ReactiveCapabilityCurves = List(Instance("CIM13r19.Wires.ReactiveCapabilityCurve"))

    # The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
    Drives_HydroPump = Instance("CIM13r19.Generation.Production.HydroPump",
        desc="The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.",
        transient=True,
        opposite="DrivenBy_SynchronousMachine",
        editor=InstanceEditor(name="_hydropumps"))

    def _get_hydropumps(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Generation.Production.HydroPump" ]
        else:
            return []

    _hydropumps = Property(fget=_get_hydropumps)

    # A synchronous machine may operate as a generator and as such becomes a member of a generating unit
    MemberOf_GeneratingUnit = Instance("CIM13r19.Generation.Production.GeneratingUnit",
        desc="A synchronous machine may operate as a generator and as such becomes a member of a generating unit",
        transient=True,
        opposite="Contains_SynchronousMachines",
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

    # Defines the default MVArCapabilityCurve for use by a SynchronousMachine.
    InitialReactiveCapabilityCurve = Instance("CIM13r19.Wires.ReactiveCapabilityCurve",
        desc="Defines the default MVArCapabilityCurve for use by a SynchronousMachine.",
        transient=True,
        opposite="InitiallyUsedBySynchronousMachine",
        editor=InstanceEditor(name="_reactivecapabilitycurves"))

    def _get_reactivecapabilitycurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Wires.ReactiveCapabilityCurve" ]
        else:
            return []

    _reactivecapabilitycurves = Property(fget=_get_reactivecapabilitycurves)

    DrivenBy_PrimeMover = List(Instance("CIM13r19.Generation.GenerationDynamics.PrimeMover"))

    # Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
    maxQ = Float(desc="Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.")

    # Method of cooling the machine.
    coolantType = CoolantType(desc="Method of cooling the machine.")

    # Quadrature-axis subtransient reactance, also known as X'q.
    xQuadSubtrans = Float(desc="Quadrature-axis subtransient reactance, also known as X'q.")

    # Quadrature-axis synchronous reactance (Xq) , the ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency.
    xQuadSync = Float(desc="Quadrature-axis synchronous reactance (Xq) , the ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency.")

    # Current mode of operation.
    operatingMode = SynchronousMachineOperatingMode(desc="Current mode of operation.")

    # Minimum reactive power limit for the unit.
    minQ = Float(desc="Minimum reactive power limit for the unit.")

    # Zero sequence reactance of the synchronous machine.
    x0 = Float(desc="Zero sequence reactance of the synchronous machine.")

    # Time delay required when switching from Manual to Automatic Voltage Regulation. This value is used in the accelerating power reference frame for powerflow solutions
    manualToAVR = Float(desc="Time delay required when switching from Manual to Automatic Voltage Regulation. This value is used in the accelerating power reference frame for powerflow solutions")

    # Maximum voltage limit for the unit.
    maxU = Float(desc="Maximum voltage limit for the unit.")

    # Negative sequence resistance.
    r2 = Float(desc="Negative sequence resistance.")

    # Direct-axis transient reactance, also known as X'd.
    xDirectTrans = Float(desc="Direct-axis transient reactance, also known as X'd.")

    # Damping torque coefficient, a proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.
    damping = Float(desc="Damping torque coefficient, a proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.")

    # Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a lagging MVAr violation.
    aVRToManualLag = Float(desc="Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a lagging MVAr violation.")

    # Positive sequence reactance of the synchronous machine.
    x = Float(desc="Positive sequence reactance of the synchronous machine.")

    # Minimum voltage  limit for the unit.
    minU = Float(desc="Minimum voltage  limit for the unit.")

    # The energy stored in the rotor when operating at rated speed. This value is used in the accelerating power reference frame for  operator training simulator solutions.
    inertia = Float(desc="The energy stored in the rotor when operating at rated speed. This value is used in the accelerating power reference frame for  operator training simulator solutions.")

    # Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a leading MVAr violation.
    aVRToManualLead = Float(desc="Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a leading MVAr violation.")

    # Positive sequence resistance of the synchronous machine.
    r = Float(desc="Positive sequence resistance of the synchronous machine.")

    # Nameplate apparent power rating for the unit
    ratedS = Float(desc="Nameplate apparent power rating for the unit")

    # Active power consumed when in condenser mode operation.
    condenserP = Float(desc="Active power consumed when in condenser mode operation.")

    # Default base reactive power value. This value represents the initial reactive power that can be used by any application function.
    baseQ = Float(desc="Default base reactive power value. This value represents the initial reactive power that can be used by any application function.")

    # Quadrature-axis transient reactance, also known as X'q.
    xQuadTrans = Float(desc="Quadrature-axis transient reactance, also known as X'q.")

    # Zero sequence resistance of the synchronous machine.
    r0 = Float(desc="Zero sequence resistance of the synchronous machine.")

    # Priority of unit for reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on.
    referencePriority = Int(desc="Priority of unit for reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on.")

    # Percent of the coordinated reactive control that comes from this machine.
    qPercent = Float(desc="Percent of the coordinated reactive control that comes from this machine.")

    # Direct-axis synchronous reactance. The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed. (Xd)
    xDirectSync = Float(desc="Direct-axis synchronous reactance. The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed. (Xd)")

    # Negative sequence reactance.
    x2 = Float(desc="Negative sequence reactance.")

    # Temperature or pressure of coolant medium
    coolantCondition = Float(desc="Temperature or pressure of coolant medium")

    # Modes that this synchronous machine can operate in.
    type = SynchronousMachineType(desc="Modes that this synchronous machine can operate in.")

    # Direct-axis subtransient reactance, also known as X'd.
    xDirectSubtrans = Float(desc="Direct-axis subtransient reactance, also known as X'd.")

    #--------------------------------------------------------------------------
    #  Begin "SynchronousMachine" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "maxQ", "coolantType", "xQuadSubtrans", "xQuadSync", "operatingMode", "minQ", "x0", "manualToAVR", "maxU", "r2", "xDirectTrans", "damping", "aVRToManualLag", "x", "minU", "inertia", "aVRToManualLead", "r", "ratedS", "condenserP", "baseQ", "xQuadTrans", "r0", "referencePriority", "qPercent", "xDirectSync", "x2", "coolantCondition", "type", "xDirectSubtrans",
                label="Attributes", columns=3),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "RegulatingControl", "Controls", "ReactiveCapabilityCurves", "Drives_HydroPump", "MemberOf_GeneratingUnit", "InitialReactiveCapabilityCurve", "DrivenBy_PrimeMover",
                label="References", columns=2),
            dock="tab"),
        id="CIM13r19.Wires.SynchronousMachine",
        title="SynchronousMachine",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SynchronousMachine" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StaticVarCompensator" class:
#------------------------------------------------------------------------------

class StaticVarCompensator(RegulatingCondEq):
    """ A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero.
    voltageSetPoint = Float(desc="The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero.")

    # Maximum available capacitive reactive power
    capacitiveRating = Float(desc="Maximum available capacitive reactive power")

    # SVC control mode.
    sVCControlMode = SVCControlMode(desc="SVC control mode.")

    # The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint.
    slope = Float(desc="The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint.")

    # Maximum available inductive reactive power
    inductiveRating = Float(desc="Maximum available inductive reactive power")

    #--------------------------------------------------------------------------
    #  Begin "StaticVarCompensator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "voltageSetPoint", "capacitiveRating", "sVCControlMode", "slope", "inductiveRating",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "RegulatingControl", "Controls",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.StaticVarCompensator",
        title="StaticVarCompensator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StaticVarCompensator" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Junction" class:
#------------------------------------------------------------------------------

class Junction(Connector):
    """ A point where one or more conducting equipments are connected with zero resistance.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "Junction" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.Junction",
        title="Junction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Junction" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Disconnector" class:
#------------------------------------------------------------------------------

class Disconnector(Switch):
    """ A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "Disconnector" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "retained", "switchOnDate", "normalOpen", "switchOnCount",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "SwitchingOperations", "CompositeSwitch",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Wires.Disconnector",
        title="Disconnector",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Disconnector" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Breaker" class:
#------------------------------------------------------------------------------

class Breaker(ProtectedSwitch):
    """ A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The transition time from open to close.
    inTransitTime = Float(desc="The transition time from open to close.")

    # Fault interrupting current rating.
    ratedCurrent = Float(desc="Fault interrupting current rating.")

    #--------------------------------------------------------------------------
    #  Begin "Breaker" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "retained", "switchOnDate", "normalOpen", "switchOnCount", "inTransitTime", "ratedCurrent",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "SwitchingOperations", "CompositeSwitch", "OperatedBy_ProtectionEquipments", "RecloseSequences",
                label="References", columns=2),
            dock="tab"),
        id="CIM13r19.Wires.Breaker",
        title="Breaker",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Breaker" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadBreakSwitch" class:
#------------------------------------------------------------------------------

class LoadBreakSwitch(ProtectedSwitch):
    """ A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Current carrying capacity of a wire or cable under stated thermal conditions.
    ratedCurrent = Float(desc="Current carrying capacity of a wire or cable under stated thermal conditions.")

    #--------------------------------------------------------------------------
    #  Begin "LoadBreakSwitch" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "phases", "retained", "switchOnDate", "normalOpen", "switchOnCount", "ratedCurrent",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Terminals", "ProtectionEquipments", "BaseVoltage", "ClearanceTags", "SwitchingOperations", "CompositeSwitch", "OperatedBy_ProtectionEquipments", "RecloseSequences",
                label="References", columns=2),
            dock="tab"),
        id="CIM13r19.Wires.LoadBreakSwitch",
        title="LoadBreakSwitch",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadBreakSwitch" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
