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

""" An extension to the Core and Wires packages that models information for protection equipment such as relays. These entities are used within training simulators and distribution network fault location applications.
"""

from cim14v13.iec61970.core import Equipment
from cim14v13.iec61970.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimProtection"

ns_uri = "http://iec.ch/TC57/CIM-generic#Protection"

class FaultIndicator(Equipment):
    """ A FaultIndicator is typically only an indicator (which may or may not be remotely monitored), and not a piece of equipment that actually initiates a protection event. It is used for FLISR (Fault Location, Isolation and Restoration) purposes, assisting with the dispatch of crews to 'most likely' part of the network (i.e. assists with determining circuit section where the fault most likely happened).
    """
    # <<< fault_indicator
    # @generated
    def __init__(self, fault_indicator_assets=None, fault_indicator_type_asset=None, *args, **kw_args):
        """ Initialises a new 'FaultIndicator' instance.

        @param fault_indicator_assets:
        @param fault_indicator_type_asset:
        """

        self._fault_indicator_assets = []
        if fault_indicator_assets is not None:
            self.fault_indicator_assets = fault_indicator_assets
        else:
            self.fault_indicator_assets = []

        self._fault_indicator_type_asset = None
        self.fault_indicator_type_asset = fault_indicator_type_asset


        super(FaultIndicator, self).__init__(*args, **kw_args)
    # >>> fault_indicator

    # <<< fault_indicator_assets
    # @generated
    def get_fault_indicator_assets(self):
        """ 
        """
        return self._fault_indicator_assets

    def set_fault_indicator_assets(self, value):
        for x in self._fault_indicator_assets:
            x._fault_indicator = None
        for y in value:
            y._fault_indicator = self
        self._fault_indicator_assets = value

    fault_indicator_assets = property(get_fault_indicator_assets, set_fault_indicator_assets)

    def add_fault_indicator_assets(self, *fault_indicator_assets):
        for obj in fault_indicator_assets:
            obj._fault_indicator = self
            self._fault_indicator_assets.append(obj)

    def remove_fault_indicator_assets(self, *fault_indicator_assets):
        for obj in fault_indicator_assets:
            obj._fault_indicator = None
            self._fault_indicator_assets.remove(obj)
    # >>> fault_indicator_assets

    # <<< fault_indicator_type_asset
    # @generated
    def get_fault_indicator_type_asset(self):
        """ 
        """
        return self._fault_indicator_type_asset

    def set_fault_indicator_type_asset(self, value):
        if self._fault_indicator_type_asset is not None:
            filtered = [x for x in self.fault_indicator_type_asset.fault_indicators if x != self]
            self._fault_indicator_type_asset._fault_indicators = filtered

        self._fault_indicator_type_asset = value
        if self._fault_indicator_type_asset is not None:
            self._fault_indicator_type_asset._fault_indicators.append(self)

    fault_indicator_type_asset = property(get_fault_indicator_type_asset, set_fault_indicator_type_asset)
    # >>> fault_indicator_type_asset



class SurgeProtector(Equipment):
    """ Shunt device, installed on the network, usually in the proximity of electrical equipment in order to protect the said equipment against transient voltage spikes caused by lightning or switching activity.
    """
    # <<< surge_protector
    # @generated
    def __init__(self, surge_protector_type_asset=None, surge_protector_asset=None, *args, **kw_args):
        """ Initialises a new 'SurgeProtector' instance.

        @param surge_protector_type_asset:
        @param surge_protector_asset:
        """

        self._surge_protector_type_asset = None
        self.surge_protector_type_asset = surge_protector_type_asset

        self._surge_protector_asset = None
        self.surge_protector_asset = surge_protector_asset


        super(SurgeProtector, self).__init__(*args, **kw_args)
    # >>> surge_protector

    # <<< surge_protector_type_asset
    # @generated
    def get_surge_protector_type_asset(self):
        """ 
        """
        return self._surge_protector_type_asset

    def set_surge_protector_type_asset(self, value):
        if self._surge_protector_type_asset is not None:
            filtered = [x for x in self.surge_protector_type_asset.surge_protectors if x != self]
            self._surge_protector_type_asset._surge_protectors = filtered

        self._surge_protector_type_asset = value
        if self._surge_protector_type_asset is not None:
            self._surge_protector_type_asset._surge_protectors.append(self)

    surge_protector_type_asset = property(get_surge_protector_type_asset, set_surge_protector_type_asset)
    # >>> surge_protector_type_asset

    # <<< surge_protector_asset
    # @generated
    def get_surge_protector_asset(self):
        """ 
        """
        return self._surge_protector_asset

    def set_surge_protector_asset(self, value):
        if self._surge_protector_asset is not None:
            self._surge_protector_asset._surge_protector = None

        self._surge_protector_asset = value
        if self._surge_protector_asset is not None:
            self._surge_protector_asset._surge_protector = self

    surge_protector_asset = property(get_surge_protector_asset, set_surge_protector_asset)
    # >>> surge_protector_asset



