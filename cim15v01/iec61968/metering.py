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

""" This package contains only diagrams, drawn by hand from Metering-related XSDs that are in Part 9 document. Entry points into the schema are filled with green. Non-used associations are light grey.
"""

from cim15v01.iec61968.common import GeoLocation
from cim15v01.iec61968.assets import AssetFunction
from cim15v01.iec61970.meas import MeasurementValue
from cim15v01.iec61970.core import IdentifiedObject
from cim15v01.iec61968.assets import AssetContainer
from cim15v01 import Element
from cim15v01.iec61968.work import Work
from cim15v01.iec61968.common import ActivityRecord

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimMetering"

ns_uri = "http://iec.ch/TC57/CIM-generic#Metering"

class SDPLocation(GeoLocation):
    """ Location of an individual service delivery point. For residential or most businesses, it is typically the location of a meter on the customer's premises. For transmission, it is the point(s) of interconnection on the transmission provider's transmission system where capacity and/or energy transmitted by the transmission provider is made available to the receiving party. The point(s) of delivery is specified in the Service Agreement.
    """
    # <<< sdplocation
    # @generated
    def __init__(self, access_method='', site_access_problem='', remark='', occupancy_date='', service_delivery_points=None, *args, **kw_args):
        """ Initialises a new 'SDPLocation' instance.

        @param access_method: Method for the service person to access this service delivery point location. For example, a description of where to obtain a key if the facility is unmanned and secured. 
        @param site_access_problem: Problems previously encountered when visiting or performing work at this service delivery point location. Examples include: bad dog, violent customer, verbally abusive occupant, obstructions, safety hazards, etc. 
        @param remark: Remarks about this location. 
        @param occupancy_date: Date when certificate of occupancy was provided for this location, 0 if valid certificate of occupancy does not exist for (inherited) 'Location.corporateCode'. 
        @param service_delivery_points: All service delivery points at this location.
        """
        # Method for the service person to access this service delivery point location. For example, a description of where to obtain a key if the facility is unmanned and secured. 
        self.access_method = access_method

        # Problems previously encountered when visiting or performing work at this service delivery point location. Examples include: bad dog, violent customer, verbally abusive occupant, obstructions, safety hazards, etc. 
        self.site_access_problem = site_access_problem

        # Remarks about this location. 
        self.remark = remark

        # Date when certificate of occupancy was provided for this location, 0 if valid certificate of occupancy does not exist for (inherited) 'Location.corporateCode'. 
        self.occupancy_date = occupancy_date


        self._service_delivery_points = []
        if service_delivery_points is not None:
            self.service_delivery_points = service_delivery_points
        else:
            self.service_delivery_points = []


        super(SDPLocation, self).__init__(*args, **kw_args)
    # >>> sdplocation

    # <<< service_delivery_points
    # @generated
    def get_service_delivery_points(self):
        """ All service delivery points at this location.
        """
        return self._service_delivery_points

    def set_service_delivery_points(self, value):
        for p in self._service_delivery_points:
            filtered = [q for q in p.sdplocations if q != self]
            self._service_delivery_points._sdplocations = filtered
        for r in value:
            if self not in r._sdplocations:
                r._sdplocations.append(self)
        self._service_delivery_points = value

    service_delivery_points = property(get_service_delivery_points, set_service_delivery_points)

    def add_service_delivery_points(self, *service_delivery_points):
        for obj in service_delivery_points:
            if self not in obj._sdplocations:
                obj._sdplocations.append(self)
            self._service_delivery_points.append(obj)

    def remove_service_delivery_points(self, *service_delivery_points):
        for obj in service_delivery_points:
            if self in obj._sdplocations:
                obj._sdplocations.remove(self)
            self._service_delivery_points.remove(obj)
    # >>> service_delivery_points



class DeviceFunction(AssetFunction):
    """ Function performed by a device such as a meter, communication equipment, controllers, etc.
    """
    # <<< device_function
    # @generated
    def __init__(self, disabled=False, com_equipment_asset=None, end_device_asset=None, registers=None, end_device_events=None, *args, **kw_args):
        """ Initialises a new 'DeviceFunction' instance.

        @param disabled: True if the device function is disabled (deactivated). Default is false (i.e., function is enabled). 
        @param com_equipment_asset: Communication equipment asset performing this device function.
        @param end_device_asset: End device asset that performs this function.
        @param registers: All registers for quantities metered by this device function.
        @param end_device_events: All events reported by this device function.
        """
        # True if the device function is disabled (deactivated). Default is false (i.e., function is enabled). 
        self.disabled = disabled


        self._com_equipment_asset = None
        self.com_equipment_asset = com_equipment_asset

        self._end_device_asset = None
        self.end_device_asset = end_device_asset

        self._registers = []
        if registers is not None:
            self.registers = registers
        else:
            self.registers = []

        self._end_device_events = []
        if end_device_events is not None:
            self.end_device_events = end_device_events
        else:
            self.end_device_events = []


        super(DeviceFunction, self).__init__(*args, **kw_args)
    # >>> device_function

    # <<< com_equipment_asset
    # @generated
    def get_com_equipment_asset(self):
        """ Communication equipment asset performing this device function.
        """
        return self._com_equipment_asset

    def set_com_equipment_asset(self, value):
        if self._com_equipment_asset is not None:
            filtered = [x for x in self.com_equipment_asset.device_functions if x != self]
            self._com_equipment_asset._device_functions = filtered

        self._com_equipment_asset = value
        if self._com_equipment_asset is not None:
            self._com_equipment_asset._device_functions.append(self)

    com_equipment_asset = property(get_com_equipment_asset, set_com_equipment_asset)
    # >>> com_equipment_asset

    # <<< end_device_asset
    # @generated
    def get_end_device_asset(self):
        """ End device asset that performs this function.
        """
        return self._end_device_asset

    def set_end_device_asset(self, value):
        if self._end_device_asset is not None:
            filtered = [x for x in self.end_device_asset.device_functions if x != self]
            self._end_device_asset._device_functions = filtered

        self._end_device_asset = value
        if self._end_device_asset is not None:
            self._end_device_asset._device_functions.append(self)

    end_device_asset = property(get_end_device_asset, set_end_device_asset)
    # >>> end_device_asset

    # <<< registers
    # @generated
    def get_registers(self):
        """ All registers for quantities metered by this device function.
        """
        return self._registers

    def set_registers(self, value):
        for x in self._registers:
            x._device_function = None
        for y in value:
            y._device_function = self
        self._registers = value

    registers = property(get_registers, set_registers)

    def add_registers(self, *registers):
        for obj in registers:
            obj._device_function = self
            self._registers.append(obj)

    def remove_registers(self, *registers):
        for obj in registers:
            obj._device_function = None
            self._registers.remove(obj)
    # >>> registers

    # <<< end_device_events
    # @generated
    def get_end_device_events(self):
        """ All events reported by this device function.
        """
        return self._end_device_events

    def set_end_device_events(self, value):
        for x in self._end_device_events:
            x._device_function = None
        for y in value:
            y._device_function = self
        self._end_device_events = value

    end_device_events = property(get_end_device_events, set_end_device_events)

    def add_end_device_events(self, *end_device_events):
        for obj in end_device_events:
            obj._device_function = self
            self._end_device_events.append(obj)

    def remove_end_device_events(self, *end_device_events):
        for obj in end_device_events:
            obj._device_function = None
            self._end_device_events.remove(obj)
    # >>> end_device_events



class IntervalReading(MeasurementValue):
    """ Data captured at regular intervals of time. Interval data could be captured as incremental data, absolute data, or relative data. The source for the data is usually a tariff quantity or an engineering quantity. Data is typically captured in time-tagged, uniform, fixed-length intervals of 5 min, 10 min, 15 min, 30 min, or 60 min. Note: Interval Data is sometimes also called 'Interval Data Readings' (IDR).
    """
    # <<< interval_reading
    # @generated
    def __init__(self, value=0.0, interval_blocks=None, reading_qualities=None, *args, **kw_args):
        """ Initialises a new 'IntervalReading' instance.

        @param value: Value of this interval reading. 
        @param interval_blocks: All blocks containing this interval reading.
        @param reading_qualities: Used only if quality of this interval reading value is different than 'Good'.
        """
        # Value of this interval reading. 
        self.value = value


        self._interval_blocks = []
        if interval_blocks is not None:
            self.interval_blocks = interval_blocks
        else:
            self.interval_blocks = []

        self._reading_qualities = []
        if reading_qualities is not None:
            self.reading_qualities = reading_qualities
        else:
            self.reading_qualities = []


        super(IntervalReading, self).__init__(*args, **kw_args)
    # >>> interval_reading

    # <<< interval_blocks
    # @generated
    def get_interval_blocks(self):
        """ All blocks containing this interval reading.
        """
        return self._interval_blocks

    def set_interval_blocks(self, value):
        for p in self._interval_blocks:
            filtered = [q for q in p.interval_readings if q != self]
            self._interval_blocks._interval_readings = filtered
        for r in value:
            if self not in r._interval_readings:
                r._interval_readings.append(self)
        self._interval_blocks = value

    interval_blocks = property(get_interval_blocks, set_interval_blocks)

    def add_interval_blocks(self, *interval_blocks):
        for obj in interval_blocks:
            if self not in obj._interval_readings:
                obj._interval_readings.append(self)
            self._interval_blocks.append(obj)

    def remove_interval_blocks(self, *interval_blocks):
        for obj in interval_blocks:
            if self in obj._interval_readings:
                obj._interval_readings.remove(self)
            self._interval_blocks.remove(obj)
    # >>> interval_blocks

    # <<< reading_qualities
    # @generated
    def get_reading_qualities(self):
        """ Used only if quality of this interval reading value is different than 'Good'.
        """
        return self._reading_qualities

    def set_reading_qualities(self, value):
        for x in self._reading_qualities:
            x._interval_reading = None
        for y in value:
            y._interval_reading = self
        self._reading_qualities = value

    reading_qualities = property(get_reading_qualities, set_reading_qualities)

    def add_reading_qualities(self, *reading_qualities):
        for obj in reading_qualities:
            obj._interval_reading = self
            self._reading_qualities.append(obj)

    def remove_reading_qualities(self, *reading_qualities):
        for obj in reading_qualities:
            obj._interval_reading = None
            self._reading_qualities.remove(obj)
    # >>> reading_qualities



