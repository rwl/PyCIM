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

""" An extension to the Core and Topology package that models information on the electrical characteristics of Transmission and Distribution networks. This package is used by network applications such as State Estimation, Load Flow and Optimal Power Flow.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.Core import Equipment
from CIM.Core import ConductingEquipment
from CIM.Core import PowerSystemResource
from CIM.Core import Curve
from CIM.Core import EquipmentContainer
from CIM.Core import IdentifiedObject
from CIM.Core import RegularIntervalSchedule
from CIM.Core import PhaseCode
from CIM.Domain import PerCent
from CIM.Domain import Voltage
from CIM.Domain import Frequency
from CIM.Domain import ActivePower
from CIM.Domain import Susceptance
from CIM.Domain import Conductance
from CIM.Domain import Seconds
from CIM.Domain import VoltagePerReactivePower
from CIM.Domain import Admittance
from CIM.Domain import ReactivePower
from CIM.Domain import Temperature
from CIM.Domain import Pressure
from CIM.Domain import LongLength
from CIM.Domain import Resistance
from CIM.Domain import Reactance
from CIM.Domain import ApparentPower
from CIM.Domain import CurrentFlow
from CIM.Domain import ShortLength
from CIM.Domain import Impedance
from CIM.Domain import AngleDegrees
from CIM.Domain import KWActivePower
from CIM.Domain import Damping
from CIM.Domain import PU
from CIM.Domain import AngleRadians
from CIM.Domain import Inductance



from enthought.traits.api import Instance, List, Property, Str, Enum, Int, Date, Float, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------
CompositeSwitchType = Str(desc="http://www.w3.org/2001/XMLSchema#stringAn alphanumeric code that can be used as a reference to extar information such as the description of the interlocking scheme if any")
OperatingMode = Str(desc="http://www.w3.org/2001/XMLSchema#stringTextual name for an operating mode")

# The construction type of the phase shifting tap changer.
PhaseTapChangerKind = Enum("asymmetrical", "unknown", "symmetrical", desc="The construction type of the phase shifting tap changer.")
# The kind of regulation model.   For example regulating voltage, reactive power, active power, etc.
RegulatingControlModeKind = Enum("activePower", "fixed", "reactivePower", "admittance", "currentFlow", "voltage", desc="The kind of regulation model.   For example regulating voltage, reactive power, active power, etc.")
# Transformer tap changer type. Indicates the capabilities of the tap changer independent of the operating mode.
TapChangerKind = Enum("fixed", "voltageAndPhaseControl", "phaseControl", "voltageControl", desc="Transformer tap changer type. Indicates the capabilities of the tap changer independent of the operating mode.")
# Method of cooling a machine.
CoolantType = Enum("hydrogenGas", "air", "water", desc="Method of cooling a machine.")
# Type of transformer cooling.
TransformerCoolingType = Str
# Synchronous machine type.
SynchronousMachineType = Enum("generator_or_condenser", "generator", "condenser", desc="Synchronous machine type.")
# Winding type.
WindingType = Enum("secondary", "tertiary", "quaternary", "primary", desc="Winding type.")
# Static VAr Compensator control mode.
SVCControlMode = Enum("reactivePower", "off", "voltage", desc="Static VAr Compensator control mode.")
# Winding connection type.
WindingConnection = Enum("D", "Y", "Z", desc="Winding connection type.")
# Control modes for a transformer.
TransformerControlMode = Enum("active", "local", "reactive", "volt", "off", desc="Control modes for a transformer.")
# Synchronous machine operating mode.
SynchronousMachineOperatingMode = Enum("generator", "condenser", desc="Synchronous machine operating mode.")

#------------------------------------------------------------------------------
#  "PowerTransformer" class:
#------------------------------------------------------------------------------

class PowerTransformer(Equipment):
    """ An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A transformer may have a heat exchanger
    HeatExchanger = Instance("CIM.Wires.HeatExchanger",
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
                    "CIM.Wires.HeatExchanger" ]
        else:
            return []

    _heatexchangers = Property(fget=_get_heatexchangers)

    # A transformer has windings
    Contains_TransformerWindings = List(Instance("CIM.Wires.TransformerWinding"),
        desc="A transformer has windings")

    # Describes the phases carried by a power transformer.
    phases = PhaseCode(desc="Describes the phases carried by a power transformer.")

    # Type of transformer cooling
    transfCoolingType = TransformerCoolingType(desc="Type of transformer cooling")

    # Core magnetizing saturation curve knee flux level.
    magSatFlux = PerCent(desc="Core magnetizing saturation curve knee flux level.")

    # Core shunt magnetizing susceptance in the saturation region.
    bmagSat = PerCent(desc="Core shunt magnetizing susceptance in the saturation region.")

    # The reference voltage at which the magnetizing saturation measurements were made
    magBaseU = Voltage(desc="The reference voltage at which the magnetizing saturation measurements were made")

    #--------------------------------------------------------------------------
    #  Begin "PowerTransformer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "transfCoolingType", "magSatFlux", "bmagSat", "magBaseU",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "HeatExchanger", "Contains_TransformerWindings",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.PowerTransformer",
        title="PowerTransformer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PowerTransformer" user definitions:
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

    # copy from ...
    RegulatingControl = Instance("CIM.Wires.RegulatingControl",
        desc="copy from ...",
        transient=True,
        opposite="RegulatingCondEq",
        editor=InstanceEditor(name="_regulatingcontrols"))

    def _get_regulatingcontrols(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Wires.RegulatingControl" ]
        else:
            return []

    _regulatingcontrols = Property(fget=_get_regulatingcontrols)

    # The controller outputs used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuator.
    Controls = List(Instance("CIM.Meas.Control"),
        desc="The controller outputs used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuator.")

    #--------------------------------------------------------------------------
    #  Begin "RegulatingCondEq" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "RegulatingControl", "Controls",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.RegulatingCondEq",
        title="RegulatingCondEq",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegulatingCondEq" user definitions:
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
    PowerTransformer = Instance("CIM.Wires.PowerTransformer",
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
                    "CIM.Wires.PowerTransformer" ]
        else:
            return []

    _powertransformers = Property(fget=_get_powertransformers)

    #--------------------------------------------------------------------------
    #  Begin "HeatExchanger" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "PowerTransformer",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.HeatExchanger",
        title="HeatExchanger",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HeatExchanger" user definitions:
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

    # Schedule for this Regulating regulating control.
    RegulationSchedule = Instance("CIM.Wires.RegulationSchedule",
        desc="Schedule for this Regulating regulating control.",
        transient=True,
        opposite="RegulatingControl",
        editor=InstanceEditor(name="_regulationschedules"))

    def _get_regulationschedules(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Wires.RegulationSchedule" ]
        else:
            return []

    _regulationschedules = Property(fget=_get_regulationschedules)

    # The terminal associated with this regulating control.
    Terminal = Instance("CIM.Core.Terminal",
        desc="The terminal associated with this regulating control.",
        transient=True,
        opposite="RegulatingControl",
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

    # copy from reg conduting eq
    TapChanger = List(Instance("CIM.Wires.TapChanger"),
        desc="copy from reg conduting eq")

    # copy from reg cond eq
    RegulatingCondEq = List(Instance("CIM.Wires.RegulatingCondEq"),
        desc="copy from reg cond eq")

    # The regulating control mode presently available.  This specifications allows for determining the kind of regualation without need for obtaining the units from a schedule.
    mode = RegulatingControlModeKind(desc="The regulating control mode presently available.  This specifications allows for determining the kind of regualation without need for obtaining the units from a schedule.")

    # This is the case input target range.   This performs the same function as the value2 attribute on the regulation schedule in the case that schedules are not used.   The units of those appropriate for the mode.
    targetRange = Float(desc="This is the case input target range.   This performs the same function as the value2 attribute on the regulation schedule in the case that schedules are not used.   The units of those appropriate for the mode.")

    # The target value specified for case input.   This value can be used for the target value wihout the use of schedules. The value has the units appropriate to the mode attribute.
    targetValue = Float(desc="The target value specified for case input.   This value can be used for the target value wihout the use of schedules. The value has the units appropriate to the mode attribute.")

    # The regulation is performed in a discrete mode.
    discrete = Bool(desc="The regulation is performed in a discrete mode.")

    #--------------------------------------------------------------------------
    #  Begin "RegulatingControl" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "mode", "targetRange", "targetValue", "discrete",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "RegulationSchedule", "Terminal", "TapChanger", "RegulatingCondEq",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.RegulatingControl",
        title="RegulatingControl",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegulatingControl" user definitions:
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

    # Synchronous machines using this curve as default.
    InitiallyUsedBySynchronousMachine = List(Instance("CIM.Wires.SynchronousMachine"),
        desc="Synchronous machines using this curve as default.")

    # Synchronous machines using this curve.
    SynchronousMachines = List(Instance("CIM.Wires.SynchronousMachine"),
        desc="Synchronous machines using this curve.")

    # The machine's coolant temperature (e.g., ambient air or stator circulating water).
    coolantTemperature = Temperature(desc="The machine's coolant temperature (e.g., ambient air or stator circulating water).")

    # The hydrogen coolant pressure
    hydrogenPressure = Pressure(desc="The hydrogen coolant pressure")

    #--------------------------------------------------------------------------
    #  Begin "ReactiveCapabilityCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "y2Unit", "y1Multiplier", "curveStyle", "y2Multiplier", "xUnit", "y1Unit", "xMultiplier", "coolantTemperature", "hydrogenPressure",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "CurveScheduleDatas", "InitiallyUsedBySynchronousMachine", "SynchronousMachines",
                label="References"),
            dock="tab"),
        id="CIM.Wires.ReactiveCapabilityCurve",
        title="ReactiveCapabilityCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ReactiveCapabilityCurve" user definitions:
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
    Region = Instance("CIM.Core.SubGeographicalRegion",
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
                    "CIM.Core.SubGeographicalRegion" ]
        else:
            return []

    _subgeographicalregions = Property(fget=_get_subgeographicalregions)

    #--------------------------------------------------------------------------
    #  Begin "Line" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "TopologicalNode", "ConnectivityNodes", "Contains_Equipments", "Region",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.Line",
        title="Line",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Line" user definitions:
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
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.Connector",
        title="Connector",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Connector" user definitions:
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
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.Ground",
        title="Ground",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Ground" user definitions:
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
    ConductorType = Instance("CIM.Wires.ConductorType",
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
                    "CIM.Wires.ConductorType" ]
        else:
            return []

    _conductortypes = Property(fget=_get_conductortypes)

    # Segment length for calculating line section capabilities
    length = LongLength(desc="Segment length for calculating line section capabilities")

    # Positive sequence series resistance of the entire line section.
    r = Resistance(desc="Positive sequence series resistance of the entire line section.")

    # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
    bch = Susceptance(desc="Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.")

    # Zero sequence series resistance of the entire line section.
    r0 = Resistance(desc="Zero sequence series resistance of the entire line section.")

    # Positive sequence series reactance of the entire line section.
    x = Reactance(desc="Positive sequence series reactance of the entire line section.")

    # Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
    b0ch = Susceptance(desc="Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.")

    # Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
    gch = Conductance(desc="Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.")

    # Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
    g0ch = Conductance(desc="Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.")

    # Zero sequence series reactance of the entire line section.
    x0 = Reactance(desc="Zero sequence series reactance of the entire line section.")

    #--------------------------------------------------------------------------
    #  Begin "Conductor" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "length", "r", "bch", "r0", "x", "b0ch", "gch", "g0ch", "x0",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "ConductorType",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.Conductor",
        title="Conductor",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Conductor" user definitions:
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

    # The winding winding tests for which the transformer winding (terminal) participates as the 'to' end of the test.
    To_WindingTest = List(Instance("CIM.Wires.WindingTest"),
        desc="The winding winding tests for which the transformer winding (terminal) participates as the 'to' end of the test.")

    # The transformer winding tests for which the transformer winding (terminal) participates as the 'from' part of the test.
    From_WindingTest = List(Instance("CIM.Wires.WindingTest"),
        desc="The transformer winding tests for which the transformer winding (terminal) participates as the 'from' part of the test.")

    # A transformer has windings
    MemberOf_PowerTransformer = Instance("CIM.Wires.PowerTransformer",
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
                    "CIM.Wires.PowerTransformer" ]
        else:
            return []

    _powertransformers = Property(fget=_get_powertransformers)

    # The ratio tap changer associated with the transformer winding.
    RatioTapChanger = Instance("CIM.Wires.RatioTapChanger",
        desc="The ratio tap changer associated with the transformer winding.",
        transient=True,
        opposite="TransformerWinding",
        editor=InstanceEditor(name="_ratiotapchangers"))

    def _get_ratiotapchangers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Wires.RatioTapChanger" ]
        else:
            return []

    _ratiotapchangers = Property(fget=_get_ratiotapchangers)

    # The phase tap changer associated with the transformer winding.
    PhaseTapChanger = Instance("CIM.Wires.PhaseTapChanger",
        desc="The phase tap changer associated with the transformer winding.",
        transient=True,
        opposite="TransformerWinding",
        editor=InstanceEditor(name="_phasetapchangers"))

    def _get_phasetapchangers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Wires.PhaseTapChanger" ]
        else:
            return []

    _phasetapchangers = Property(fget=_get_phasetapchangers)

    # The type of connection of the winding.
    connectionType = WindingConnection(desc="The type of connection of the winding.")

    # The type of winding.
    windingType = WindingType(desc="The type of winding.")

    # The apparent power that the winding can carry  under emergency conditions.
    emergencyS = ApparentPower(desc="The apparent power that the winding can carry  under emergency conditions.")

    # Positive sequence series resistance of the winding.
    r = Resistance(desc="Positive sequence series resistance of the winding.")

    # Set if the winding is grounded.
    grounded = Bool(desc="Set if the winding is grounded.")

    # Zero sequence series resistance of the winding.
    r0 = Resistance(desc="Zero sequence series resistance of the winding.")

    # Positive sequence series reactance of the winding.
    x = Reactance(desc="Positive sequence series reactance of the winding.")

    # Basic insulation level voltage rating
    insulationU = Voltage(desc="Basic insulation level voltage rating")

    # Zero sequence series reactance of the winding.
    x0 = Reactance(desc="Zero sequence series reactance of the winding.")

    # Zero sequence magnetizing branch conductance.
    g0 = Conductance(desc="Zero sequence magnetizing branch conductance.")

    # Apparent power that the winding can carry for a short period of time.
    shortTermS = ApparentPower(desc="Apparent power that the winding can carry for a short period of time.")

    # Zero sequence magnetizing branch susceptance.
    b0 = Susceptance(desc="Zero sequence magnetizing branch susceptance.")

    # The normal apparent power rating for the winding
    ratedS = ApparentPower(desc="The normal apparent power rating for the winding")

    # Magnetizing branch susceptance (B mag).
    b = Susceptance(desc="Magnetizing branch susceptance (B mag).")

    # Magnetizing branch conductance (G mag).
    g = Conductance(desc="Magnetizing branch conductance (G mag).")

    # Ground resistance path through connected grounding transformer.
    rground = Resistance(desc="Ground resistance path through connected grounding transformer.")

    # The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.
    ratedU = Voltage(desc="The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.")

    # Ground reactance path through connected grounding transformer.
    xground = Reactance(desc="Ground reactance path through connected grounding transformer.")

    #--------------------------------------------------------------------------
    #  Begin "TransformerWinding" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "connectionType", "windingType", "emergencyS", "r", "grounded", "r0", "x", "insulationU", "x0", "g0", "shortTermS", "b0", "ratedS", "b", "g", "rground", "ratedU", "xground",
                label="Attributes", columns=2),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "To_WindingTest", "From_WindingTest", "MemberOf_PowerTransformer", "RatioTapChanger", "PhaseTapChanger",
                label="References", columns=2),
            dock="tab"),
        id="CIM.Wires.TransformerWinding",
        title="TransformerWinding",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TransformerWinding" user definitions:
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
    ConductorType = Instance("CIM.Wires.ConductorType",
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
                    "CIM.Wires.ConductorType" ]
        else:
            return []

    _conductortypes = Property(fget=_get_conductortypes)

    # A WireType is mounted at a specified place in a WireArrangement.
    WireType = Instance("CIM.Wires.WireType",
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
                    "CIM.Wires.WireType" ]
        else:
            return []

    _wiretypes = Property(fget=_get_wiretypes)

    # Mounting point where wire One is mounted.
    mountingPointY = Int(desc="Mounting point where wire One is mounted.")

    # Mounting point where wire One is mounted.
    mountingPointX = Int(desc="Mounting point where wire One is mounted.")

    #--------------------------------------------------------------------------
    #  Begin "WireArrangement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "mountingPointY", "mountingPointX",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "ConductorType", "WireType",
                label="References"),
            dock="tab"),
        id="CIM.Wires.WireArrangement",
        title="WireArrangement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WireArrangement" user definitions:
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

    # The load response characteristic of this load.
    LoadResponse = Instance("CIM.LoadModel.LoadResponseCharacteristic",
        desc="The load response characteristic of this load.",
        transient=True,
        opposite="EnergyConsumer",
        editor=InstanceEditor(name="_loadresponsecharacteristics"))

    def _get_loadresponsecharacteristics(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.LoadModel.LoadResponseCharacteristic" ]
        else:
            return []

    _loadresponsecharacteristics = Property(fget=_get_loadresponsecharacteristics)

    # An energy consumer is assigned to a power cut zone
    PowerCutZone = Instance("CIM.LoadModel.PowerCutZone",
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
                    "CIM.LoadModel.PowerCutZone" ]
        else:
            return []

    _powercutzones = Property(fget=_get_powercutzones)

    # Fixed reactive power as per cent of load group fixed reactive power.
    qfixedPct = PerCent(desc="Fixed reactive power as per cent of load group fixed reactive power.")

    # Fixed active power as per cent of load group fixed active power
    pfixedPct = PerCent(desc="Fixed active power as per cent of load group fixed active power")

    # Active power of the load that is a fixed quantity.
    pfixed = ActivePower(desc="Active power of the load that is a fixed quantity.")

    # Number of individual customers represented by this Demand
    customerCount = Int(desc="Number of individual customers represented by this Demand")

    # Reactive power of the load that is a fixed quantity.
    qfixed = ReactivePower(desc="Reactive power of the load that is a fixed quantity.")

    #--------------------------------------------------------------------------
    #  Begin "EnergyConsumer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "qfixedPct", "pfixedPct", "pfixed", "customerCount", "qfixed",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "LoadResponse", "PowerCutZone",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.EnergyConsumer",
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
    SwitchingOperations = List(Instance("CIM.Outage.SwitchingOperation"),
        desc="A switch may be operated by many schedules.")

    # Composite switch this Switch belongs to
    CompositeSwitch = Instance("CIM.Wires.CompositeSwitch",
        desc="Composite switch this Switch belongs to",
        transient=True,
        opposite="Switches",
        editor=InstanceEditor(name="_compositeswitchs"))

    def _get_compositeswitchs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Wires.CompositeSwitch" ]
        else:
            return []

    _compositeswitchs = Property(fget=_get_compositeswitchs)

    # Branch is retained in a bus branch model.
    retained = Bool(desc="Branch is retained in a bus branch model.")

    # The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.
    normalOpen = Bool(desc="The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.")

    # The date and time when the switch was last switched on.
    switchOnDate = Date(desc="The date and time when the switch was last switched on.")

    # The switch on count since the switch was last reset or initialized.
    switchOnCount = Int(desc="The switch on count since the switch was last reset or initialized.")

    #--------------------------------------------------------------------------
    #  Begin "Switch" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "retained", "normalOpen", "switchOnDate", "switchOnCount",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "SwitchingOperations", "CompositeSwitch",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.Switch",
        title="Switch",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Switch" user definitions:
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
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "TopologicalNode", "ConnectivityNodes", "Contains_Equipments",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.Plant",
        title="Plant",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Plant" user definitions:
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
    WireArrangements = List(Instance("CIM.Wires.WireArrangement"),
        desc="A WireType is mounted at a specified place in a WireArrangement.")

    # Number of conductor strands in the (symmetrical) bundle (1-12)
    phaseConductorCount = Int(desc="Number of conductor strands in the (symmetrical) bundle (1-12)")

    # The resistance per unit length of the conductor
    resistance = Resistance(desc="The resistance per unit length of the conductor")

    # Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor.
    gMR = ShortLength(desc="Geometric Mean Radius. If we replace the conductor by a thin walled tube of radius GMR, then its reactance is identical to the reactance of the actual conductor.")

    # The radius of the conductor
    radius = ShortLength(desc="The radius of the conductor")

    # Distance between conductor strands in a (symmetrical) bundle.
    phaseConductorSpacing = ShortLength(desc="Distance between conductor strands in a (symmetrical) bundle.")

    # Current carrying capacity of a wire or cable under stated thermal conditions
    ratedCurrent = CurrentFlow(desc="Current carrying capacity of a wire or cable under stated thermal conditions")

    #--------------------------------------------------------------------------
    #  Begin "WireType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "phaseConductorCount", "resistance", "gMR", "radius", "phaseConductorSpacing", "ratedCurrent",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "WireArrangements",
                label="References"),
            dock="tab"),
        id="CIM.Wires.WireType",
        title="WireType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WireType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RegulationSchedule" class:
#------------------------------------------------------------------------------

class RegulationSchedule(RegularIntervalSchedule):
    """ A pre-established pattern over time for a controlled variable, e.g., busbar voltage.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Regulating controls that have this Schedule.
    RegulatingControl = List(Instance("CIM.Wires.RegulatingControl"),
        desc="Regulating controls that have this Schedule.")

    # A VoltageControlZone may have a  voltage regulation schedule.
    VoltageControlZones = List(Instance("CIM.Wires.VoltageControlZone"),
        desc="A VoltageControlZone may have a  voltage regulation schedule.")

    # Line drop reactance.
    lineDropX = Reactance(desc="Line drop reactance.")

    # Line drop resistance.
    lineDropR = Resistance(desc="Line drop resistance.")

    # Flag to indicate that line drop compensation is to be applied
    lineDropCompensation = Bool(desc="Flag to indicate that line drop compensation is to be applied")

    #--------------------------------------------------------------------------
    #  Begin "RegulationSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "value1Unit", "value2Multiplier", "value1Multiplier", "value2Unit", "startTime", "timeStep", "endTime", "lineDropX", "lineDropR", "lineDropCompensation",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "TimePoints", "RegulatingControl", "VoltageControlZones",
                label="References"),
            dock="tab"),
        id="CIM.Wires.RegulationSchedule",
        title="RegulationSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegulationSchedule" user definitions:
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

    # The winding to which the test was conducted.  Note that although the 'from' side of the test is required, the 'to' side of a test is not always required.
    To_TransformerWinding = Instance("CIM.Wires.TransformerWinding",
        desc="The winding to which the test was conducted.  Note that although the 'from' side of the test is required, the 'to' side of a test is not always required.",
        transient=True,
        opposite="To_WindingTest",
        editor=InstanceEditor(name="_transformerwindings"))

    def _get_transformerwindings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Wires.TransformerWinding" ]
        else:
            return []

    _transformerwindings = Property(fget=_get_transformerwindings)

    # The winding from which the test was conducted
    From_TransformerWinding = Instance("CIM.Wires.TransformerWinding",
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
                    "CIM.Wires.TransformerWinding" ]
        else:
            return []

    _transformerwindings = Property(fget=_get_transformerwindings)

    # The leakage impedance measured at the 'from' winding  with the 'to' winding short-circuited and all other windings open-circuited.  Leakage impedance is expressed in units based on the apparent power and voltage ratings of the 'from' winding.
    leakageImpedance = Impedance(desc="The leakage impedance measured at the 'from' winding  with the 'to' winding short-circuited and all other windings open-circuited.  Leakage impedance is expressed in units based on the apparent power and voltage ratings of the 'from' winding.")

    # The tap step number for the 'from' winding of the test pair.
    fromTapStep = Int(desc="The tap step number for the 'from' winding of the test pair.")

    # The phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
    phaseShift = AngleDegrees(desc="The phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.")

    # The exciting current on open-circuit test, expressed as a percentage of rated current, at nominal voltage
    excitingCurrent = PerCent(desc="The exciting current on open-circuit test, expressed as a percentage of rated current, at nominal voltage")

    # The no load loss kW 'to' winding open-circuited) from the test report.
    noLoadLoss = KWActivePower(desc="The no load loss kW 'to' winding open-circuited) from the test report.")

    # The tap step number for the 'to' winding of the test pair.
    toTapStep = Int(desc="The tap step number for the 'to' winding of the test pair.")

    # The load loss kW ('to' winding short-circuited) from the test report.
    loadLoss = KWActivePower(desc="The load loss kW ('to' winding short-circuited) from the test report.")

    # The voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
    voltage = Voltage(desc="The voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.")

    #--------------------------------------------------------------------------
    #  Begin "WindingTest" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "leakageImpedance", "fromTapStep", "phaseShift", "excitingCurrent", "noLoadLoss", "toTapStep", "loadLoss", "voltage",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "To_TransformerWinding", "From_TransformerWinding",
                label="References"),
            dock="tab"),
        id="CIM.Wires.WindingTest",
        title="WindingTest",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WindingTest" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MutualCoupling" class:
#------------------------------------------------------------------------------

class MutualCoupling(IdentifiedObject):
    """ This class represents the zero sequence line mutual coupling.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The second line associated with the mutual coupling.
    delete_this_Second_ACLineSegment = Instance("CIM.Wires.ACLineSegment",
        desc="The second line associated with the mutual coupling.",
        transient=True,
        opposite="delete_this_HasSecond_MutualCoupling",
        editor=InstanceEditor(name="_aclinesegments"))

    def _get_aclinesegments(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Wires.ACLineSegment" ]
        else:
            return []

    _aclinesegments = Property(fget=_get_aclinesegments)

    # The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments.
    First_Terminal = Instance("CIM.Core.Terminal",
        desc="The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments.",
        transient=True,
        opposite="HasFirst_MutualCoupling",
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

    # First line associated with the mutual coupling.
    delete_this_First_ACLineSegment = Instance("CIM.Wires.ACLineSegment",
        desc="First line associated with the mutual coupling.",
        transient=True,
        opposite="delete_this_HasFirst_MutualCoupling",
        editor=InstanceEditor(name="_aclinesegments"))

    def _get_aclinesegments(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Wires.ACLineSegment" ]
        else:
            return []

    _aclinesegments = Property(fget=_get_aclinesegments)

    # The starting terminal for the calculation of distances along the second branch of the mutual coupling.
    Second_Terminal = Instance("CIM.Core.Terminal",
        desc="The starting terminal for the calculation of distances along the second branch of the mutual coupling.",
        transient=True,
        opposite="HasSecond_MutualCoupling",
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

    # Zero sequence branch-to-branch mutual impedance coupling, resistance
    r0 = Resistance(desc="Zero sequence branch-to-branch mutual impedance coupling, resistance")

    # Distance from the second line's specified terminal to end of coupled region
    distance22 = LongLength(desc="Distance from the second line's specified terminal to end of coupled region")

    # Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section.
    g0ch = Conductance(desc="Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section.")

    # Distance from the first line's specified terminal to start of coupled region
    distance11 = LongLength(desc="Distance from the first line's specified terminal to start of coupled region")

    # Zero sequence branch-to-branch mutual impedance coupling, reactance
    x0 = Resistance(desc="Zero sequence branch-to-branch mutual impedance coupling, reactance")

    # Distance from the first line's from specified terminal to end of coupled region
    distance12 = LongLength(desc="Distance from the first line's from specified terminal to end of coupled region")

    # Distance from the second line's specified terminal to start of coupled region
    distance21 = LongLength(desc="Distance from the second line's specified terminal to start of coupled region")

    # Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section.
    b0ch = Susceptance(desc="Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section.")

    #--------------------------------------------------------------------------
    #  Begin "MutualCoupling" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "r0", "distance22", "g0ch", "distance11", "x0", "distance12", "distance21", "b0ch",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "delete_this_Second_ACLineSegment", "First_Terminal", "delete_this_First_ACLineSegment", "Second_Terminal",
                label="References"),
            dock="tab"),
        id="CIM.Wires.MutualCoupling",
        title="MutualCoupling",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MutualCoupling" user definitions:
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
    x = Reactance(desc="Positive sequence reactance.")

    # Positive sequence resistance.
    r = Resistance(desc="Positive sequence resistance.")

    #--------------------------------------------------------------------------
    #  Begin "SeriesCompensator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "x", "r",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.SeriesCompensator",
        title="SeriesCompensator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SeriesCompensator" user definitions:
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

    # Switches contained in this Composite switch.
    Switches = List(Instance("CIM.Wires.Switch"),
        desc="Switches contained in this Composite switch.")

    # An alphanumeric code that can be used as a reference to extar information such as the description of the interlocking scheme if any
    compositeSwitchType = CompositeSwitchType(desc="An alphanumeric code that can be used as a reference to extar information such as the description of the interlocking scheme if any")

    #--------------------------------------------------------------------------
    #  Begin "CompositeSwitch" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "compositeSwitchType",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "Switches",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.CompositeSwitch",
        title="CompositeSwitch",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CompositeSwitch" user definitions:
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

    RegulatingControl = Instance("CIM.Wires.RegulatingControl",
        transient=True,
        opposite="TapChanger",
        editor=InstanceEditor(name="_regulatingcontrols"))

    def _get_regulatingcontrols(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Wires.RegulatingControl" ]
        else:
            return []

    _regulatingcontrols = Property(fget=_get_regulatingcontrols)

    # The tap step state associated with the tap changer.
    SvTapStep = Instance("CIM.StateVariables.SvTapStep",
        desc="The tap step state associated with the tap changer.",
        transient=True,
        opposite="TapChanger",
        editor=InstanceEditor(name="_svtapsteps"))

    def _get_svtapsteps(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.StateVariables.SvTapStep" ]
        else:
            return []

    _svtapsteps = Property(fget=_get_svtapsteps)

    # For an LTC, the tap changer control mode.
    tculControlMode = TransformerControlMode(desc="For an LTC, the tap changer control mode.")

    # The type of tap changer. Indicates the ability of the transformer to perform various regulation tasks. The tap changer must be also be associated wtih a RegulationControl object before any regulation is possible.
    type = TapChangerKind(desc="The type of tap changer. Indicates the ability of the transformer to perform various regulation tasks. The tap changer must be also be associated wtih a RegulationControl object before any regulation is possible.")

    # The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.
    normalStep = Int(desc="The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.")

    # The neutral tap step position for this winding.
    neutralStep = Int(desc="The neutral tap step position for this winding.")

    # For an LTC, the delay for initial tap changer operation (first step change)
    initialDelay = Seconds(desc="For an LTC, the delay for initial tap changer operation (first step change)")

    # Voltage at which the winding operates at the neutral tap setting.
    neutralU = Voltage(desc="Voltage at which the winding operates at the neutral tap setting.")

    # Tap step increment, in per cent of nominal voltage, per step position. This could be supplanted by more detailed model information in either the PhaseTapChanger if modeled or in detailed per tap step table information.
    stepVoltageIncrement = PerCent(desc="Tap step increment, in per cent of nominal voltage, per step position. This could be supplanted by more detailed model information in either the PhaseTapChanger if modeled or in detailed per tap step table information.")

    # Highest possible tap step position, advance from neutral
    highStep = Int(desc="Highest possible tap step position, advance from neutral")

    # Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer).
    stepPhaseShiftIncrement_DeleteThis = AngleDegrees(desc="Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer).")

    # For an LTC, the delay for subsequent tap changer operation (second and later step changes)
    subsequentDelay = Seconds(desc="For an LTC, the delay for subsequent tap changer operation (second and later step changes)")

    # Lowest possible tap step position, retard from neutral
    lowStep = Int(desc="Lowest possible tap step position, retard from neutral")

    #--------------------------------------------------------------------------
    #  Begin "TapChanger" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "tculControlMode", "type", "normalStep", "neutralStep", "initialDelay", "neutralU", "stepVoltageIncrement", "highStep", "stepPhaseShiftIncrement_DeleteThis", "subsequentDelay", "lowStep",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "RegulatingControl", "SvTapStep",
                label="References"),
            dock="tab"),
        id="CIM.Wires.TapChanger",
        title="TapChanger",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TapChanger" user definitions:
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

    # The maximum voltage on the DC side at which the converter should operate.
    maxU = Voltage(desc="The maximum voltage on the DC side at which the converter should operate.")

    # Rectifier/inverter primary base voltage
    ratedU = Voltage(desc="Rectifier/inverter primary base voltage")

    # The maximum active power on the DC side at which the fconverter should operate.
    maxP = ActivePower(desc="The maximum active power on the DC side at which the fconverter should operate.")

    # Commutating reactance at AC bus frequency.
    commutatingReactance = Reactance(desc="Commutating reactance at AC bus frequency.")

    # Operating mode for the converter.
    operatingMode = OperatingMode(desc="Operating mode for the converter.")

    # Number of bridges
    bridges = Int(desc="Number of bridges")

    # Frequency on the AC side.
    frequency = Frequency(desc="Frequency on the AC side.")

    # Commutating resistance.
    commutatingResistance = Resistance(desc="Commutating resistance.")

    # Compounding resistance.
    compoundResistance = Resistance(desc="Compounding resistance.")

    # Minimum compounded DC voltage
    minCompoundVoltage = Voltage(desc="Minimum compounded DC voltage")

    # The minimum active power on the DC side at which the converter should operate.
    minP = ActivePower(desc="The minimum active power on the DC side at which the converter should operate.")

    # The minimum voltage on the DC side at which the converter should operate.
    minU = Voltage(desc="The minimum voltage on the DC side at which the converter should operate.")

    #--------------------------------------------------------------------------
    #  Begin "RectifierInverter" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "maxU", "ratedU", "maxP", "commutatingReactance", "operatingMode", "bridges", "frequency", "commutatingResistance", "compoundResistance", "minCompoundVoltage", "minP", "minU",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.RectifierInverter",
        title="RectifierInverter",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RectifierInverter" user definitions:
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

    # A ConductorType is made up of wires that can be configured in several ways.
    WireArrangements = List(Instance("CIM.Wires.WireArrangement"),
        desc="A ConductorType is made up of wires that can be configured in several ways.")

    # Sections of conductor are physically described by a conductor type
    Conductors = List(Instance("CIM.Wires.Conductor"),
        desc="Sections of conductor are physically described by a conductor type")

    # Reactance of the sheath for cable conductors.
    sheathReactance = Reactance(desc="Reactance of the sheath for cable conductors.")

    # Resistance of the sheath for cable conductors.
    sheathResistance = Resistance(desc="Resistance of the sheath for cable conductors.")

    #--------------------------------------------------------------------------
    #  Begin "ConductorType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "sheathReactance", "sheathResistance",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "WireArrangements", "Conductors",
                label="References"),
            dock="tab"),
        id="CIM.Wires.ConductorType",
        title="ConductorType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ConductorType" user definitions:
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

    # A VoltageControlZone is controlled by a designated BusbarSection.
    BusbarSection = Instance("CIM.Wires.BusbarSection",
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
                    "CIM.Wires.BusbarSection" ]
        else:
            return []

    _busbarsections = Property(fget=_get_busbarsections)

    # A VoltageControlZone may have a  voltage regulation schedule.
    RegulationSchedule = Instance("CIM.Wires.RegulationSchedule",
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
                    "CIM.Wires.RegulationSchedule" ]
        else:
            return []

    _regulationschedules = Property(fget=_get_regulationschedules)

    #--------------------------------------------------------------------------
    #  Begin "VoltageControlZone" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "BusbarSection", "RegulationSchedule",
                label="References"),
            dock="tab"),
        id="CIM.Wires.VoltageControlZone",
        title="VoltageControlZone",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "VoltageControlZone" user definitions:
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

    # Phase-to-phase nominal voltage.
    nominalVoltage = Voltage(desc="Phase-to-phase nominal voltage.")

    # Negative sequence Thevenin resistance.
    rn = Resistance(desc="Negative sequence Thevenin resistance.")

    # Negative sequence Thevenin reactance.
    xn = Reactance(desc="Negative sequence Thevenin reactance.")

    # Zero sequence Thevenin resistance.
    r0 = Resistance(desc="Zero sequence Thevenin resistance.")

    # Zero sequence Thevenin reactance.
    x0 = Reactance(desc="Zero sequence Thevenin reactance.")

    # Phase angle of a-phase open circuit.
    voltageAngle = AngleRadians(desc="Phase angle of a-phase open circuit.")

    # Positive sequence Thevenin resistance.
    r = Resistance(desc="Positive sequence Thevenin resistance.")

    # High voltage source load
    activePower = ActivePower(desc="High voltage source load")

    # Positive sequence Thevenin reactance.
    x = Reactance(desc="Positive sequence Thevenin reactance.")

    # Phase-to-phase open circuit voltage magnitude.
    voltageMagnitude = Voltage(desc="Phase-to-phase open circuit voltage magnitude.")

    #--------------------------------------------------------------------------
    #  Begin "EnergySource" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "nominalVoltage", "rn", "xn", "r0", "x0", "voltageAngle", "r", "activePower", "x", "voltageMagnitude",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.EnergySource",
        title="EnergySource",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EnergySource" user definitions:
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

    # The maximum voltage on the DC side at which the frequency converter should operate.
    maxU = Voltage(desc="The maximum voltage on the DC side at which the frequency converter should operate.")

    # Frequency on the AC side.
    frequency = Frequency(desc="Frequency on the AC side.")

    # The minimum active power on the DC side at which the frequence converter should operate.
    minP = ActivePower(desc="The minimum active power on the DC side at which the frequence converter should operate.")

    # The minimum voltage on the DC side at which the frequency converter should operate.
    minU = Voltage(desc="The minimum voltage on the DC side at which the frequency converter should operate.")

    # Operating mode for the frequency converter
    operatingMode = OperatingMode(desc="Operating mode for the frequency converter")

    # The maximum active power on the DC side at which the frequence converter should operate.
    maxP = ActivePower(desc="The maximum active power on the DC side at which the frequence converter should operate.")

    #--------------------------------------------------------------------------
    #  Begin "FrequencyConverter" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "maxU", "frequency", "minP", "minU", "operatingMode", "maxP",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "RegulatingControl", "Controls",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.FrequencyConverter",
        title="FrequencyConverter",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FrequencyConverter" user definitions:
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

    # The state for the number of shunt compensator sections in service.
    SvShuntCompensatorSections = Instance("CIM.StateVariables.SvShuntCompensatorSections",
        desc="The state for the number of shunt compensator sections in service.",
        transient=True,
        opposite="ShuntCompensator",
        editor=InstanceEditor(name="_svshuntcompensatorsectionss"))

    def _get_svshuntcompensatorsectionss(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.StateVariables.SvShuntCompensatorSections" ]
        else:
            return []

    _svshuntcompensatorsectionss = Property(fget=_get_svshuntcompensatorsectionss)

    # Zero sequence shunt (charging) susceptance per section
    b0PerSection = Susceptance(desc="Zero sequence shunt (charging) susceptance per section")

    # The switch on count since the capacitor count was last reset or initialized.
    switchOnCount = Int(desc="The switch on count since the capacitor count was last reset or initialized.")

    # Zero sequence shunt (charging) conductance per section
    g0PerSection = Conductance(desc="Zero sequence shunt (charging) conductance per section")

    # Time delay required for the device to be connected or disconnected by automatic voltage regulation (AVR).
    aVRDelay = Seconds(desc="Time delay required for the device to be connected or disconnected by automatic voltage regulation (AVR).")

    # For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).
    normalSections = Int(desc="For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).")

    # Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive power.
    voltageSensitivity = VoltagePerReactivePower(desc="Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive power.")

    # For a capacitor bank, the maximum number of sections that may be switched in.
    maximumSections = Int(desc="For a capacitor bank, the maximum number of sections that may be switched in.")

    # For a capacitor bank, the admittance of each switchable section. Calculated using the reactive power per section and corrected for network voltage.
    yPerSection = Admittance(desc="For a capacitor bank, the admittance of each switchable section. Calculated using the reactive power per section and corrected for network voltage.")

    # Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive.
    nomQ = ReactivePower(desc="Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive.")

    # For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.
    reactivePerSection = ReactivePower(desc="For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.")

    # The maximum voltage at which the capacitor bank should operate.
    maxU = Voltage(desc="The maximum voltage at which the capacitor bank should operate.")

    # The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.
    nomU = Voltage(desc="The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.")

    # Positive sequence shunt (charging) conductance per section
    gPerSection = Conductance(desc="Positive sequence shunt (charging) conductance per section")

    # The date and time when the capacitor bank was last switched on.
    switchOnDate = Date(desc="The date and time when the capacitor bank was last switched on.")

    # Positive sequence shunt (charging) susceptance per section
    bPerSection = Susceptance(desc="Positive sequence shunt (charging) susceptance per section")

    # The minimum voltage at which the capacitor bank should operate.
    minU = Voltage(desc="The minimum voltage at which the capacitor bank should operate.")

    #--------------------------------------------------------------------------
    #  Begin "ShuntCompensator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "b0PerSection", "switchOnCount", "g0PerSection", "aVRDelay", "normalSections", "voltageSensitivity", "maximumSections", "yPerSection", "nomQ", "reactivePerSection", "maxU", "nomU", "gPerSection", "switchOnDate", "bPerSection", "minU",
                label="Attributes", columns=2),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "RegulatingControl", "Controls", "SvShuntCompensatorSections",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.ShuntCompensator",
        title="ShuntCompensator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ShuntCompensator" user definitions:
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
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.Junction",
        title="Junction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Junction" user definitions:
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

    # Protection equipments that operate this ProtectedSwitch.
    OperatedBy_ProtectionEquipments = List(Instance("CIM.Protection.ProtectionEquipment"),
        desc="Protection equipments that operate this ProtectedSwitch.")

    # A breaker may have zero or more automatic reclosures after a trip occurs.
    RecloseSequences = List(Instance("CIM.Protection.RecloseSequence"),
        desc="A breaker may have zero or more automatic reclosures after a trip occurs.")

    #--------------------------------------------------------------------------
    #  Begin "ProtectedSwitch" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "retained", "normalOpen", "switchOnDate", "switchOnCount",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "SwitchingOperations", "CompositeSwitch", "OperatedBy_ProtectionEquipments", "RecloseSequences",
                label="References", columns=2),
            dock="tab"),
        id="CIM.Wires.ProtectedSwitch",
        title="ProtectedSwitch",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ProtectedSwitch" user definitions:
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
    ratedCurrent = CurrentFlow(desc="Current carrying capacity of a wire or cable under stated thermal conditions.")

    #--------------------------------------------------------------------------
    #  Begin "LoadBreakSwitch" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "retained", "normalOpen", "switchOnDate", "switchOnCount", "ratedCurrent",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "SwitchingOperations", "CompositeSwitch", "OperatedBy_ProtectionEquipments", "RecloseSequences",
                label="References", columns=2),
            dock="tab"),
        id="CIM.Wires.LoadBreakSwitch",
        title="LoadBreakSwitch",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadBreakSwitch" user definitions:
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

    # Mutual couplings associated with this line as the 'second' line.
    delete_this_HasSecond_MutualCoupling = List(Instance("CIM.Wires.MutualCoupling"),
        desc="Mutual couplings associated with this line as the 'second' line.")

    # Mutual couplings associated with the line as the 'first' line.
    delete_this_HasFirst_MutualCoupling = List(Instance("CIM.Wires.MutualCoupling"),
        desc="Mutual couplings associated with the line as the 'first' line.")

    #--------------------------------------------------------------------------
    #  Begin "ACLineSegment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "length", "r", "bch", "r0", "x", "b0ch", "gch", "g0ch", "x0",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "ConductorType", "delete_this_HasSecond_MutualCoupling", "delete_this_HasFirst_MutualCoupling",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.ACLineSegment",
        title="ACLineSegment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ACLineSegment" user definitions:
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
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "retained", "normalOpen", "switchOnDate", "switchOnCount",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "SwitchingOperations", "CompositeSwitch",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.Disconnector",
        title="Disconnector",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Disconnector" user definitions:
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
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "retained", "normalOpen", "switchOnDate", "switchOnCount",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "SwitchingOperations", "CompositeSwitch",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.GroundDisconnector",
        title="GroundDisconnector",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GroundDisconnector" user definitions:
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

    # Prime movers that drive this SynchronousMachine.
    DrivenBy_PrimeMover = List(Instance("CIM.Generation.GenerationDynamics.PrimeMover"),
        desc="Prime movers that drive this SynchronousMachine.")

    # The default ReactiveCapabilityCurve for use by a SynchronousMachine
    InitialReactiveCapabilityCurve = Instance("CIM.Wires.ReactiveCapabilityCurve",
        desc="The default ReactiveCapabilityCurve for use by a SynchronousMachine",
        transient=True,
        opposite="InitiallyUsedBySynchronousMachine",
        editor=InstanceEditor(name="_reactivecapabilitycurves"))

    def _get_reactivecapabilitycurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Wires.ReactiveCapabilityCurve" ]
        else:
            return []

    _reactivecapabilitycurves = Property(fget=_get_reactivecapabilitycurves)

    # All available Reactive capability curves for this SynchronousMachine.
    ReactiveCapabilityCurves = List(Instance("CIM.Wires.ReactiveCapabilityCurve"),
        desc="All available Reactive capability curves for this SynchronousMachine.")

    # A synchronous machine may operate as a generator and as such becomes a member of a generating unit
    MemberOf_GeneratingUnit = Instance("CIM.Generation.Production.GeneratingUnit",
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
                    "CIM.Generation.Production.GeneratingUnit" ]
        else:
            return []

    _generatingunits = Property(fget=_get_generatingunits)

    # The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
    Drives_HydroPump = Instance("CIM.Generation.Production.HydroPump",
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
                    "CIM.Generation.Production.HydroPump" ]
        else:
            return []

    _hydropumps = Property(fget=_get_hydropumps)

    # Method of cooling the machine.
    coolantType = CoolantType(desc="Method of cooling the machine.")

    # Current mode of operation.
    operatingMode = SynchronousMachineOperatingMode(desc="Current mode of operation.")

    # Modes that this synchronous machine can operate in.
    type = SynchronousMachineType(desc="Modes that this synchronous machine can operate in.")

    # Nameplate apparent power rating for the unit
    ratedS = ApparentPower(desc="Nameplate apparent power rating for the unit")

    # Damping torque coefficient, a proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.
    damping = Damping(desc="Damping torque coefficient, a proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.")

    # Quadrature-axis synchronous reactance (Xq) , the ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency.
    xQuadSync = Reactance(desc="Quadrature-axis synchronous reactance (Xq) , the ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency.")

    # Positive sequence resistance of the synchronous machine.
    r = Resistance(desc="Positive sequence resistance of the synchronous machine.")

    # Default base reactive power value. This value represents the initial reactive power that can be used by any application function.
    baseQ = ReactivePower(desc="Default base reactive power value. This value represents the initial reactive power that can be used by any application function.")

    # Zero sequence resistance of the synchronous machine.
    r0 = Resistance(desc="Zero sequence resistance of the synchronous machine.")

    # Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
    maxQ = ReactivePower(desc="Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.")

    # Quadrature-axis subtransient reactance, also known as X'q.
    xQuadSubtrans = Reactance(desc="Quadrature-axis subtransient reactance, also known as X'q.")

    # Active power consumed when in condenser mode operation.
    condenserP = ActivePower(desc="Active power consumed when in condenser mode operation.")

    # Temperature or pressure of coolant medium
    coolantCondition = Float(desc="Temperature or pressure of coolant medium")

    # Negative sequence resistance.
    r2 = Resistance(desc="Negative sequence resistance.")

    # Minimum reactive power limit for the unit.
    minQ = ReactivePower(desc="Minimum reactive power limit for the unit.")

    # Maximum voltage limit for the unit.
    maxU = Voltage(desc="Maximum voltage limit for the unit.")

    # The energy stored in the rotor when operating at rated speed. This value is used in the accelerating power reference frame for  operator training simulator solutions.
    inertia = PU(desc="The energy stored in the rotor when operating at rated speed. This value is used in the accelerating power reference frame for  operator training simulator solutions.")

    # Positive sequence reactance of the synchronous machine.
    x = Reactance(desc="Positive sequence reactance of the synchronous machine.")

    # Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a lagging MVAr violation.
    aVRToManualLag = Seconds(desc="Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a lagging MVAr violation.")

    # Quadrature-axis transient reactance, also known as X'q.
    xQuadTrans = Reactance(desc="Quadrature-axis transient reactance, also known as X'q.")

    # Percent of the coordinated reactive control that comes from this machine.
    qPercent = PerCent(desc="Percent of the coordinated reactive control that comes from this machine.")

    # Priority of unit for reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on.
    referencePriority = Int(desc="Priority of unit for reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on.")

    # Direct-axis transient reactance, also known as X'd.
    xDirectTrans = Reactance(desc="Direct-axis transient reactance, also known as X'd.")

    # Direct-axis subtransient reactance, also known as X'd.
    xDirectSubtrans = Reactance(desc="Direct-axis subtransient reactance, also known as X'd.")

    # Zero sequence reactance of the synchronous machine.
    x0 = Reactance(desc="Zero sequence reactance of the synchronous machine.")

    # Direct-axis synchronous reactance. The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed. (Xd)
    xDirectSync = Reactance(desc="Direct-axis synchronous reactance. The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed. (Xd)")

    # Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a leading MVAr violation.
    aVRToManualLead = Seconds(desc="Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a leading MVAr violation.")

    # Minimum voltage  limit for the unit.
    minU = Voltage(desc="Minimum voltage  limit for the unit.")

    # Negative sequence reactance.
    x2 = Reactance(desc="Negative sequence reactance.")

    # Time delay required when switching from Manual to Automatic Voltage Regulation. This value is used in the accelerating power reference frame for powerflow solutions
    manualToAVR = Seconds(desc="Time delay required when switching from Manual to Automatic Voltage Regulation. This value is used in the accelerating power reference frame for powerflow solutions")

    #--------------------------------------------------------------------------
    #  Begin "SynchronousMachine" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "coolantType", "operatingMode", "type", "ratedS", "damping", "xQuadSync", "r", "baseQ", "r0", "maxQ", "xQuadSubtrans", "condenserP", "coolantCondition", "r2", "minQ", "maxU", "inertia", "x", "aVRToManualLag", "xQuadTrans", "qPercent", "referencePriority", "xDirectTrans", "xDirectSubtrans", "x0", "xDirectSync", "aVRToManualLead", "minU", "x2", "manualToAVR",
                label="Attributes", columns=3),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "RegulatingControl", "Controls", "DrivenBy_PrimeMover", "InitialReactiveCapabilityCurve", "ReactiveCapabilityCurves", "MemberOf_GeneratingUnit", "Drives_HydroPump",
                label="References", columns=2),
            dock="tab"),
        id="CIM.Wires.SynchronousMachine",
        title="SynchronousMachine",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SynchronousMachine" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PhaseTapChanger" class:
#------------------------------------------------------------------------------

class PhaseTapChanger(TapChanger):
    """ A specialization of a voltage tap changer that has detailed modeling for phase shifting capabilities.   A phase shifting tap changer is also in general a voltage magnitude transformer.    The symmetrical and asymmetrical transformer tap changer models are defined here.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The transformer winding to which the phase tap changer belongs.
    TransformerWinding = Instance("CIM.Wires.TransformerWinding",
        desc="The transformer winding to which the phase tap changer belongs.",
        transient=True,
        opposite="PhaseTapChanger",
        editor=InstanceEditor(name="_transformerwindings"))

    def _get_transformerwindings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Wires.TransformerWinding" ]
        else:
            return []

    _transformerwindings = Property(fget=_get_transformerwindings)

    # The type of phase shifter construction.
    phaseTapChangerType = PhaseTapChangerKind(desc="The type of phase shifter construction.")

    # The reactance at the maximum tap step.
    xStepMax = Reactance(desc="The reactance at the maximum tap step.")

    # The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees.
    windingConnectionAngle = AngleDegrees(desc="The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees.")

    # Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accureatly computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available.
    stepPhaseShiftIncrement = AngleDegrees(desc="Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accureatly computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available.")

    # Similar to TapChanger.nominalVoltage, but this is the nominal voltage in the out of phase winding at the nominal tap step. A typical case may have zero voltage at the nominal step, indicating no phase shift at the nominal voltage.
    nominalVoltageOutOfPhase = Voltage(desc="Similar to TapChanger.nominalVoltage, but this is the nominal voltage in the out of phase winding at the nominal tap step. A typical case may have zero voltage at the nominal step, indicating no phase shift at the nominal voltage.")

    # The reactance at the minimum tap step.
    xStepMin = Reactance(desc="The reactance at the minimum tap step.")

    # The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding.
    voltageStepIncrementOutOfPhase = Voltage(desc="The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding.")

    #--------------------------------------------------------------------------
    #  Begin "PhaseTapChanger" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "tculControlMode", "type", "normalStep", "neutralStep", "initialDelay", "neutralU", "stepVoltageIncrement", "highStep", "stepPhaseShiftIncrement_DeleteThis", "subsequentDelay", "lowStep", "phaseTapChangerType", "xStepMax", "windingConnectionAngle", "stepPhaseShiftIncrement", "nominalVoltageOutOfPhase", "xStepMin", "voltageStepIncrementOutOfPhase",
                label="Attributes", columns=2),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "RegulatingControl", "SvTapStep", "TransformerWinding",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.PhaseTapChanger",
        title="PhaseTapChanger",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PhaseTapChanger" user definitions:
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

    # SVC control mode.
    sVCControlMode = SVCControlMode(desc="SVC control mode.")

    # Maximum available inductive reactive power
    inductiveRating = Reactance(desc="Maximum available inductive reactive power")

    # Maximum available capacitive reactive power
    capacitiveRating = Reactance(desc="Maximum available capacitive reactive power")

    # The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint.
    slope = VoltagePerReactivePower(desc="The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint.")

    # The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero.
    voltageSetPoint = Voltage(desc="The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero.")

    #--------------------------------------------------------------------------
    #  Begin "StaticVarCompensator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "sVCControlMode", "inductiveRating", "capacitiveRating", "slope", "voltageSetPoint",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "RegulatingControl", "Controls",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.StaticVarCompensator",
        title="StaticVarCompensator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StaticVarCompensator" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RatioTapChanger" class:
#------------------------------------------------------------------------------

class RatioTapChanger(TapChanger):
    """ A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The transformer winding to which the ratio tap changer belongs.
    TransformerWinding = Instance("CIM.Wires.TransformerWinding",
        desc="The transformer winding to which the ratio tap changer belongs.",
        transient=True,
        opposite="RatioTapChanger",
        editor=InstanceEditor(name="_transformerwindings"))

    def _get_transformerwindings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Wires.TransformerWinding" ]
        else:
            return []

    _transformerwindings = Property(fget=_get_transformerwindings)

    #--------------------------------------------------------------------------
    #  Begin "RatioTapChanger" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "tculControlMode", "type", "normalStep", "neutralStep", "initialDelay", "neutralU", "stepVoltageIncrement", "highStep", "stepPhaseShiftIncrement_DeleteThis", "subsequentDelay", "lowStep",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "RegulatingControl", "SvTapStep", "TransformerWinding",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.RatioTapChanger",
        title="RatioTapChanger",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RatioTapChanger" user definitions:
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
    ampRating = CurrentFlow(desc="Fault interrupting current rating.")

    #--------------------------------------------------------------------------
    #  Begin "Fuse" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "retained", "normalOpen", "switchOnDate", "switchOnCount", "ampRating",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "SwitchingOperations", "CompositeSwitch",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.Fuse",
        title="Fuse",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Fuse" user definitions:
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
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "retained", "normalOpen", "switchOnDate", "switchOnCount",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "SwitchingOperations", "CompositeSwitch",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.Jumper",
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

    # Resistance of the DC line segment.
    dcSegmentResistance = Resistance(desc="Resistance of the DC line segment.")

    # Inductance of the DC line segment.
    dcSegmentInductance = Inductance(desc="Inductance of the DC line segment.")

    #--------------------------------------------------------------------------
    #  Begin "DCLineSegment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "length", "r", "bch", "r0", "x", "b0ch", "gch", "g0ch", "x0", "dcSegmentResistance", "dcSegmentInductance",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "ConductorType",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.DCLineSegment",
        title="DCLineSegment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DCLineSegment" user definitions:
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

    # Fault interrupting current rating.
    ratedCurrent = CurrentFlow(desc="Fault interrupting current rating.")

    # The transition time from open to close.
    inTransitTime = Seconds(desc="The transition time from open to close.")

    #--------------------------------------------------------------------------
    #  Begin "Breaker" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases", "retained", "normalOpen", "switchOnDate", "switchOnCount", "ratedCurrent", "inTransitTime",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "SwitchingOperations", "CompositeSwitch", "OperatedBy_ProtectionEquipments", "RecloseSequences",
                label="References", columns=2),
            dock="tab"),
        id="CIM.Wires.Breaker",
        title="Breaker",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Breaker" user definitions:
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
    VoltageControlZone = Instance("CIM.Wires.VoltageControlZone",
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
                    "CIM.Wires.VoltageControlZone" ]
        else:
            return []

    _voltagecontrolzones = Property(fget=_get_voltagecontrolzones)

    #--------------------------------------------------------------------------
    #  Begin "BusbarSection" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "phases",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "SvStatus", "BaseVoltage", "ProtectionEquipments", "Terminals", "ClearanceTags", "VoltageControlZone",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Wires.BusbarSection",
        title="BusbarSection",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BusbarSection" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