class RecloseSequence(IdentifiedObject):
    """ A reclose sequence (open and close) is defined for each possible reclosure of a breaker.
    """
    # <<< reclose_sequence
    # @generated
    def __init__(self, reclose_step=0, reclose_delay=0.0, protected_switch=None, *args, **kw_args):
        """ Initialises a new 'RecloseSequence' instance.

        @param reclose_step: Indicates the ordinal position of the reclose step relative to other steps in the sequence. 
        @param reclose_delay: Indicates the time lapse before the reclose step will execute a reclose. 
        @param protected_switch: A breaker may have zero or more automatic reclosures after a trip occurs.
        """
        # Indicates the ordinal position of the reclose step relative to other steps in the sequence. 
        self.reclose_step = reclose_step

        # Indicates the time lapse before the reclose step will execute a reclose. 
        self.reclose_delay = reclose_delay


        self._protected_switch = None
        self.protected_switch = protected_switch


        super(RecloseSequence, self).__init__(*args, **kw_args)
    # >>> reclose_sequence

    # <<< protected_switch
    # @generated
    def get_protected_switch(self):
        """ A breaker may have zero or more automatic reclosures after a trip occurs.
        """
        return self._protected_switch

    def set_protected_switch(self, value):
        if self._protected_switch is not None:
            filtered = [x for x in self.protected_switch.reclose_sequences if x != self]
            self._protected_switch._reclose_sequences = filtered

        self._protected_switch = value
        if self._protected_switch is not None:
            self._protected_switch._reclose_sequences.append(self)

    protected_switch = property(get_protected_switch, set_protected_switch)
    # >>> protected_switch



class ProtectionEquipment(Equipment):
    """ An electrical device designed to respond to input conditions in a prescribed manner and after specified conditions are met to cause contact operation or similar abrupt change in associated electric control circuits, or simply to display the detected condition. Protection equipment are associated with conducting equipment and usually operate circuit breakers.
    """
    # <<< protection_equipment
    # @generated
    def __init__(self, high_limit=0.0, power_direction_flag=False, low_limit=0.0, relay_delay_time=0.0, protected_switches=None, unit=None, conducting_equipments=None, *args, **kw_args):
        """ Initialises a new 'ProtectionEquipment' instance.

        @param high_limit: The maximum allowable value. 
        @param power_direction_flag: Direction same as positive active power flow value. 
        @param low_limit: The minimum allowable value. 
        @param relay_delay_time: The time delay from detection of abnormal conditions to relay operation. 
        @param protected_switches: Protected switches operated by this ProtectionEquipment.
        @param unit: The Unit for the Protection Equipment.
        @param conducting_equipments: Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
        """
        # The maximum allowable value. 
        self.high_limit = high_limit

        # Direction same as positive active power flow value. 
        self.power_direction_flag = power_direction_flag

        # The minimum allowable value. 
        self.low_limit = low_limit

        # The time delay from detection of abnormal conditions to relay operation. 
        self.relay_delay_time = relay_delay_time


        if protected_switches is not None:
            self.protected_switches = protected_switches
        else:
            self.protected_switches = []

        self._unit = None
        self.unit = unit

        self._conducting_equipments = []
        if conducting_equipments is not None:
            self.conducting_equipments = conducting_equipments
        else:
            self.conducting_equipments = []


        super(ProtectionEquipment, self).__init__(*args, **kw_args)
    # >>> protection_equipment

    # <<< protected_switches
    # @generated
    def add_protected_switches(self, *protected_switches):
        for obj in protected_switches:
            self.protected_switches.append(obj)

    def remove_protected_switches(self, *protected_switches):
        for obj in protected_switches:
            self.protected_switches.remove(obj)
    # >>> protected_switches

    # <<< unit
    # @generated
    def get_unit(self):
        """ The Unit for the Protection Equipment.
        """
        return self._unit

    def set_unit(self, value):
        if self._unit is not None:
            filtered = [x for x in self.unit.protection_equipments if x != self]
            self._unit._protection_equipments = filtered

        self._unit = value
        if self._unit is not None:
            self._unit._protection_equipments.append(self)

    unit = property(get_unit, set_unit)
    # >>> unit

    # <<< conducting_equipments
    # @generated
    def get_conducting_equipments(self):
        """ Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
        """
        return self._conducting_equipments

    def set_conducting_equipments(self, value):
        for p in self._conducting_equipments:
            filtered = [q for q in p.protection_equipments if q != self]
            self._conducting_equipments._protection_equipments = filtered
        for r in value:
            if self not in r._protection_equipments:
                r._protection_equipments.append(self)
        self._conducting_equipments = value

    conducting_equipments = property(get_conducting_equipments, set_conducting_equipments)

    def add_conducting_equipments(self, *conducting_equipments):
        for obj in conducting_equipments:
            if self not in obj._protection_equipments:
                obj._protection_equipments.append(self)
            self._conducting_equipments.append(obj)

    def remove_conducting_equipments(self, *conducting_equipments):
        for obj in conducting_equipments:
            if self in obj._protection_equipments:
                obj._protection_equipments.remove(self)
            self._conducting_equipments.remove(obj)
    # >>> conducting_equipments



