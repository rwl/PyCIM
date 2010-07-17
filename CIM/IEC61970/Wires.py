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

from CIM.IEC61970.Core import ConductingEquipment
from CIM.IEC61970.Core import Equipment
from CIM.IEC61970.Core import PowerSystemResource
from CIM.IEC61970.LoadModel import SeasonDayTypeSchedule
from CIM.IEC61970.Core import EquipmentContainer
from CIM.IEC61970.Core import Curve
from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61970.Domain import CurrentFlow
from CIM.IEC61970.Domain import Seconds
from CIM.IEC61970.Domain import Voltage
from CIM.IEC61970.Domain import PerCent
from CIM.IEC61970.Domain import AngleDegrees
from CIM.IEC61970.Domain import Reactance
from CIM.IEC61970.Domain import Resistance
from CIM.IEC61970.Domain import ActivePower
from CIM.IEC61970.Domain import ReactivePower
from CIM.IEC61970.Domain import AngleRadians
from CIM.IEC61970.Domain import Temperature
from CIM.IEC61970.Domain import Pressure
from CIM.IEC61970.Domain import KWActivePower
from CIM.IEC61970.Domain import Impedance
from CIM.IEC61970.Domain import Length
from CIM.IEC61970.Domain import Susceptance
from CIM.IEC61970.Domain import Conductance
from CIM.IEC61970.Domain import VoltagePerReactivePower
from CIM.IEC61970.Domain import Damping
from CIM.IEC61970.Domain import PU
from CIM.IEC61970.Domain import ApparentPower
from CIM.IEC61970.Domain import Frequency
from CIM.IEC61970.Domain import Inductance



from enthought.traits.api import Instance, List, Property, Str, Enum, Int, Bool, Date, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------
OperatingMode = Str(desc="http://www.w3.org/2001/XMLSchema#stringTextual name for an operating mode")
CompositeSwitchType = Str(desc="http://www.w3.org/2001/XMLSchema#stringAn alphanumeric code that can be used as a reference to extar information such as the description of the interlocking scheme if any")

# Control modes for a transformer.
TransformerControlMode = Enum("volt", "reactive", desc="Control modes for a transformer.")
# Synchronous machine type.
SynchronousMachineType = Enum("generator", "generator_or_condenser", "condenser", desc="Synchronous machine type.")
# Winding connection type.
WindingConnection = Enum("Y", "Yn", "Zn", "I", "A", "D", "Z", desc="Winding connection type.")
# Winding type.
WindingType = Enum("tertiary", "secondary", "primary", "quaternary", desc="Winding type.")
# The kind of regulation model.   For example regulating voltage, reactive power, active power, etc.
RegulatingControlModeKind = Enum("reactivePower", "timeScheduled", "voltage", "currentFlow", "admittance", "fixed", "powerFactor", "temperature", "activePower", desc="The kind of regulation model.   For example regulating voltage, reactive power, active power, etc.")
# Transformer tap changer type. Indicates the capabilities of the tap changer independent of the operating mode.
TapChangerKind = Enum("voltageControl", "fixed", "phaseControl", "voltageAndPhaseControl", desc="Transformer tap changer type. Indicates the capabilities of the tap changer independent of the operating mode.")
# Method of cooling a machine.
CoolantType = Enum("air", "hydrogenGas", "water", desc="Method of cooling a machine.")
# Synchronous machine operating mode.
SynchronousMachineOperatingMode = Enum("condenser", "generator", desc="Synchronous machine operating mode.")
# The construction type of the phase shifting tap changer.
PhaseTapChangerKind = Enum("symmetrical", "unknown", "asymmetrical", desc="The construction type of the phase shifting tap changer.")
# Static VAr Compensator control mode.
SVCControlMode = Enum("off", "reactivePower", "voltage", desc="Static VAr Compensator control mode.")

#------------------------------------------------------------------------------
#  "Switch" class:
#------------------------------------------------------------------------------