class ReadingType(IdentifiedObject):
    """ Type of data conveyed by a specific Reading.
    """
    # <<< reading_type
    # @generated
    def __init__(self, kind='power', unit='m2', multiplier='m', channel_number=0, default_quality='', dynamic_configuration='', interval_length=0.0, reverse_chronology=False, default_value_data_type='', pending=None, readings=None, interval_blocks=None, register=None, *args, **kw_args):
        """ Initialises a new 'ReadingType' instance.

        @param kind: Kind of reading. Values are: "power", "voltage_angle", "other", "energy", "phase_angle", "date", "time", "volume", "voltage", "demand", "power_factor", "frequency", "current_angle", "pressure", "current"
        @param unit: Unit for the reading value. Values are: "m2", "var", "m3", "g", "varh", "f", "hz", "deg", "w/s", "v", "v/var", "rad", "min", "ohm", "m", "h", "s", "w/hz", "kg/j", "wh", "va", "s", "none", "º_c", "s-1", "j", "n", "h", "j/s", "hz-1", "pa", "w", "a", "vah"
        @param multiplier: Multiplier for 'unit'. Values are: "m", "t", "p", "k", "m", "micro", "n", "d", "g", "c", "none"
        @param channel_number: Logical positioning of this measurement data. 
        @param default_quality: Characteristics of a data value conveyed by a specific Reading, which allow an application to understand how a specific Reading is to be interpreted. 
        @param dynamic_configuration: Demand configuration such as block, rolling, logarithmic and sizes such as 15 min, 30 min, 5 min subinterval. 
        @param interval_length: (if incremental reading value) Length of increment interval. 
        @param reverse_chronology: True for systems that must operate in 'reverse' chronological order. 
        @param default_value_data_type: Numeric type to be expected for the associated IntervalBlock.value (e.g. unsignedInteger). 
        @param pending: Pending conversion that produced this reading type.
        @param readings: All reading values with this type information.
        @param interval_blocks: All blocks containing interval reading values with this type information.
        @param register: Register displaying values with this type information.
        """
        # Kind of reading. Values are: "power", "voltage_angle", "other", "energy", "phase_angle", "date", "time", "volume", "voltage", "demand", "power_factor", "frequency", "current_angle", "pressure", "current"
        self.kind = kind

        # Unit for the reading value. Values are: "m2", "var", "m3", "g", "varh", "f", "hz", "deg", "w/s", "v", "v/var", "rad", "min", "ohm", "m", "h", "s", "w/hz", "kg/j", "wh", "va", "s", "none", "º_c", "s-1", "j", "n", "h", "j/s", "hz-1", "pa", "w", "a", "vah"
        self.unit = unit

        # Multiplier for 'unit'. Values are: "m", "t", "p", "k", "m", "micro", "n", "d", "g", "c", "none"
        self.multiplier = multiplier

        # Logical positioning of this measurement data. 
        self.channel_number = channel_number

        # Characteristics of a data value conveyed by a specific Reading, which allow an application to understand how a specific Reading is to be interpreted. 
        self.default_quality = default_quality

        # Demand configuration such as block, rolling, logarithmic and sizes such as 15 min, 30 min, 5 min subinterval. 
        self.dynamic_configuration = dynamic_configuration

        # (if incremental reading value) Length of increment interval. 
        self.interval_length = interval_length

        # True for systems that must operate in 'reverse' chronological order. 
        self.reverse_chronology = reverse_chronology

        # Numeric type to be expected for the associated IntervalBlock.value (e.g. unsignedInteger). 
        self.default_value_data_type = default_value_data_type


        self._pending = None
        self.pending = pending

        self._readings = []
        if readings is not None:
            self.readings = readings
        else:
            self.readings = []

        self._interval_blocks = []
        if interval_blocks is not None:
            self.interval_blocks = interval_blocks
        else:
            self.interval_blocks = []

        self._register = None
        self.register = register


        super(ReadingType, self).__init__(*args, **kw_args)
    # >>> reading_type

    # <<< pending
    # @generated
    def get_pending(self):
        """ Pending conversion that produced this reading type.
        """
        return self._pending

    def set_pending(self, value):
        if self._pending is not None:
            self._pending._reading_type = None

        self._pending = value
        if self._pending is not None:
            self._pending._reading_type = self

    pending = property(get_pending, set_pending)
    # >>> pending

    # <<< readings
    # @generated
    def get_readings(self):
        """ All reading values with this type information.
        """
        return self._readings

    def set_readings(self, value):
        for x in self._readings:
            x._reading_type = None
        for y in value:
            y._reading_type = self
        self._readings = value

    readings = property(get_readings, set_readings)

    def add_readings(self, *readings):
        for obj in readings:
            obj._reading_type = self
            self._readings.append(obj)

    def remove_readings(self, *readings):
        for obj in readings:
            obj._reading_type = None
            self._readings.remove(obj)
    # >>> readings

    # <<< interval_blocks
    # @generated
    def get_interval_blocks(self):
        """ All blocks containing interval reading values with this type information.
        """
        return self._interval_blocks

    def set_interval_blocks(self, value):
        for x in self._interval_blocks:
            x._reading_type = None
        for y in value:
            y._reading_type = self
        self._interval_blocks = value

    interval_blocks = property(get_interval_blocks, set_interval_blocks)

    def add_interval_blocks(self, *interval_blocks):
        for obj in interval_blocks:
            obj._reading_type = self
            self._interval_blocks.append(obj)

    def remove_interval_blocks(self, *interval_blocks):
        for obj in interval_blocks:
            obj._reading_type = None
            self._interval_blocks.remove(obj)
    # >>> interval_blocks

    # <<< register
    # @generated
    def get_register(self):
        """ Register displaying values with this type information.
        """
        return self._register

    def set_register(self, value):
        if self._register is not None:
            self._register._reading_type = None

        self._register = value
        if self._register is not None:
            self._register._reading_type = self

    register = property(get_register, set_register)
    # >>> register



class EndDeviceAsset(AssetContainer):
    """ AssetContainer that performs one or more end device functions. One type of EndDeviceAsset is a MeterAsset which can perform metering, load management, connect/disconnect, accounting functions, etc. Some EndDeviceAssets, such as ones monitoring and controlling air conditioner, refrigerator, pool pumps may be connected to a MeterAsset. All EndDeviceAssets may have communication capability defined by the associated ComFunction(s). An EndDeviceAsset may be owned by a consumer, a service provider, utility or otherwise. There may be a related end device function that identifies a sensor or control point within a metering application or communications systems (e.g., water, gas, electricity). Some devices may use an optical port that conforms to the ANSI C12.18 standard for communications.
    """
    # <<< end_device_asset
    # @generated
    def __init__(self, read_request=False, metrology=False, disconnect=False, relay_capable=False, outage_report=False, amr_system='', reverse_flow_handling=False, load_control=False, dst_enabled=False, time_zone_offset=0.0, demand_response=False, end_device_groups=None, end_device_controls=None, electrical_infos=None, readings=None, service_location=None, end_device_model=None, device_functions=None, customer=None, service_delivery_point=None, *args, **kw_args):
        """ Initialises a new 'EndDeviceAsset' instance.

        @param read_request: True if this end device asset is capable of supporting on-request reads for this end device. 
        @param metrology: True if this end device asset is capable of supporting the presentation of metered values to a user or another system (always true for a meter, but might not be true for a load control unit.) 
        @param disconnect: True if this end device asset is capable of supporting remote whole-house disconnect capability. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the ConnectDisconnectFunction contained by this end device asset. 
        @param relay_capable: True if this end device asset is capable of supporting one or more relays. The relays may be programmable in the meter and tied to TOU, time pulse, load control or other functions. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset. 
        @param outage_report: True if this end device asset is capable of supporting the means to report historical power interruption data. 
        @param amr_system: Automated meter reading (AMR) system responsible for communications to this end device. 
        @param reverse_flow_handling: True if this EndDeviceAsset is capable of supporting detection and monitoring of reverse flow. 
        @param load_control: True if this end device asset is capable of supporting load control functions through either the meter or the AMR option. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset. 
        @param dst_enabled: True if this end device asset is capable of supporting the autonomous application of daylight savings time (DST). 
        @param time_zone_offset: Time zone offset relative to GMT for the location of this end device. 
        @param demand_response: True if this end device asset is capable of supporting demand response functions. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset. 
        @param end_device_groups: All end device groups referring to this end device asset.
        @param end_device_controls: All end device controls sending commands to this end device asset.
        @param electrical_infos: All sets of electrical properties for this end device asset.
        @param readings:
        @param service_location: Service location whose service delivery is measured by this end device asset.
        @param end_device_model: Product documentation for this end device asset.
        @param device_functions: All device functions this end device asset performs.
        @param customer: Customer owning this end device asset.
        @param service_delivery_point: Service delivery point to which this end device asset belongs.
        """
        # True if this end device asset is capable of supporting on-request reads for this end device. 
        self.read_request = read_request

        # True if this end device asset is capable of supporting the presentation of metered values to a user or another system (always true for a meter, but might not be true for a load control unit.) 
        self.metrology = metrology

        # True if this end device asset is capable of supporting remote whole-house disconnect capability. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the ConnectDisconnectFunction contained by this end device asset. 
        self.disconnect = disconnect

        # True if this end device asset is capable of supporting one or more relays. The relays may be programmable in the meter and tied to TOU, time pulse, load control or other functions. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset. 
        self.relay_capable = relay_capable

        # True if this end device asset is capable of supporting the means to report historical power interruption data. 
        self.outage_report = outage_report

        # Automated meter reading (AMR) system responsible for communications to this end device. 
        self.amr_system = amr_system

        # True if this EndDeviceAsset is capable of supporting detection and monitoring of reverse flow. 
        self.reverse_flow_handling = reverse_flow_handling

        # True if this end device asset is capable of supporting load control functions through either the meter or the AMR option. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset. 
        self.load_control = load_control

        # True if this end device asset is capable of supporting the autonomous application of daylight savings time (DST). 
        self.dst_enabled = dst_enabled

        # Time zone offset relative to GMT for the location of this end device. 
        self.time_zone_offset = time_zone_offset

        # True if this end device asset is capable of supporting demand response functions. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset. 
        self.demand_response = demand_response


        self._end_device_groups = []
        if end_device_groups is not None:
            self.end_device_groups = end_device_groups
        else:
            self.end_device_groups = []

        self._end_device_controls = []
        if end_device_controls is not None:
            self.end_device_controls = end_device_controls
        else:
            self.end_device_controls = []

        self._electrical_infos = []
        if electrical_infos is not None:
            self.electrical_infos = electrical_infos
        else:
            self.electrical_infos = []

        self._readings = []
        if readings is not None:
            self.readings = readings
        else:
            self.readings = []

        self._service_location = None
        self.service_location = service_location

        self._end_device_model = None
        self.end_device_model = end_device_model

        self._device_functions = []
        if device_functions is not None:
            self.device_functions = device_functions
        else:
            self.device_functions = []

        self._customer = None
        self.customer = customer

        self._service_delivery_point = None
        self.service_delivery_point = service_delivery_point


        super(EndDeviceAsset, self).__init__(*args, **kw_args)
    # >>> end_device_asset

    # <<< end_device_groups
    # @generated
    def get_end_device_groups(self):
        """ All end device groups referring to this end device asset.
        """
        return self._end_device_groups

    def set_end_device_groups(self, value):
        for p in self._end_device_groups:
            filtered = [q for q in p.end_device_assets if q != self]
            self._end_device_groups._end_device_assets = filtered
        for r in value:
            if self not in r._end_device_assets:
                r._end_device_assets.append(self)
        self._end_device_groups = value

    end_device_groups = property(get_end_device_groups, set_end_device_groups)

    def add_end_device_groups(self, *end_device_groups):
        for obj in end_device_groups:
            if self not in obj._end_device_assets:
                obj._end_device_assets.append(self)
            self._end_device_groups.append(obj)

    def remove_end_device_groups(self, *end_device_groups):
        for obj in end_device_groups:
            if self in obj._end_device_assets:
                obj._end_device_assets.remove(self)
            self._end_device_groups.remove(obj)
    # >>> end_device_groups

    # <<< end_device_controls
    # @generated
    def get_end_device_controls(self):
        """ All end device controls sending commands to this end device asset.
        """
        return self._end_device_controls

    def set_end_device_controls(self, value):
        for x in self._end_device_controls:
            x._end_device_asset = None
        for y in value:
            y._end_device_asset = self
        self._end_device_controls = value

    end_device_controls = property(get_end_device_controls, set_end_device_controls)

    def add_end_device_controls(self, *end_device_controls):
        for obj in end_device_controls:
            obj._end_device_asset = self
            self._end_device_controls.append(obj)

    def remove_end_device_controls(self, *end_device_controls):
        for obj in end_device_controls:
            obj._end_device_asset = None
            self._end_device_controls.remove(obj)
    # >>> end_device_controls

    # <<< electrical_infos
    # @generated
    def get_electrical_infos(self):
        """ All sets of electrical properties for this end device asset.
        """
        return self._electrical_infos

    def set_electrical_infos(self, value):
        for p in self._electrical_infos:
            filtered = [q for q in p.end_device_assets if q != self]
            self._electrical_infos._end_device_assets = filtered
        for r in value:
            if self not in r._end_device_assets:
                r._end_device_assets.append(self)
        self._electrical_infos = value

    electrical_infos = property(get_electrical_infos, set_electrical_infos)

    def add_electrical_infos(self, *electrical_infos):
        for obj in electrical_infos:
            if self not in obj._end_device_assets:
                obj._end_device_assets.append(self)
            self._electrical_infos.append(obj)

    def remove_electrical_infos(self, *electrical_infos):
        for obj in electrical_infos:
            if self in obj._end_device_assets:
                obj._end_device_assets.remove(self)
            self._electrical_infos.remove(obj)
    # >>> electrical_infos

    # <<< readings
    # @generated
    def get_readings(self):
        """ 
        """
        return self._readings

    def set_readings(self, value):
        for x in self._readings:
            x._end_device_asset = None
        for y in value:
            y._end_device_asset = self
        self._readings = value

    readings = property(get_readings, set_readings)

    def add_readings(self, *readings):
        for obj in readings:
            obj._end_device_asset = self
            self._readings.append(obj)

    def remove_readings(self, *readings):
        for obj in readings:
            obj._end_device_asset = None
            self._readings.remove(obj)
    # >>> readings

    # <<< service_location
    # @generated
    def get_service_location(self):
        """ Service location whose service delivery is measured by this end device asset.
        """
        return self._service_location

    def set_service_location(self, value):
        if self._service_location is not None:
            filtered = [x for x in self.service_location.end_device_assets if x != self]
            self._service_location._end_device_assets = filtered

        self._service_location = value
        if self._service_location is not None:
            self._service_location._end_device_assets.append(self)

    service_location = property(get_service_location, set_service_location)
    # >>> service_location

    # <<< end_device_model
    # @generated
    def get_end_device_model(self):
        """ Product documentation for this end device asset.
        """
        return self._end_device_model

    def set_end_device_model(self, value):
        if self._end_device_model is not None:
            filtered = [x for x in self.end_device_model.end_device_assets if x != self]
            self._end_device_model._end_device_assets = filtered

        self._end_device_model = value
        if self._end_device_model is not None:
            self._end_device_model._end_device_assets.append(self)

    end_device_model = property(get_end_device_model, set_end_device_model)
    # >>> end_device_model

    # <<< device_functions
    # @generated
    def get_device_functions(self):
        """ All device functions this end device asset performs.
        """
        return self._device_functions

    def set_device_functions(self, value):
        for x in self._device_functions:
            x._end_device_asset = None
        for y in value:
            y._end_device_asset = self
        self._device_functions = value

    device_functions = property(get_device_functions, set_device_functions)

    def add_device_functions(self, *device_functions):
        for obj in device_functions:
            obj._end_device_asset = self
            self._device_functions.append(obj)

    def remove_device_functions(self, *device_functions):
        for obj in device_functions:
            obj._end_device_asset = None
            self._device_functions.remove(obj)
    # >>> device_functions

    # <<< customer
    # @generated
    def get_customer(self):
        """ Customer owning this end device asset.
        """
        return self._customer

    def set_customer(self, value):
        if self._customer is not None:
            filtered = [x for x in self.customer.end_device_assets if x != self]
            self._customer._end_device_assets = filtered

        self._customer = value
        if self._customer is not None:
            self._customer._end_device_assets.append(self)

    customer = property(get_customer, set_customer)
    # >>> customer

    # <<< service_delivery_point
    # @generated
    def get_service_delivery_point(self):
        """ Service delivery point to which this end device asset belongs.
        """
        return self._service_delivery_point

    def set_service_delivery_point(self, value):
        if self._service_delivery_point is not None:
            filtered = [x for x in self.service_delivery_point.end_device_assets if x != self]
            self._service_delivery_point._end_device_assets = filtered

        self._service_delivery_point = value
        if self._service_delivery_point is not None:
            self._service_delivery_point._end_device_assets.append(self)

    service_delivery_point = property(get_service_delivery_point, set_service_delivery_point)
    # >>> service_delivery_point



