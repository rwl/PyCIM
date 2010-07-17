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

from CPSM.IEC61970.Core import Equipment
from CPSM.IEC61970.Core import ConductingEquipment
from CPSM.IEC61970.Core import PowerSystemResource
from CPSM.IEC61970.Core import RegularIntervalSchedule
from CPSM.IEC61970.Core import Curve
from CPSM.IEC61970.Core import EquipmentContainer
from CPSM.IEC61970.Domain import ReactivePower
from CPSM.IEC61970.Domain import Voltage
from CPSM.IEC61970.Domain import CurrentFlow
from CPSM.IEC61970.Domain import PerCent
from CPSM.IEC61970.Domain import ActivePower
from CPSM.IEC61970.Domain import ApparentPower
from CPSM.IEC61970.Domain import Reactance
from CPSM.IEC61970.Domain import Resistance
from CPSM.IEC61970.Domain import Susceptance
from CPSM.IEC61970.Domain import AngleDegrees
from CPSM.IEC61970.Domain import VoltagePerReactivePower



from enthought.traits.api import Instance, List, Property, Enum, Int, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


SynchronousMachineOperatingMode = Enum("generator", "condenser")

TapChangerKind = Enum("voltageAndPhaseControl", "phaseControl", "fixed", "voltageControl")

SVCControlMode = Enum("voltage", "off", "reactivePower")

WindingType = Enum("primary", "tertiary", "secondary", "quaternary")

SynchronousMachineType = Enum("generator", "generator_or_condenser", "condenser")

TransformerControlMode = Enum("local", "active", "volt", "off", "reactive")

#------------------------------------------------------------------------------
#  "PowerTransformer" class:
#------------------------------------------------------------------------------