class Switch(ConductingEquipment):
    """ A generic device designed to close, or open, or both, one or more electric circuits.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    LoadMgmtFunctions = List(Instance("CIM.IEC61968.Informative.InfLoadControl.LoadMgmtFunction"))

    # Composite switch this Switch belongs to
    CompositeSwitch = Instance("CIM.IEC61970.Wires.CompositeSwitch",
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
                    "CIM.IEC61970.Wires.CompositeSwitch" ]
        else:
            return []

    _compositeswitchs = Property(fget=_get_compositeswitchs)

    # A Switch can be associated with SwitchSchedules.
    SwitchSchedules = List(Instance("CIM.IEC61970.Wires.SwitchSchedule"),
        desc="A Switch can be associated with SwitchSchedules.")

    ConnectDisconnectFunctions = List(Instance("CIM.IEC61968.LoadControl.ConnectDisconnectFunction"))

    # A switch may be operated by many schedules.
    SwitchingOperations = List(Instance("CIM.IEC61970.Outage.SwitchingOperation"),
        desc="A switch may be operated by many schedules.")

    # The switch on count since the switch was last reset or initialized.
    switchOnCount = Int(desc="The switch on count since the switch was last reset or initialized.")

    # The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.
    normalOpen = Bool(desc="The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.")

    # Branch is retained in a bus branch model.
    retained = Bool(desc="Branch is retained in a bus branch model.")

    # The date and time when the switch was last switched on.
    switchOnDate = Date(desc="The date and time when the switch was last switched on.")

    #--------------------------------------------------------------------------
    #  Begin "Switch" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "switchOnCount", "normalOpen", "retained", "switchOnDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "LoadMgmtFunctions", "CompositeSwitch", "SwitchSchedules", "ConnectDisconnectFunctions", "SwitchingOperations",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Wires.Switch",
        title="Switch",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Switch" user definitions:
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
    PowerTransformer = Instance("CIM.IEC61970.Wires.PowerTransformer",
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
                    "CIM.IEC61970.Wires.PowerTransformer" ]
        else:
            return []

    _powertransformers = Property(fget=_get_powertransformers)

    #--------------------------------------------------------------------------
    #  Begin "HeatExchanger" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "PowerTransformer",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Wires.HeatExchanger",
        title="HeatExchanger",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "HeatExchanger" user definitions:
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

    RegulatingControl = Instance("CIM.IEC61970.Wires.RegulatingControl",
        transient=True,
        opposite="TapChanger",
        editor=InstanceEditor(name="_regulatingcontrols"))

    def _get_regulatingcontrols(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.RegulatingControl" ]
        else:
            return []

    _regulatingcontrols = Property(fget=_get_regulatingcontrols)

    # A TapChanger can have an associated ImpedanceVariationCurve to define impedance variations with tap step changes.
    ImpedanceVariationCurve = Instance("CIM.IEC61970.Wires.ImpedanceVariationCurve",
        desc="A TapChanger can have an associated ImpedanceVariationCurve to define impedance variations with tap step changes.",
        transient=True,
        opposite="TapChanger",
        editor=InstanceEditor(name="_impedancevariationcurves"))

    def _get_impedancevariationcurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.ImpedanceVariationCurve" ]
        else:
            return []

    _impedancevariationcurves = Property(fget=_get_impedancevariationcurves)

    # The tap step state associated with the tap changer.
    SvTapStep = Instance("CIM.IEC61970.StateVariables.SvTapStep",
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
                    "CIM.IEC61970.StateVariables.SvTapStep" ]
        else:
            return []

    _svtapsteps = Property(fget=_get_svtapsteps)

    # A TapChanger can have TapSchedules.
    TapSchedules = List(Instance("CIM.IEC61970.Wires.TapSchedule"),
        desc="A TapChanger can have TapSchedules.")

    # The neutral tap step position for this winding.
    neutralStep = Int(desc="The neutral tap step position for this winding.")

    # For an LTC, the delay for subsequent tap changer operation (second and later step changes)
    subsequentDelay = Seconds(desc="For an LTC, the delay for subsequent tap changer operation (second and later step changes)")

    # Voltage at which the winding operates at the neutral tap setting.
    neutralU = Voltage(desc="Voltage at which the winding operates at the neutral tap setting.")

    # Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step.
    stepVoltageIncrement = PerCent(desc="Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step.")

    # Lowest possible tap step position, retard from neutral
    lowStep = Int(desc="Lowest possible tap step position, retard from neutral")

    # The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.
    normalStep = Int(desc="The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.")

    # Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating.
    regulationStatus = Bool(desc="Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating.")

    # Highest possible tap step position, advance from neutral
    highStep = Int(desc="Highest possible tap step position, advance from neutral")

    # For an LTC, the delay for initial tap changer operation (first step change)
    initialDelay = Seconds(desc="For an LTC, the delay for initial tap changer operation (first step change)")

    # Specifies whether or not a TapChanger has load tap changing capabilities.
    ltcFlag = Bool(desc="Specifies whether or not a TapChanger has load tap changing capabilities.")

    #--------------------------------------------------------------------------
    #  Begin "TapChanger" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "neutralStep", "subsequentDelay", "neutralU", "stepVoltageIncrement", "lowStep", "normalStep", "regulationStatus", "highStep", "initialDelay", "ltcFlag",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "RegulatingControl", "ImpedanceVariationCurve", "SvTapStep", "TapSchedules",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Wires.TapChanger",
        title="TapChanger",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TapChanger" user definitions:
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
    RegulationSchedule = List(Instance("CIM.IEC61970.Wires.RegulationSchedule"),
        desc="Schedule for this Regulating regulating control.")

    # copy from reg conduting eq
    TapChanger = List(Instance("CIM.IEC61970.Wires.TapChanger"),
        desc="copy from reg conduting eq")

    # The equipment that participates in this regulating control scheme.
    RegulatingCondEq = List(Instance("CIM.IEC61970.Wires.RegulatingCondEq"),
        desc="The equipment that participates in this regulating control scheme.")

    # The terminal associated with this regulating control.
    Terminal = Instance("CIM.IEC61970.Core.Terminal",
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
                    "CIM.IEC61970.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

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
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "mode", "targetRange", "targetValue", "discrete",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "RegulationSchedule", "TapChanger", "RegulatingCondEq", "Terminal",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Wires.RegulatingControl",
        title="RegulatingControl",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegulatingControl" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TapSchedule" class:
#------------------------------------------------------------------------------

class TapSchedule(SeasonDayTypeSchedule):
    """ A pre-established pattern over time for a tap step.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A TapSchedule is associated with a TapChanger.
    TapChanger = Instance("CIM.IEC61970.Wires.TapChanger",
        desc="A TapSchedule is associated with a TapChanger.",
        transient=True,
        opposite="TapSchedules",
        editor=InstanceEditor(name="_tapchangers"))

    def _get_tapchangers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.TapChanger" ]
        else:
            return []

    _tapchangers = Property(fget=_get_tapchangers)

    # Line drop reactance.
    lineDropX = Reactance(desc="Line drop reactance.")

    # Flag to indicate that line drop compensation is to be applied
    lineDropCompensation = Bool(desc="Flag to indicate that line drop compensation is to be applied")

    # Line drop resistance.
    lineDropR = Resistance(desc="Line drop resistance.")

    #--------------------------------------------------------------------------
    #  Begin "TapSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value2Multiplier", "value1Unit", "value2Unit", "value1Multiplier", "startTime", "timeStep", "endTime", "lineDropX", "lineDropCompensation", "lineDropR",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "DayType", "Season", "TapChanger",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Wires.TapSchedule",
        title="TapSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TapSchedule" user definitions:
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
    PowerCutZone = Instance("CIM.IEC61970.LoadModel.PowerCutZone",
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
                    "CIM.IEC61970.LoadModel.PowerCutZone" ]
        else:
            return []

    _powercutzones = Property(fget=_get_powercutzones)

    ServiceDeliveryPoints = List(Instance("CIM.IEC61968.Metering.ServiceDeliveryPoint"))

    # The load response characteristic of this load.
    LoadResponse = Instance("CIM.IEC61970.LoadModel.LoadResponseCharacteristic",
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
                    "CIM.IEC61970.LoadModel.LoadResponseCharacteristic" ]
        else:
            return []

    _loadresponsecharacteristics = Property(fget=_get_loadresponsecharacteristics)

    # Fixed reactive power as per cent of load group fixed reactive power.
    qfixedPct = PerCent(desc="Fixed reactive power as per cent of load group fixed reactive power.")

    # Active power of the load that is a fixed quantity.
    pfixed = ActivePower(desc="Active power of the load that is a fixed quantity.")

    # Number of individual customers represented by this Demand
    customerCount = Int(desc="Number of individual customers represented by this Demand")

    # Reactive power of the load that is a fixed quantity.
    qfixed = ReactivePower(desc="Reactive power of the load that is a fixed quantity.")

    # Fixed active power as per cent of load group fixed active power
    pfixedPct = PerCent(desc="Fixed active power as per cent of load group fixed active power")

    #--------------------------------------------------------------------------
    #  Begin "EnergyConsumer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "qfixedPct", "pfixed", "customerCount", "qfixed", "pfixedPct",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "PowerCutZone", "ServiceDeliveryPoints", "LoadResponse",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Wires.EnergyConsumer",
        title="EnergyConsumer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EnergyConsumer" user definitions:
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

    # Negative sequence Thevenin resistance.
    rn = Resistance(desc="Negative sequence Thevenin resistance.")

    # Positive sequence Thevenin resistance.
    r = Resistance(desc="Positive sequence Thevenin resistance.")

    # Zero sequence Thevenin resistance.
    r0 = Resistance(desc="Zero sequence Thevenin resistance.")

    # Phase-to-phase open circuit voltage magnitude.
    voltageMagnitude = Voltage(desc="Phase-to-phase open circuit voltage magnitude.")

    # Positive sequence Thevenin reactance.
    x = Reactance(desc="Positive sequence Thevenin reactance.")

    # Phase angle of a-phase open circuit.
    voltageAngle = AngleRadians(desc="Phase angle of a-phase open circuit.")

    # Negative sequence Thevenin reactance.
    xn = Reactance(desc="Negative sequence Thevenin reactance.")

    # Zero sequence Thevenin reactance.
    x0 = Reactance(desc="Zero sequence Thevenin reactance.")

    # High voltage source load
    activePower = ActivePower(desc="High voltage source load")

    # Phase-to-phase nominal voltage.
    nominalVoltage = Voltage(desc="Phase-to-phase nominal voltage.")

    #--------------------------------------------------------------------------
    #  Begin "EnergySource" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "rn", "r", "r0", "voltageMagnitude", "x", "voltageAngle", "xn", "x0", "activePower", "nominalVoltage",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Wires.EnergySource",
        title="EnergySource",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EnergySource" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SwitchSchedule" class:
#------------------------------------------------------------------------------