class Reading(MeasurementValue):
    """ Specific value measured by a meter or other asset. Each Reading is associated with a specific ReadingType.
    """
    # <<< reading
    # @generated
    def __init__(self, value=0.0, end_device_asset=None, reading_qualities=None, reading_type=None, meter_readings=None, *args, **kw_args):
        """ Initialises a new 'Reading' instance.

        @param value: Value of this reading. 
        @param end_device_asset:
        @param reading_qualities: Used only if quality of this reading value is different than 'Good'.
        @param reading_type: Type information for this reading value.
        @param meter_readings: All meter readings (sets of values) containing this reading value.
        """
        # Value of this reading. 
        self.value = value


        self._end_device_asset = None
        self.end_device_asset = end_device_asset

        self._reading_qualities = []
        if reading_qualities is not None:
            self.reading_qualities = reading_qualities
        else:
            self.reading_qualities = []

        self._reading_type = None
        self.reading_type = reading_type

        self._meter_readings = []
        if meter_readings is not None:
            self.meter_readings = meter_readings
        else:
            self.meter_readings = []


        super(Reading, self).__init__(*args, **kw_args)
    # >>> reading

    # <<< end_device_asset
    # @generated
    def get_end_device_asset(self):
        """ 
        """
        return self._end_device_asset

    def set_end_device_asset(self, value):
        if self._end_device_asset is not None:
            filtered = [x for x in self.end_device_asset.readings if x != self]
            self._end_device_asset._readings = filtered

        self._end_device_asset = value
        if self._end_device_asset is not None:
            self._end_device_asset._readings.append(self)

    end_device_asset = property(get_end_device_asset, set_end_device_asset)
    # >>> end_device_asset

    # <<< reading_qualities
    # @generated
    def get_reading_qualities(self):
        """ Used only if quality of this reading value is different than 'Good'.
        """
        return self._reading_qualities

    def set_reading_qualities(self, value):
        for x in self._reading_qualities:
            x._reading = None
        for y in value:
            y._reading = self
        self._reading_qualities = value

    reading_qualities = property(get_reading_qualities, set_reading_qualities)

    def add_reading_qualities(self, *reading_qualities):
        for obj in reading_qualities:
            obj._reading = self
            self._reading_qualities.append(obj)

    def remove_reading_qualities(self, *reading_qualities):
        for obj in reading_qualities:
            obj._reading = None
            self._reading_qualities.remove(obj)
    # >>> reading_qualities

    # <<< reading_type
    # @generated
    def get_reading_type(self):
        """ Type information for this reading value.
        """
        return self._reading_type

    def set_reading_type(self, value):
        if self._reading_type is not None:
            filtered = [x for x in self.reading_type.readings if x != self]
            self._reading_type._readings = filtered

        self._reading_type = value
        if self._reading_type is not None:
            self._reading_type._readings.append(self)

    reading_type = property(get_reading_type, set_reading_type)
    # >>> reading_type

    # <<< meter_readings
    # @generated
    def get_meter_readings(self):
        """ All meter readings (sets of values) containing this reading value.
        """
        return self._meter_readings

    def set_meter_readings(self, value):
        for p in self._meter_readings:
            filtered = [q for q in p.readings if q != self]
            self._meter_readings._readings = filtered
        for r in value:
            if self not in r._readings:
                r._readings.append(self)
        self._meter_readings = value

    meter_readings = property(get_meter_readings, set_meter_readings)

    def add_meter_readings(self, *meter_readings):
        for obj in meter_readings:
            if self not in obj._readings:
                obj._readings.append(self)
            self._meter_readings.append(obj)

    def remove_meter_readings(self, *meter_readings):
        for obj in meter_readings:
            if self in obj._readings:
                obj._readings.remove(self)
            self._meter_readings.remove(obj)
    # >>> meter_readings



class Register(IdentifiedObject):
    """ Display for quantity that is metered on an end device such as a meter.
    """
    # <<< register
    # @generated
    def __init__(self, right_digit_count=0, left_digit_count=0, reading_type=None, device_function=None, *args, **kw_args):
        """ Initialises a new 'Register' instance.

        @param right_digit_count: Number of digits (dials on a mechanical meter) to the right of the decimal place. 
        @param left_digit_count: Number of digits (dials on a mechanical meter) to the left of the decimal place; default is 5. 
        @param reading_type: Reading type for values displayed by this register.
        @param device_function: Device function metering quantities displayed by this register.
        """
        # Number of digits (dials on a mechanical meter) to the right of the decimal place. 
        self.right_digit_count = right_digit_count

        # Number of digits (dials on a mechanical meter) to the left of the decimal place; default is 5. 
        self.left_digit_count = left_digit_count


        self._reading_type = None
        self.reading_type = reading_type

        self._device_function = None
        self.device_function = device_function


        super(Register, self).__init__(*args, **kw_args)
    # >>> register

    # <<< reading_type
    # @generated
    def get_reading_type(self):
        """ Reading type for values displayed by this register.
        """
        return self._reading_type

    def set_reading_type(self, value):
        if self._reading_type is not None:
            self._reading_type._register = None

        self._reading_type = value
        if self._reading_type is not None:
            self._reading_type._register = self

    reading_type = property(get_reading_type, set_reading_type)
    # >>> reading_type

    # <<< device_function
    # @generated
    def get_device_function(self):
        """ Device function metering quantities displayed by this register.
        """
        return self._device_function

    def set_device_function(self, value):
        if self._device_function is not None:
            filtered = [x for x in self.device_function.registers if x != self]
            self._device_function._registers = filtered

        self._device_function = value
        if self._device_function is not None:
            self._device_function._registers.append(self)

    device_function = property(get_device_function, set_device_function)
    # >>> device_function