class SynchrocheckRelay(ProtectionEquipment):
    """ A device that operates when two AC circuits are within the desired limits of frequency, phase angle, and voltage, to permit or to cause the paralleling of these two circuits. Used to prevent the paralleling of non-synchronous topological islands.
    """
    # <<< synchrocheck_relay
    # @generated
    def __init__(self, max_freq_diff=0.0, max_volt_diff=0.0, max_angle_diff=0.0, *args, **kw_args):
        """ Initialises a new 'SynchrocheckRelay' instance.

        @param max_freq_diff: The maximum allowable frequency difference across the open device 
        @param max_volt_diff: The maximum allowable difference voltage across the open device 
        @param max_angle_diff: The maximum allowable voltage vector phase angle difference across the open device 
        """
        # The maximum allowable frequency difference across the open device 
        self.max_freq_diff = max_freq_diff

        # The maximum allowable difference voltage across the open device 
        self.max_volt_diff = max_volt_diff

        # The maximum allowable voltage vector phase angle difference across the open device 
        self.max_angle_diff = max_angle_diff



        super(SynchrocheckRelay, self).__init__(*args, **kw_args)
    # >>> synchrocheck_relay



class CurrentRelay(ProtectionEquipment):
    """ A device that checks current flow values in any direction or designated direction
    """
    # <<< current_relay
    # @generated
    def __init__(self, time_delay2=0.0, current_limit2=0.0, current_limit3=0.0, inverse_time_flag=False, time_delay3=0.0, current_limit1=0.0, time_delay1=0.0, *args, **kw_args):
        """ Initialises a new 'CurrentRelay' instance.

        @param time_delay2: Inverse time delay #2 for current limit #2 
        @param current_limit2: Current limit #2 for inverse time pickup 
        @param current_limit3: Current limit #3 for inverse time pickup 
        @param inverse_time_flag: Set true if the current relay has inverse time characteristic. 
        @param time_delay3: Inverse time delay #3 for current limit #3 
        @param current_limit1: Current limit #1 for inverse time pickup 
        @param time_delay1: Inverse time delay #1 for current limit #1 
        """
        # Inverse time delay #2 for current limit #2 
        self.time_delay2 = time_delay2

        # Current limit #2 for inverse time pickup 
        self.current_limit2 = current_limit2

        # Current limit #3 for inverse time pickup 
        self.current_limit3 = current_limit3

        # Set true if the current relay has inverse time characteristic. 
        self.inverse_time_flag = inverse_time_flag

        # Inverse time delay #3 for current limit #3 
        self.time_delay3 = time_delay3

        # Current limit #1 for inverse time pickup 
        self.current_limit1 = current_limit1

        # Inverse time delay #1 for current limit #1 
        self.time_delay1 = time_delay1



        super(CurrentRelay, self).__init__(*args, **kw_args)
    # >>> current_relay



# <<< protection
# @generated
# >>> protection