class PowerTransformer(Equipment):
    """ An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).An electrical device consisting of  two or more coupled windings, with or without a magnetic core, for introducing mutual coupling between electric circuits. Transformers can be used to control voltage and phase shift (active power flow).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A transformer has windingsA transformer has windings
    Contains_TransformerWindings = List(Instance("CPSM.IEC61970.Wires.TransformerWinding"),
        desc="A transformer has windingsA transformer has windings")

    #--------------------------------------------------------------------------
    #  Begin "PowerTransformer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "Contains_TransformerWindings",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.PowerTransformer",
        title="PowerTransformer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PowerTransformer" user definitions:
    #--------------------------------------------------------------------------

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
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.BusbarSection",
        title="BusbarSection",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BusbarSection" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RegulatingCondEq" class:
#------------------------------------------------------------------------------

class RegulatingCondEq(ConductingEquipment):
    """ RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.RegulatingCondEq is a type of ConductingEquipment that can regulate Measurements and have a RegulationSchedule.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # copy from ...copy from ...
    RegulatingControl = Instance("CPSM.IEC61970.Wires.RegulatingControl",
        desc="copy from ...copy from ...",
        transient=True,
        opposite="RegulatingCondEq",
        editor=InstanceEditor(name="_regulatingcontrols"))

    def _get_regulatingcontrols(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Wires.RegulatingControl" ]
        else:
            return []

    _regulatingcontrols = Property(fget=_get_regulatingcontrols)

    #--------------------------------------------------------------------------
    #  Begin "RegulatingCondEq" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals", "RegulatingControl",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.RegulatingCondEq",
        title="RegulatingCondEq",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegulatingCondEq" user definitions:
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
    LoadResponse = Instance("CPSM.IEC61970.LoadModel.LoadResponseCharacteristic",
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
                    "CPSM.IEC61970.LoadModel.LoadResponseCharacteristic" ]
        else:
            return []

    _loadresponsecharacteristics = Property(fget=_get_loadresponsecharacteristics)

    # Fixed reactive power as per cent of load group fixed reactive power.Fixed reactive power as per cent of load group fixed reactive power.
    qfixedPct = PerCent(desc="Fixed reactive power as per cent of load group fixed reactive power.Fixed reactive power as per cent of load group fixed reactive power.")

    # Active power of the load that is a fixed quantity.Active power of the load that is a fixed quantity.
    pfixed = ActivePower(desc="Active power of the load that is a fixed quantity.Active power of the load that is a fixed quantity.")

    # Reactive power of the load that is a fixed quantity.Reactive power of the load that is a fixed quantity.
    qfixed = ReactivePower(desc="Reactive power of the load that is a fixed quantity.Reactive power of the load that is a fixed quantity.")

    # Fixed active power as per cent of load group fixed active powerFixed active power as per cent of load group fixed active power
    pfixedPct = PerCent(desc="Fixed active power as per cent of load group fixed active powerFixed active power as per cent of load group fixed active power")

    #--------------------------------------------------------------------------
    #  Begin "EnergyConsumer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "qfixedPct", "pfixed", "qfixed", "pfixedPct",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals", "LoadResponse",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.EnergyConsumer",
        title="EnergyConsumer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EnergyConsumer" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TransformerWinding" class:
#------------------------------------------------------------------------------

class TransformerWinding(ConductingEquipment):
    """ A winding is associated with each defined terminal of a transformer (or phase shifter).A winding is associated with each defined terminal of a transformer (or phase shifter).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A transformer winding may have tap changers, separately for voltage and phase angle.  If a TransformerWinding does not have an associated TapChanger, the winding is assumed to be fixed tap.A transformer winding may have tap changers, separately for voltage and phase angle.  If a TransformerWinding does not have an associated TapChanger, the winding is assumed to be fixed tap.
    TapChangers = List(Instance("CPSM.IEC61970.Wires.TapChanger"),
        desc="A transformer winding may have tap changers, separately for voltage and phase angle.  If a TransformerWinding does not have an associated TapChanger, the winding is assumed to be fixed tap.A transformer winding may have tap changers, separately for voltage and phase angle.  If a TransformerWinding does not have an associated TapChanger, the winding is assumed to be fixed tap.")

    # A transformer has windingsA transformer has windings
    MemberOf_PowerTransformer = Instance("CPSM.IEC61970.Wires.PowerTransformer", allow_none=False,
        desc="A transformer has windingsA transformer has windings",
        transient=True,
        opposite="Contains_TransformerWindings",
        editor=InstanceEditor(name="_powertransformers"))

    def _get_powertransformers(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Wires.PowerTransformer" ]
        else:
            return []

    _powertransformers = Property(fget=_get_powertransformers)

    # The type of winding.The type of winding.
    windingType = WindingType(desc="The type of winding.The type of winding.")

    # The normal apparent power rating for the windingThe normal apparent power rating for the winding
    ratedS = ApparentPower(desc="The normal apparent power rating for the windingThe normal apparent power rating for the winding")

    # Positive sequence series reactance of the winding.Positive sequence series reactance of the winding.
    x = Reactance(desc="Positive sequence series reactance of the winding.Positive sequence series reactance of the winding.")

    # The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.
    ratedU = Voltage(desc="The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.")

    # Positive sequence series resistance of the winding.Positive sequence series resistance of the winding.
    r = Resistance(desc="Positive sequence series resistance of the winding.Positive sequence series resistance of the winding.")

    # Magnetizing branch susceptance (B mag).Magnetizing branch susceptance (B mag).
    b = Susceptance(desc="Magnetizing branch susceptance (B mag).Magnetizing branch susceptance (B mag).")

    #--------------------------------------------------------------------------
    #  Begin "TransformerWinding" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "windingType", "ratedS", "x", "ratedU", "r", "b",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals", "TapChangers", "MemberOf_PowerTransformer",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.TransformerWinding",
        title="TransformerWinding",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TransformerWinding" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RegulatingControl" class:
#------------------------------------------------------------------------------

class RegulatingControl(PowerSystemResource):
    """ Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The terminal associated with this regulating control.The terminal associated with this regulating control.
    Terminal = Instance("CPSM.IEC61970.Core.Terminal", allow_none=False,
        desc="The terminal associated with this regulating control.The terminal associated with this regulating control.",
        transient=True,
        opposite="RegulatingControl",
        editor=InstanceEditor(name="_terminals"))

    def _get_terminals(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    # Schedule for this Regulating regulating control.Schedule for this Regulating regulating control.
    RegulationSchedule = Instance("CPSM.IEC61970.Wires.RegulationSchedule", allow_none=False,
        desc="Schedule for this Regulating regulating control.Schedule for this Regulating regulating control.",
        transient=True,
        opposite="RegulatingControl",
        editor=InstanceEditor(name="_regulationschedules"))

    def _get_regulationschedules(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Wires.RegulationSchedule" ]
        else:
            return []

    _regulationschedules = Property(fget=_get_regulationschedules)

    # copy from reg conduting eqcopy from reg conduting eq
    TapChanger = List(Instance("CPSM.IEC61970.Wires.TapChanger"),
        desc="copy from reg conduting eqcopy from reg conduting eq")

    # copy from reg cond eqcopy from reg cond eq
    RegulatingCondEq = List(Instance("CPSM.IEC61970.Wires.RegulatingCondEq"),
        desc="copy from reg cond eqcopy from reg cond eq")

    #--------------------------------------------------------------------------
    #  Begin "RegulatingControl" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "Terminal", "RegulationSchedule", "TapChanger", "RegulatingCondEq",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.RegulatingControl",
        title="RegulatingControl",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegulatingControl" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RegulationSchedule" class:
#------------------------------------------------------------------------------

class RegulationSchedule(RegularIntervalSchedule):
    """ A pre-established pattern over time for a controlled variable, e.g., busbar voltage.A pre-established pattern over time for a controlled variable, e.g., busbar voltage.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Regulating controls that have this Schedule.Regulating controls that have this Schedule.
    RegulatingControl = List(Instance("CPSM.IEC61970.Wires.RegulatingControl"),
        desc="Regulating controls that have this Schedule.Regulating controls that have this Schedule.")

    #--------------------------------------------------------------------------
    #  Begin "RegulationSchedule" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "startTime", "value1Unit", "value2Unit", "endTime", "timeStep",
                label="Attributes"),
            VGroup("Model", "TimePoints", "RegulatingControl",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.RegulationSchedule",
        title="RegulationSchedule",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegulationSchedule" user definitions:
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
            VGroup("UUID", "pathName", "description", "aliasName", "name", "normalOpen",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.Switch",
        title="Switch",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Switch" user definitions:
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

    # Positive sequence series resistance of the entire line section.Positive sequence series resistance of the entire line section.
    r = Resistance(desc="Positive sequence series resistance of the entire line section.Positive sequence series resistance of the entire line section.")

    # Positive sequence series reactance of the entire line section.Positive sequence series reactance of the entire line section.
    x = Reactance(desc="Positive sequence series reactance of the entire line section.Positive sequence series reactance of the entire line section.")

    # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
    bch = Susceptance(desc="Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.")

    #--------------------------------------------------------------------------
    #  Begin "Conductor" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "r", "x", "bch",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.Conductor",
        title="Conductor",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Conductor" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ReactiveCapabilityCurve" class:
#------------------------------------------------------------------------------

class ReactiveCapabilityCurve(Curve):
    """ Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Synchronous machines using this curve as default.Synchronous machines using this curve as default.
    InitiallyUsedBySynchronousMachine = List(Instance("CPSM.IEC61970.Wires.SynchronousMachine"),
        desc="Synchronous machines using this curve as default.Synchronous machines using this curve as default.")

    #--------------------------------------------------------------------------
    #  Begin "ReactiveCapabilityCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "y2Unit", "xUnit", "curveStyle", "y1Unit",
                label="Attributes"),
            VGroup("Model", "CurveScheduleDatas", "InitiallyUsedBySynchronousMachine",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.ReactiveCapabilityCurve",
        title="ReactiveCapabilityCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ReactiveCapabilityCurve" user definitions:
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

    RegulatingControl = Instance("CPSM.IEC61970.Wires.RegulatingControl", allow_none=False,
        transient=True,
        opposite="TapChanger",
        editor=InstanceEditor(name="_regulatingcontrols"))

    def _get_regulatingcontrols(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Wires.RegulatingControl" ]
        else:
            return []

    _regulatingcontrols = Property(fget=_get_regulatingcontrols)

    # A transformer winding may have tap changers, separately for voltage and phase angleA transformer winding may have tap changers, separately for voltage and phase angle
    TransformerWinding = Instance("CPSM.IEC61970.Wires.TransformerWinding", allow_none=False,
        desc="A transformer winding may have tap changers, separately for voltage and phase angleA transformer winding may have tap changers, separately for voltage and phase angle",
        transient=True,
        opposite="TapChangers",
        editor=InstanceEditor(name="_transformerwindings"))

    def _get_transformerwindings(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Wires.TransformerWinding" ]
        else:
            return []

    _transformerwindings = Property(fget=_get_transformerwindings)

    # The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.
    normalStep = Int(desc="The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting.")

    # Highest possible tap step position, advance from neutralHighest possible tap step position, advance from neutral
    highStep = Int(desc="Highest possible tap step position, advance from neutralHighest possible tap step position, advance from neutral")

    # Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer).Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer).
    stepPhaseShiftIncrement = AngleDegrees(desc="Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer).Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer).")

    # The neutral tap step position for this winding.The neutral tap step position for this winding.
    neutralStep = Int(desc="The neutral tap step position for this winding.The neutral tap step position for this winding.")

    # Lowest possible tap step position, retard from neutralLowest possible tap step position, retard from neutral
    lowStep = Int(desc="Lowest possible tap step position, retard from neutralLowest possible tap step position, retard from neutral")

    # For an LTC, the tap changer control mode.For an LTC, the tap changer control mode.
    tculControlMode = TransformerControlMode(desc="For an LTC, the tap changer control mode.For an LTC, the tap changer control mode.")

    # Tap step increment, in per cent of nominal voltage, per step position.Tap step increment, in per cent of nominal voltage, per step position.
    stepVoltageIncrement = PerCent(desc="Tap step increment, in per cent of nominal voltage, per step position.Tap step increment, in per cent of nominal voltage, per step position.")

    # The type of tap changer. Indicates the ability of the transformer to perform various regulation tasks. The tap changer must be also be associated wtih a RegulationControl object before any regulation is possible.The type of tap changer. Indicates the ability of the transformer to perform various regulation tasks. The tap changer must be also be associated wtih a RegulationControl object before any regulation is possible.
    type = TapChangerKind(desc="The type of tap changer. Indicates the ability of the transformer to perform various regulation tasks. The tap changer must be also be associated wtih a RegulationControl object before any regulation is possible.The type of tap changer. Indicates the ability of the transformer to perform various regulation tasks. The tap changer must be also be associated wtih a RegulationControl object before any regulation is possible.")

    # Voltage at which the winding operates at the neutral tap setting.Voltage at which the winding operates at the neutral tap setting.
    neutralU = Voltage(desc="Voltage at which the winding operates at the neutral tap setting.Voltage at which the winding operates at the neutral tap setting.")

    #--------------------------------------------------------------------------
    #  Begin "TapChanger" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "normalStep", "highStep", "stepPhaseShiftIncrement", "neutralStep", "lowStep", "tculControlMode", "stepVoltageIncrement", "type", "neutralU",
                label="Attributes", columns=1),
            VGroup("Model", "Contains_Measurements", "RegulatingControl", "TransformerWinding",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.TapChanger",
        title="TapChanger",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TapChanger" user definitions:
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
    Region = Instance("CPSM.IEC61970.Core.SubGeographicalRegion", allow_none=False,
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
                    "CPSM.IEC61970.Core.SubGeographicalRegion" ]
        else:
            return []

    _subgeographicalregions = Property(fget=_get_subgeographicalregions)

    #--------------------------------------------------------------------------
    #  Begin "Line" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "ConnectivityNodes", "Contains_Equipments", "Region",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.Line",
        title="Line",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Line" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SeriesCompensator" class:
#------------------------------------------------------------------------------

class SeriesCompensator(ConductingEquipment):
    """ A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.A Series Compensator is a series capacitor or reactor or an AC transmission line without charging susceptance.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Positive sequence resistance.Positive sequence resistance.
    r = Resistance(desc="Positive sequence resistance.Positive sequence resistance.")

    # Positive sequence reactance.Positive sequence reactance.
    x = Reactance(desc="Positive sequence reactance.Positive sequence reactance.")

    #--------------------------------------------------------------------------
    #  Begin "SeriesCompensator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "r", "x",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.SeriesCompensator",
        title="SeriesCompensator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SeriesCompensator" user definitions:
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
            VGroup("UUID", "pathName", "description", "aliasName", "name", "normalOpen",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.Disconnector",
        title="Disconnector",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Disconnector" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SynchronousMachine" class:
#------------------------------------------------------------------------------

class SynchronousMachine(RegulatingCondEq):
    """ An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The default ReactiveCapabilityCurve for use by a SynchronousMachineThe default ReactiveCapabilityCurve for use by a SynchronousMachine
    InitialReactiveCapabilityCurve = Instance("CPSM.IEC61970.Wires.ReactiveCapabilityCurve",
        desc="The default ReactiveCapabilityCurve for use by a SynchronousMachineThe default ReactiveCapabilityCurve for use by a SynchronousMachine",
        transient=True,
        opposite="InitiallyUsedBySynchronousMachine",
        editor=InstanceEditor(name="_reactivecapabilitycurves"))

    def _get_reactivecapabilitycurves(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.IEC61970.Wires.ReactiveCapabilityCurve" ]
        else:
            return []

    _reactivecapabilitycurves = Property(fget=_get_reactivecapabilitycurves)

    # A synchronous machine may operate as a generator and as such becomes a member of a generating unitA synchronous machine may operate as a generator and as such becomes a member of a generating unit
    MemberOf_GeneratingUnit = Instance("CPSM.IEC61970.Generation.Production.GeneratingUnit", allow_none=False,
        desc="A synchronous machine may operate as a generator and as such becomes a member of a generating unitA synchronous machine may operate as a generator and as such becomes a member of a generating unit",
        transient=True,
        opposite="Contains_SynchronousMachines",
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

    # Current mode of operation.Current mode of operation.
    operatingMode = SynchronousMachineOperatingMode(desc="Current mode of operation.Current mode of operation.")

    # Minimum reactive power limit for the unit.Minimum reactive power limit for the unit.
    minQ = ReactivePower(desc="Minimum reactive power limit for the unit.Minimum reactive power limit for the unit.")

    # Modes that this synchronous machine can operate in.Modes that this synchronous machine can operate in.
    type = SynchronousMachineType(desc="Modes that this synchronous machine can operate in.Modes that this synchronous machine can operate in.")

    # Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
    maxQ = ReactivePower(desc="Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.")

    #--------------------------------------------------------------------------
    #  Begin "SynchronousMachine" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "operatingMode", "minQ", "type", "maxQ",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals", "RegulatingControl", "InitialReactiveCapabilityCurve", "MemberOf_GeneratingUnit",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.SynchronousMachine",
        title="SynchronousMachine",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SynchronousMachine" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ShuntCompensator" class:
#------------------------------------------------------------------------------

class ShuntCompensator(RegulatingCondEq):
    """ A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # For a capacitor bank, the maximum number of sections that may be switched in.For a capacitor bank, the maximum number of sections that may be switched in.
    maximumSections = Int(desc="For a capacitor bank, the maximum number of sections that may be switched in.For a capacitor bank, the maximum number of sections that may be switched in.")

    # For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).
    normalSections = Int(desc="For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ).")

    # The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.
    nomU = Voltage(desc="The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network.")

    # For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.
    reactivePerSection = ReactivePower(desc="For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage.")

    #--------------------------------------------------------------------------
    #  Begin "ShuntCompensator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "maximumSections", "normalSections", "nomU", "reactivePerSection",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals", "RegulatingControl",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.ShuntCompensator",
        title="ShuntCompensator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ShuntCompensator" user definitions:
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
            VGroup("UUID", "pathName", "description", "aliasName", "name", "normalOpen", "ratedCurrent",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.LoadBreakSwitch",
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
    """ A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "ACLineSegment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "r", "x", "bch",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.ACLineSegment",
        title="ACLineSegment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ACLineSegment" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "StaticVarCompensator" class:
#------------------------------------------------------------------------------

class StaticVarCompensator(RegulatingCondEq):
    """ A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.A facility for providing variable and controllable shunt reactive power. The SVC typically consists of a stepdown transformer, filter, thyristor-controlled reactor, and thyristor-switched capacitor arms.  The SVC may operate in fixed MVar output mode or in voltage control mode.  When in voltage control mode, the output of the SVC will be proportional to the deviation of voltage at the controlled bus from the voltage setpoint.  The SVC characteristic slope defines the proportion.  If the voltage at the controlled bus is equal to the voltage setpoint, the SVC MVar output is zero.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero.The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero.
    voltageSetPoint = Voltage(desc="The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero.The reactive power output of the SVC is proportional to the difference between the voltage at the regulated bus and the voltage setpoint.  When the regulated bus voltage is equal to the voltage setpoint, the reactive power output is zero.")

    # SVC control mode.SVC control mode.
    sVCControlMode = SVCControlMode(desc="SVC control mode.SVC control mode.")

    # Maximum available capacitive reactive powerMaximum available capacitive reactive power
    capacitiveRating = Reactance(desc="Maximum available capacitive reactive powerMaximum available capacitive reactive power")

    # The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint.The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint.
    slope = VoltagePerReactivePower(desc="The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint.The characteristics slope of an SVC defines how the reactive power output changes in proportion to the difference between the regulated bus voltage and the voltage setpoint.")

    # Maximum available inductive reactive powerMaximum available inductive reactive power
    inductiveRating = Reactance(desc="Maximum available inductive reactive powerMaximum available inductive reactive power")

    #--------------------------------------------------------------------------
    #  Begin "StaticVarCompensator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "pathName", "description", "aliasName", "name", "voltageSetPoint", "sVCControlMode", "capacitiveRating", "slope", "inductiveRating",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals", "RegulatingControl",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.StaticVarCompensator",
        title="StaticVarCompensator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "StaticVarCompensator" user definitions:
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
            VGroup("UUID", "pathName", "description", "aliasName", "name", "normalOpen", "ratedCurrent",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals",
                label="References"),
            dock="tab"),
        id="CPSM.IEC61970.Wires.Breaker",
        title="Breaker",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Breaker" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