class ReadingQuality(Element):
    """ Quality of a specific reading value or interval reading value. Note that more than one Quality may be applicable to a given Reading. Typically not used unless problems or unusual conditions occur (i.e., quality for each Reading is assumed to be 'Good' unless stated otherwise in associated ReadingQuality).
    """
    # <<< reading_quality
    # @generated
    def __init__(self, quality='', reading=None, interval_reading=None, *args, **kw_args):
        """ Initialises a new 'ReadingQuality' instance.

        @param quality: Quality, to be specified if different than 'Good'. 
        @param reading: Reading value to which this quality applies.
        @param interval_reading: Interval reading value to which this quality applies.
        """
        # Quality, to be specified if different than 'Good'. 
        self.quality = quality


        self._reading = None
        self.reading = reading

        self._interval_reading = None
        self.interval_reading = interval_reading


        super(ReadingQuality, self).__init__(*args, **kw_args)
    # >>> reading_quality

    # <<< reading
    # @generated
    def get_reading(self):
        """ Reading value to which this quality applies.
        """
        return self._reading

    def set_reading(self, value):
        if self._reading is not None:
            filtered = [x for x in self.reading.reading_qualities if x != self]
            self._reading._reading_qualities = filtered

        self._reading = value
        if self._reading is not None:
            self._reading._reading_qualities.append(self)

    reading = property(get_reading, set_reading)
    # >>> reading

    # <<< interval_reading
    # @generated
    def get_interval_reading(self):
        """ Interval reading value to which this quality applies.
        """
        return self._interval_reading

    def set_interval_reading(self, value):
        if self._interval_reading is not None:
            filtered = [x for x in self.interval_reading.reading_qualities if x != self]
            self._interval_reading._reading_qualities = filtered

        self._interval_reading = value
        if self._interval_reading is not None:
            self._interval_reading._reading_qualities.append(self)

    interval_reading = property(get_interval_reading, set_interval_reading)
    # >>> interval_reading



class MeterServiceWork(Work):
    """ Work involving meters.
    """
    # <<< meter_service_work
    # @generated
    def __init__(self, meter_asset=None, old_meter_asset=None, *args, **kw_args):
        """ Initialises a new 'MeterServiceWork' instance.

        @param meter_asset: Meter asset on which this non-replacement work is performed.
        @param old_meter_asset: Old meter asset replaced by this work.
        """

        self._meter_asset = None
        self.meter_asset = meter_asset

        self._old_meter_asset = None
        self.old_meter_asset = old_meter_asset


        super(MeterServiceWork, self).__init__(*args, **kw_args)
    # >>> meter_service_work

    # <<< meter_asset
    # @generated
    def get_meter_asset(self):
        """ Meter asset on which this non-replacement work is performed.
        """
        return self._meter_asset

    def set_meter_asset(self, value):
        if self._meter_asset is not None:
            filtered = [x for x in self.meter_asset.meter_service_works if x != self]
            self._meter_asset._meter_service_works = filtered

        self._meter_asset = value
        if self._meter_asset is not None:
            self._meter_asset._meter_service_works.append(self)

    meter_asset = property(get_meter_asset, set_meter_asset)
    # >>> meter_asset

    # <<< old_meter_asset
    # @generated
    def get_old_meter_asset(self):
        """ Old meter asset replaced by this work.
        """
        return self._old_meter_asset

    def set_old_meter_asset(self, value):
        if self._old_meter_asset is not None:
            filtered = [x for x in self.old_meter_asset.meter_replacement_works if x != self]
            self._old_meter_asset._meter_replacement_works = filtered

        self._old_meter_asset = value
        if self._old_meter_asset is not None:
            self._old_meter_asset._meter_replacement_works.append(self)

    old_meter_asset = property(get_old_meter_asset, set_old_meter_asset)
    # >>> old_meter_asset



class IntervalBlock(Element):
    """ Time sequence of Readings of the same ReadingType. Contained IntervalReadings may need conversion through the application of an offset and a scalar defined in associated Pending.
    """
    # <<< interval_block
    # @generated
    def __init__(self, interval_readings=None, meter_reading=None, reading_type=None, pending=None, *args, **kw_args):
        """ Initialises a new 'IntervalBlock' instance.

        @param interval_readings: Interval reading contained in this block.
        @param meter_reading: Meter reading containing this interval block.
        @param reading_type: Type information for interval reading values contained in this block.
        @param pending: Pending conversion to apply to interval reading values contained by this block (after which the resulting reading type is different than the original because it reflects the conversion result).
        """

        self._interval_readings = []
        if interval_readings is not None:
            self.interval_readings = interval_readings
        else:
            self.interval_readings = []

        self._meter_reading = None
        self.meter_reading = meter_reading

        self._reading_type = None
        self.reading_type = reading_type

        self._pending = None
        self.pending = pending


        super(IntervalBlock, self).__init__(*args, **kw_args)
    # >>> interval_block

    # <<< interval_readings
    # @generated
    def get_interval_readings(self):
        """ Interval reading contained in this block.
        """
        return self._interval_readings

    def set_interval_readings(self, value):
        for p in self._interval_readings:
            filtered = [q for q in p.interval_blocks if q != self]
            self._interval_readings._interval_blocks = filtered
        for r in value:
            if self not in r._interval_blocks:
                r._interval_blocks.append(self)
        self._interval_readings = value

    interval_readings = property(get_interval_readings, set_interval_readings)

    def add_interval_readings(self, *interval_readings):
        for obj in interval_readings:
            if self not in obj._interval_blocks:
                obj._interval_blocks.append(self)
            self._interval_readings.append(obj)

    def remove_interval_readings(self, *interval_readings):
        for obj in interval_readings:
            if self in obj._interval_blocks:
                obj._interval_blocks.remove(self)
            self._interval_readings.remove(obj)
    # >>> interval_readings

    # <<< meter_reading
    # @generated
    def get_meter_reading(self):
        """ Meter reading containing this interval block.
        """
        return self._meter_reading

    def set_meter_reading(self, value):
        if self._meter_reading is not None:
            filtered = [x for x in self.meter_reading.interval_blocks if x != self]
            self._meter_reading._interval_blocks = filtered

        self._meter_reading = value
        if self._meter_reading is not None:
            self._meter_reading._interval_blocks.append(self)

    meter_reading = property(get_meter_reading, set_meter_reading)
    # >>> meter_reading

    # <<< reading_type
    # @generated
    def get_reading_type(self):
        """ Type information for interval reading values contained in this block.
        """
        return self._reading_type

    def set_reading_type(self, value):
        if self._reading_type is not None:
            filtered = [x for x in self.reading_type.interval_blocks if x != self]
            self._reading_type._interval_blocks = filtered

        self._reading_type = value
        if self._reading_type is not None:
            self._reading_type._interval_blocks.append(self)

    reading_type = property(get_reading_type, set_reading_type)
    # >>> reading_type

    # <<< pending
    # @generated
    def get_pending(self):
        """ Pending conversion to apply to interval reading values contained by this block (after which the resulting reading type is different than the original because it reflects the conversion result).
        """
        return self._pending

    def set_pending(self, value):
        if self._pending is not None:
            filtered = [x for x in self.pending.interval_blocks if x != self]
            self._pending._interval_blocks = filtered

        self._pending = value
        if self._pending is not None:
            self._pending._interval_blocks.append(self)

    pending = property(get_pending, set_pending)
    # >>> pending



class MeterReading(IdentifiedObject):
    """ Set of values obtained from the meter.
    """
    # <<< meter_reading
    # @generated
    def __init__(self, interval_blocks=None, customer_agreement=None, service_delivery_point=None, meter_asset=None, values_interval=None, readings=None, end_device_events=None, *args, **kw_args):
        """ Initialises a new 'MeterReading' instance.

        @param interval_blocks: All interval blocks contained in this meter reading.
        @param customer_agreement: (could be deprecated in the future) Customer agreement for this meter reading.
        @param service_delivery_point: Service delivery point from which this meter reading (set of values) has been obtained.
        @param meter_asset: Meter asset providing this meter reading.
        @param values_interval: Date and time interval of the data items contained within this meter reading.
        @param readings: All reading values contained within this meter reading.
        @param end_device_events: All end device events associated with this set of measured values.
        """

        self._interval_blocks = []
        if interval_blocks is not None:
            self.interval_blocks = interval_blocks
        else:
            self.interval_blocks = []

        self._customer_agreement = None
        self.customer_agreement = customer_agreement

        self._service_delivery_point = None
        self.service_delivery_point = service_delivery_point

        self._meter_asset = None
        self.meter_asset = meter_asset

        self.values_interval = values_interval

        self._readings = []
        if readings is not None:
            self.readings = readings
        else:
            self.readings = []

        self._end_device_events = []
        if end_device_events is not None:
            self.end_device_events = end_device_events
        else:
            self.end_device_events = []


        super(MeterReading, self).__init__(*args, **kw_args)
    # >>> meter_reading

    # <<< interval_blocks
    # @generated
    def get_interval_blocks(self):
        """ All interval blocks contained in this meter reading.
        """
        return self._interval_blocks

    def set_interval_blocks(self, value):
        for x in self._interval_blocks:
            x._meter_reading = None
        for y in value:
            y._meter_reading = self
        self._interval_blocks = value

    interval_blocks = property(get_interval_blocks, set_interval_blocks)

    def add_interval_blocks(self, *interval_blocks):
        for obj in interval_blocks:
            obj._meter_reading = self
            self._interval_blocks.append(obj)

    def remove_interval_blocks(self, *interval_blocks):
        for obj in interval_blocks:
            obj._meter_reading = None
            self._interval_blocks.remove(obj)
    # >>> interval_blocks

    # <<< customer_agreement
    # @generated
    def get_customer_agreement(self):
        """ (could be deprecated in the future) Customer agreement for this meter reading.
        """
        return self._customer_agreement

    def set_customer_agreement(self, value):
        if self._customer_agreement is not None:
            filtered = [x for x in self.customer_agreement.meter_readings if x != self]
            self._customer_agreement._meter_readings = filtered

        self._customer_agreement = value
        if self._customer_agreement is not None:
            self._customer_agreement._meter_readings.append(self)

    customer_agreement = property(get_customer_agreement, set_customer_agreement)
    # >>> customer_agreement

    # <<< service_delivery_point
    # @generated
    def get_service_delivery_point(self):
        """ Service delivery point from which this meter reading (set of values) has been obtained.
        """
        return self._service_delivery_point

    def set_service_delivery_point(self, value):
        if self._service_delivery_point is not None:
            filtered = [x for x in self.service_delivery_point.meter_readings if x != self]
            self._service_delivery_point._meter_readings = filtered

        self._service_delivery_point = value
        if self._service_delivery_point is not None:
            self._service_delivery_point._meter_readings.append(self)

    service_delivery_point = property(get_service_delivery_point, set_service_delivery_point)
    # >>> service_delivery_point

    # <<< meter_asset
    # @generated
    def get_meter_asset(self):
        """ Meter asset providing this meter reading.
        """
        return self._meter_asset

    def set_meter_asset(self, value):
        if self._meter_asset is not None:
            filtered = [x for x in self.meter_asset.meter_readings if x != self]
            self._meter_asset._meter_readings = filtered

        self._meter_asset = value
        if self._meter_asset is not None:
            self._meter_asset._meter_readings.append(self)

    meter_asset = property(get_meter_asset, set_meter_asset)
    # >>> meter_asset

    # <<< values_interval
    # @generated
    # Date and time interval of the data items contained within this meter reading.
    values_interval = None
    # >>> values_interval

    # <<< readings
    # @generated
    def get_readings(self):
        """ All reading values contained within this meter reading.
        """
        return self._readings

    def set_readings(self, value):
        for p in self._readings:
            filtered = [q for q in p.meter_readings if q != self]
            self._readings._meter_readings = filtered
        for r in value:
            if self not in r._meter_readings:
                r._meter_readings.append(self)
        self._readings = value

    readings = property(get_readings, set_readings)

    def add_readings(self, *readings):
        for obj in readings:
            if self not in obj._meter_readings:
                obj._meter_readings.append(self)
            self._readings.append(obj)

    def remove_readings(self, *readings):
        for obj in readings:
            if self in obj._meter_readings:
                obj._meter_readings.remove(self)
            self._readings.remove(obj)
    # >>> readings

    # <<< end_device_events
    # @generated
    def get_end_device_events(self):
        """ All end device events associated with this set of measured values.
        """
        return self._end_device_events

    def set_end_device_events(self, value):
        for x in self._end_device_events:
            x._meter_reading = None
        for y in value:
            y._meter_reading = self
        self._end_device_events = value

    end_device_events = property(get_end_device_events, set_end_device_events)

    def add_end_device_events(self, *end_device_events):
        for obj in end_device_events:
            obj._meter_reading = self
            self._end_device_events.append(obj)

    def remove_end_device_events(self, *end_device_events):
        for obj in end_device_events:
            obj._meter_reading = None
            self._end_device_events.remove(obj)
    # >>> end_device_events



