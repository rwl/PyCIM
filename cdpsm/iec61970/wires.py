# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

""" An extension to the Core and Topology package that models information on the electrical characteristics of Transmission and Distribution networks. This package is used by network applications such as State Estimation, Load Flow and Optimal Power Flow.
"""

from cdpsm.iec61970.core import ConductingEquipment
from cdpsm.iec61970.core import PowerSystemResource
from cdpsm.iec61970.core import EquipmentContainer

# <<< imports
# @generated
# >>> imports

ns_prefix = "cim"

ns_uri = "http://iec.ch/TC57/2009/CIM-schema-cim14#Package_Wires"

class BusbarSection(ConductingEquipment):
    """ A conductor, or group of conductors, with negligible impedance, that serve to connect other conducting equipment within a single substation.  Voltage measurements are typically obtained from VoltageTransformers that are connected to busbar sections. A bus bar section may have many physical terminals but for analysis is modelled with exactly one logical terminal.
    """
    pass
    # <<< busbar_section
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'BusbarSection' instance.

        """


        super(BusbarSection, self).__init__(*args, **kw_args)
    # >>> busbar_section



class TapChanger(PowerSystemResource):
    """ Mechanism for changing transformer winding tap positions.
    """
    # <<< tap_changer
    # @generated
    def __init__(self, step_voltage_increment=0.0, subsequent_delay=0.0, neutral_step=0, normal_step=0, ltc_flag=False, neutral_u=0.0, low_step=0, initial_delay=0.0, regulation_status=False, high_step=0, sv_tap_step=None, *args, **kw_args):
        """ Initialises a new 'TapChanger' instance.

        @param step_voltage_increment: Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step. 
        @param subsequent_delay: For an LTC, the delay for subsequent tap changer operation (second and later step changes) 
        @param neutral_step: The neutral tap step position for this winding. 
        @param normal_step: The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting. 
        @param ltc_flag: Specifies whether or not a TapChanger has load tap changing capabilities. 
        @param neutral_u: Voltage at which the winding operates at the neutral tap setting. 
        @param low_step: Lowest possible tap step position, retard from neutral 
        @param initial_delay: For an LTC, the delay for initial tap changer operation (first step change) 
        @param regulation_status: Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating. 
        @param high_step: Highest possible tap step position, advance from neutral 
        @param sv_tap_step: The tap step state associated with the tap changer.
        """
        # Tap step increment, in per cent of nominal voltage, per step position.  For a symmetrical PhaseTapChanger, the stepVoltageIncrement is used in the formula for calculation of the phase angle.  For a symmetrical PhaseTapChanger, the voltage magnitude does not change with tap step. 
        self.step_voltage_increment = step_voltage_increment

        # For an LTC, the delay for subsequent tap changer operation (second and later step changes) 
        self.subsequent_delay = subsequent_delay

        # The neutral tap step position for this winding. 
        self.neutral_step = neutral_step

        # The tap step position used in 'normal' network operation for this winding. For a 'Fixed' tap changer indicates the current physical tap setting. 
        self.normal_step = normal_step

        # Specifies whether or not a TapChanger has load tap changing capabilities. 
        self.ltc_flag = ltc_flag

        # Voltage at which the winding operates at the neutral tap setting. 
        self.neutral_u = neutral_u

        # Lowest possible tap step position, retard from neutral 
        self.low_step = low_step

        # For an LTC, the delay for initial tap changer operation (first step change) 
        self.initial_delay = initial_delay

        # Specifies the default regulation status of the TapChanger.  True is regulating.  False is not regulating. 
        self.regulation_status = regulation_status

        # Highest possible tap step position, advance from neutral 
        self.high_step = high_step


        self._sv_tap_step = None
        self.sv_tap_step = sv_tap_step


        super(TapChanger, self).__init__(*args, **kw_args)
    # >>> tap_changer

    # <<< sv_tap_step
    # @generated
    def get_sv_tap_step(self):
        """ The tap step state associated with the tap changer.
        """
        return self._sv_tap_step

    def set_sv_tap_step(self, value):
        if self._sv_tap_step is not None:
            self._sv_tap_step._tap_changer = None

        self._sv_tap_step = value
        if self._sv_tap_step is not None:
            self._sv_tap_step._tap_changer = self

    sv_tap_step = property(get_sv_tap_step, set_sv_tap_step)
    # >>> sv_tap_step



class Junction(ConductingEquipment):
    """ A point where one or more conducting equipments are connected with zero resistance.
    """
    pass
    # <<< junction
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'Junction' instance.

        """


        super(Junction, self).__init__(*args, **kw_args)
    # >>> junction