class SwitchSchedule(SeasonDayTypeSchedule):
    """ A schedule of switch positions.  If RegularTimePoint.value1 is 0, the switch is open.  If 1, the switch is closed.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A SwitchSchedule is associated with a Switch.
    Switch = Instance("CIM.IEC61970.Wires.Switch",
        desc="A SwitchSchedule is associated with a Switch.",
        transient=True,
        opposite="SwitchSchedules",
        editor=InstanceEditor(name="_switchs"))

    def _get_switchs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.Switch" ]
        else:
            return []

    _switchs = Property(fget=_get_switchs)

    #--------------------------------------------------------------------------
    #  Begin "SwitchSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value2Multiplier", "value1Unit", "value2Unit", "value1Multiplier", "startTime", "timeStep", "endTime",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "DayType", "Season", "Switch",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Wires.SwitchSchedule",
        title="SwitchSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SwitchSchedule" user definitions:
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

    # A transmission line can be part of a transmission corridor
    TransmissionRightOfWay = Instance("CIM.IEC61968.Informative.EnergyScheduling.TransmissionRightOfWay",
        desc="A transmission line can be part of a transmission corridor",
        transient=True,
        opposite="Lines",
        editor=InstanceEditor(name="_transmissionrightofways"))

    def _get_transmissionrightofways(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.TransmissionRightOfWay" ]
        else:
            return []

    _transmissionrightofways = Property(fget=_get_transmissionrightofways)

    Flowgates = List(Instance("CIM.IEC61968.Informative.MarketOperations.Flowgate"))

    # A Line can be contained by a SubGeographical Region.
    Region = Instance("CIM.IEC61970.Core.SubGeographicalRegion",
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
                    "CIM.IEC61970.Core.SubGeographicalRegion" ]
        else:
            return []

    _subgeographicalregions = Property(fget=_get_subgeographicalregions)

    #--------------------------------------------------------------------------
    #  Begin "Line" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "TopologicalNode", "ConnectivityNodes", "Equipments", "TransmissionRightOfWay", "Flowgates", "Region",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Wires.Line",
        title="Line",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Line" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RatioVariationCurve" class:
#------------------------------------------------------------------------------

class RatioVariationCurve(Curve):
    """ A Ratio Variation Curve describes the change in tap ratio in relationship to tap step changes.  The tap step is represented using the xValue and the ratio using y1value.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A RatioVariationCurve defines tap ratio changes for a RatioTapChanger.
    RatioTapChanger = Instance("CIM.IEC61970.Wires.RatioTapChanger",
        desc="A RatioVariationCurve defines tap ratio changes for a RatioTapChanger.",
        transient=True,
        opposite="RatioVariationCurve",
        editor=InstanceEditor(name="_ratiotapchangers"))

    def _get_ratiotapchangers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.RatioTapChanger" ]
        else:
            return []

    _ratiotapchangers = Property(fget=_get_ratiotapchangers)

    #--------------------------------------------------------------------------
    #  Begin "RatioVariationCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "RatioTapChanger",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Wires.RatioVariationCurve",
        title="RatioVariationCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RatioVariationCurve" user definitions:
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

    # Synchronous machines using this curve.
    SynchronousMachines = List(Instance("CIM.IEC61970.Wires.SynchronousMachine"),
        desc="Synchronous machines using this curve.")

    # Synchronous machines using this curve as default.
    InitiallyUsedBySynchronousMachines = List(Instance("CIM.IEC61970.Wires.SynchronousMachine"),
        desc="Synchronous machines using this curve as default.")

    # The machine's coolant temperature (e.g., ambient air or stator circulating water).
    coolantTemperature = Temperature(desc="The machine's coolant temperature (e.g., ambient air or stator circulating water).")

    # The hydrogen coolant pressure
    hydrogenPressure = Pressure(desc="The hydrogen coolant pressure")

    #--------------------------------------------------------------------------
    #  Begin "ReactiveCapabilityCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit", "coolantTemperature", "hydrogenPressure",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "SynchronousMachines", "InitiallyUsedBySynchronousMachines",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Wires.ReactiveCapabilityCurve",
        title="ReactiveCapabilityCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ReactiveCapabilityCurve" user definitions:
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
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Wires.Connector",
        title="Connector",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Connector" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Resistor" class:
#------------------------------------------------------------------------------