class DemandResponseProgram(IdentifiedObject):
    """ Demand response program.
    """
    # <<< demand_response_program
    # @generated
    def __init__(self, type='', end_device_groups=None, validity_interval=None, customer_agreements=None, end_device_controls=None, *args, **kw_args):
        """ Initialises a new 'DemandResponseProgram' instance.

        @param type: Type of demand response program; examples are CPP (critical-peak pricing), RTP (real-time pricing), DLC (direct load control), DBP (demand bidding program), BIP (base interruptible program). Note that possible types change a lot and it would be impossible to enumerate them all. 
        @param end_device_groups: All groups of end devices with this demand response program.
        @param validity_interval: Interval within which the program is valid.
        @param customer_agreements: All customer agreements with this demand response program.
        @param end_device_controls: All end device controls with this demand response program.
        """
        # Type of demand response program; examples are CPP (critical-peak pricing), RTP (real-time pricing), DLC (direct load control), DBP (demand bidding program), BIP (base interruptible program). Note that possible types change a lot and it would be impossible to enumerate them all. 
        self.type = type


        self._end_device_groups = []
        if end_device_groups is not None:
            self.end_device_groups = end_device_groups
        else:
            self.end_device_groups = []

        self.validity_interval = validity_interval

        self._customer_agreements = []
        if customer_agreements is not None:
            self.customer_agreements = customer_agreements
        else:
            self.customer_agreements = []

        self._end_device_controls = []
        if end_device_controls is not None:
            self.end_device_controls = end_device_controls
        else:
            self.end_device_controls = []


        super(DemandResponseProgram, self).__init__(*args, **kw_args)
    # >>> demand_response_program

    # <<< end_device_groups
    # @generated
    def get_end_device_groups(self):
        """ All groups of end devices with this demand response program.
        """
        return self._end_device_groups

    def set_end_device_groups(self, value):
        for x in self._end_device_groups:
            x._demand_response_program = None
        for y in value:
            y._demand_response_program = self
        self._end_device_groups = value

    end_device_groups = property(get_end_device_groups, set_end_device_groups)

    def add_end_device_groups(self, *end_device_groups):
        for obj in end_device_groups:
            obj._demand_response_program = self
            self._end_device_groups.append(obj)

    def remove_end_device_groups(self, *end_device_groups):
        for obj in end_device_groups:
            obj._demand_response_program = None
            self._end_device_groups.remove(obj)
    # >>> end_device_groups

    # <<< validity_interval
    # @generated
    # Interval within which the program is valid.
    validity_interval = None
    # >>> validity_interval

    # <<< customer_agreements
    # @generated
    def get_customer_agreements(self):
        """ All customer agreements with this demand response program.
        """
        return self._customer_agreements

    def set_customer_agreements(self, value):
        for x in self._customer_agreements:
            x._demand_response_program = None
        for y in value:
            y._demand_response_program = self
        self._customer_agreements = value

    customer_agreements = property(get_customer_agreements, set_customer_agreements)

    def add_customer_agreements(self, *customer_agreements):
        for obj in customer_agreements:
            obj._demand_response_program = self
            self._customer_agreements.append(obj)

    def remove_customer_agreements(self, *customer_agreements):
        for obj in customer_agreements:
            obj._demand_response_program = None
            self._customer_agreements.remove(obj)
    # >>> customer_agreements

    # <<< end_device_controls
    # @generated
    def get_end_device_controls(self):
        """ All end device controls with this demand response program.
        """
        return self._end_device_controls

    def set_end_device_controls(self, value):
        for x in self._end_device_controls:
            x._demand_response_program = None
        for y in value:
            y._demand_response_program = self
        self._end_device_controls = value

    end_device_controls = property(get_end_device_controls, set_end_device_controls)

    def add_end_device_controls(self, *end_device_controls):
        for obj in end_device_controls:
            obj._demand_response_program = self
            self._end_device_controls.append(obj)

    def remove_end_device_controls(self, *end_device_controls):
        for obj in end_device_controls:
            obj._demand_response_program = None
            self._end_device_controls.remove(obj)
    # >>> end_device_controls



class EndDeviceEvent(ActivityRecord):
    """ Event detected by a DeviceFunction associated with EndDeviceAsset.
    """
    # <<< end_device_event
    # @generated
    def __init__(self, user_id='', device_function=None, meter_reading=None, *args, **kw_args):
        """ Initialises a new 'EndDeviceEvent' instance.

        @param user_id: (if user initiated) ID of user who initiated this end device event. 
        @param device_function: Device function that reported this end device event.
        @param meter_reading: Set of measured values to which this event applies.
        """
        # (if user initiated) ID of user who initiated this end device event. 
        self.user_id = user_id


        self._device_function = None
        self.device_function = device_function

        self._meter_reading = None
        self.meter_reading = meter_reading


        super(EndDeviceEvent, self).__init__(*args, **kw_args)
    # >>> end_device_event

    # <<< device_function
    # @generated
    def get_device_function(self):
        """ Device function that reported this end device event.
        """
        return self._device_function

    def set_device_function(self, value):
        if self._device_function is not None:
            filtered = [x for x in self.device_function.end_device_events if x != self]
            self._device_function._end_device_events = filtered

        self._device_function = value
        if self._device_function is not None:
            self._device_function._end_device_events.append(self)

    device_function = property(get_device_function, set_device_function)
    # >>> device_function

    # <<< meter_reading
    # @generated
    def get_meter_reading(self):
        """ Set of measured values to which this event applies.
        """
        return self._meter_reading

    def set_meter_reading(self, value):
        if self._meter_reading is not None:
            filtered = [x for x in self.meter_reading.end_device_events if x != self]
            self._meter_reading._end_device_events = filtered

        self._meter_reading = value
        if self._meter_reading is not None:
            self._meter_reading._end_device_events.append(self)

    meter_reading = property(get_meter_reading, set_meter_reading)
    # >>> meter_reading



class EndDeviceControl(IdentifiedObject):
    """ Instructs an EndDeviceAsset (or EndDeviceGroup) to perform a specified action.
    """
    # <<< end_device_control
    # @generated
    def __init__(self, type='', dr_program_mandatory=False, price_signal=0.0, dr_program_level=0, end_device_asset=None, scheduled_interval=None, end_device_group=None, customer_agreement=None, demand_response_program=None, *args, **kw_args):
        """ Initialises a new 'EndDeviceControl' instance.

        @param type: Type of control. 
        @param dr_program_mandatory: Whether a demand response program request is mandatory. Note: Attribute is not defined on DemandResponseProgram as it is not its inherent property (it serves to control it). 
        @param price_signal: (if applicable) Price signal used as parameter for this end device control. 
        @param dr_program_level: Level of a demand response program request, where 0=emergency. Note: Attribute is not defined on DemandResponseProgram as it is not its inherent property (it serves to control it). 
        @param end_device_asset: End device asset receiving commands from this end device control.
        @param scheduled_interval: (if control has scheduled duration) Date and time interval the control has been scheduled to execute within.
        @param end_device_group: End device group receiving commands from this end device control.
        @param customer_agreement: Could be deprecated in the future.
        @param demand_response_program: Demand response program for this end device control.
        """
        # Type of control. 
        self.type = type

        # Whether a demand response program request is mandatory. Note: Attribute is not defined on DemandResponseProgram as it is not its inherent property (it serves to control it). 
        self.dr_program_mandatory = dr_program_mandatory

        # (if applicable) Price signal used as parameter for this end device control. 
        self.price_signal = price_signal

        # Level of a demand response program request, where 0=emergency. Note: Attribute is not defined on DemandResponseProgram as it is not its inherent property (it serves to control it). 
        self.dr_program_level = dr_program_level


        self._end_device_asset = None
        self.end_device_asset = end_device_asset

        self.scheduled_interval = scheduled_interval

        self._end_device_group = None
        self.end_device_group = end_device_group

        self._customer_agreement = None
        self.customer_agreement = customer_agreement

        self._demand_response_program = None
        self.demand_response_program = demand_response_program


        super(EndDeviceControl, self).__init__(*args, **kw_args)
    # >>> end_device_control

    # <<< end_device_asset
    # @generated
    def get_end_device_asset(self):
        """ End device asset receiving commands from this end device control.
        """
        return self._end_device_asset

    def set_end_device_asset(self, value):
        if self._end_device_asset is not None:
            filtered = [x for x in self.end_device_asset.end_device_controls if x != self]
            self._end_device_asset._end_device_controls = filtered

        self._end_device_asset = value
        if self._end_device_asset is not None:
            self._end_device_asset._end_device_controls.append(self)

    end_device_asset = property(get_end_device_asset, set_end_device_asset)
    # >>> end_device_asset

    # <<< scheduled_interval
    # @generated
    # (if control has scheduled duration) Date and time interval the control has been scheduled to execute within.
    scheduled_interval = None
    # >>> scheduled_interval

    # <<< end_device_group
    # @generated
    def get_end_device_group(self):
        """ End device group receiving commands from this end device control.
        """
        return self._end_device_group

    def set_end_device_group(self, value):
        if self._end_device_group is not None:
            filtered = [x for x in self.end_device_group.end_device_controls if x != self]
            self._end_device_group._end_device_controls = filtered

        self._end_device_group = value
        if self._end_device_group is not None:
            self._end_device_group._end_device_controls.append(self)

    end_device_group = property(get_end_device_group, set_end_device_group)
    # >>> end_device_group

    # <<< customer_agreement
    # @generated
    def get_customer_agreement(self):
        """ Could be deprecated in the future.
        """
        return self._customer_agreement

    def set_customer_agreement(self, value):
        if self._customer_agreement is not None:
            filtered = [x for x in self.customer_agreement.end_device_controls if x != self]
            self._customer_agreement._end_device_controls = filtered

        self._customer_agreement = value
        if self._customer_agreement is not None:
            self._customer_agreement._end_device_controls.append(self)

    customer_agreement = property(get_customer_agreement, set_customer_agreement)
    # >>> customer_agreement

    # <<< demand_response_program
    # @generated
    def get_demand_response_program(self):
        """ Demand response program for this end device control.
        """
        return self._demand_response_program

    def set_demand_response_program(self, value):
        if self._demand_response_program is not None:
            filtered = [x for x in self.demand_response_program.end_device_controls if x != self]
            self._demand_response_program._end_device_controls = filtered

        self._demand_response_program = value
        if self._demand_response_program is not None:
            self._demand_response_program._end_device_controls.append(self)

    demand_response_program = property(get_demand_response_program, set_demand_response_program)
    # >>> demand_response_program