class EnergySource(ConductingEquipment):
    """ A generic equivalent for an energy supplier on a transmission or distribution voltage level.
    """
    # <<< energy_source
    # @generated
    def __init__(self, x=0.0, voltage_magnitude=0.0, voltage_angle=0.0, nominal_voltage=0.0, *args, **kw_args):
        """ Initialises a new 'EnergySource' instance.

        @param x: Positive sequence Thevenin reactance. 
        @param voltage_magnitude: Phase-to-phase open circuit voltage magnitude. 
        @param voltage_angle: Phase angle of a-phase open circuit. 
        @param nominal_voltage: Phase-to-phase nominal voltage. 
        """
        # Positive sequence Thevenin reactance. 
        self.x = x

        # Phase-to-phase open circuit voltage magnitude. 
        self.voltage_magnitude = voltage_magnitude

        # Phase angle of a-phase open circuit. 
        self.voltage_angle = voltage_angle

        # Phase-to-phase nominal voltage. 
        self.nominal_voltage = nominal_voltage



        super(EnergySource, self).__init__(*args, **kw_args)
    # >>> energy_source



class SynchronousMachine(ConductingEquipment):
    """ An electromechanical device that operates synchronously with the network. It is a single machine operating either as a generator or synchronous condenser or pump.
    """
    # <<< synchronous_machine
    # @generated
    def __init__(self, base_q=0.0, operating_mode='condenser', type='condenser', max_q=0.0, min_q=0.0, generating_unit=None, *args, **kw_args):
        """ Initialises a new 'SynchronousMachine' instance.

        @param base_q: Default base reactive power value. This value represents the initial reactive power that can be used by any application function. 
        @param operating_mode: Current mode of operation. Values are: "condenser", "generator"
        @param type: Modes that this synchronous machine can operate in. Values are: "condenser", "generator_or_condenser", "generator"
        @param max_q: Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. 
        @param min_q: Minimum reactive power limit for the unit. 
        @param generating_unit: A synchronous machine may operate as a generator and as such becomes a member of a generating unit
        """
        # Default base reactive power value. This value represents the initial reactive power that can be used by any application function. 
        self.base_q = base_q

        # Current mode of operation. Values are: "condenser", "generator"
        self.operating_mode = operating_mode

        # Modes that this synchronous machine can operate in. Values are: "condenser", "generator_or_condenser", "generator"
        self.type = type

        # Maximum reactive power limit. This is the maximum (nameplate) limit for the unit. 
        self.max_q = max_q

        # Minimum reactive power limit for the unit. 
        self.min_q = min_q


        self._generating_unit = None
        self.generating_unit = generating_unit


        super(SynchronousMachine, self).__init__(*args, **kw_args)
    # >>> synchronous_machine

    # <<< generating_unit
    # @generated
    def get_generating_unit(self):
        """ A synchronous machine may operate as a generator and as such becomes a member of a generating unit
        """
        return self._generating_unit

    def set_generating_unit(self, value):
        if self._generating_unit is not None:
            filtered = [x for x in self.generating_unit.synchronous_machines if x != self]
            self._generating_unit._synchronous_machines = filtered

        self._generating_unit = value
        if self._generating_unit is not None:
            self._generating_unit._synchronous_machines.append(self)

    generating_unit = property(get_generating_unit, set_generating_unit)
    # >>> generating_unit



class EnergyConsumer(ConductingEquipment):
    """ Generic user of energy - a  point of consumption on the power system model
    """
    # <<< energy_consumer
    # @generated
    def __init__(self, pfixed=0.0, pfixed_pct=0.0, qfixed_pct=0.0, qfixed=0.0, customer_count=0, load_response=None, *args, **kw_args):
        """ Initialises a new 'EnergyConsumer' instance.

        @param pfixed: Active power of the load that is a fixed quantity. 
        @param pfixed_pct: Fixed active power as per cent of load group fixed active power 
        @param qfixed_pct: Fixed reactive power as per cent of load group fixed reactive power. 
        @param qfixed: Reactive power of the load that is a fixed quantity. 
        @param customer_count: Number of individual customers represented by this Demand 
        @param load_response: The load response characteristic of this load.
        """
        # Active power of the load that is a fixed quantity. 
        self.pfixed = pfixed

        # Fixed active power as per cent of load group fixed active power 
        self.pfixed_pct = pfixed_pct

        # Fixed reactive power as per cent of load group fixed reactive power. 
        self.qfixed_pct = qfixed_pct

        # Reactive power of the load that is a fixed quantity. 
        self.qfixed = qfixed

        # Number of individual customers represented by this Demand 
        self.customer_count = customer_count


        self._load_response = None
        self.load_response = load_response


        super(EnergyConsumer, self).__init__(*args, **kw_args)
    # >>> energy_consumer

    # <<< load_response
    # @generated
    def get_load_response(self):
        """ The load response characteristic of this load.
        """
        return self._load_response

    def set_load_response(self, value):
        if self._load_response is not None:
            filtered = [x for x in self.load_response.energy_consumer if x != self]
            self._load_response._energy_consumer = filtered

        self._load_response = value
        if self._load_response is not None:
            self._load_response._energy_consumer.append(self)

    load_response = property(get_load_response, set_load_response)
    # >>> load_response



