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

from UCTE.Core import ConductingEquipment
from UCTE.Core import IdentifiedObject
from UCTE.Core import Curve
from UCTE.Core import Equipment
from UCTE.Core import EquipmentContainer
from UCTE.Domain import PerCent
from UCTE.Domain import Voltage
from UCTE.Domain import Reactance
from UCTE.Domain import Susceptance
from UCTE.Domain import ApparentPower
from UCTE.Domain import Resistance
from UCTE.Domain import Conductance
from UCTE.Domain import AngleDegrees
from UCTE.Domain import LongLength
from UCTE.Domain import ReactivePower



from enthought.traits.api import Instance, List, Property, Enum, Int, Bool, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


WindingType = Enum("tertiary", "primary", "secondary")

WindingConnection = Enum("Z", "Y", "D")

RegulatingControlModeKind = Enum("reactivePower", "voltage", "activePower", "currentFlow", "fixed", "admittance")

SynchronousMachineType = Enum("condenser", "generator_or_condenser", "generator")

SynchronousMachineOperatingMode = Enum("condenser", "generator")

PhaseTapChangerKind = Enum("asymmetrical", "symmetrical")

#------------------------------------------------------------------------------
#  "BusbarSection" class:
#------------------------------------------------------------------------------

class BusbarSection(ConductingEquipment):
    """ A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.Terminals of Switches can also be used for regulation.A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.Terminals of Switches can also be used for regulation.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A VoltageControlZone is controlled by a designated BusbarSection.A VoltageControlZone is controlled by a designated BusbarSection.
    VoltageControlZone = Instance("UCTE.Wires.VoltageControlZone", allow_none=False,
        desc="A VoltageControlZone is controlled by a designated BusbarSection.A VoltageControlZone is controlled by a designated BusbarSection.",
        transient=True,
        opposite="BusbarSection",
        editor=InstanceEditor(name="_voltagecontrolzones"))

    def _get_voltagecontrolzones(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Wires.VoltageControlZone" ]
        else:
            return []

    _voltagecontrolzones = Property(fget=_get_voltagecontrolzones)

    #--------------------------------------------------------------------------
    #  Begin "BusbarSection" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "equivalent",
                label="Attributes"),
            VGroup("Model", "MemberOf_EquipmentContainer", "BaseVoltage", "Terminals", "VoltageControlZone",
                label="References"),
            dock="tab"),
        id="UCTE.Wires.BusbarSection",
        title="BusbarSection",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "BusbarSection" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TapChanger" class:
#------------------------------------------------------------------------------

class TapChanger(IdentifiedObject):
    """ Mechanism for changing transformer winding tap positions.Mechanism for changing transformer winding tap positions.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The tap step state associated with the tap changer.The tap step state associated with the tap changer.
    SvTapStep = Instance("UCTE.StateVariables.SvTapStep",
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
                    "UCTE.StateVariables.SvTapStep" ]
        else:
            return []

    _svtapsteps = Property(fget=_get_svtapsteps)

    RegulatingControl = Instance("UCTE.Wires.RegulatingControl",
        transient=True,
        opposite="TapChanger",
        editor=InstanceEditor(name="_regulatingcontrols"))

    def _get_regulatingcontrols(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Wires.RegulatingControl" ]
        else:
            return []

    _regulatingcontrols = Property(fget=_get_regulatingcontrols)

    # Tap step increment, in per cent of nominal voltage, per step position. This could be supplanted by more detailed model information in either the PhaseTapChanger if modeled or in detailed per tap step table information.This is required for RatioTapChanger. It is Optional for most phase shifters since these are not used to regulate voltagesTap step increment, in per cent of nominal voltage, per step position. This could be supplanted by more detailed model information in either the PhaseTapChanger if modeled or in detailed per tap step table information.This is required for RatioTapChanger. It is Optional for most phase shifters since these are not used to regulate voltages
    stepVoltageIncrement = PerCent(desc="Tap step increment, in per cent of nominal voltage, per step position. This could be supplanted by more detailed model information in either the PhaseTapChanger if modeled or in detailed per tap step table information.This is required for RatioTapChanger. It is Optional for most phase shifters since these are not used to regulate voltagesTap step increment, in per cent of nominal voltage, per step position. This could be supplanted by more detailed model information in either the PhaseTapChanger if modeled or in detailed per tap step table information.This is required for RatioTapChanger. It is Optional for most phase shifters since these are not used to regulate voltages")

    # Voltage at which the winding operates at the neutral tap setting.Voltage at which the winding operates at the neutral tap setting.
    neutralU = Voltage(desc="Voltage at which the winding operates at the neutral tap setting.Voltage at which the winding operates at the neutral tap setting.")

    # Lowest possible tap step position, retard from neutralLowest possible tap step position, retard from neutral
    lowStep = Int(desc="Lowest possible tap step position, retard from neutralLowest possible tap step position, retard from neutral")

    # The neutral tap step position for this winding.This attribute is used to define the neutral step for a tap changer or a phase tap changer.  The neutralStep value cannot be higher than the highStep value or lower than the lowStep value. The neutral tap step position for this winding.This attribute is used to define the neutral step for a tap changer or a phase tap changer.  The neutralStep value cannot be higher than the highStep value or lower than the lowStep value. 
    neutralStep = Int(desc="The neutral tap step position for this winding.This attribute is used to define the neutral step for a tap changer or a phase tap changer.  The neutralStep value cannot be higher than the highStep value or lower than the lowStep value. The neutral tap step position for this winding.This attribute is used to define the neutral step for a tap changer or a phase tap changer.  The neutralStep value cannot be higher than the highStep value or lower than the lowStep value. ")

    # Highest possible tap step position, advance from neutralHighest possible tap step position, advance from neutral
    highStep = Int(desc="Highest possible tap step position, advance from neutralHighest possible tap step position, advance from neutral")

    #--------------------------------------------------------------------------
    #  Begin "TapChanger" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "stepVoltageIncrement", "neutralU", "lowStep", "neutralStep", "highStep",
                label="Attributes"),
            VGroup("Model", "SvTapStep", "RegulatingControl",
                label="References"),
            dock="tab"),
        id="UCTE.Wires.TapChanger",
        title="TapChanger",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TapChanger" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TransformerWinding" class:
#------------------------------------------------------------------------------

class TransformerWinding(ConductingEquipment):
    """ A winding is associated with each defined terminal of a transformer (or phase shifter).The association between the TransformerWinding class and MemberOf_EquipmentContainer is not used in this Profile since the association to Power Transformer is already there.  The only time this association should be used is if the association refers to a different substation than what is used in the PowerTransformer association.A winding is associated with each defined terminal of a transformer (or phase shifter).The association between the TransformerWinding class and MemberOf_EquipmentContainer is not used in this Profile since the association to Power Transformer is already there.  The only time this association should be used is if the association refers to a different substation than what is used in the PowerTransformer association.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A transformer has windingsA transformer has windings
    MemberOf_PowerTransformer = Instance("UCTE.Wires.PowerTransformer", allow_none=False,
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
                    "UCTE.Wires.PowerTransformer" ]
        else:
            return []

    _powertransformers = Property(fget=_get_powertransformers)

    # The ratio tap changer associated with the transformer winding.The ratio tap changer associated with the transformer winding.
    RatioTapChanger = Instance("UCTE.Wires.RatioTapChanger",
        desc="The ratio tap changer associated with the transformer winding.The ratio tap changer associated with the transformer winding.",
        transient=True,
        opposite="TransformerWinding",
        editor=InstanceEditor(name="_ratiotapchangers"))

    def _get_ratiotapchangers(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Wires.RatioTapChanger" ]
        else:
            return []

    _ratiotapchangers = Property(fget=_get_ratiotapchangers)

    # The phase tap changer associated with the transformer winding.The phase tap changer associated with the transformer winding.
    PhaseTapChanger = Instance("UCTE.Wires.PhaseTapChanger",
        desc="The phase tap changer associated with the transformer winding.The phase tap changer associated with the transformer winding.",
        transient=True,
        opposite="TransformerWinding",
        editor=InstanceEditor(name="_phasetapchangers"))

    def _get_phasetapchangers(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Wires.PhaseTapChanger" ]
        else:
            return []

    _phasetapchangers = Property(fget=_get_phasetapchangers)

    # Positive sequence series reactance of the winding.Positive sequence series reactance of the winding.
    x = Reactance(desc="Positive sequence series reactance of the winding.Positive sequence series reactance of the winding.")

    # Magnetizing branch susceptance (B mag).Magnetizing branch susceptance (B mag).
    b = Susceptance(desc="Magnetizing branch susceptance (B mag).Magnetizing branch susceptance (B mag).")

    # The type of connection of the winding.The type of connection of the winding.
    connectionType = WindingConnection(desc="The type of connection of the winding.The type of connection of the winding.")

    # The normal apparent power rating for the windingThe normal apparent power rating for the winding
    ratedS = ApparentPower(desc="The normal apparent power rating for the windingThe normal apparent power rating for the winding")

    # Zero sequence series reactance of the winding.This is for Short Circuit only.Zero sequence series reactance of the winding.This is for Short Circuit only.
    x0 = Reactance(desc="Zero sequence series reactance of the winding.This is for Short Circuit only.Zero sequence series reactance of the winding.This is for Short Circuit only.")

    # Positive sequence series resistance of the winding.Positive sequence series resistance of the winding.
    r = Resistance(desc="Positive sequence series resistance of the winding.Positive sequence series resistance of the winding.")

    # Zero sequence series resistance of the winding.This is for Short Circuit only.Zero sequence series resistance of the winding.This is for Short Circuit only.
    r0 = Resistance(desc="Zero sequence series resistance of the winding.This is for Short Circuit only.Zero sequence series resistance of the winding.This is for Short Circuit only.")

    # Zero sequence magnetizing branch susceptance.This is for Short Circuit only.Zero sequence magnetizing branch susceptance.This is for Short Circuit only.
    b0 = Susceptance(desc="Zero sequence magnetizing branch susceptance.This is for Short Circuit only.Zero sequence magnetizing branch susceptance.This is for Short Circuit only.")

    # The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.
    ratedU = Voltage(desc="The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.The rated voltage (phase-to-phase) of the winding, usually the same as the neutral voltage.")

    # Zero sequence magnetizing branch conductance.This is for Short Circuit only.Zero sequence magnetizing branch conductance.This is for Short Circuit only.
    g0 = Conductance(desc="Zero sequence magnetizing branch conductance.This is for Short Circuit only.Zero sequence magnetizing branch conductance.This is for Short Circuit only.")

    # Magnetizing branch conductance (G mag).Magnetizing branch conductance (G mag).
    g = Conductance(desc="Magnetizing branch conductance (G mag).Magnetizing branch conductance (G mag).")

    # Ground reactance path through connected grounding transformer.This is for Short Circuit only.Ground reactance path through connected grounding transformer.This is for Short Circuit only.
    xground = Reactance(desc="Ground reactance path through connected grounding transformer.This is for Short Circuit only.Ground reactance path through connected grounding transformer.This is for Short Circuit only.")

    # The type of winding.The type of winding.
    windingType = WindingType(desc="The type of winding.The type of winding.")

    # Ground resistance path through connected grounding transformer.This is for Short Circuit only.Ground resistance path through connected grounding transformer.This is for Short Circuit only.
    rground = Resistance(desc="Ground resistance path through connected grounding transformer.This is for Short Circuit only.Ground resistance path through connected grounding transformer.This is for Short Circuit only.")

    #--------------------------------------------------------------------------
    #  Begin "TransformerWinding" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "equivalent", "x", "b", "connectionType", "ratedS", "x0", "r", "r0", "b0", "ratedU", "g0", "g", "xground", "windingType", "rground",
                label="Attributes", columns=1),
            VGroup("Model", "MemberOf_EquipmentContainer", "BaseVoltage", "Terminals", "MemberOf_PowerTransformer", "RatioTapChanger", "PhaseTapChanger",
                label="References"),
            dock="tab"),
        id="UCTE.Wires.TransformerWinding",
        title="TransformerWinding",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TransformerWinding" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "RegulatingControl" class:
#------------------------------------------------------------------------------

class RegulatingControl(IdentifiedObject):
    """ Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.Regulating control scheme in which this equipment participates.Specifies a set of equipment that works together to control a power system quantity such as voltage or flow.Regulating control scheme in which this equipment participates.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The terminal associated with this regulating control.The terminal associated with this regulating control.
    Terminal = Instance("UCTE.Core.Terminal", allow_none=False,
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
                    "UCTE.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    # copy from reg cond eqcopy from reg cond eq
    RegulatingCondEq = List(Instance("UCTE.Wires.RegulatingCondEq"),
        desc="copy from reg cond eqcopy from reg cond eq")

    # copy from reg conduting eqcopy from reg conduting eq
    TapChanger = List(Instance("UCTE.Wires.TapChanger"),
        desc="copy from reg conduting eqcopy from reg conduting eq")

    # The regulating control mode presently available.  This specifications allows for determining the kind of regualation without need for obtaining the units from a schedule.The regulating control mode presently available.  This specifications allows for determining the kind of regualation without need for obtaining the units from a schedule.
    mode = RegulatingControlModeKind(desc="The regulating control mode presently available.  This specifications allows for determining the kind of regualation without need for obtaining the units from a schedule.The regulating control mode presently available.  This specifications allows for determining the kind of regualation without need for obtaining the units from a schedule.")

    # The regulation is performed in a discrete mode.The regulation is performed in a discrete mode.
    discrete = Bool(desc="The regulation is performed in a discrete mode.The regulation is performed in a discrete mode.")

    # The target value specified for case input.   This value can be used for the target value wihout the use of schedules. The value has the units appropriate to the mode attribute.The target value specified for case input.   This value can be used for the target value wihout the use of schedules. The value has the units appropriate to the mode attribute.
    targetValue = Float(desc="The target value specified for case input.   This value can be used for the target value wihout the use of schedules. The value has the units appropriate to the mode attribute.The target value specified for case input.   This value can be used for the target value wihout the use of schedules. The value has the units appropriate to the mode attribute.")

    # This is the case input target range.   This performs the same function as the value2 attribute on the regulation schedule in the case that schedules are not used.   The units of those appropriate for the mode.This is the case input target range.   This performs the same function as the value2 attribute on the regulation schedule in the case that schedules are not used.   The units of those appropriate for the mode.
    targetRange = Float(desc="This is the case input target range.   This performs the same function as the value2 attribute on the regulation schedule in the case that schedules are not used.   The units of those appropriate for the mode.This is the case input target range.   This performs the same function as the value2 attribute on the regulation schedule in the case that schedules are not used.   The units of those appropriate for the mode.")

    #--------------------------------------------------------------------------
    #  Begin "RegulatingControl" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "mode", "discrete", "targetValue", "targetRange",
                label="Attributes"),
            VGroup("Model", "Terminal", "RegulatingCondEq", "TapChanger",
                label="References"),
            dock="tab"),
        id="UCTE.Wires.RegulatingControl",
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
    """ Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.By convention in this profile, the CurveData points have y1multiplier of M, y2Multiplier of M, y1Units of W and y2Units of W,  xUnits of W and xMultiplier of M.Reactive power rating envelope versus the synchronous machine's active power, in both the generating and motoring modes. For each active power value there is a corresponding high and low reactive power limit  value. Typically there will be a separate curve for each coolant condition, such as hydrogen pressure.  The Y1 axis values represent reactive minimum and the Y2 axis values represent reactive maximum.By convention in this profile, the CurveData points have y1multiplier of M, y2Multiplier of M, y1Units of W and y2Units of W,  xUnits of W and xMultiplier of M.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Synchronous machines using this curve as default.Synchronous machines using this curve as default.
    InitiallyUsedBySynchronousMachine = List(Instance("UCTE.Wires.SynchronousMachine"),
        desc="Synchronous machines using this curve as default.Synchronous machines using this curve as default.")

    #--------------------------------------------------------------------------
    #  Begin "ReactiveCapabilityCurve" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName",
                label="Attributes"),
            VGroup("Model", "CurveScheduleDatas", "InitiallyUsedBySynchronousMachine",
                label="References"),
            dock="tab"),
        id="UCTE.Wires.ReactiveCapabilityCurve",
        title="ReactiveCapabilityCurve",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ReactiveCapabilityCurve" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MutualCoupling" class:
#------------------------------------------------------------------------------

class MutualCoupling(IdentifiedObject):
    """ This class represents the zero sequence line mutual coupling.This class is Optional and only used for Short Circuit.This class represents the zero sequence line mutual coupling.This class is Optional and only used for Short Circuit.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments.The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments.
    First_Terminal = Instance("UCTE.Core.Terminal", allow_none=False,
        desc="The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments.The starting terminal for the calculation of distances along the first branch of the mutual coupling.  Normally MutualCoupling would only be used for terminals of AC line segments.  The first and second terminals of a mutual coupling should point to different AC line segments.",
        transient=True,
        opposite="HasFirst_MutualCoupling",
        editor=InstanceEditor(name="_terminals"))

    def _get_terminals(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    # The starting terminal for the calculation of distances along the second branch of the mutual coupling.The starting terminal for the calculation of distances along the second branch of the mutual coupling.
    Second_Terminal = Instance("UCTE.Core.Terminal", allow_none=False,
        desc="The starting terminal for the calculation of distances along the second branch of the mutual coupling.The starting terminal for the calculation of distances along the second branch of the mutual coupling.",
        transient=True,
        opposite="HasSecond_MutualCoupling",
        editor=InstanceEditor(name="_terminals"))

    def _get_terminals(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Core.Terminal" ]
        else:
            return []

    _terminals = Property(fget=_get_terminals)

    # Distance from the second line's specified terminal to end of coupled regionMust be greater than the value of distance21 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.Distance from the second line's specified terminal to end of coupled regionMust be greater than the value of distance21 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.
    distance22 = LongLength(desc="Distance from the second line's specified terminal to end of coupled regionMust be greater than the value of distance21 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.Distance from the second line's specified terminal to end of coupled regionMust be greater than the value of distance21 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.")

    # Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section.Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section.
    g0ch = Conductance(desc="Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section.Zero sequence mutual coupling shunt (charging) conductance, uniformly distributed, of the entire line section.")

    # Distance from the second line's specified terminal to start of coupled regionCannot be equal to distance22 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.Distance from the second line's specified terminal to start of coupled regionCannot be equal to distance22 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.
    distance21 = LongLength(desc="Distance from the second line's specified terminal to start of coupled regionCannot be equal to distance22 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.Distance from the second line's specified terminal to start of coupled regionCannot be equal to distance22 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.")

    # Zero sequence branch-to-branch mutual impedance coupling, resistanceZero sequence branch-to-branch mutual impedance coupling, resistance
    r0 = Resistance(desc="Zero sequence branch-to-branch mutual impedance coupling, resistanceZero sequence branch-to-branch mutual impedance coupling, resistance")

    # Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section.Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section.
    b0ch = Susceptance(desc="Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section.Zero sequence mutual coupling shunt (charging) susceptance, uniformly distributed, of the entire line section.")

    # Zero sequence branch-to-branch mutual impedance coupling, reactanceZero sequence branch-to-branch mutual impedance coupling, reactance
    x0 = Resistance(desc="Zero sequence branch-to-branch mutual impedance coupling, reactanceZero sequence branch-to-branch mutual impedance coupling, reactance")

    # Distance from the first line's specified terminal to start of coupled regionCannot be equal to distance12 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.Distance from the first line's specified terminal to start of coupled regionCannot be equal to distance12 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.
    distance11 = LongLength(desc="Distance from the first line's specified terminal to start of coupled regionCannot be equal to distance12 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.Distance from the first line's specified terminal to start of coupled regionCannot be equal to distance12 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.")

    # Distance from the first line's from specified terminal to end of coupled regionMust be greater than the value of distance11 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.Distance from the first line's from specified terminal to end of coupled regionMust be greater than the value of distance11 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.
    distance12 = LongLength(desc="Distance from the first line's from specified terminal to end of coupled regionMust be greater than the value of distance11 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.Distance from the first line's from specified terminal to end of coupled regionMust be greater than the value of distance11 and connot be greater than Conductor.length of the referenced line.  The value of Conductor.length attribute must be a positive number.")

    #--------------------------------------------------------------------------
    #  Begin "MutualCoupling" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "distance22", "g0ch", "distance21", "r0", "b0ch", "x0", "distance11", "distance12",
                label="Attributes"),
            VGroup("Model", "First_Terminal", "Second_Terminal",
                label="References"),
            dock="tab"),
        id="UCTE.Wires.MutualCoupling",
        title="MutualCoupling",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MutualCoupling" user definitions:
    #--------------------------------------------------------------------------

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
    Contains_TransformerWindings = List(Instance("UCTE.Wires.TransformerWinding"),
        desc="A transformer has windingsA transformer has windings")

    #--------------------------------------------------------------------------
    #  Begin "PowerTransformer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "equivalent",
                label="Attributes"),
            VGroup("Model", "MemberOf_EquipmentContainer", "Contains_TransformerWindings",
                label="References"),
            dock="tab"),
        id="UCTE.Wires.PowerTransformer",
        title="PowerTransformer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PowerTransformer" user definitions:
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
    LoadResponse = Instance("UCTE.LoadModel.LoadResponseCharacteristic", allow_none=False,
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
                    "UCTE.LoadModel.LoadResponseCharacteristic" ]
        else:
            return []

    _loadresponsecharacteristics = Property(fget=_get_loadresponsecharacteristics)

    #--------------------------------------------------------------------------
    #  Begin "EnergyConsumer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "equivalent",
                label="Attributes"),
            VGroup("Model", "MemberOf_EquipmentContainer", "BaseVoltage", "Terminals", "LoadResponse",
                label="References"),
            dock="tab"),
        id="UCTE.Wires.EnergyConsumer",
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

    pass
    #--------------------------------------------------------------------------
    #  Begin "Switch" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "equivalent",
                label="Attributes"),
            VGroup("Model", "MemberOf_EquipmentContainer", "BaseVoltage", "Terminals",
                label="References"),
            dock="tab"),
        id="UCTE.Wires.Switch",
        title="Switch",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Switch" user definitions:
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

    # copy from ...Regulating control scheme in which this equipment participates.copy from ...Regulating control scheme in which this equipment participates.
    RegulatingControl = Instance("UCTE.Wires.RegulatingControl",
        desc="copy from ...Regulating control scheme in which this equipment participates.copy from ...Regulating control scheme in which this equipment participates.",
        transient=True,
        opposite="RegulatingCondEq",
        editor=InstanceEditor(name="_regulatingcontrols"))

    def _get_regulatingcontrols(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Wires.RegulatingControl" ]
        else:
            return []

    _regulatingcontrols = Property(fget=_get_regulatingcontrols)

    #--------------------------------------------------------------------------
    #  Begin "RegulatingCondEq" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "equivalent",
                label="Attributes"),
            VGroup("Model", "MemberOf_EquipmentContainer", "BaseVoltage", "Terminals", "RegulatingControl",
                label="References"),
            dock="tab"),
        id="UCTE.Wires.RegulatingCondEq",
        title="RegulatingCondEq",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RegulatingCondEq" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "VoltageControlZone" class:
#------------------------------------------------------------------------------

class VoltageControlZone(IdentifiedObject):
    """ An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled.An area of the power system network which is defined for secondary voltage control purposes. A voltage control zone consists of a collection of substations with a designated bus bar section whose voltage will be controlled.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A VoltageControlZone is controlled by a designated BusbarSection.A VoltageControlZone is controlled by a designated BusbarSection.
    BusbarSection = Instance("UCTE.Wires.BusbarSection",
        desc="A VoltageControlZone is controlled by a designated BusbarSection.A VoltageControlZone is controlled by a designated BusbarSection.",
        transient=True,
        opposite="VoltageControlZone",
        editor=InstanceEditor(name="_busbarsections"))

    def _get_busbarsections(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Wires.BusbarSection" ]
        else:
            return []

    _busbarsections = Property(fget=_get_busbarsections)

    #--------------------------------------------------------------------------
    #  Begin "VoltageControlZone" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName",
                label="Attributes"),
            VGroup("Model", "BusbarSection",
                label="References"),
            dock="tab"),
        id="UCTE.Wires.VoltageControlZone",
        title="VoltageControlZone",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "VoltageControlZone" user definitions:
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

    pass
    #--------------------------------------------------------------------------
    #  Begin "Line" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName",
                label="Attributes"),
            VGroup("Model", "TopologicalNode", "Contains_Equipments",
                label="References"),
            dock="tab"),
        id="UCTE.Wires.Line",
        title="Line",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Line" user definitions:
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

    # Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.This is for Short Circuit only.Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.This is for Short Circuit only.
    b0ch = Susceptance(desc="Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.This is for Short Circuit only.Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.This is for Short Circuit only.")

    # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.
    bch = Susceptance(desc="Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.")

    # Zero sequence series resistance of the entire line section.This is for Short Circuit only.Zero sequence series resistance of the entire line section.This is for Short Circuit only.
    r0 = Resistance(desc="Zero sequence series resistance of the entire line section.This is for Short Circuit only.Zero sequence series resistance of the entire line section.This is for Short Circuit only.")

    # Zero sequence series reactance of the entire line section.This is for Short Circuit only.Zero sequence series reactance of the entire line section.This is for Short Circuit only.
    x0 = Reactance(desc="Zero sequence series reactance of the entire line section.This is for Short Circuit only.Zero sequence series reactance of the entire line section.This is for Short Circuit only.")

    # Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only.Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only.
    gch = Conductance(desc="Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only.Positive sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only.")

    # Positive sequence series reactance of the entire line section.Positive sequence series reactance of the entire line section.
    x = Reactance(desc="Positive sequence series reactance of the entire line section.Positive sequence series reactance of the entire line section.")

    # Segment length for calculating line section capabilitiesRequired only for ACLineSegement objects involved in MutualCoupling.Segment length for calculating line section capabilitiesRequired only for ACLineSegement objects involved in MutualCoupling.
    length = LongLength(desc="Segment length for calculating line section capabilitiesRequired only for ACLineSegement objects involved in MutualCoupling.Segment length for calculating line section capabilitiesRequired only for ACLineSegement objects involved in MutualCoupling.")

    # Positive sequence series resistance of the entire line section.Positive sequence series resistance of the entire line section.
    r = Resistance(desc="Positive sequence series resistance of the entire line section.Positive sequence series resistance of the entire line section.")

    # Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only.Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only.
    g0ch = Conductance(desc="Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only.Zero sequence shunt (charging) conductance, uniformly distributed, of the entire line section.This is for Short Circuit only.")

    #--------------------------------------------------------------------------
    #  Begin "Conductor" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "equivalent", "b0ch", "bch", "r0", "x0", "gch", "x", "length", "r", "g0ch",
                label="Attributes", columns=1),
            VGroup("Model", "MemberOf_EquipmentContainer", "BaseVoltage", "Terminals",
                label="References"),
            dock="tab"),
        id="UCTE.Wires.Conductor",
        title="Conductor",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Conductor" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ACLineSegment" class:
#------------------------------------------------------------------------------

class ACLineSegment(Conductor):
    """ A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.Series compensators can be modeled as ACLineSegement.  The attribute Conductor.length is required only when used in conjunction with a Mutual Coupling.A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.Series compensators can be modeled as ACLineSegement.  The attribute Conductor.length is required only when used in conjunction with a Mutual Coupling.
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
            VGroup("UUID", "description", "name", "aliasName", "equivalent", "b0ch", "bch", "r0", "x0", "gch", "x", "length", "r", "g0ch",
                label="Attributes", columns=1),
            VGroup("Model", "MemberOf_EquipmentContainer", "BaseVoltage", "Terminals",
                label="References"),
            dock="tab"),
        id="UCTE.Wires.ACLineSegment",
        title="ACLineSegment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ACLineSegment" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PhaseTapChanger" class:
#------------------------------------------------------------------------------

class PhaseTapChanger(TapChanger):
    """ A specialization of a voltage tap changer that has detailed modeling for phase shifting capabilities.   A phase shifting tap changer is also in general a voltage magnitude transformer.    The symmetrical and asymmetrical transformer tap changer models are defined here.A specialization of a voltage tap changer that has detailed modeling for phase shifting capabilities.   A phase shifting tap changer is also in general a voltage magnitude transformer.    The symmetrical and asymmetrical transformer tap changer models are defined here.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The transformer winding to which the phase tap changer belongs.The transformer winding to which the phase tap changer belongs.
    TransformerWinding = Instance("UCTE.Wires.TransformerWinding", allow_none=False,
        desc="The transformer winding to which the phase tap changer belongs.The transformer winding to which the phase tap changer belongs.",
        transient=True,
        opposite="PhaseTapChanger",
        editor=InstanceEditor(name="_transformerwindings"))

    def _get_transformerwindings(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Wires.TransformerWinding" ]
        else:
            return []

    _transformerwindings = Property(fget=_get_transformerwindings)

    # The reactance at the minimum tap step.The reactance at the minimum tap step.
    xStepMin = Reactance(desc="The reactance at the minimum tap step.The reactance at the minimum tap step.")

    # The reactance at the maximum tap step.The reactance at the maximum tap step.
    xStepMax = Reactance(desc="The reactance at the maximum tap step.The reactance at the maximum tap step.")

    # Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accureatly computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available.Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accureatly computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available.
    stepPhaseShiftIncrement = AngleDegrees(desc="Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accureatly computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available.Phase shift per step position. A positive value indicates a positive phase shift from the winding where the tap is located to the other winding (for a two-winding transformer). The actual phase shift increment might be more accureatly computed from the symmetrical or asymmetrical models or a tap step table lookup if those are available.")

    # The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees.This is required if PST is AsymmetricalThe phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees.This is required if PST is Asymmetrical
    windingConnectionAngle = AngleDegrees(desc="The phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees.This is required if PST is AsymmetricalThe phase angle between the in-phase winding and the out-of -phase winding used for creating phase shift.   It is only possible to have a symmemtrical transformer if this angle is 90 degrees.This is required if PST is Asymmetrical")

    # The type of phase shifter construction.The type of phase shifter construction.
    phaseTapChangerType = PhaseTapChangerKind(desc="The type of phase shifter construction.The type of phase shifter construction.")

    # The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding.This is required if PST is Asymmetrical.The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding.This is required if PST is Asymmetrical.
    voltageStepIncrementOutOfPhase = Voltage(desc="The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding.This is required if PST is Asymmetrical.The voltage step increment on the out of phase winding.    This voltage step on the out of phase winding of the phase shifter.  Similar to TapChanger.voltageStepIncrement, but it is applied only to the out of phase winding.This is required if PST is Asymmetrical.")

    #--------------------------------------------------------------------------
    #  Begin "PhaseTapChanger" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "stepVoltageIncrement", "neutralU", "lowStep", "neutralStep", "highStep", "xStepMin", "xStepMax", "stepPhaseShiftIncrement", "windingConnectionAngle", "phaseTapChangerType", "voltageStepIncrementOutOfPhase",
                label="Attributes", columns=1),
            VGroup("Model", "SvTapStep", "RegulatingControl", "TransformerWinding",
                label="References"),
            dock="tab"),
        id="UCTE.Wires.PhaseTapChanger",
        title="PhaseTapChanger",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PhaseTapChanger" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SynchronousMachine" class:
#------------------------------------------------------------------------------

class SynchronousMachine(RegulatingCondEq):
    """ An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.In this profile: - If a SynchronousMachine is not associated with a ReactiveCapabilityCurve, then the minQ and maxQ attributes will be used.    - If a ReactiveCapabilityCurve is supplied, then the minQ and maxQ attributes are not required.  - For UCTE, there is no synchronous condenser mode; therefore, the SynchronousMachine must be associated with one and only one  GeneratingUnit.  In this case, the type and operatingMode attributes must both be set to ?condenser?. An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.In this profile: - If a SynchronousMachine is not associated with a ReactiveCapabilityCurve, then the minQ and maxQ attributes will be used.    - If a ReactiveCapabilityCurve is supplied, then the minQ and maxQ attributes are not required.  - For UCTE, there is no synchronous condenser mode; therefore, the SynchronousMachine must be associated with one and only one  GeneratingUnit.  In this case, the type and operatingMode attributes must both be set to ?condenser?. 
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The default ReactiveCapabilityCurve for use by a SynchronousMachineThe default ReactiveCapabilityCurve for use by a SynchronousMachine
    InitialReactiveCapabilityCurve = Instance("UCTE.Wires.ReactiveCapabilityCurve",
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
                    "UCTE.Wires.ReactiveCapabilityCurve" ]
        else:
            return []

    _reactivecapabilitycurves = Property(fget=_get_reactivecapabilitycurves)

    # The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.
    Drives_HydroPump = Instance("UCTE.Generation.Production.HydroPump",
        desc="The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.The synchronous machine drives the turbine which moves the water from a low elevation to a higher elevation. The direction of machine rotation for pumping may or may not be the same as for generating.",
        transient=True,
        opposite="DrivenBy_SynchronousMachine",
        editor=InstanceEditor(name="_hydropumps"))

    def _get_hydropumps(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Generation.Production.HydroPump" ]
        else:
            return []

    _hydropumps = Property(fget=_get_hydropumps)

    # A synchronous machine may operate as a generator and as such becomes a member of a generating unitEach SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection.A synchronous machine may operate as a generator and as such becomes a member of a generating unitEach SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection.
    MemberOf_GeneratingUnit = Instance("UCTE.Generation.Production.GeneratingUnit", allow_none=False,
        desc="A synchronous machine may operate as a generator and as such becomes a member of a generating unitEach SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection.A synchronous machine may operate as a generator and as such becomes a member of a generating unitEach SynchronousMachine is a member of one and only one GeneratingUnit plus each GeneratingUnit should have one and only one SynchronousMachine.   This is required to properly proportion generation limits specified on GeneratingUnit to the appropriate injection points specified by SynchronousMachine and its Terminal connection.",
        transient=True,
        opposite="Contains_SynchronousMachines",
        editor=InstanceEditor(name="_generatingunits"))

    def _get_generatingunits(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Generation.Production.GeneratingUnit" ]
        else:
            return []

    _generatingunits = Property(fget=_get_generatingunits)

    # Zero sequence reactance of the synchronous machine.This is for Short Circuit only.Zero sequence reactance of the synchronous machine.This is for Short Circuit only.
    x0 = Reactance(desc="Zero sequence reactance of the synchronous machine.This is for Short Circuit only.Zero sequence reactance of the synchronous machine.This is for Short Circuit only.")

    # Current mode of operation.Current mode of operation.
    operatingMode = SynchronousMachineOperatingMode(desc="Current mode of operation.Current mode of operation.")

    # Zero sequence resistance of the synchronous machine.This is for Short Circuit only.Zero sequence resistance of the synchronous machine.This is for Short Circuit only.
    r0 = Resistance(desc="Zero sequence resistance of the synchronous machine.This is for Short Circuit only.Zero sequence resistance of the synchronous machine.This is for Short Circuit only.")

    # Percent of the coordinated reactive control that comes from this machine.Percent of the coordinated reactive control that comes from this machine.
    qPercent = PerCent(desc="Percent of the coordinated reactive control that comes from this machine.Percent of the coordinated reactive control that comes from this machine.")

    # Negative sequence reactance.This is for Short Circuit only.Negative sequence reactance.This is for Short Circuit only.
    x2 = Reactance(desc="Negative sequence reactance.This is for Short Circuit only.Negative sequence reactance.This is for Short Circuit only.")

    # Modes that this synchronous machine can operate in.Modes that this synchronous machine can operate in.
    type = SynchronousMachineType(desc="Modes that this synchronous machine can operate in.Modes that this synchronous machine can operate in.")

    # Negative sequence resistance.This is for Short Circuit only.Negative sequence resistance.This is for Short Circuit only.
    r2 = Resistance(desc="Negative sequence resistance.This is for Short Circuit only.Negative sequence resistance.This is for Short Circuit only.")

    # Positive sequence resistance of the synchronous machine.Positive sequence resistance of the synchronous machine.
    r = Resistance(desc="Positive sequence resistance of the synchronous machine.Positive sequence resistance of the synchronous machine.")

    # Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.
    maxQ = ReactivePower(desc="Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.Maximum reactive power limit. This is the maximum (nameplate) limit for the unit.")

    # Positive sequence reactance of the synchronous machine.Positive sequence reactance of the synchronous machine.
    x = Reactance(desc="Positive sequence reactance of the synchronous machine.Positive sequence reactance of the synchronous machine.")

    # Nameplate apparent power rating for the unitNameplate apparent power rating for the unit
    ratedS = ApparentPower(desc="Nameplate apparent power rating for the unitNameplate apparent power rating for the unit")

    # Minimum reactive power limit for the unit.Minimum reactive power limit for the unit.
    minQ = ReactivePower(desc="Minimum reactive power limit for the unit.Minimum reactive power limit for the unit.")

    #--------------------------------------------------------------------------
    #  Begin "SynchronousMachine" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "equivalent", "x0", "operatingMode", "r0", "qPercent", "x2", "type", "r2", "r", "maxQ", "x", "ratedS", "minQ",
                label="Attributes", columns=1),
            VGroup("Model", "MemberOf_EquipmentContainer", "BaseVoltage", "Terminals", "RegulatingControl", "InitialReactiveCapabilityCurve", "Drives_HydroPump", "MemberOf_GeneratingUnit",
                label="References"),
            dock="tab"),
        id="UCTE.Wires.SynchronousMachine",
        title="SynchronousMachine",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SynchronousMachine" user definitions:
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

    # The transformer winding to which the ratio tap changer belongs.The transformer winding to which the ratio tap changer belongs.
    TransformerWinding = Instance("UCTE.Wires.TransformerWinding", allow_none=False,
        desc="The transformer winding to which the ratio tap changer belongs.The transformer winding to which the ratio tap changer belongs.",
        transient=True,
        opposite="RatioTapChanger",
        editor=InstanceEditor(name="_transformerwindings"))

    def _get_transformerwindings(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.Wires.TransformerWinding" ]
        else:
            return []

    _transformerwindings = Property(fget=_get_transformerwindings)

    #--------------------------------------------------------------------------
    #  Begin "RatioTapChanger" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "stepVoltageIncrement", "neutralU", "lowStep", "neutralStep", "highStep",
                label="Attributes"),
            VGroup("Model", "SvTapStep", "RegulatingControl", "TransformerWinding",
                label="References"),
            dock="tab"),
        id="UCTE.Wires.RatioTapChanger",
        title="RatioTapChanger",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RatioTapChanger" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ShuntCompensator" class:
#------------------------------------------------------------------------------

class ShuntCompensator(RegulatingCondEq):
    """ A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.mVArPerSection and nominalMVAr is now bPerSection.A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  Negative values for mVArPerSection and nominalMVAr indicate that the compensator is a reactor.mVArPerSection and nominalMVAr is now bPerSection.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The state for the number of shunt compensator sections in service.The state for the number of shunt compensator sections in service.
    SvShuntCompensatorSections = Instance("UCTE.StateVariables.SvShuntCompensatorSections",
        desc="The state for the number of shunt compensator sections in service.The state for the number of shunt compensator sections in service.",
        transient=True,
        opposite="ShuntCompensator",
        editor=InstanceEditor(name="_svshuntcompensatorsectionss"))

    def _get_svshuntcompensatorsectionss(self):
        """ Property getter.
        """
        if self.Model is not None:
            return [e for e in self.Model.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "UCTE.StateVariables.SvShuntCompensatorSections" ]
        else:
            return []

    _svshuntcompensatorsectionss = Property(fget=_get_svshuntcompensatorsectionss)

    # Zero sequence shunt (charging) susceptance per sectionThis is for Short Circuit only.Zero sequence shunt (charging) susceptance per sectionThis is for Short Circuit only.
    b0PerSection = Susceptance(desc="Zero sequence shunt (charging) susceptance per sectionThis is for Short Circuit only.Zero sequence shunt (charging) susceptance per sectionThis is for Short Circuit only.")

    # For a capacitor bank, the maximum number of sections that may be switched in.For a capacitor bank, the maximum number of sections that may be switched in.
    maximumSections = Int(desc="For a capacitor bank, the maximum number of sections that may be switched in.For a capacitor bank, the maximum number of sections that may be switched in.")

    # Zero sequence shunt (charging) conductance per sectionThis is for Short Circuit only.Zero sequence shunt (charging) conductance per sectionThis is for Short Circuit only.
    g0PerSection = Conductance(desc="Zero sequence shunt (charging) conductance per sectionThis is for Short Circuit only.Zero sequence shunt (charging) conductance per sectionThis is for Short Circuit only.")

    # Positive sequence shunt (charging) susceptance per sectionPositive sequence shunt (charging) susceptance per section
    bPerSection = Susceptance(desc="Positive sequence shunt (charging) susceptance per sectionPositive sequence shunt (charging) susceptance per section")

    # Positive sequence shunt (charging) conductance per sectionPositive sequence shunt (charging) conductance per section
    gPerSection = Conductance(desc="Positive sequence shunt (charging) conductance per sectionPositive sequence shunt (charging) conductance per section")

    #--------------------------------------------------------------------------
    #  Begin "ShuntCompensator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "name", "aliasName", "equivalent", "b0PerSection", "maximumSections", "g0PerSection", "bPerSection", "gPerSection",
                label="Attributes"),
            VGroup("Model", "MemberOf_EquipmentContainer", "BaseVoltage", "Terminals", "RegulatingControl", "SvShuntCompensatorSections",
                label="References"),
            dock="tab"),
        id="UCTE.Wires.ShuntCompensator",
        title="ShuntCompensator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ShuntCompensator" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