class ServiceDeliveryPoint(IdentifiedObject):
    """ Logical point on the network where the ownership of the service changes hands. It is one of potentially many service points within a ServiceLocation, delivering service in accordance with a CustomerAgreement. Used at the place where a meter may be installed.
    """
    # <<< service_delivery_point
    # @generated
    def __init__(self, phase_code='bc', billing_cycle='', load_mgmt='', rated_power=0.0, nominal_service_voltage=0, rated_current=0.0, estimated_load=0.0, check_billing=False, service_delivery_remark='', service_priority='', budget_bill='', grounded=False, consumption_real_energy=0.0, ctpt_reference=0, service_supplier=None, sdplocations=None, customer_agreement=None, meter_readings=None, energy_consumer=None, pricing_structures=None, service_category=None, power_quality_pricings=None, service_location=None, end_device_assets=None, *args, **kw_args):
        """ Initialises a new 'ServiceDeliveryPoint' instance.

        @param phase_code: Phase code. Number of wires and number of phases can be deduced from enumeration literal values. For example, ABCN is three-phase, four-wire. s12n (splitSecondary12N) is single-phase, three-wire. s1n and s2n are single-phase, two-wire. Values are: "bc", "ab", "b", "ac", "s2_n", "abc", "abn", "abcn", "cn", "an", "bcn", "acn", "a", "c", "n", "s12_n", "bn", "s1_n"
        @param billing_cycle: Billing cycle. 
        @param load_mgmt: Load management code. 
        @param rated_power: Power that this service delivery point is configured to deliver. 
        @param nominal_service_voltage: Nominal service voltage. 
        @param rated_current: Current that this service delivery point is configured to deliver. 
        @param estimated_load: Estimated load. 
        @param check_billing: True if as a result of an inspection or otherwise, there is a reason to suspect that a previous billing may have been performed with erroneous data. Value should be reset once this potential discrepancy has been resolved. 
        @param service_delivery_remark: Remarks about this service delivery point, for example the reason for it being rated with a non-nominal priority. 
        @param service_priority: Priority of service for this service delivery point. Note that service delivery points at the same service location can have different priorities. 
        @param budget_bill: Budget bill code. 
        @param grounded: True if grounded. 
        @param consumption_real_energy: Cumulative totalizing register of consumed service at this service delivery point over its lifetime. 
        @param ctpt_reference: (optional for medium voltage connections) Reference to the low side terminal of a CT or PT that obtain readings from a medium or high voltage point. 
        @param service_supplier: ServiceSupplier (Utility) utilising this service delivery point to deliver a service.
        @param sdplocations: All locations of this service delivery point.
        @param customer_agreement: Customer agreement regulating this service delivery point.
        @param meter_readings: All meter readings obtained from this service delivery point.
        @param energy_consumer:
        @param pricing_structures: All pricing structures applicable to this service delivery point (with prepayment meter running as a stand-alone device, with no CustomerAgreement or Customer).
        @param service_category: Service category delivered by this service delivery point.
        @param power_quality_pricings:
        @param service_location: Service location where the service delivered by this service delivery point is consumed.
        @param end_device_assets: All end device assets at this service delivery point.
        """
        # Phase code. Number of wires and number of phases can be deduced from enumeration literal values. For example, ABCN is three-phase, four-wire. s12n (splitSecondary12N) is single-phase, three-wire. s1n and s2n are single-phase, two-wire. Values are: "bc", "ab", "b", "ac", "s2_n", "abc", "abn", "abcn", "cn", "an", "bcn", "acn", "a", "c", "n", "s12_n", "bn", "s1_n"
        self.phase_code = phase_code

        # Billing cycle. 
        self.billing_cycle = billing_cycle

        # Load management code. 
        self.load_mgmt = load_mgmt

        # Power that this service delivery point is configured to deliver. 
        self.rated_power = rated_power

        # Nominal service voltage. 
        self.nominal_service_voltage = nominal_service_voltage

        # Current that this service delivery point is configured to deliver. 
        self.rated_current = rated_current

        # Estimated load. 
        self.estimated_load = estimated_load

        # True if as a result of an inspection or otherwise, there is a reason to suspect that a previous billing may have been performed with erroneous data. Value should be reset once this potential discrepancy has been resolved. 
        self.check_billing = check_billing

        # Remarks about this service delivery point, for example the reason for it being rated with a non-nominal priority. 
        self.service_delivery_remark = service_delivery_remark

        # Priority of service for this service delivery point. Note that service delivery points at the same service location can have different priorities. 
        self.service_priority = service_priority

        # Budget bill code. 
        self.budget_bill = budget_bill

        # True if grounded. 
        self.grounded = grounded

        # Cumulative totalizing register of consumed service at this service delivery point over its lifetime. 
        self.consumption_real_energy = consumption_real_energy

        # (optional for medium voltage connections) Reference to the low side terminal of a CT or PT that obtain readings from a medium or high voltage point. 
        self.ctpt_reference = ctpt_reference


        self._service_supplier = None
        self.service_supplier = service_supplier

        self._sdplocations = []
        if sdplocations is not None:
            self.sdplocations = sdplocations
        else:
            self.sdplocations = []

        self._customer_agreement = None
        self.customer_agreement = customer_agreement

        self._meter_readings = []
        if meter_readings is not None:
            self.meter_readings = meter_readings
        else:
            self.meter_readings = []

        self._energy_consumer = None
        self.energy_consumer = energy_consumer

        self._pricing_structures = []
        if pricing_structures is not None:
            self.pricing_structures = pricing_structures
        else:
            self.pricing_structures = []

        self._service_category = None
        self.service_category = service_category

        self._power_quality_pricings = []
        if power_quality_pricings is not None:
            self.power_quality_pricings = power_quality_pricings
        else:
            self.power_quality_pricings = []

        self._service_location = None
        self.service_location = service_location

        self._end_device_assets = []
        if end_device_assets is not None:
            self.end_device_assets = end_device_assets
        else:
            self.end_device_assets = []


        super(ServiceDeliveryPoint, self).__init__(*args, **kw_args)
    # >>> service_delivery_point

    # <<< service_supplier
    # @generated
    def get_service_supplier(self):
        """ ServiceSupplier (Utility) utilising this service delivery point to deliver a service.
        """
        return self._service_supplier

    def set_service_supplier(self, value):
        if self._service_supplier is not None:
            filtered = [x for x in self.service_supplier.service_delivery_points if x != self]
            self._service_supplier._service_delivery_points = filtered

        self._service_supplier = value
        if self._service_supplier is not None:
            self._service_supplier._service_delivery_points.append(self)

    service_supplier = property(get_service_supplier, set_service_supplier)
    # >>> service_supplier

    # <<< sdplocations
    # @generated
    def get_sdplocations(self):
        """ All locations of this service delivery point.
        """
        return self._sdplocations

    def set_sdplocations(self, value):
        for p in self._sdplocations:
            filtered = [q for q in p.service_delivery_points if q != self]
            self._sdplocations._service_delivery_points = filtered
        for r in value:
            if self not in r._service_delivery_points:
                r._service_delivery_points.append(self)
        self._sdplocations = value

    sdplocations = property(get_sdplocations, set_sdplocations)

    def add_sdplocations(self, *sdplocations):
        for obj in sdplocations:
            if self not in obj._service_delivery_points:
                obj._service_delivery_points.append(self)
            self._sdplocations.append(obj)

    def remove_sdplocations(self, *sdplocations):
        for obj in sdplocations:
            if self in obj._service_delivery_points:
                obj._service_delivery_points.remove(self)
            self._sdplocations.remove(obj)
    # >>> sdplocations

    # <<< customer_agreement
    # @generated
    def get_customer_agreement(self):
        """ Customer agreement regulating this service delivery point.
        """
        return self._customer_agreement

    def set_customer_agreement(self, value):
        if self._customer_agreement is not None:
            filtered = [x for x in self.customer_agreement.service_delivery_points if x != self]
            self._customer_agreement._service_delivery_points = filtered

        self._customer_agreement = value
        if self._customer_agreement is not None:
            self._customer_agreement._service_delivery_points.append(self)

    customer_agreement = property(get_customer_agreement, set_customer_agreement)
    # >>> customer_agreement

    # <<< meter_readings
    # @generated
    def get_meter_readings(self):
        """ All meter readings obtained from this service delivery point.
        """
        return self._meter_readings

    def set_meter_readings(self, value):
        for x in self._meter_readings:
            x._service_delivery_point = None
        for y in value:
            y._service_delivery_point = self
        self._meter_readings = value

    meter_readings = property(get_meter_readings, set_meter_readings)

    def add_meter_readings(self, *meter_readings):
        for obj in meter_readings:
            obj._service_delivery_point = self
            self._meter_readings.append(obj)

    def remove_meter_readings(self, *meter_readings):
        for obj in meter_readings:
            obj._service_delivery_point = None
            self._meter_readings.remove(obj)
    # >>> meter_readings

    # <<< energy_consumer
    # @generated
    def get_energy_consumer(self):
        """ 
        """
        return self._energy_consumer

    def set_energy_consumer(self, value):
        if self._energy_consumer is not None:
            filtered = [x for x in self.energy_consumer.service_delivery_points if x != self]
            self._energy_consumer._service_delivery_points = filtered

        self._energy_consumer = value
        if self._energy_consumer is not None:
            self._energy_consumer._service_delivery_points.append(self)

    energy_consumer = property(get_energy_consumer, set_energy_consumer)
    # >>> energy_consumer

    # <<< pricing_structures
    # @generated
    def get_pricing_structures(self):
        """ All pricing structures applicable to this service delivery point (with prepayment meter running as a stand-alone device, with no CustomerAgreement or Customer).
        """
        return self._pricing_structures

    def set_pricing_structures(self, value):
        for p in self._pricing_structures:
            filtered = [q for q in p.service_delivery_points if q != self]
            self._pricing_structures._service_delivery_points = filtered
        for r in value:
            if self not in r._service_delivery_points:
                r._service_delivery_points.append(self)
        self._pricing_structures = value

    pricing_structures = property(get_pricing_structures, set_pricing_structures)

    def add_pricing_structures(self, *pricing_structures):
        for obj in pricing_structures:
            if self not in obj._service_delivery_points:
                obj._service_delivery_points.append(self)
            self._pricing_structures.append(obj)

    def remove_pricing_structures(self, *pricing_structures):
        for obj in pricing_structures:
            if self in obj._service_delivery_points:
                obj._service_delivery_points.remove(self)
            self._pricing_structures.remove(obj)
    # >>> pricing_structures

    # <<< service_category
    # @generated
    def get_service_category(self):
        """ Service category delivered by this service delivery point.
        """
        return self._service_category

    def set_service_category(self, value):
        if self._service_category is not None:
            filtered = [x for x in self.service_category.service_delivery_points if x != self]
            self._service_category._service_delivery_points = filtered

        self._service_category = value
        if self._service_category is not None:
            self._service_category._service_delivery_points.append(self)

    service_category = property(get_service_category, set_service_category)
    # >>> service_category

    # <<< power_quality_pricings
    # @generated
    def get_power_quality_pricings(self):
        """ 
        """
        return self._power_quality_pricings

    def set_power_quality_pricings(self, value):
        for p in self._power_quality_pricings:
            filtered = [q for q in p.service_delivery_points if q != self]
            self._power_quality_pricings._service_delivery_points = filtered
        for r in value:
            if self not in r._service_delivery_points:
                r._service_delivery_points.append(self)
        self._power_quality_pricings = value

    power_quality_pricings = property(get_power_quality_pricings, set_power_quality_pricings)

    def add_power_quality_pricings(self, *power_quality_pricings):
        for obj in power_quality_pricings:
            if self not in obj._service_delivery_points:
                obj._service_delivery_points.append(self)
            self._power_quality_pricings.append(obj)

    def remove_power_quality_pricings(self, *power_quality_pricings):
        for obj in power_quality_pricings:
            if self in obj._service_delivery_points:
                obj._service_delivery_points.remove(self)
            self._power_quality_pricings.remove(obj)
    # >>> power_quality_pricings

    # <<< service_location
    # @generated
    def get_service_location(self):
        """ Service location where the service delivered by this service delivery point is consumed.
        """
        return self._service_location

    def set_service_location(self, value):
        if self._service_location is not None:
            filtered = [x for x in self.service_location.service_delivery_points if x != self]
            self._service_location._service_delivery_points = filtered

        self._service_location = value
        if self._service_location is not None:
            self._service_location._service_delivery_points.append(self)

    service_location = property(get_service_location, set_service_location)
    # >>> service_location

    # <<< end_device_assets
    # @generated
    def get_end_device_assets(self):
        """ All end device assets at this service delivery point.
        """
        return self._end_device_assets

    def set_end_device_assets(self, value):
        for x in self._end_device_assets:
            x._service_delivery_point = None
        for y in value:
            y._service_delivery_point = self
        self._end_device_assets = value

    end_device_assets = property(get_end_device_assets, set_end_device_assets)

    def add_end_device_assets(self, *end_device_assets):
        for obj in end_device_assets:
            obj._service_delivery_point = self
            self._end_device_assets.append(obj)

    def remove_end_device_assets(self, *end_device_assets):
        for obj in end_device_assets:
            obj._service_delivery_point = None
            self._end_device_assets.remove(obj)
    # >>> end_device_assets



