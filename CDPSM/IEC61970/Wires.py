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

""" An extension to the Core and Topology package that models information on the electrical characteristics of Transmission and Distribution networks. This package is used by network applications such as State Estimation, Load Flow and Optimal Power Flow.An extension to the Core and Topology package that models information on the electrical characteristics of Transmission and Distribution networks. This package is used by network applications such as State Estimation, Load Flow and Optimal Power Flow.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CDPSM.IEC61970.Core import ConductingEquipment
from CDPSM.IEC61970.Core import PowerSystemResource
from CDPSM.IEC61970.Core import EquipmentContainer
from CDPSM.IEC61970.Domain import CurrentFlow
from CDPSM.IEC61970.Domain import PerCent
from CDPSM.IEC61970.Domain import Seconds
from CDPSM.IEC61970.Domain import Voltage
from CDPSM.IEC61970.Domain import Resistance
from CDPSM.IEC61970.Domain import Reactance
from CDPSM.IEC61970.Domain import Susceptance
from CDPSM.IEC61970.Domain import AngleRadians
from CDPSM.IEC61970.Domain import ReactivePower
from CDPSM.IEC61970.Domain import ActivePower
from CDPSM.IEC61970.Domain import Length



from enthought.traits.api import Instance, List, Property, Enum, Int, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


TransformerControlMode = Enum("reactive", "volt")

WindingConnection = Enum("I", "Z", "Yn", "Y", "A", "D", "Zn")

SynchronousMachineType = Enum("condenser", "generator_or_condenser", "generator")

SynchronousMachineOperatingMode = Enum("condenser", "generator")

#------------------------------------------------------------------------------
#  "BusbarSection" class:
#------------------------------------------------------------------------------

class BusbarSection(ConductingEquipment):
    """ A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "BusbarSection" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "normaIlyInService", "phases",
                label="Attributes"),
            VGroup("Model", "GeoLocation", "PSRType", "EquipmentContainer", "Terminals", "BaseVoltage",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Wires.BusbarSection",
        title="BusbarSection",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BusbarSection" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TapChanger" class:
#------------------------------------------------------------------------------

class TapChanger(PowerSystemResource):
    """ Mechanism for changing transformer winding tap positions.Mechanism for changing transformer winding tap positions.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The tap step state associated with the tap changer.The tap step state associated with the tap changer.
    SvTapStep = Instance("CDPSM.IEC61970.StateVariables.SvTapStep", allow_none=False,
        desc="The tap step state associated with the tap changer.The tap step state associated with the tap changer.",
        transient=True,
        opposite="TapChanger",
        editor=InstanceEditor(name="_svtapsteps"))

    def _get_svtapsteps(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61970.StateVariables.SvTapStep" ]
        else:
            return []

    _svtapsteps = Property(fget=_get_svtapsteps)

    # Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step.Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step.
    stepVoltageIncrement = PerCent(desc="Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step.Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step.")

    # For an LTC, the delay for subsequent tap changer operation (second and later step changes)For an LTC, the delay for subsequent tap changer operation (second and later step changes)
    subsequentDelay = Seconds(desc="For an LTC, the delay for subsequent tap changer operation (second and later step changes)For an LTC, the delay for subsequent tap changer operation (second and later step changes)")

    # The neutral tap step position for this winding.The neutral tap step position for this winding.
    neutralStep = Int(desc="The neutral tap step position for this winding.The neutral tap step position for this winding.")

    # The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.
    normalStep = Int(desc="The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.")

    # Specifies whether or not a TapChanger has load tap changing capabilities.Specifies whether or not a TapChanger has load tap changing capabilities.
    ltcFlag = Bool(desc="Specifies whether or not a TapChanger has load tap changing capabilities.Specifies whether or not a TapChanger has load tap changing capabilities.")

    # Voltage at which the winding operates at the neutral tap setting.Voltage at which the winding operates at the neutral tap setting.
    neutralU = Voltage(desc="Voltage at which the winding operates at the neutral tap setting.Voltage at which the winding operates at the neutral tap setting.")

    # Lowest possible tap step position, retard from neutralLowest possible tap step position, retard from neutral
    lowStep = Int(desc="Lowest possible tap step position, retard from neutralLowest possible tap step position, retard from neutral")

    # For an LTC, the delay for initial tap changer operation (first step change)For an LTC, the delay for initial tap changer operation (first step change)
    initialDelay = Seconds(desc="For an LTC, the delay for initial tap changer operation (first step change)For an LTC, the delay for initial tap changer operation (first step change)")

    # Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating.Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating.
    regulationStatus = Bool(desc="Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating.Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating.")

    # Highest possible tap step position, advance from neutralHighest possible tap step position, advance from neutral
    highStep = Int(desc="Highest possible tap step position, advance from neutralHighest possible tap step position, advance from neutral")

    #--------------------------------------------------------------------------
    #  Begin "TapChanger" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "stepVoltageIncrement", "subsequentDelay", "neutralStep", "normalStep", "ltcFlag", "neutralU", "lowStep", "initialDelay", "regulationStatus", "highStep",
                label="Attributes", columns=1),
            VGroup("Model", "GeoLocation", "PSRType", "SvTapStep",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Wires.TapChanger",
        title="TapChanger",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TapChanger" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Junction" class:
#------------------------------------------------------------------------------

class Junction(ConductingEquipment):
    """ A point where one or more conducting equipments are connected with zero resistance.A point where one or more conducting equipments are connected with zero resistance.
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
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "normaIlyInService", "phases",
                label="Attributes"),
            VGroup("Model", "GeoLocation", "PSRType", "EquipmentContainer", "Terminals", "BaseVoltage",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Wires.Junction",
        title="Junction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Junction" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EnergySource" class:
#------------------------------------------------------------------------------

class EnergySource(ConductingEquipment):
    """ A generic equivalent for an energy supplier on a transmission or distribution voltage level.A generic equivalent for an energy supplier on a transmission or distribution voltage level.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Positive sequence Thevenin reactance.Positive sequence Thevenin reactance.
    x = Reactance(desc="Positive sequence Thevenin reactance.Positive sequence Thevenin reactance.")

    # Phase-to-phase open circuit voltage magnitude.Phase-to-phase open circuit voltage magnitude.
    voltageMagnitude = Voltage(desc="Phase-to-phase open circuit voltage magnitude.Phase-to-phase open circuit voltage magnitude.")

    # Phase angle of a-phase open circuit.Phase angle of a-phase open circuit.
    voltageAngle = AngleRadians(desc="Phase angle of a-phase open circuit.Phase angle of a-phase open circuit.")

    # Phase-to-phase nominal voltage.Phase-to-phase nominal voltage.
    nominalVoltage = Voltage(desc="Phase-to-phase nominal voltage.Phase-to-phase nominal voltage.")

    #--------------------------------------------------------------------------
    #  Begin "EnergySource" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "normaIlyInService", "phases", "x", "voltageMagnitude", "voltageAngle", "nominalVoltage",
                label="Attributes"),
            VGroup("Model", "GeoLocation", "PSRType", "EquipmentContainer", "Terminals", "BaseVoltage",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Wires.EnergySource",
        title="EnergySource",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EnergySource" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SynchronousMachine" class:
#------------------------------------------------------------------------------

class SynchronousMachine(ConductingEquipment):
    """ An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A synchronous machine may operate as a generator and as such becomes a member of a generating unitA synchronous machine may operate as a generator and as such becomes a member of a generating unit
    GeneratingUnit = Instance("CDPSM.IEC61970.Generation.Production.GeneratingUnit", allow_none=False,
        desc="A synchronous machine may operate as a generator and as such becomes a member of a generating unitA synchronous machine may operate as a generator and as such becomes a member of a generating unit",
        transient=True,
        opposite="SynchronousMachines",
        editor=InstanceEditor(name="_generatingunits"))

    def _get_generatingunits(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61970.Generation.Production.GeneratingUnit" ]
        else:
            return []

    _generatingunits = Property(fget=_get_generatingunits)

    # Default base reactive power value. This value represents the initial reactive power that can be used by any application function.Default base reactive power value. This value represents the initial reactive power that can be used by any application function.
    baseQ = ReactivePower(desc="Default base reactive power value. This value represents the initial reactive power that can be used by any application function.Default base reactive power value. This value represents the initial reactive power that can be used by any application function.")

    # Current mode of operation.Current mode of operation.
    operatingMode = SynchronousMachineOperatingMode(desc="Current mode of operation.Current mode of operation.")

    # Modes that this synchronous machine can operate in.Modes that this synchronous machine can operate in.
    type = SynchronousMachineType(desc="Modes that this synchronous machine can operate in.Modes that this synchronous machine can operate in.")

    # Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
    maxQ = ReactivePower(desc="Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.")

    # Minimum reactive power limit for the unit.Minimum reactive power limit for the unit.
    minQ = ReactivePower(desc="Minimum reactive power limit for the unit.Minimum reactive power limit for the unit.")

    #--------------------------------------------------------------------------
    #  Begin "SynchronousMachine" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "normaIlyInService", "phases", "baseQ", "operatingMode", "type", "maxQ", "minQ",
                label="Attributes", columns=1),
            VGroup("Model", "GeoLocation", "PSRType", "EquipmentContainer", "Terminals", "BaseVoltage", "GeneratingUnit",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Wires.SynchronousMachine",
        title="SynchronousMachine",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SynchronousMachine" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EnergyConsumer" class:
#------------------------------------------------------------------------------

class EnergyConsumer(ConductingEquipment):
    """ Generic user of energy - a  point of consumption on the power system modelGeneric user of energy - a  point of consumption on the power system model
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The load response characteristic of this load.The load response characteristic of this load.
    LoadResponse = Instance("CDPSM.IEC61970.LoadModel.LoadResponseCharacteristic",
        desc="The load response characteristic of this load.The load response characteristic of this load.",
        transient=True,
        opposite="EnergyConsumer",
        editor=InstanceEditor(name="_loadresponsecharacteristics"))

    def _get_loadresponsecharacteristics(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61970.LoadModel.LoadResponseCharacteristic" ]
        else:
            return []

    _loadresponsecharacteristics = Property(fget=_get_loadresponsecharacteristics)

    # Active power of the load that is a fixed quantity.Active power of the load that is a fixed quantity.
    pfixed = ActivePower(desc="Active power of the load that is a fixed quantity.Active power of the load that is a fixed quantity.")

    # Fixed active power as per cent of load group fixed active powerFixed active power as per cent of load group fixed active power
    pfixedPct = PerCent(desc="Fixed active power as per cent of load group fixed active powerFixed active power as per cent of load group fixed active power")

    # Fixed reactive power as per cent of load group fixed reactive power.Fixed reactive power as per cent of load group fixed reactive power.
    qfixedPct = PerCent(desc="Fixed reactive power as per cent of load group fixed reactive power.Fixed reactive power as per cent of load group fixed reactive power.")

    # Reactive power of the load that is a fixed quantity.Reactive power of the load that is a fixed quantity.
    qfixed = ReactivePower(desc="Reactive power of the load that is a fixed quantity.Reactive power of the load that is a fixed quantity.")

    # Number of individual customers represented by this DemandNumber of individual customers represented by this Demand
    customerCount = Int(desc="Number of individual customers represented by this DemandNumber of individual customers represented by this Demand")

    #--------------------------------------------------------------------------
    #  Begin "EnergyConsumer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "normaIlyInService", "phases", "pfixed", "pfixedPct", "qfixedPct", "qfixed", "customerCount",
                label="Attributes", columns=1),
            VGroup("Model", "GeoLocation", "PSRType", "EquipmentContainer", "Terminals", "BaseVoltage", "LoadResponse",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Wires.EnergyConsumer",
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
    """ A generic device designed to close, or open, or both, one or more electric circuits.A generic device designed to close, or open, or both, one or more electric circuits.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.
    normalOpen = Bool(desc="The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen.")

    #--------------------------------------------------------------------------
    #  Begin "Switch" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "normaIlyInService", "phases", "normalOpen",
                label="Attributes"),
            VGroup("Model", "GeoLocation", "PSRType", "EquipmentContainer", "Terminals", "BaseVoltage",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Wires.Switch",
        title="Switch",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Switch" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Line" class:
#------------------------------------------------------------------------------

class Line(EquipmentContainer):
    """ A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A Line can be contained by a SubGeographical Region.A Line can be contained by a SubGeographical Region.
    Region = Instance("CDPSM.IEC61970.Core.SubGeographicalRegion", allow_none=False,
        desc="A Line can be contained by a SubGeographical Region.A Line can be contained by a SubGeographical Region.",
        transient=True,
        opposite="Lines",
        editor=InstanceEditor(name="_subgeographicalregions"))

    def _get_subgeographicalregions(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61970.Core.SubGeographicalRegion" ]
        else:
            return []

    _subgeographicalregions = Property(fget=_get_subgeographicalregions)

    #--------------------------------------------------------------------------
    #  Begin "Line" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName",
                label="Attributes"),
            VGroup("Model", "GeoLocation", "PSRType", "ConnectivityNodes", "Equipments", "Region",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Wires.Line",
        title="Line",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Line" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ShuntCompensator" class:
#------------------------------------------------------------------------------

class ShuntCompensator(ConductingEquipment):
    """ A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive.Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive.
    nomQ = ReactivePower(desc="Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive.Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive.")

    # The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.
    nomU = Voltage(desc="The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.")

    # For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).
    normalSections = Int(desc="For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).")

    # For a capacitor bank, the maximum number of sections that may be switched in.For a capacitor bank, the maximum number of sections that may be switched in.
    maximumSections = Int(desc="For a capacitor bank, the maximum number of sections that may be switched in.For a capacitor bank, the maximum number of sections that may be switched in.")

    # For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.
    reactivePerSection = ReactivePower(desc="For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.")

    #--------------------------------------------------------------------------
    #  Begin "ShuntCompensator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "normaIlyInService", "phases", "nomQ", "nomU", "normalSections", "maximumSections", "reactivePerSection",
                label="Attributes", columns=1),
            VGroup("Model", "GeoLocation", "PSRType", "EquipmentContainer", "Terminals", "BaseVoltage",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Wires.ShuntCompensator",
        title="ShuntCompensator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ShuntCompensator" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Conductor" class:
#------------------------------------------------------------------------------

class Conductor(ConductingEquipment):
    """ Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Segment length for calculating line section capabilitiesSegment length for calculating line section capabilities
    length = Length(desc="Segment length for calculating line section capabilitiesSegment length for calculating line section capabilities")

    #--------------------------------------------------------------------------
    #  Begin "Conductor" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "normaIlyInService", "phases", "length",
                label="Attributes"),
            VGroup("Model", "GeoLocation", "PSRType", "EquipmentContainer", "Terminals", "BaseVoltage",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Wires.Conductor",
        title="Conductor",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Conductor" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadBreakSwitch" class:
#------------------------------------------------------------------------------

class LoadBreakSwitch(Switch):
    """ A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Current carrying capacity of a wire or cable under stated thermal conditions.Current carrying capacity of a wire or cable under stated thermal conditions.
    ratedCurrent = CurrentFlow(desc="Current carrying capacity of a wire or cable under stated thermal conditions.Current carrying capacity of a wire or cable under stated thermal conditions.")

    #--------------------------------------------------------------------------
    #  Begin "LoadBreakSwitch" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "normaIlyInService", "phases", "normalOpen", "ratedCurrent",
                label="Attributes"),
            VGroup("Model", "GeoLocation", "PSRType", "EquipmentContainer", "Terminals", "BaseVoltage",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Wires.LoadBreakSwitch",
        title="LoadBreakSwitch",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadBreakSwitch" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Fuse" class:
#------------------------------------------------------------------------------

class Fuse(Switch):
    """ An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current.An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Fault interrupting current rating.Fault interrupting current rating.
    ratingCurrent = CurrentFlow(desc="Fault interrupting current rating.Fault interrupting current rating.")

    #--------------------------------------------------------------------------
    #  Begin "Fuse" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "normaIlyInService", "phases", "normalOpen", "ratingCurrent",
                label="Attributes"),
            VGroup("Model", "GeoLocation", "PSRType", "EquipmentContainer", "Terminals", "BaseVoltage",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Wires.Fuse",
        title="Fuse",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Fuse" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ACLineSegment" class:
#------------------------------------------------------------------------------

class ACLineSegment(Conductor):
    """ A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.If the instance is an ACLineSegment, the resistance and reactance is mandatory.  However, if the line segment is for a DistributionLineSegment, these are not mandatory.A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.If the instance is an ACLineSegment, the resistance and reactance is mandatory.  However, if the line segment is for a DistributionLineSegment, these are not mandatory.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Positive sequence series resistance of the entire line section.Positive sequence series resistance of the entire line section.
    r = Resistance(desc="Positive sequence series resistance of the entire line section.Positive sequence series resistance of the entire line section.")

    # Zero sequence series reactance of the entire line section.Zero sequence series reactance of the entire line section.
    x0 = Reactance(desc="Zero sequence series reactance of the entire line section.Zero sequence series reactance of the entire line section.")

    # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line.Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line.
    bch = Susceptance(desc="Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line.Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line.")

    # Positive sequence series reactance of the entire line section.Positive sequence series reactance of the entire line section.
    x = Reactance(desc="Positive sequence series reactance of the entire line section.Positive sequence series reactance of the entire line section.")

    # Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
    b0ch = Susceptance(desc="Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.")

    # Zero sequence series resistance of the entire line section.Zero sequence series resistance of the entire line section.
    r0 = Resistance(desc="Zero sequence series resistance of the entire line section.Zero sequence series resistance of the entire line section.")

    #--------------------------------------------------------------------------
    #  Begin "ACLineSegment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "normaIlyInService", "phases", "length", "r", "x0", "bch", "x", "b0ch", "r0",
                label="Attributes", columns=1),
            VGroup("Model", "GeoLocation", "PSRType", "EquipmentContainer", "Terminals", "BaseVoltage",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Wires.ACLineSegment",
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
    """ A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.
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
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "normaIlyInService", "phases", "normalOpen",
                label="Attributes"),
            VGroup("Model", "GeoLocation", "PSRType", "EquipmentContainer", "Terminals", "BaseVoltage",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Wires.Disconnector",
        title="Disconnector",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Disconnector" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RatioTapChanger" class:
#------------------------------------------------------------------------------

class RatioTapChanger(TapChanger):
    """ A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Winding to which this ratio tap changer belongs.Winding to which this ratio tap changer belongs.
    Winding = Instance("CDPSM.IEC61968.WiresExt.DistributionTransformerWinding", allow_none=False,
        desc="Winding to which this ratio tap changer belongs.Winding to which this ratio tap changer belongs.",
        transient=True,
        opposite="RatioTapChanger",
        editor=InstanceEditor(name="_distributiontransformerwindings"))

    def _get_distributiontransformerwindings(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CDPSM.IEC61968.WiresExt.DistributionTransformerWinding" ]
        else:
            return []

    _distributiontransformerwindings = Property(fget=_get_distributiontransformerwindings)

    # Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger.Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger.
    tculControlMode = TransformerControlMode(desc="Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger.Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger.")

    #--------------------------------------------------------------------------
    #  Begin "RatioTapChanger" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "stepVoltageIncrement", "subsequentDelay", "neutralStep", "normalStep", "ltcFlag", "neutralU", "lowStep", "initialDelay", "regulationStatus", "highStep", "tculControlMode",
                label="Attributes", columns=1),
            VGroup("Model", "GeoLocation", "PSRType", "SvTapStep", "Winding",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Wires.RatioTapChanger",
        title="RatioTapChanger",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RatioTapChanger" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Breaker" class:
#------------------------------------------------------------------------------

class Breaker(Switch):
    """ A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Fault interrupting current rating.Fault interrupting current rating.
    ratedCurrent = CurrentFlow(desc="Fault interrupting current rating.Fault interrupting current rating.")

    #--------------------------------------------------------------------------
    #  Begin "Breaker" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "description", "name", "localName", "aliasName", "normaIlyInService", "phases", "normalOpen", "ratedCurrent",
                label="Attributes"),
            VGroup("Model", "GeoLocation", "PSRType", "EquipmentContainer", "Terminals", "BaseVoltage",
                label="References"),
            dock="tab"),
        id="CDPSM.IEC61970.Wires.Breaker",
        title="Breaker",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Breaker" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