class Switch(ConductingEquipment):
    """ A generic device designed to close, or open, or both, one or more electric circuits.
    """
    # <<< switch
    # @generated
    def __init__(self, normal_open=False, *args, **kw_args):
        """ Initialises a new 'Switch' instance.

        @param normal_open: The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen. 
        """
        # The attribute is used in cases when no Measurement for the status value is present. If the Switch has a status measurment the Discrete.normalValue is expected to match with the Switch.normalOpen. 
        self.normal_open = normal_open



        super(Switch, self).__init__(*args, **kw_args)
    # >>> switch



class Line(EquipmentContainer):
    """ A component part of a system extending between adjacent substations or from a substation to an adjacent interconnection point.
    """
    # <<< line
    # @generated
    def __init__(self, region=None, *args, **kw_args):
        """ Initialises a new 'Line' instance.

        @param region: A Line can be contained by a SubGeographical Region.
        """

        self._region = None
        self.region = region


        super(Line, self).__init__(*args, **kw_args)
    # >>> line

    # <<< region
    # @generated
    def get_region(self):
        """ A Line can be contained by a SubGeographical Region.
        """
        return self._region

    def set_region(self, value):
        if self._region is not None:
            filtered = [x for x in self.region.lines if x != self]
            self._region._lines = filtered

        self._region = value
        if self._region is not None:
            self._region._lines.append(self)

    region = property(get_region, set_region)
    # >>> region



class ShuntCompensator(ConductingEquipment):
    """ A shunt capacitor or reactor or switchable bank of shunt capacitors or reactors. A section of a shunt compensator is an individual capacitor or reactor.  A negative value for reactivePerSection indicates that the compensator is a reactor. ShuntCompensator is a single terminal device.  Ground is implied.
    """
    # <<< shunt_compensator
    # @generated
    def __init__(self, nom_q=0.0, nom_u=0.0, normal_sections=0, maximum_sections=0, reactive_per_section=0.0, *args, **kw_args):
        """ Initialises a new 'ShuntCompensator' instance.

        @param nom_q: Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive. 
        @param nom_u: The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network. 
        @param normal_sections: For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ). 
        @param maximum_sections: For a capacitor bank, the maximum number of sections that may be switched in. 
        @param reactive_per_section: For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage. 
        """
        # Nominal reactive power output of the capacitor bank at the nominal voltage. This number should be positive. 
        self.nom_q = nom_q

        # The nominal voltage at which the nominal reactive power was measured. This should normally be within 10% of the voltage at which the capacitor is connected to the network. 
        self.nom_u = nom_u

        # For a capacitor bank, the normal number of sections switched in. This number should correspond to the nominal reactive power (nomQ). 
        self.normal_sections = normal_sections

        # For a capacitor bank, the maximum number of sections that may be switched in. 
        self.maximum_sections = maximum_sections

        # For a capacitor bank, the size in reactive power of each switchable section at the nominal voltage. 
        self.reactive_per_section = reactive_per_section



        super(ShuntCompensator, self).__init__(*args, **kw_args)
    # >>> shunt_compensator



class Conductor(ConductingEquipment):
    """ Combination of conducting material with consistent electrical characteristics, building a single electrical system, used to carry current between points in the power system.
    """
    # <<< conductor
    # @generated
    def __init__(self, length=0.0, *args, **kw_args):
        """ Initialises a new 'Conductor' instance.

        @param length: Segment length for calculating line section capabilities 
        """
        # Segment length for calculating line section capabilities 
        self.length = length



        super(Conductor, self).__init__(*args, **kw_args)
    # >>> conductor



class LoadBreakSwitch(Switch):
    """ A mechanical switching device capable of making, carrying, and breaking currents under normal operating conditions.
    """
    # <<< load_break_switch
    # @generated
    def __init__(self, rated_current=0.0, *args, **kw_args):
        """ Initialises a new 'LoadBreakSwitch' instance.

        @param rated_current: Current carrying capacity of a wire or cable under stated thermal conditions. 
        """
        # Current carrying capacity of a wire or cable under stated thermal conditions. 
        self.rated_current = rated_current



        super(LoadBreakSwitch, self).__init__(*args, **kw_args)
    # >>> load_break_switch