class EndDeviceGroup(IdentifiedObject):
    """ Abstraction for management of group communications within a two-way AMR system or the data for a group of related meters. Commands can be issued to all of the meters that belong to a meter group using a defined group address and the underlying AMR communication infrastructure.
    """
    # <<< end_device_group
    # @generated
    def __init__(self, group_address=0, demand_response_program=None, end_device_assets=None, end_device_controls=None, *args, **kw_args):
        """ Initialises a new 'EndDeviceGroup' instance.

        @param group_address: Address of this end device group. 
        @param demand_response_program: Demand response program for this group of end devices.
        @param end_device_assets: All end device assets this end device group refers to.
        @param end_device_controls: All end device controls sending commands to this end device group.
        """
        # Address of this end device group. 
        self.group_address = group_address


        self._demand_response_program = None
        self.demand_response_program = demand_response_program

        self._end_device_assets = []
        if end_device_assets is not None:
            self.end_device_assets = end_device_assets
        else:
            self.end_device_assets = []

        self._end_device_controls = []
        if end_device_controls is not None:
            self.end_device_controls = end_device_controls
        else:
            self.end_device_controls = []


        super(EndDeviceGroup, self).__init__(*args, **kw_args)
    # >>> end_device_group

    # <<< demand_response_program
    # @generated
    def get_demand_response_program(self):
        """ Demand response program for this group of end devices.
        """
        return self._demand_response_program

    def set_demand_response_program(self, value):
        if self._demand_response_program is not None:
            filtered = [x for x in self.demand_response_program.end_device_groups if x != self]
            self._demand_response_program._end_device_groups = filtered

        self._demand_response_program = value
        if self._demand_response_program is not None:
            self._demand_response_program._end_device_groups.append(self)

    demand_response_program = property(get_demand_response_program, set_demand_response_program)
    # >>> demand_response_program

    # <<< end_device_assets
    # @generated
    def get_end_device_assets(self):
        """ All end device assets this end device group refers to.
        """
        return self._end_device_assets

    def set_end_device_assets(self, value):
        for p in self._end_device_assets:
            filtered = [q for q in p.end_device_groups if q != self]
            self._end_device_assets._end_device_groups = filtered
        for r in value:
            if self not in r._end_device_groups:
                r._end_device_groups.append(self)
        self._end_device_assets = value

    end_device_assets = property(get_end_device_assets, set_end_device_assets)

    def add_end_device_assets(self, *end_device_assets):
        for obj in end_device_assets:
            if self not in obj._end_device_groups:
                obj._end_device_groups.append(self)
            self._end_device_assets.append(obj)

    def remove_end_device_assets(self, *end_device_assets):
        for obj in end_device_assets:
            if self in obj._end_device_groups:
                obj._end_device_groups.remove(self)
            self._end_device_assets.remove(obj)
    # >>> end_device_assets

    # <<< end_device_controls
    # @generated
    def get_end_device_controls(self):
        """ All end device controls sending commands to this end device group.
        """
        return self._end_device_controls

    def set_end_device_controls(self, value):
        for x in self._end_device_controls:
            x._end_device_group = None
        for y in value:
            y._end_device_group = self
        self._end_device_controls = value

    end_device_controls = property(get_end_device_controls, set_end_device_controls)

    def add_end_device_controls(self, *end_device_controls):
        for obj in end_device_controls:
            obj._end_device_group = self
            self._end_device_controls.append(obj)

    def remove_end_device_controls(self, *end_device_controls):
        for obj in end_device_controls:
            obj._end_device_group = None
            self._end_device_controls.remove(obj)
    # >>> end_device_controls



class Pending(Element):
    """ When present, a scalar conversion that is associated with IntervalBlock and which needs to be applied to every contained IntervalReading value. This conversion results in a new associated ReadingType, reflecting the true dimensions of interval reading values after the conversion.
    """
    # <<< pending
    # @generated
    def __init__(self, offset=0, scalar_numerator=0, scalar_float=0.0, scalar_denominator=0, multiply_before_add=False, reading_type=None, interval_blocks=None, *args, **kw_args):
        """ Initialises a new 'Pending' instance.

        @param offset: (if applicable) Offset to be added as well as multiplication using scalars. 
        @param scalar_numerator: (if scalar is integer or rational number)  When the scalar is a simple integer, and this attribute is presented alone and multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'. It is never used in conjunction with 'scalarFloat', only with 'scalarDenominator'. 
        @param scalar_float: (if scalar is floating number) When multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'. 
        @param scalar_denominator: (if scalar is rational number) When 'IntervalReading.value' is multiplied by this attribute and divided by 'scalarDenominator, it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'. 
        @param multiply_before_add: Whether scalars should be applied before adding the 'offset'. 
        @param reading_type: Reading type resulting from this pending conversion.
        @param interval_blocks: All blocks of interval reading values to which this pending conversion applies.
        """
        # (if applicable) Offset to be added as well as multiplication using scalars. 
        self.offset = offset

        # (if scalar is integer or rational number)  When the scalar is a simple integer, and this attribute is presented alone and multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'. It is never used in conjunction with 'scalarFloat', only with 'scalarDenominator'. 
        self.scalar_numerator = scalar_numerator

        # (if scalar is floating number) When multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'. 
        self.scalar_float = scalar_float

        # (if scalar is rational number) When 'IntervalReading.value' is multiplied by this attribute and divided by 'scalarDenominator, it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'. 
        self.scalar_denominator = scalar_denominator

        # Whether scalars should be applied before adding the 'offset'. 
        self.multiply_before_add = multiply_before_add


        self._reading_type = None
        self.reading_type = reading_type

        self._interval_blocks = []
        if interval_blocks is not None:
            self.interval_blocks = interval_blocks
        else:
            self.interval_blocks = []


        super(Pending, self).__init__(*args, **kw_args)
    # >>> pending

    # <<< reading_type
    # @generated
    def get_reading_type(self):
        """ Reading type resulting from this pending conversion.
        """
        return self._reading_type

    def set_reading_type(self, value):
        if self._reading_type is not None:
            self._reading_type._pending = None

        self._reading_type = value
        if self._reading_type is not None:
            self._reading_type._pending = self

    reading_type = property(get_reading_type, set_reading_type)
    # >>> reading_type

    # <<< interval_blocks
    # @generated
    def get_interval_blocks(self):
        """ All blocks of interval reading values to which this pending conversion applies.
        """
        return self._interval_blocks

    def set_interval_blocks(self, value):
        for x in self._interval_blocks:
            x._pending = None
        for y in value:
            y._pending = self
        self._interval_blocks = value

    interval_blocks = property(get_interval_blocks, set_interval_blocks)

    def add_interval_blocks(self, *interval_blocks):
        for obj in interval_blocks:
            obj._pending = self
            self._interval_blocks.append(obj)

    def remove_interval_blocks(self, *interval_blocks):
        for obj in interval_blocks:
            obj._pending = None
            self._interval_blocks.remove(obj)
    # >>> interval_blocks



class ComFunction(DeviceFunction):
    """ Communication function of communication equipment or a device such as a meter.
    """
    # <<< com_function
    # @generated
    def __init__(self, two_way=False, amr_address='', amr_router='', *args, **kw_args):
        """ Initialises a new 'ComFunction' instance.

        @param two_way: True when the AMR module can both send and receive messages. Default is false (i.e., module can only send). 
        @param amr_address: Communication ID number (e.g. serial number, IP address, telephone number, etc.) of the AMR module which serves this meter. 
        @param amr_router: Communication ID number (e.g. port number, serial number, data collector ID, etc.) of the parent device associated to this AMR module. Note: If someone swaps out a meter, they may inadvertently disrupt the AMR system. Some technologies route readings from nearby meters through a common collection point on an electricity meter. Removal of such a meter disrupts AMR for numerous nearby meters. 
        """
        # True when the AMR module can both send and receive messages. Default is false (i.e., module can only send). 
        self.two_way = two_way

        # Communication ID number (e.g. serial number, IP address, telephone number, etc.) of the AMR module which serves this meter. 
        self.amr_address = amr_address

        # Communication ID number (e.g. port number, serial number, data collector ID, etc.) of the parent device associated to this AMR module. Note: If someone swaps out a meter, they may inadvertently disrupt the AMR system. Some technologies route readings from nearby meters through a common collection point on an electricity meter. Removal of such a meter disrupts AMR for numerous nearby meters. 
        self.amr_router = amr_router



        super(ComFunction, self).__init__(*args, **kw_args)
    # >>> com_function