class Resistor(ConductingEquipment):
    """ Resistor, typically used in filter configurations or as earthing resistor for transformers.  Used for electrical model of distribution networks.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ResistorTypeAsset = Instance("CIM.IEC61968.Informative.InfTypeAsset.ResistorTypeAsset",
        transient=True,
        opposite="Resistors",
        editor=InstanceEditor(name="_resistortypeassets"))

    def _get_resistortypeassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfTypeAsset.ResistorTypeAsset" ]
        else:
            return []

    _resistortypeassets = Property(fget=_get_resistortypeassets)

    ResistorAsset = Instance("CIM.IEC61968.Informative.InfAssets.ResistorAsset",
        transient=True,
        opposite="Resistor",
        editor=InstanceEditor(name="_resistorassets"))

    def _get_resistorassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.ResistorAsset" ]
        else:
            return []

    _resistorassets = Property(fget=_get_resistorassets)

    #--------------------------------------------------------------------------
    #  Begin "Resistor" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "ResistorTypeAsset", "ResistorAsset",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Wires.Resistor",
        title="Resistor",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Resistor" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SeriesCompensator" class:
#------------------------------------------------------------------------------

class SeriesCompensator(ConductingEquipment):
    """ A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.  It is a two terminal device.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Positive sequence resistance.
    r = Resistance(desc="Positive sequence resistance.")

    # Positive sequence reactance.
    x = Reactance(desc="Positive sequence reactance.")

    #--------------------------------------------------------------------------
    #  Begin "SeriesCompensator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "r", "x",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Wires.SeriesCompensator",
        title="SeriesCompensator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SeriesCompensator" user definitions:
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
    To_TransformerWinding = Instance("CIM.IEC61970.Wires.TransformerWinding",
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
                    "CIM.IEC61970.Wires.TransformerWinding" ]
        else:
            return []

    _transformerwindings = Property(fget=_get_transformerwindings)

    # The winding from which the test was conducted
    From_TransformerWinding = Instance("CIM.IEC61970.Wires.TransformerWinding",
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
                    "CIM.IEC61970.Wires.TransformerWinding" ]
        else:
            return []

    _transformerwindings = Property(fget=_get_transformerwindings)

    # The phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
    phaseShift = AngleDegrees(desc="The phase shift measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.")

    # The tap step number for the 'from' winding of the test pair.
    fromTapStep = Int(desc="The tap step number for the 'from' winding of the test pair.")

    # The no load loss kW 'to' winding open-circuited) from the test report.
    noLoadLoss = KWActivePower(desc="The no load loss kW 'to' winding open-circuited) from the test report.")

    # The tap step number for the 'to' winding of the test pair.
    toTapStep = Int(desc="The tap step number for the 'to' winding of the test pair.")

    # The exciting current on open-circuit test, expressed as a percentage of rated current, at nominal voltage
    excitingCurrent = PerCent(desc="The exciting current on open-circuit test, expressed as a percentage of rated current, at nominal voltage")

    # The load loss kW ('to' winding short-circuited) from the test report.
    loadLoss = KWActivePower(desc="The load loss kW ('to' winding short-circuited) from the test report.")

    # The leakage impedance measured at the 'from' winding  with the 'to' winding short-circuited and all other windings open-circuited.  Leakage impedance is expressed in units based on the apparent power and voltage ratings of the 'from' winding.
    leakageImpedance = Impedance(desc="The leakage impedance measured at the 'from' winding  with the 'to' winding short-circuited and all other windings open-circuited.  Leakage impedance is expressed in units based on the apparent power and voltage ratings of the 'from' winding.")

    # The voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.
    voltage = Voltage(desc="The voltage measured at the open-circuited 'to' winding, with the 'from' winding set to the 'from' winding's rated voltage and all other windings open-circuited.")

    #--------------------------------------------------------------------------
    #  Begin "WindingTest" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "phaseShift", "fromTapStep", "noLoadLoss", "toTapStep", "excitingCurrent", "loadLoss", "leakageImpedance", "voltage",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "To_TransformerWinding", "From_TransformerWinding",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Wires.WindingTest",
        title="WindingTest",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "WindingTest" user definitions:
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

    # Segment length for calculating line section capabilities
    length = Length(desc="Segment length for calculating line section capabilities")

    #--------------------------------------------------------------------------
    #  Begin "Conductor" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "length",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Wires.Conductor",
        title="Conductor",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Conductor" user definitions:
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
    TransformerWindings = List(Instance("CIM.IEC61970.Wires.TransformerWinding"),
        desc="A transformer has windings")

    Flowgates = List(Instance("CIM.IEC61968.Informative.MarketOperations.Flowgate"))

    # A transformer may have a heat exchanger
    HeatExchanger = Instance("CIM.IEC61970.Wires.HeatExchanger",
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
                    "CIM.IEC61970.Wires.HeatExchanger" ]
        else:
            return []

    _heatexchangers = Property(fget=_get_heatexchangers)

    # Core shunt magnetizing susceptance in the saturation region.
    bmagSat = PerCent(desc="Core shunt magnetizing susceptance in the saturation region.")

    # The reference voltage at which the magnetizing saturation measurements were made
    magBaseU = Voltage(desc="The reference voltage at which the magnetizing saturation measurements were made")

    # Core magnetizing saturation curve knee flux level.
    magSatFlux = PerCent(desc="Core magnetizing saturation curve knee flux level.")

    #--------------------------------------------------------------------------
    #  Begin "PowerTransformer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "bmagSat", "magBaseU", "magSatFlux",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "TransformerWindings", "Flowgates", "HeatExchanger",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Wires.PowerTransformer",
        title="PowerTransformer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PowerTransformer" user definitions:
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

    # The starting terminal for the calculation of distances along the second branch of the mutual coupling.
    Second_Terminal = Instance("CIM.IEC61970.Core.Terminal",
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
                    "CIM.IEC61970.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    # The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments.
    First_Terminal = Instance("CIM.IEC61970.Core.Terminal",
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
                    "CIM.IEC61970.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    # Distance from the first line's from specified terminal to end of coupled region
    distance12 = Length(desc="Distance from the first line's from specified terminal to end of coupled region")

    # Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section.
    b0ch = Susceptance(desc="Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section.")

    # Zero sequence branch-to-branch mutual impedance coupling, resistance
    r0 = Resistance(desc="Zero sequence branch-to-branch mutual impedance coupling, resistance")

    # Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section.
    g0ch = Conductance(desc="Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section.")

    # Distance from the second line's specified terminal to end of coupled region
    distance22 = Length(desc="Distance from the second line's specified terminal to end of coupled region")

    # Distance from the second line's specified terminal to start of coupled region
    distance21 = Length(desc="Distance from the second line's specified terminal to start of coupled region")

    # Distance from the first line's specified terminal to start of coupled region
    distance11 = Length(desc="Distance from the first line's specified terminal to start of coupled region")

    # Zero sequence branch-to-branch mutual impedance coupling, reactance
    x0 = Reactance(desc="Zero sequence branch-to-branch mutual impedance coupling, reactance")

    #--------------------------------------------------------------------------
    #  Begin "MutualCoupling" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "distance12", "b0ch", "r0", "g0ch", "distance22", "distance21", "distance11", "x0",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Second_Terminal", "First_Terminal",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Wires.MutualCoupling",
        title="MutualCoupling",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MutualCoupling" user definitions:
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

    WindingInsulations = List(Instance("CIM.IEC61968.Informative.InfAssets.WindingInsulation"))

    #--------------------------------------------------------------------------
    #  Begin "Ground" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "WindingInsulations",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Wires.Ground",
        title="Ground",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Ground" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ImpedanceVariationCurve" class:
#------------------------------------------------------------------------------

class ImpedanceVariationCurve(Curve):
    """ An Impedance Variation Curve describes the change in Transformer Winding impedance values in relationship to tap step changes.  The tap step is represented using the xValue, resistance using y1value, reactance using y2value, and magnetizing susceptance using y3value.  The resistance (r), reactance (x), and magnetizing susceptance (b) of the associated TransformerWinding define the impedance when the tap is at neutral step.  The curve values represent the change to the impedance from the neutral step values.  The impedance at a non-neutral step is calculated by adding the neutral step impedance (from the TransformerWinding) to the delta value from the curve.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # An ImpedanceVariationCurve is defines impedance changes for a TapChanger.
    TapChanger = Instance("CIM.IEC61970.Wires.TapChanger",
        desc="An ImpedanceVariationCurve is defines impedance changes for a TapChanger.",
        transient=True,
        opposite="ImpedanceVariationCurve",
        editor=InstanceEditor(name="_tapchangers"))

    def _get_tapchangers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.TapChanger" ]
        else:
            return []

    _tapchangers = Property(fget=_get_tapchangers)

    #--------------------------------------------------------------------------
    #  Begin "ImpedanceVariationCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "TapChanger",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Wires.ImpedanceVariationCurve",
        title="ImpedanceVariationCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ImpedanceVariationCurve" user definitions:
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
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "TopologicalNode", "ConnectivityNodes", "Equipments",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Wires.Plant",
        title="Plant",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Plant" user definitions:
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

    # The regulating control scheme in which this equipment participates.
    RegulatingControl = Instance("CIM.IEC61970.Wires.RegulatingControl",
        desc="The regulating control scheme in which this equipment participates.",
        transient=True,
        opposite="RegulatingCondEq",
        editor=InstanceEditor(name="_regulatingcontrols"))

    def _get_regulatingcontrols(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.RegulatingControl" ]
        else:
            return []

    _regulatingcontrols = Property(fget=_get_regulatingcontrols)

    # The controller outputs used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuator.
    Controls = List(Instance("CIM.IEC61970.Meas.Control"),
        desc="The controller outputs used to actually govern a regulating device, e.g. the magnetization of a synchronous machine or capacitor bank breaker actuator.")

    #--------------------------------------------------------------------------
    #  Begin "RegulatingCondEq" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "RegulatingControl", "Controls",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Wires.RegulatingCondEq",
        title="RegulatingCondEq",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegulatingCondEq" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PhaseVariationCurve" class:
#------------------------------------------------------------------------------

class PhaseVariationCurve(Curve):
    """ A Ratio Variation Curve describes the change in tap ratio in relationship to tap step changes.  The tap step is represented using the xValue and the ratio using y1value.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A PhaseVariationCurve defines phase shift changes for a PhaseTapChanger.
    PhaseTapChanger = Instance("CIM.IEC61970.Wires.PhaseTapChanger",
        desc="A PhaseVariationCurve defines phase shift changes for a PhaseTapChanger.",
        transient=True,
        opposite="PhaseVariationCurve",
        editor=InstanceEditor(name="_phasetapchangers"))

    def _get_phasetapchangers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.PhaseTapChanger" ]
        else:
            return []

    _phasetapchangers = Property(fget=_get_phasetapchangers)

    #--------------------------------------------------------------------------
    #  Begin "PhaseVariationCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "y3Multiplier", "y2Multiplier", "xMultiplier", "y2Unit", "curveStyle", "y1Unit", "y1Multiplier", "y3Unit", "xUnit",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "CurveDatas", "PhaseTapChanger",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Wires.PhaseVariationCurve",
        title="PhaseVariationCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PhaseVariationCurve" user definitions:
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
    To_WindingTest = List(Instance("CIM.IEC61970.Wires.WindingTest"),
        desc="The winding winding tests for which the transformer winding (terminal) participates as the 'to' end of the test.")

    # A transformer has windings
    PowerTransformer = Instance("CIM.IEC61970.Wires.PowerTransformer",
        desc="A transformer has windings",
        transient=True,
        opposite="TransformerWindings",
        editor=InstanceEditor(name="_powertransformers"))

    def _get_powertransformers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.PowerTransformer" ]
        else:
            return []

    _powertransformers = Property(fget=_get_powertransformers)

    # The transformer winding tests for which the transformer winding (terminal) participates as the 'from' part of the test.
    From_WindingTest = List(Instance("CIM.IEC61970.Wires.WindingTest"),
        desc="The transformer winding tests for which the transformer winding (terminal) participates as the 'from' part of the test.")

    # The ratio tap changer associated with the transformer winding.
    RatioTapChanger = Instance("CIM.IEC61970.Wires.RatioTapChanger",
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
                    "CIM.IEC61970.Wires.RatioTapChanger" ]
        else:
            return []

    _ratiotapchangers = Property(fget=_get_ratiotapchangers)

    # The phase tap changer associated with the transformer winding.
    PhaseTapChanger = Instance("CIM.IEC61970.Wires.PhaseTapChanger",
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
                    "CIM.IEC61970.Wires.PhaseTapChanger" ]
        else:
            return []

    _phasetapchangers = Property(fget=_get_phasetapchangers)

    # The type of winding.
    windingType = WindingType(desc="The type of winding.")

    # The type of connection of the winding.
    connectionType = WindingConnection(desc="The type of connection of the winding.")

    # Apparent power that the winding can carry for a short period of time.
    shortTermS = ApparentPower(desc="Apparent power that the winding can carry for a short period of time.")

    # The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.
    ratedU = Voltage(desc="The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.")

    # Set if the winding is grounded.
    grounded = Bool(desc="Set if the winding is grounded.")

    # Zero sequence series resistance of the winding.
    r0 = Resistance(desc="Zero sequence series resistance of the winding.")

    # The normal apparent power rating for the winding
    ratedS = ApparentPower(desc="The normal apparent power rating for the winding")

    # The apparent power that the winding can carry  under emergency conditions.
    emergencyS = ApparentPower(desc="The apparent power that the winding can carry  under emergency conditions.")

    # Zero sequence magnetizing branch susceptance.
    b0 = Susceptance(desc="Zero sequence magnetizing branch susceptance.")

    # Ground reactance path through connected grounding transformer.
    xground = Reactance(desc="Ground reactance path through connected grounding transformer.")

    # Zero sequence magnetizing branch conductance.
    g0 = Conductance(desc="Zero sequence magnetizing branch conductance.")

    # Magnetizing branch susceptance (B mag).  The value can be positive or negative.
    b = Susceptance(desc="Magnetizing branch susceptance (B mag).  The value can be positive or negative.")

    # Positive sequence series resistance of the winding.  For a two winding transformer, the full resistance of the transformer should be entered on the primary (high voltage) winding.
    r = Resistance(desc="Positive sequence series resistance of the winding.  For a two winding transformer, the full resistance of the transformer should be entered on the primary (high voltage) winding.")

    # Ground resistance path through connected grounding transformer.
    rground = Resistance(desc="Ground resistance path through connected grounding transformer.")

    # Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding.
    x = Reactance(desc="Positive sequence series reactance of the winding.  For a two winding transformer, the full reactance of the transformer should be entered on the primary (high voltage) winding.")

    # Basic insulation level voltage rating
    insulationU = Voltage(desc="Basic insulation level voltage rating")

    # Magnetizing branch conductance (G mag).
    g = Conductance(desc="Magnetizing branch conductance (G mag).")

    # Zero sequence series reactance of the winding.
    x0 = Reactance(desc="Zero sequence series reactance of the winding.")

    #--------------------------------------------------------------------------
    #  Begin "TransformerWinding" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "windingType", "connectionType", "shortTermS", "ratedU", "grounded", "r0", "ratedS", "emergencyS", "b0", "xground", "g0", "b", "r", "rground", "x", "insulationU", "g", "x0",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "To_WindingTest", "PowerTransformer", "From_WindingTest", "RatioTapChanger", "PhaseTapChanger",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Wires.TransformerWinding",
        title="TransformerWinding",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TransformerWinding" user definitions:
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
    Switches = List(Instance("CIM.IEC61970.Wires.Switch"),
        desc="Switches contained in this Composite switch.")

    # An alphanumeric code that can be used as a reference to extar information such as the description of the interlocking scheme if any
    compositeSwitchType = CompositeSwitchType(desc="An alphanumeric code that can be used as a reference to extar information such as the description of the interlocking scheme if any")

    #--------------------------------------------------------------------------
    #  Begin "CompositeSwitch" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "compositeSwitchType",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Switches",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Wires.CompositeSwitch",
        title="CompositeSwitch",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CompositeSwitch" user definitions:
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
    RegulationSchedule = Instance("CIM.IEC61970.Wires.RegulationSchedule",
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
                    "CIM.IEC61970.Wires.RegulationSchedule" ]
        else:
            return []

    _regulationschedules = Property(fget=_get_regulationschedules)

    # A VoltageControlZone is controlled by a designated BusbarSection.
    BusbarSection = Instance("CIM.IEC61970.Wires.BusbarSection",
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
                    "CIM.IEC61970.Wires.BusbarSection" ]
        else:
            return []

    _busbarsections = Property(fget=_get_busbarsections)

    #--------------------------------------------------------------------------
    #  Begin "VoltageControlZone" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "RegulationSchedule", "BusbarSection",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Wires.VoltageControlZone",
        title="VoltageControlZone",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "VoltageControlZone" user definitions:
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
    ratedU = Voltage(desc="Rectifier/inverter primary base voltage")

    # The maximum active power on the DC side at which the fconverter should operate.
    maxP = ActivePower(desc="The maximum active power on the DC side at which the fconverter should operate.")

    # The minimum active power on the DC side at which the converter should operate.
    minP = ActivePower(desc="The minimum active power on the DC side at which the converter should operate.")

    # Commutating resistance.
    commutatingResistance = Resistance(desc="Commutating resistance.")

    # Number of bridges
    bridges = Int(desc="Number of bridges")

    # Compounding resistance.
    compoundResistance = Resistance(desc="Compounding resistance.")

    # Minimum compounded DC voltage
    minCompoundVoltage = Voltage(desc="Minimum compounded DC voltage")

    # Commutating reactance at AC bus frequency.
    commutatingReactance = Reactance(desc="Commutating reactance at AC bus frequency.")

    # The minimum voltage on the DC side at which the converter should operate.
    minU = Voltage(desc="The minimum voltage on the DC side at which the converter should operate.")

    # Operating mode for the converter.
    operatingMode = OperatingMode(desc="Operating mode for the converter.")

    # The maximum voltage on the DC side at which the converter should operate.
    maxU = Voltage(desc="The maximum voltage on the DC side at which the converter should operate.")

    # Frequency on the AC side.
    frequency = Frequency(desc="Frequency on the AC side.")

    #--------------------------------------------------------------------------
    #  Begin "RectifierInverter" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "ratedU", "maxP", "minP", "commutatingResistance", "bridges", "compoundResistance", "minCompoundVoltage", "commutatingReactance", "minU", "operatingMode", "maxU", "frequency",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Wires.RectifierInverter",
        title="RectifierInverter",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RectifierInverter" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RegulationSchedule" class:
#------------------------------------------------------------------------------

class RegulationSchedule(SeasonDayTypeSchedule):
    """ A pre-established pattern over time for a controlled variable, e.g., busbar voltage.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Regulating controls that have this Schedule.
    RegulatingControl = Instance("CIM.IEC61970.Wires.RegulatingControl",
        desc="Regulating controls that have this Schedule.",
        transient=True,
        opposite="RegulationSchedule",
        editor=InstanceEditor(name="_regulatingcontrols"))

    def _get_regulatingcontrols(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.RegulatingControl" ]
        else:
            return []

    _regulatingcontrols = Property(fget=_get_regulatingcontrols)

    # A VoltageControlZone may have a  voltage regulation schedule.
    VoltageControlZones = List(Instance("CIM.IEC61970.Wires.VoltageControlZone"),
        desc="A VoltageControlZone may have a  voltage regulation schedule.")

    # Flag to indicate that line drop compensation is to be applied
    lineDropCompensation = Bool(desc="Flag to indicate that line drop compensation is to be applied")

    # Line drop reactance.
    lineDropX = Reactance(desc="Line drop reactance.")

    # Line drop resistance.
    lineDropR = Resistance(desc="Line drop resistance.")

    #--------------------------------------------------------------------------
    #  Begin "RegulationSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "value2Multiplier", "value1Unit", "value2Unit", "value1Multiplier", "startTime", "timeStep", "endTime", "lineDropCompensation", "lineDropX", "lineDropR",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "TimePoints", "DayType", "Season", "RegulatingControl", "VoltageControlZones",
                label="References"),
            dock="tab"),
        id="CIM.IEC61970.Wires.RegulationSchedule",
        title="RegulationSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegulationSchedule" user definitions:
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
    ratingCurrent = CurrentFlow(desc="Fault interrupting current rating.")

    #--------------------------------------------------------------------------
    #  Begin "Fuse" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "switchOnCount", "normalOpen", "retained", "switchOnDate", "ratingCurrent",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "LoadMgmtFunctions", "CompositeSwitch", "SwitchSchedules", "ConnectDisconnectFunctions", "SwitchingOperations",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Wires.Fuse",
        title="Fuse",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Fuse" user definitions:
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

    # A PhaseTapChanger can have an associated PhaseVariationCurve to define phase shift variations with tap step changes.
    PhaseVariationCurve = Instance("CIM.IEC61970.Wires.PhaseVariationCurve",
        desc="A PhaseTapChanger can have an associated PhaseVariationCurve to define phase shift variations with tap step changes.",
        transient=True,
        opposite="PhaseTapChanger",
        editor=InstanceEditor(name="_phasevariationcurves"))

    def _get_phasevariationcurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.PhaseVariationCurve" ]
        else:
            return []

    _phasevariationcurves = Property(fget=_get_phasevariationcurves)

    # Transformer winding to which this phase tap changer belongs.
    Winding = Instance("CIM.IEC61968.WiresExt.DistributionTransformerWinding",
        desc="Transformer winding to which this phase tap changer belongs.",
        transient=True,
        opposite="PhaseTapChanger",
        editor=InstanceEditor(name="_distributiontransformerwindings"))

    def _get_distributiontransformerwindings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.WiresExt.DistributionTransformerWinding" ]
        else:
            return []

    _distributiontransformerwindings = Property(fget=_get_distributiontransformerwindings)

    # The transformer winding to which the phase tap changer belongs.
    TransformerWinding = Instance("CIM.IEC61970.Wires.TransformerWinding",
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
                    "CIM.IEC61970.Wires.TransformerWinding" ]
        else:
            return []

    _transformerwindings = Property(fget=_get_transformerwindings)

    # The type of phase shifter construction.
    phaseTapChangerType = PhaseTapChangerKind(desc="The type of phase shifter construction.")

    # The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees.
    windingConnectionAngle = AngleDegrees(desc="The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees.")

    # Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accureatly computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available.
    stepPhaseShiftIncrement = AngleDegrees(desc="Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accureatly computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available.")

    # The reactance at the maximum tap step.
    xStepMax = Reactance(desc="The reactance at the maximum tap step.")

    # The reactance at the minimum tap step.
    xStepMin = Reactance(desc="The reactance at the minimum tap step.")

    # The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding.
    voltageStepIncrementOutOfPhase = Voltage(desc="The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding.")

    # Similar to TapChanger.nominalVoltage, but this is the nominal voltage in the out of phase winding at the nominal tap step. A typical case may have zero voltage at the nominal step, indicating no phase shift at the nominal voltage.
    nominalVoltageOutOfPhase = Voltage(desc="Similar to TapChanger.nominalVoltage, but this is the nominal voltage in the out of phase winding at the nominal tap step. A typical case may have zero voltage at the nominal step, indicating no phase shift at the nominal voltage.")

    #--------------------------------------------------------------------------
    #  Begin "PhaseTapChanger" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "neutralStep", "subsequentDelay", "neutralU", "stepVoltageIncrement", "lowStep", "normalStep", "regulationStatus", "highStep", "initialDelay", "ltcFlag", "phaseTapChangerType", "windingConnectionAngle", "stepPhaseShiftIncrement", "xStepMax", "xStepMin", "voltageStepIncrementOutOfPhase", "nominalVoltageOutOfPhase",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "RegulatingControl", "ImpedanceVariationCurve", "SvTapStep", "TapSchedules", "PhaseVariationCurve", "Winding", "TransformerWinding",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Wires.PhaseTapChanger",
        title="PhaseTapChanger",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PhaseTapChanger" user definitions:
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

    # A breaker may have zero or more automatic reclosures after a trip occurs.
    RecloseSequences = List(Instance("CIM.IEC61970.Protection.RecloseSequence"),
        desc="A breaker may have zero or more automatic reclosures after a trip occurs.")

    #--------------------------------------------------------------------------
    #  Begin "ProtectedSwitch" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "switchOnCount", "normalOpen", "retained", "switchOnDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "LoadMgmtFunctions", "CompositeSwitch", "SwitchSchedules", "ConnectDisconnectFunctions", "SwitchingOperations", "RecloseSequences",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Wires.ProtectedSwitch",
        title="ProtectedSwitch",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ProtectedSwitch" user definitions:
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
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "switchOnCount", "normalOpen", "retained", "switchOnDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "LoadMgmtFunctions", "CompositeSwitch", "SwitchSchedules", "ConnectDisconnectFunctions", "SwitchingOperations",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Wires.Disconnector",
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
    inTransitTime = Seconds(desc="The transition time from open to close.")

    # Fault interrupting current rating.
    ratedCurrent = CurrentFlow(desc="Fault interrupting current rating.")

    #--------------------------------------------------------------------------
    #  Begin "Breaker" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "switchOnCount", "normalOpen", "retained", "switchOnDate", "inTransitTime", "ratedCurrent",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "LoadMgmtFunctions", "CompositeSwitch", "SwitchSchedules", "ConnectDisconnectFunctions", "SwitchingOperations", "RecloseSequences",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Wires.Breaker",
        title="Breaker",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Breaker" user definitions:
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
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "switchOnCount", "normalOpen", "retained", "switchOnDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "LoadMgmtFunctions", "CompositeSwitch", "SwitchSchedules", "ConnectDisconnectFunctions", "SwitchingOperations",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Wires.Jumper",
        title="Jumper",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Jumper" user definitions:
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

    # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line.
    bch = Susceptance(desc="Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line.")

    # Positive sequence series resistance of the entire line section.
    r = Resistance(desc="Positive sequence series resistance of the entire line section.")

    # Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
    gch = Conductance(desc="Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.")

    # Zero sequence series resistance of the entire line section.
    r0 = Resistance(desc="Zero sequence series resistance of the entire line section.")

    # Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
    b0ch = Susceptance(desc="Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.")

    # Zero sequence series reactance of the entire line section.
    x0 = Reactance(desc="Zero sequence series reactance of the entire line section.")

    # Positive sequence series reactance of the entire line section.
    x = Reactance(desc="Positive sequence series reactance of the entire line section.")

    # Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.
    g0ch = Conductance(desc="Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.")

    #--------------------------------------------------------------------------
    #  Begin "ACLineSegment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "length", "bch", "r", "gch", "r0", "b0ch", "x0", "x", "g0ch",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Wires.ACLineSegment",
        title="ACLineSegment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ACLineSegment" user definitions:
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
    VoltageControlZone = Instance("CIM.IEC61970.Wires.VoltageControlZone",
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
                    "CIM.IEC61970.Wires.VoltageControlZone" ]
        else:
            return []

    _voltagecontrolzones = Property(fget=_get_voltagecontrolzones)

    #--------------------------------------------------------------------------
    #  Begin "BusbarSection" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "VoltageControlZone",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Wires.BusbarSection",
        title="BusbarSection",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BusbarSection" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ShuntCompensator" class:
#------------------------------------------------------------------------------

class ShuntCompensator(RegulatingCondEq):
    """ A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The state for the number of shunt compensator sections in service.
    SvShuntCompensatorSections = Instance("CIM.IEC61970.StateVariables.SvShuntCompensatorSections",
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
                    "CIM.IEC61970.StateVariables.SvShuntCompensatorSections" ]
        else:
            return []

    _svshuntcompensatorsectionss = Property(fget=_get_svshuntcompensatorsectionss)

    # Zero sequence shunt (charging) susceptance per section
    b0PerSection = Susceptance(desc="Zero sequence shunt (charging) susceptance per section")

    # For a capacitor bank, the maximum number of sections that may be switched in.
    maximumSections = Int(desc="For a capacitor bank, the maximum number of sections that may be switched in.")

    # For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).
    normalSections = Int(desc="For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).")

    # Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive.
    nomQ = ReactivePower(desc="Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive.")

    # The switch on count since the capacitor count was last reset or initialized.
    switchOnCount = Int(desc="The switch on count since the capacitor count was last reset or initialized.")

    # The maximum voltage at which the capacitor bank should operate.
    maxU = Voltage(desc="The maximum voltage at which the capacitor bank should operate.")

    # For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.
    reactivePerSection = ReactivePower(desc="For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.")

    # Time delay required for the device to be connected or disconnected by automatic voltage regulation (AVR).
    aVRDelay = Seconds(desc="Time delay required for the device to be connected or disconnected by automatic voltage regulation (AVR).")

    # Positive sequence shunt (charging) susceptance per section
    bPerSection = Susceptance(desc="Positive sequence shunt (charging) susceptance per section")

    # Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive power.
    voltageSensitivity = VoltagePerReactivePower(desc="Voltage sensitivity required for the device to regulate the bus voltage, in voltage/reactive power.")

    # The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.
    nomU = Voltage(desc="The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.")

    # Positive sequence shunt (charging) conductance per section
    gPerSection = Conductance(desc="Positive sequence shunt (charging) conductance per section")

    # The minimum voltage at which the capacitor bank should operate.
    minU = Voltage(desc="The minimum voltage at which the capacitor bank should operate.")

    # The date and time when the capacitor bank was last switched on.
    switchOnDate = Date(desc="The date and time when the capacitor bank was last switched on.")

    # Zero sequence shunt (charging) conductance per section
    g0PerSection = Conductance(desc="Zero sequence shunt (charging) conductance per section")

    #--------------------------------------------------------------------------
    #  Begin "ShuntCompensator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "b0PerSection", "maximumSections", "normalSections", "nomQ", "switchOnCount", "maxU", "reactivePerSection", "aVRDelay", "bPerSection", "voltageSensitivity", "nomU", "gPerSection", "minU", "switchOnDate", "g0PerSection",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "RegulatingControl", "Controls", "SvShuntCompensatorSections",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Wires.ShuntCompensator",
        title="ShuntCompensator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ShuntCompensator" user definitions:
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

    # All available Reactive capability curves for this SynchronousMachine.
    ReactiveCapabilityCurves = List(Instance("CIM.IEC61970.Wires.ReactiveCapabilityCurve"),
        desc="All available Reactive capability curves for this SynchronousMachine.")

    # The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
    HydroPump = Instance("CIM.IEC61970.Generation.Production.HydroPump",
        desc="The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.",
        transient=True,
        opposite="SynchronousMachine",
        editor=InstanceEditor(name="_hydropumps"))

    def _get_hydropumps(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.HydroPump" ]
        else:
            return []

    _hydropumps = Property(fget=_get_hydropumps)

    # Prime movers that drive this SynchronousMachine.
    PrimeMovers = List(Instance("CIM.IEC61970.Generation.GenerationDynamics.PrimeMover"),
        desc="Prime movers that drive this SynchronousMachine.")

    # A synchronous machine may operate as a generator and as such becomes a member of a generating unit
    GeneratingUnit = Instance("CIM.IEC61970.Generation.Production.GeneratingUnit",
        desc="A synchronous machine may operate as a generator and as such becomes a member of a generating unit",
        transient=True,
        opposite="SynchronousMachines",
        editor=InstanceEditor(name="_generatingunits"))

    def _get_generatingunits(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Generation.Production.GeneratingUnit" ]
        else:
            return []

    _generatingunits = Property(fget=_get_generatingunits)

    # The default ReactiveCapabilityCurve for use by a SynchronousMachine
    InitialReactiveCapabilityCurve = Instance("CIM.IEC61970.Wires.ReactiveCapabilityCurve",
        desc="The default ReactiveCapabilityCurve for use by a SynchronousMachine",
        transient=True,
        opposite="InitiallyUsedBySynchronousMachines",
        editor=InstanceEditor(name="_reactivecapabilitycurves"))

    def _get_reactivecapabilitycurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.ReactiveCapabilityCurve" ]
        else:
            return []

    _reactivecapabilitycurves = Property(fget=_get_reactivecapabilitycurves)

    # Modes that this synchronous machine can operate in.
    type = SynchronousMachineType(desc="Modes that this synchronous machine can operate in.")

    # Method of cooling the machine.
    coolantType = CoolantType(desc="Method of cooling the machine.")

    # Current mode of operation.
    operatingMode = SynchronousMachineOperatingMode(desc="Current mode of operation.")

    # Negative sequence reactance.
    x2 = Reactance(desc="Negative sequence reactance.")

    # Zero sequence reactance of the synchronous machine.
    x0 = Reactance(desc="Zero sequence reactance of the synchronous machine.")

    # Percent of the coordinated reactive control that comes from this machine.
    qPercent = PerCent(desc="Percent of the coordinated reactive control that comes from this machine.")

    # Damping torque coefficient, a proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.
    damping = Damping(desc="Damping torque coefficient, a proportionality constant that, when multiplied by the angular velocity of the rotor poles with respect to the magnetic field (frequency), results in the damping torque.")

    # Time delay required when switching from Manual to Automatic Voltage Regulation. This value is used in the accelerating power reference frame for powerflow solutions
    manualToAVR = Seconds(desc="Time delay required when switching from Manual to Automatic Voltage Regulation. This value is used in the accelerating power reference frame for powerflow solutions")

    # Positive sequence reactance of the synchronous machine.
    x = Reactance(desc="Positive sequence reactance of the synchronous machine.")

    # Minimum reactive power limit for the unit.
    minQ = ReactivePower(desc="Minimum reactive power limit for the unit.")

    # Quadrature-axis synchronous reactance (Xq) , the ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency.
    xQuadSync = Reactance(desc="Quadrature-axis synchronous reactance (Xq) , the ratio of the component of reactive armature voltage, due to the quadrature-axis component of armature current, to this component of current, under steady state conditions and at rated frequency.")

    # Quadrature-axis subtransient reactance, also known as X'q.
    xQuadSubtrans = Reactance(desc="Quadrature-axis subtransient reactance, also known as X'q.")

    # Negative sequence resistance.
    r2 = Resistance(desc="Negative sequence resistance.")

    # The energy stored in the rotor when operating at rated speed. This value is used in the accelerating power reference frame for  operator training simulator solutions.
    inertia = PU(desc="The energy stored in the rotor when operating at rated speed. This value is used in the accelerating power reference frame for  operator training simulator solutions.")

    # Positive sequence resistance of the synchronous machine.
    r = Resistance(desc="Positive sequence resistance of the synchronous machine.")

    # Direct-axis synchronous reactance. The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed. (Xd)
    xDirectSync = Reactance(desc="Direct-axis synchronous reactance. The quotient of a sustained value of that AC component of armature voltage that is produced by the total direct-axis flux due to direct-axis armature current and the value of the AC component of this current, the machine running at rated speed. (Xd)")

    # Quadrature-axis transient reactance, also known as X'q.
    xQuadTrans = Reactance(desc="Quadrature-axis transient reactance, also known as X'q.")

    # Direct-axis transient reactance, also known as X'd.
    xDirectTrans = Reactance(desc="Direct-axis transient reactance, also known as X'd.")

    # Priority of unit for reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on.
    referencePriority = Int(desc="Priority of unit for reference bus selection. 0 = don t care (default) 1 = highest priority. 2 is less than 1 and so on.")

    # Zero sequence resistance of the synchronous machine.
    r0 = Resistance(desc="Zero sequence resistance of the synchronous machine.")

    # Minimum voltage  limit for the unit.
    minU = Voltage(desc="Minimum voltage  limit for the unit.")

    # Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
    maxQ = ReactivePower(desc="Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.")

    # Active power consumed when in condenser mode operation.
    condenserP = ActivePower(desc="Active power consumed when in condenser mode operation.")

    # Default base reactive power value. This value represents the initial reactive power that can be used by any application function.
    baseQ = ReactivePower(desc="Default base reactive power value. This value represents the initial reactive power that can be used by any application function.")

    # Direct-axis subtransient reactance, also known as X'd.
    xDirectSubtrans = Reactance(desc="Direct-axis subtransient reactance, also known as X'd.")

    # Nameplate apparent power rating for the unit
    ratedS = ApparentPower(desc="Nameplate apparent power rating for the unit")

    # Maximum voltage limit for the unit.
    maxU = Voltage(desc="Maximum voltage limit for the unit.")

    # Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a leading MVAr violation.
    aVRToManualLead = Seconds(desc="Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a leading MVAr violation.")

    # Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a lagging MVAr violation.
    aVRToManualLag = Seconds(desc="Time delay required when switching from Automatic Voltage Regulation (AVR) to Manual for a lagging MVAr violation.")

    # Temperature or pressure of coolant medium
    coolantCondition = Float(desc="Temperature or pressure of coolant medium")

    #--------------------------------------------------------------------------
    #  Begin "SynchronousMachine" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "type", "coolantType", "operatingMode", "x2", "x0", "qPercent", "damping", "manualToAVR", "x", "minQ", "xQuadSync", "xQuadSubtrans", "r2", "inertia", "r", "xDirectSync", "xQuadTrans", "xDirectTrans", "referencePriority", "r0", "minU", "maxQ", "condenserP", "baseQ", "xDirectSubtrans", "ratedS", "maxU", "aVRToManualLead", "aVRToManualLag", "coolantCondition",
                label="Attributes", columns=3),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "RegulatingControl", "Controls", "ReactiveCapabilityCurves", "HydroPump", "PrimeMovers", "GeneratingUnit", "InitialReactiveCapabilityCurve",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Wires.SynchronousMachine",
        title="SynchronousMachine",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SynchronousMachine" user definitions:
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

    # The minimum voltage on the DC side at which the frequency converter should operate.
    minU = Voltage(desc="The minimum voltage on the DC side at which the frequency converter should operate.")

    # The minimum active power on the DC side at which the frequence converter should operate.
    minP = ActivePower(desc="The minimum active power on the DC side at which the frequence converter should operate.")

    # Frequency on the AC side.
    frequency = Frequency(desc="Frequency on the AC side.")

    # The maximum active power on the DC side at which the frequence converter should operate.
    maxP = ActivePower(desc="The maximum active power on the DC side at which the frequence converter should operate.")

    # Operating mode for the frequency converter
    operatingMode = OperatingMode(desc="Operating mode for the frequency converter")

    #--------------------------------------------------------------------------
    #  Begin "FrequencyConverter" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "maxU", "minU", "minP", "frequency", "maxP", "operatingMode",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "RegulatingControl", "Controls",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Wires.FrequencyConverter",
        title="FrequencyConverter",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "FrequencyConverter" user definitions:
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
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Wires.Junction",
        title="Junction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Junction" user definitions:
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
    dcSegmentInductance = Inductance(desc="Inductance of the DC line segment.")

    # Resistance of the DC line segment.
    dcSegmentResistance = Resistance(desc="Resistance of the DC line segment.")

    #--------------------------------------------------------------------------
    #  Begin "DCLineSegment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "length", "dcSegmentInductance", "dcSegmentResistance",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Wires.DCLineSegment",
        title="DCLineSegment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DCLineSegment" user definitions:
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

    # Winding to which this ratio tap changer belongs.
    Winding = Instance("CIM.IEC61968.WiresExt.DistributionTransformerWinding",
        desc="Winding to which this ratio tap changer belongs.",
        transient=True,
        opposite="RatioTapChanger",
        editor=InstanceEditor(name="_distributiontransformerwindings"))

    def _get_distributiontransformerwindings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.WiresExt.DistributionTransformerWinding" ]
        else:
            return []

    _distributiontransformerwindings = Property(fget=_get_distributiontransformerwindings)

    # A RatioTapChanger can have an associated RatioVariationCurve to define tap ratio variations with tap step changes.
    RatioVariationCurve = Instance("CIM.IEC61970.Wires.RatioVariationCurve",
        desc="A RatioTapChanger can have an associated RatioVariationCurve to define tap ratio variations with tap step changes.",
        transient=True,
        opposite="RatioTapChanger",
        editor=InstanceEditor(name="_ratiovariationcurves"))

    def _get_ratiovariationcurves(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.RatioVariationCurve" ]
        else:
            return []

    _ratiovariationcurves = Property(fget=_get_ratiovariationcurves)

    # The transformer winding to which the ratio tap changer belongs.
    TransformerWinding = Instance("CIM.IEC61970.Wires.TransformerWinding",
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
                    "CIM.IEC61970.Wires.TransformerWinding" ]
        else:
            return []

    _transformerwindings = Property(fget=_get_transformerwindings)

    # Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger.
    tculControlMode = TransformerControlMode(desc="Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger.")

    #--------------------------------------------------------------------------
    #  Begin "RatioTapChanger" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "neutralStep", "subsequentDelay", "neutralU", "stepVoltageIncrement", "lowStep", "normalStep", "regulationStatus", "highStep", "initialDelay", "ltcFlag", "tculControlMode",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "RegulatingControl", "ImpedanceVariationCurve", "SvTapStep", "TapSchedules", "Winding", "RatioVariationCurve", "TransformerWinding",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61970.Wires.RatioTapChanger",
        title="RatioTapChanger",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RatioTapChanger" user definitions:
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

    # Maximum available capacitive reactive power
    capacitiveRating = Reactance(desc="Maximum available capacitive reactive power")

    # The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint.
    slope = VoltagePerReactivePower(desc="The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint.")

    # The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero.
    voltageSetPoint = Voltage(desc="The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero.")

    # Maximum available inductive reactive power
    inductiveRating = Reactance(desc="Maximum available inductive reactive power")

    #--------------------------------------------------------------------------
    #  Begin "StaticVarCompensator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "sVCControlMode", "capacitiveRating", "slope", "voltageSetPoint", "inductiveRating",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "RegulatingControl", "Controls",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Wires.StaticVarCompensator",
        title="StaticVarCompensator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StaticVarCompensator" user definitions:
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
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "switchOnCount", "normalOpen", "retained", "switchOnDate", "ratedCurrent",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "LoadMgmtFunctions", "CompositeSwitch", "SwitchSchedules", "ConnectDisconnectFunctions", "SwitchingOperations", "RecloseSequences",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Wires.LoadBreakSwitch",
        title="LoadBreakSwitch",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadBreakSwitch" user definitions:
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
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "normaIlyInService", "phases", "switchOnCount", "normalOpen", "retained", "switchOnDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ChangeItems", "AssetRoles", "GeoLocation", "SafetyDocuments", "OutageSchedule", "Measurements", "ErpOrganisationRoles", "PSRType", "PsrLists", "PSREvent", "OperatingShare", "ScheduleSteps", "DocumentRoles", "ReportingGroup", "CircuitSections", "NetworkDataSets", "ContingencyEquipment", "CustomerAgreements", "OperationalLimitSet", "EquipmentContainer", "Terminals", "ClearanceTags", "OutageStepRoles", "BaseVoltage", "ElectricalAssets", "SvStatus", "ProtectionEquipments", "LoadMgmtFunctions", "CompositeSwitch", "SwitchSchedules", "ConnectDisconnectFunctions", "SwitchingOperations",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61970.Wires.GroundDisconnector",
        title="GroundDisconnector",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GroundDisconnector" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