class Fuse(Switch):
    """ An overcurrent protective device with a circuit opening fusible part that is heated and severed by the passage of overcurrent through it. A fuse is considered a switching device because it breaks current.
    """
    # <<< fuse
    # @generated
    def __init__(self, rating_current=0.0, *args, **kw_args):
        """ Initialises a new 'Fuse' instance.

        @param rating_current: Fault interrupting current rating. 
        """
        # Fault interrupting current rating. 
        self.rating_current = rating_current



        super(Fuse, self).__init__(*args, **kw_args)
    # >>> fuse



class ACLineSegment(Conductor):
    """ A wire or combination of wires, with consistent electrical characteristics, building a single electrical system, used to carry alternating current between points in the power system.If the instance is an ACLineSegment, the resistance and reactance is mandatory.  However, if the line segment is for a DistributionLineSegment, these are not mandatory.
    """
    # <<< acline_segment
    # @generated
    def __init__(self, r=0.0, x0=0.0, bch=0.0, x=0.0, b0ch=0.0, r0=0.0, *args, **kw_args):
        """ Initialises a new 'ACLineSegment' instance.

        @param r: Positive sequence series resistance of the entire line section. 
        @param x0: Zero sequence series reactance of the entire line section. 
        @param bch: Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line. 
        @param x: Positive sequence series reactance of the entire line section. 
        @param b0ch: Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. 
        @param r0: Zero sequence series resistance of the entire line section. 
        """
        # Positive sequence series resistance of the entire line section. 
        self.r = r

        # Zero sequence series reactance of the entire line section. 
        self.x0 = x0

        # Positive sequence shunt (charging) susceptance, uniformly distributed, of the entire line section.  This value represents the full charging over the full length of the line. 
        self.bch = bch

        # Positive sequence series reactance of the entire line section. 
        self.x = x

        # Zero sequence shunt (charging) susceptance, uniformly distributed, of the entire line section. 
        self.b0ch = b0ch

        # Zero sequence series resistance of the entire line section. 
        self.r0 = r0



        super(ACLineSegment, self).__init__(*args, **kw_args)
    # >>> acline_segment



class Disconnector(Switch):
    """ A manually operated or motor operated mechanical switching device used for changing the connections in a circuit, or for isolating a circuit or equipment from a source of power. It is required to open or close circuits when negligible current is broken or made.
    """
    pass
    # <<< disconnector
    # @generated
    def __init__(self, *args, **kw_args):
        """ Initialises a new 'Disconnector' instance.

        """


        super(Disconnector, self).__init__(*args, **kw_args)
    # >>> disconnector



class RatioTapChanger(TapChanger):
    """ A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..
    """
    # <<< ratio_tap_changer
    # @generated
    def __init__(self, tcul_control_mode='reactive', winding=None, *args, **kw_args):
        """ Initialises a new 'RatioTapChanger' instance.

        @param tcul_control_mode: Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger. Values are: "reactive", "volt"
        @param winding: Winding to which this ratio tap changer belongs.
        """
        # Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger. Values are: "reactive", "volt"
        self.tcul_control_mode = tcul_control_mode


        self._winding = None
        self.winding = winding


        super(RatioTapChanger, self).__init__(*args, **kw_args)
    # >>> ratio_tap_changer

    # <<< winding
    # @generated
    def get_winding(self):
        """ Winding to which this ratio tap changer belongs.
        """
        return self._winding

    def set_winding(self, value):
        if self._winding is not None:
            self._winding._ratio_tap_changer = None

        self._winding = value
        if self._winding is not None:
            self._winding._ratio_tap_changer = self

    winding = property(get_winding, set_winding)
    # >>> winding



class Breaker(Switch):
    """ A mechanical switching device capable of making, carrying, and breaking currents under normal circuit conditions and also making, carrying for a specified time, and breaking currents under specified abnormal circuit conditions e.g.  those of short circuit.
    """
    # <<< breaker
    # @generated
    def __init__(self, rated_current=0.0, *args, **kw_args):
        """ Initialises a new 'Breaker' instance.

        @param rated_current: Fault interrupting current rating. 
        """
        # Fault interrupting current rating. 
        self.rated_current = rated_current



        super(Breaker, self).__init__(*args, **kw_args)
    # >>> breaker



# <<< wires
# @generated
# >>> wires