class MeterAsset(EndDeviceAsset):
    """ Physical asset that performs the metering role of the ServiceDeliveryPoint. Used for measuring consumption and detection of events.
    """
    # <<< meter_asset
    # @generated
    def __init__(self, form_number='', k_h=0.0, k_r=0.0, meter_readings=None, vending_transactions=None, meter_service_works=None, meter_replacement_works=None, meter_asset_model=None, *args, **kw_args):
        """ Initialises a new 'MeterAsset' instance.

        @param form_number: Meter form designation per ANSI C12.10 or other applicable standard. An alphanumeric designation denoting the circuit arrangement for which the meter is applicable and its specific terminal arrangement. 
        @param k_h: Meter kh (watthour) constant. It is the number of watthours that must be applied to the meter to cause one disk revolution for an electromechanical meter or the number of watthours represented by one increment pulse for an electronic meter. 
        @param k_r: Display multiplier used to produce a displayed value from a register value. 
        @param meter_readings: All meter readings provided by this meter asset.
        @param vending_transactions: All vending transactions on this meter asset.
        @param meter_service_works: All non-replacement works on this meter asset.
        @param meter_replacement_works: All works on replacement of this old meter asset.
        @param meter_asset_model:
        """
        # Meter form designation per ANSI C12.10 or other applicable standard. An alphanumeric designation denoting the circuit arrangement for which the meter is applicable and its specific terminal arrangement. 
        self.form_number = form_number

        # Meter kh (watthour) constant. It is the number of watthours that must be applied to the meter to cause one disk revolution for an electromechanical meter or the number of watthours represented by one increment pulse for an electronic meter. 
        self.k_h = k_h

        # Display multiplier used to produce a displayed value from a register value. 
        self.k_r = k_r


        self._meter_readings = []
        if meter_readings is not None:
            self.meter_readings = meter_readings
        else:
            self.meter_readings = []

        self._vending_transactions = []
        if vending_transactions is not None:
            self.vending_transactions = vending_transactions
        else:
            self.vending_transactions = []

        self._meter_service_works = []
        if meter_service_works is not None:
            self.meter_service_works = meter_service_works
        else:
            self.meter_service_works = []

        self._meter_replacement_works = []
        if meter_replacement_works is not None:
            self.meter_replacement_works = meter_replacement_works
        else:
            self.meter_replacement_works = []

        self._meter_asset_model = None
        self.meter_asset_model = meter_asset_model


        super(MeterAsset, self).__init__(*args, **kw_args)
    # >>> meter_asset

    # <<< meter_readings
    # @generated
    def get_meter_readings(self):
        """ All meter readings provided by this meter asset.
        """
        return self._meter_readings

    def set_meter_readings(self, value):
        for x in self._meter_readings:
            x._meter_asset = None
        for y in value:
            y._meter_asset = self
        self._meter_readings = value

    meter_readings = property(get_meter_readings, set_meter_readings)

    def add_meter_readings(self, *meter_readings):
        for obj in meter_readings:
            obj._meter_asset = self
            self._meter_readings.append(obj)

    def remove_meter_readings(self, *meter_readings):
        for obj in meter_readings:
            obj._meter_asset = None
            self._meter_readings.remove(obj)
    # >>> meter_readings

    # <<< vending_transactions
    # @generated
    def get_vending_transactions(self):
        """ All vending transactions on this meter asset.
        """
        return self._vending_transactions

    def set_vending_transactions(self, value):
        for x in self._vending_transactions:
            x._meter_asset = None
        for y in value:
            y._meter_asset = self
        self._vending_transactions = value

    vending_transactions = property(get_vending_transactions, set_vending_transactions)

    def add_vending_transactions(self, *vending_transactions):
        for obj in vending_transactions:
            obj._meter_asset = self
            self._vending_transactions.append(obj)

    def remove_vending_transactions(self, *vending_transactions):
        for obj in vending_transactions:
            obj._meter_asset = None
            self._vending_transactions.remove(obj)
    # >>> vending_transactions

    # <<< meter_service_works
    # @generated
    def get_meter_service_works(self):
        """ All non-replacement works on this meter asset.
        """
        return self._meter_service_works

    def set_meter_service_works(self, value):
        for x in self._meter_service_works:
            x._meter_asset = None
        for y in value:
            y._meter_asset = self
        self._meter_service_works = value

    meter_service_works = property(get_meter_service_works, set_meter_service_works)

    def add_meter_service_works(self, *meter_service_works):
        for obj in meter_service_works:
            obj._meter_asset = self
            self._meter_service_works.append(obj)

    def remove_meter_service_works(self, *meter_service_works):
        for obj in meter_service_works:
            obj._meter_asset = None
            self._meter_service_works.remove(obj)
    # >>> meter_service_works

    # <<< meter_replacement_works
    # @generated
    def get_meter_replacement_works(self):
        """ All works on replacement of this old meter asset.
        """
        return self._meter_replacement_works

    def set_meter_replacement_works(self, value):
        for x in self._meter_replacement_works:
            x._old_meter_asset = None
        for y in value:
            y._old_meter_asset = self
        self._meter_replacement_works = value

    meter_replacement_works = property(get_meter_replacement_works, set_meter_replacement_works)

    def add_meter_replacement_works(self, *meter_replacement_works):
        for obj in meter_replacement_works:
            obj._old_meter_asset = self
            self._meter_replacement_works.append(obj)

    def remove_meter_replacement_works(self, *meter_replacement_works):
        for obj in meter_replacement_works:
            obj._old_meter_asset = None
            self._meter_replacement_works.remove(obj)
    # >>> meter_replacement_works

    # <<< meter_asset_model
    # @generated
    def get_meter_asset_model(self):
        """ 
        """
        return self._meter_asset_model

    def set_meter_asset_model(self, value):
        if self._meter_asset_model is not None:
            filtered = [x for x in self.meter_asset_model.meter_assets if x != self]
            self._meter_asset_model._meter_assets = filtered

        self._meter_asset_model = value
        if self._meter_asset_model is not None:
            self._meter_asset_model._meter_assets.append(self)

    meter_asset_model = property(get_meter_asset_model, set_meter_asset_model)
    # >>> meter_asset_model



class ElectricMeteringFunction(DeviceFunction):
    """ Functionality performed by an electric meter.
    """
    # <<< electric_metering_function
    # @generated
    def __init__(self, k_wmultiplier=0, billing_multiplier=0.0, billing_multiplier_applied=False, transformer_ctratio=0.0, demand_multiplier=0.0, transformer_ratios_applied=False, transformer_vtratio=0.0, demand_multiplier_applied=False, current_rating=0.0, k_wh_multiplier=0, voltage_rating=0.0, metering_function_configuration=None, *args, **kw_args):
        """ Initialises a new 'ElectricMeteringFunction' instance.

        @param k_wmultiplier: Meter kW (pulse) multiplier, used as a multiplier for a meter register reading to determine the actual amount of usage for which to bill a customer. 
        @param billing_multiplier: Customer billing value = meter multiplier * transformer ratios * reading value. The multiplier identifies the scaling value to apply to the reported value after delivery of the tagged item. 
        @param billing_multiplier_applied: True if the billingMultiplier ratio has already been applied to the associated quantities. 
        @param transformer_ctratio: Current transformer ratio used to convert associated quantities to real measurements. 
        @param demand_multiplier: An additional multiplier that may be used for normalization of the demand value to an hourly value. For example, if the demand interval were set to 15 min, the demand multiplier would be 4. If the meter design is such that the demand value reported and displayed is compensated for by the meter itself and no additional scaling is required outside of the meter, the value of the demand multiplier should be '1'. 
        @param transformer_ratios_applied: True if transformer ratios have been already applied to the associated quantities. 
        @param transformer_vtratio: Voltage transformer ratio used to convert associated quantities to real measurements. 
        @param demand_multiplier_applied: True if the demandMultiplier ratio has already been applied to the associated quantities. 
        @param current_rating: The current class of the meter. Typical current classes in North America are 10 A, 20 A, 100 A, 200 A, or 320 A. 
        @param k_wh_multiplier: Meter kWh multiplier, used as a multiplier for a meter register reading to determine the actual amount of usage for which to bill a customer. 
        @param voltage_rating: The service voltage at which the meter is designed to operate. Typical voltage ratings in North America are 120 V, 240 V, 277 V or 480 V. 
        @param metering_function_configuration: Configuration for this electric metering function.
        """
        # Meter kW (pulse) multiplier, used as a multiplier for a meter register reading to determine the actual amount of usage for which to bill a customer. 
        self.k_wmultiplier = k_wmultiplier

        # Customer billing value = meter multiplier * transformer ratios * reading value. The multiplier identifies the scaling value to apply to the reported value after delivery of the tagged item. 
        self.billing_multiplier = billing_multiplier

        # True if the billingMultiplier ratio has already been applied to the associated quantities. 
        self.billing_multiplier_applied = billing_multiplier_applied

        # Current transformer ratio used to convert associated quantities to real measurements. 
        self.transformer_ctratio = transformer_ctratio

        # An additional multiplier that may be used for normalization of the demand value to an hourly value. For example, if the demand interval were set to 15 min, the demand multiplier would be 4. If the meter design is such that the demand value reported and displayed is compensated for by the meter itself and no additional scaling is required outside of the meter, the value of the demand multiplier should be '1'. 
        self.demand_multiplier = demand_multiplier

        # True if transformer ratios have been already applied to the associated quantities. 
        self.transformer_ratios_applied = transformer_ratios_applied

        # Voltage transformer ratio used to convert associated quantities to real measurements. 
        self.transformer_vtratio = transformer_vtratio

        # True if the demandMultiplier ratio has already been applied to the associated quantities. 
        self.demand_multiplier_applied = demand_multiplier_applied

        # The current class of the meter. Typical current classes in North America are 10 A, 20 A, 100 A, 200 A, or 320 A. 
        self.current_rating = current_rating

        # Meter kWh multiplier, used as a multiplier for a meter register reading to determine the actual amount of usage for which to bill a customer. 
        self.k_wh_multiplier = k_wh_multiplier

        # The service voltage at which the meter is designed to operate. Typical voltage ratings in North America are 120 V, 240 V, 277 V or 480 V. 
        self.voltage_rating = voltage_rating


        self._metering_function_configuration = None
        self.metering_function_configuration = metering_function_configuration


        super(ElectricMeteringFunction, self).__init__(*args, **kw_args)
    # >>> electric_metering_function

    # <<< metering_function_configuration
    # @generated
    def get_metering_function_configuration(self):
        """ Configuration for this electric metering function.
        """
        return self._metering_function_configuration

    def set_metering_function_configuration(self, value):
        if self._metering_function_configuration is not None:
            filtered = [x for x in self.metering_function_configuration.electric_metering_functions if x != self]
            self._metering_function_configuration._electric_metering_functions = filtered

        self._metering_function_configuration = value
        if self._metering_function_configuration is not None:
            self._metering_function_configuration._electric_metering_functions.append(self)

    metering_function_configuration = property(get_metering_function_configuration, set_metering_function_configuration)
    # >>> metering_function_configuration



# <<< metering
# @generated
# >>> metering
