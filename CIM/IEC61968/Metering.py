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

""" This package contains only diagrams, drawn by hand from Metering-related XSDs that are in Part 9 document. Entry points into the schema are filled with green. Non-used associations are light grey.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.IEC61968.Common import Location
from CIM.IEC61968.Assets import AssetFunction
from CIM.IEC61970.Meas import MeasurementValue
from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61968.Assets import AssetContainer
from CIM import Element
from CIM.IEC61968.Work import Work
from CIM.IEC61968.Common import ActivityRecord
from CIM.IEC61970.Domain import AbsoluteDate
from CIM.IEC61970.Domain import UnitSymbol
from CIM.IEC61970.Domain import UnitMultiplier
from CIM.IEC61970.Domain import Seconds
from CIM.IEC61970.Domain import Minutes
from CIM.IEC61970.Domain import CurrentFlow
from CIM.IEC61970.Domain import Voltage
from CIM.IEC61970.Domain import FloatQuantity
from CIM.IEC61970.Domain import ActivePower
from CIM.IEC61970.Domain import RealEnergy



from enthought.traits.api import Instance, List, Property, Enum, Str, Bool, Float, Int
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------

# Kind of reading.
ReadingKind = Enum("power", "voltageAngle", "other", "energy", "phaseAngle", "date", "time", "volume", "voltage", "demand", "powerFactor", "currentAngle", "pressure", "current", desc="Kind of reading.")
# Kind of phase configuration. Note that there is an enum Wires::WindingConnection with values {D, Y, Z, Yn, Zn}. However, there are many more phase configurations than delta (threePhaseThreeWire) and  wye (threePhaseFourWire), which are defined here.
PhaseConfigurationKind = Enum("other", "twoPhaseTwoWire", "threePhaseTwoWire", "threePhaseFourWire", "twoPhaseThreeWire", "threePhaseThreeWire", "onePhaseThreeWire", "onePhaseTwoWire", desc="Kind of phase configuration. Note that there is an enum Wires::WindingConnection with values {D, Y, Z, Yn, Zn}. However, there are many more phase configurations than delta (threePhaseThreeWire) and  wye (threePhaseFourWire), which are defined here.")

#------------------------------------------------------------------------------
#  "SDPLocation" class:
#------------------------------------------------------------------------------

class SDPLocation(Location):
    """ Location of an individual service delivery point. For residential or most businesses, it is typically the location of a meter on the customer's premises. For transmission, it is the point(s) of interconnection on the transmission provider's transmission system where capacity and/or energy transmitted by the transmission provider is made available to the receiving party. The point(s) of delivery is specified in the Service Agreement.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All service delivery points at this location.
    ServiceDeliveryPoints = List(Instance("CIM.IEC61968.Metering.ServiceDeliveryPoint"),
        desc="All service delivery points at this location.")

    # Method for the service person to access this service delivery point location. For example, a description of where to obtain a key if the facility is unmanned and secured.
    accessMethod = Str(desc="Method for the service person to access this service delivery point location. For example, a description of where to obtain a key if the facility is unmanned and secured.")

    # Problems previously encountered when visiting or performing work at this service delivery point location. Examples include: bad dog, violent customer, verbally abusive occupant, obstructions, safety hazards, etc.
    siteAccessProblem = Str(desc="Problems previously encountered when visiting or performing work at this service delivery point location. Examples include: bad dog, violent customer, verbally abusive occupant, obstructions, safety hazards, etc.")

    # Remarks about this location.
    remark = Str(desc="Remarks about this location.")

    # Date when certificate of occupancy was provided for this location, 0 if valid certificate of occupancy does not exist for (inherited) 'Location.corporateCode'.
    occupancyDate = AbsoluteDate(desc="Date when certificate of occupancy was provided for this location, 0 if valid certificate of occupancy does not exist for (inherited) 'Location.corporateCode'.")

    #--------------------------------------------------------------------------
    #  Begin "SDPLocation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "corporateCode", "direction", "isPolygon", "category", "geoInfoReference", "accessMethod", "siteAccessProblem", "remark", "occupancyDate",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "DocumentRoles", "ErpPersonRoles", "ElectronicAddresses", "ChangeItems", "Routes", "PositionPoints", "GmlSelectors", "mainAddress", "FromLocationRoles", "status", "ToLocationRoles", "TelephoneNumbers", "secondaryAddress", "LandProperties", "Measurements", "ErpOrganisationRoles", "DimensionsInfo", "AssetRoles", "Crews", "RedLines", "GmlObservatins", "Hazards", "ActivityRecords", "ServiceDeliveryPoints",
                label="References", columns=2),
            dock="tab"),
        id="CIM.IEC61968.Metering.SDPLocation",
        title="SDPLocation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SDPLocation" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DeviceFunction" class:
#------------------------------------------------------------------------------

class DeviceFunction(AssetFunction):
    """ Function performed by a device such as a meter, communication equipment, controllers, etc.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Communication equipment asset performing this device function.
    ComEquipmentAsset = Instance("CIM.IEC61968.Informative.InfAssets.ComEquipmentAsset",
        desc="Communication equipment asset performing this device function.",
        transient=True,
        opposite="DeviceFunctions",
        editor=InstanceEditor(name="_comequipmentassets"))

    def _get_comequipmentassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssets.ComEquipmentAsset" ]
        else:
            return []

    _comequipmentassets = Property(fget=_get_comequipmentassets)

    # End device asset that performs this function.
    EndDeviceAsset = Instance("CIM.IEC61968.Metering.EndDeviceAsset",
        desc="End device asset that performs this function.",
        transient=True,
        opposite="DeviceFunctions",
        editor=InstanceEditor(name="_enddeviceassets"))

    def _get_enddeviceassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.EndDeviceAsset" ]
        else:
            return []

    _enddeviceassets = Property(fget=_get_enddeviceassets)

    # All registers for quantities metered by this device function.
    Registers = List(Instance("CIM.IEC61968.Metering.Register"),
        desc="All registers for quantities metered by this device function.")

    # All events reported by this device function.
    EndDeviceEvents = List(Instance("CIM.IEC61968.Metering.EndDeviceEvent"),
        desc="All events reported by this device function.")

    # True if the device function is disabled (deactivated). Default is false (i.e., function is enabled).
    disabled = Bool(desc="True if the device function is disabled (deactivated). Default is false (i.e., function is enabled).")

    #--------------------------------------------------------------------------
    #  Begin "DeviceFunction" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "hardwareID", "configID", "programID", "password", "firmwareID", "disabled",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "Asset", "AssetFunctionAssetModel", "ComEquipmentAsset", "EndDeviceAsset", "Registers", "EndDeviceEvents",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Metering.DeviceFunction",
        title="DeviceFunction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DeviceFunction" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "IntervalReading" class:
#------------------------------------------------------------------------------

class IntervalReading(MeasurementValue):
    """ Data captured at regular intervals of time. Interval data could be captured as incremental data, absolute data, or relative data. The source for the data is usually a tariff quantity or an engineering quantity. Data is typically captured in time-tagged, uniform, fixed-length intervals of 5 min, 10 min, 15 min, 30 min, or 60 min. Note: Interval Data is sometimes also called 'Interval Data Readings' (IDR).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All blocks containing this interval reading.
    IntervalBlocks = List(Instance("CIM.IEC61968.Metering.IntervalBlock"),
        desc="All blocks containing this interval reading.")

    # Used only if quality of this interval reading value is different than 'Good'.
    ReadingQualities = List(Instance("CIM.IEC61968.Metering.ReadingQuality"),
        desc="Used only if quality of this interval reading value is different than 'Good'.")

    # Value of this interval reading.
    value = Float(desc="Value of this interval reading.")

    #--------------------------------------------------------------------------
    #  Begin "IntervalReading" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "sensorAccuracy", "timeStamp", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlValues", "MeasurementValueSource", "ErpPerson", "ProcedureDataSets", "RemoteSource", "MeasurementValueQuality", "IntervalBlocks", "ReadingQualities",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Metering.IntervalReading",
        title="IntervalReading",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IntervalReading" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ReadingType" class:
#------------------------------------------------------------------------------

class ReadingType(IdentifiedObject):
    """ Type of data conveyed by a specific Reading.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Pending conversion that produced this reading type.
    Pending = Instance("CIM.IEC61968.Metering.Pending",
        desc="Pending conversion that produced this reading type.",
        transient=True,
        opposite="ReadingType",
        editor=InstanceEditor(name="_pendings"))

    def _get_pendings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.Pending" ]
        else:
            return []

    _pendings = Property(fget=_get_pendings)

    # All reading values with this type information.
    Readings = List(Instance("CIM.IEC61968.Metering.Reading"),
        desc="All reading values with this type information.")

    # All blocks containing interval reading values with this type information.
    IntervalBlocks = List(Instance("CIM.IEC61968.Metering.IntervalBlock"),
        desc="All blocks containing interval reading values with this type information.")

    # Register displaying values with this type information.
    Register = Instance("CIM.IEC61968.Metering.Register",
        desc="Register displaying values with this type information.",
        transient=True,
        opposite="ReadingType",
        editor=InstanceEditor(name="_registers"))

    def _get_registers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.Register" ]
        else:
            return []

    _registers = Property(fget=_get_registers)

    # Kind of reading.
    kind = ReadingKind(desc="Kind of reading.")

    # Unit for the reading value.
    unit = UnitSymbol(desc="Unit for the reading value.")

    # Multiplier for 'unit'.
    multiplier = UnitMultiplier(desc="Multiplier for 'unit'.")

    # Logical positioning of this measurement data.
    channelNumber = Int(desc="Logical positioning of this measurement data.")

    # Characteristics of a data value conveyed by a specific Reading, which allow an application to understand how a specific Reading is to be interpreted.
    defaultQuality = Str(desc="Characteristics of a data value conveyed by a specific Reading, which allow an application to understand how a specific Reading is to be interpreted.")

    # Demand configuration such as block, rolling, logarithmic and sizes such as 15 min, 30 min, 5 min subinterval.
    dynamicConfiguration = Str(desc="Demand configuration such as block, rolling, logarithmic and sizes such as 15 min, 30 min, 5 min subinterval.")

    # (if incremental reading value) Length of increment interval.
    intervalLength = Seconds(desc="(if incremental reading value) Length of increment interval.")

    # True for systems that must operate in 'reverse' chronological order.
    reverseChronology = Bool(desc="True for systems that must operate in 'reverse' chronological order.")

    # Numeric type to be expected for the associated IntervalBlock.value (e.g. unsignedInteger).
    defaultValueDataType = Str(desc="Numeric type to be expected for the associated IntervalBlock.value (e.g. unsignedInteger).")

    #--------------------------------------------------------------------------
    #  Begin "ReadingType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "kind", "unit", "multiplier", "channelNumber", "defaultQuality", "dynamicConfiguration", "intervalLength", "reverseChronology", "defaultValueDataType",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "Pending", "Readings", "IntervalBlocks", "Register",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Metering.ReadingType",
        title="ReadingType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ReadingType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EndDeviceAsset" class:
#------------------------------------------------------------------------------

class EndDeviceAsset(AssetContainer):
    """ AssetContainer that performs one or more end device functions. One type of EndDeviceAsset is a MeterAsset which can perform metering, load management, connect/disconnect, accounting functions, etc. Some EndDeviceAssets, such as ones monitoring and controlling air conditioner, refrigerator, pool pumps may be connected to a MeterAsset. All EndDeviceAssets may have communication capability defined by the associated ComFunction(s). An EndDeviceAsset may be owned by a consumer, a service provider, utility or otherwise. There may be a related end device function that identifies a sensor or control point within a metering application or communications systems (e.g., water, gas, electricity). Some devices may use an optical port that conforms to the ANSI C12.18 standard for communications.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All end device groups referring to this end device asset.
    EndDeviceGroups = List(Instance("CIM.IEC61968.Metering.EndDeviceGroup"),
        desc="All end device groups referring to this end device asset.")

    # All end device controls sending commands to this end device asset.
    EndDeviceControls = List(Instance("CIM.IEC61968.Metering.EndDeviceControl"),
        desc="All end device controls sending commands to this end device asset.")

    # All sets of electrical properties for this end device asset.
    ElectricalInfos = List(Instance("CIM.IEC61968.Assets.ElectricalInfo"),
        desc="All sets of electrical properties for this end device asset.")

    Readings = List(Instance("CIM.IEC61968.Metering.Reading"))

    # Service location whose service delivery is measured by this end device asset.
    ServiceLocation = Instance("CIM.IEC61968.Customers.ServiceLocation",
        desc="Service location whose service delivery is measured by this end device asset.",
        transient=True,
        opposite="EndDeviceAssets",
        editor=InstanceEditor(name="_servicelocations"))

    def _get_servicelocations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Customers.ServiceLocation" ]
        else:
            return []

    _servicelocations = Property(fget=_get_servicelocations)

    # Product documentation for this end device asset.
    EndDeviceModel = Instance("CIM.IEC61968.AssetModels.EndDeviceModel",
        desc="Product documentation for this end device asset.",
        transient=True,
        opposite="EndDeviceAssets",
        editor=InstanceEditor(name="_enddevicemodels"))

    def _get_enddevicemodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.AssetModels.EndDeviceModel" ]
        else:
            return []

    _enddevicemodels = Property(fget=_get_enddevicemodels)

    # All device functions this end device asset performs.
    DeviceFunctions = List(Instance("CIM.IEC61968.Metering.DeviceFunction"),
        desc="All device functions this end device asset performs.")

    # Customer owning this end device asset.
    Customer = Instance("CIM.IEC61968.Customers.Customer",
        desc="Customer owning this end device asset.",
        transient=True,
        opposite="EndDeviceAssets",
        editor=InstanceEditor(name="_customers"))

    def _get_customers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Customers.Customer" ]
        else:
            return []

    _customers = Property(fget=_get_customers)

    # Service delivery point to which this end device asset belongs.
    ServiceDeliveryPoint = Instance("CIM.IEC61968.Metering.ServiceDeliveryPoint",
        desc="Service delivery point to which this end device asset belongs.",
        transient=True,
        opposite="EndDeviceAssets",
        editor=InstanceEditor(name="_servicedeliverypoints"))

    def _get_servicedeliverypoints(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.ServiceDeliveryPoint" ]
        else:
            return []

    _servicedeliverypoints = Property(fget=_get_servicedeliverypoints)

    # True if this end device asset is capable of supporting on-request reads for this end device.
    readRequest = Bool(desc="True if this end device asset is capable of supporting on-request reads for this end device.")

    # True if this end device asset is capable of supporting the presentation of metered values to a user or another system (always true for a meter, but might not be true for a load control unit.)
    metrology = Bool(desc="True if this end device asset is capable of supporting the presentation of metered values to a user or another system (always true for a meter, but might not be true for a load control unit.)")

    # True if this end device asset is capable of supporting remote whole-house disconnect capability. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the ConnectDisconnectFunction contained by this end device asset.
    disconnect = Bool(desc="True if this end device asset is capable of supporting remote whole-house disconnect capability. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the ConnectDisconnectFunction contained by this end device asset.")

    # True if this end device asset is capable of supporting one or more relays. The relays may be programmable in the meter and tied to TOU, time pulse, load control or other functions. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset.
    relayCapable = Bool(desc="True if this end device asset is capable of supporting one or more relays. The relays may be programmable in the meter and tied to TOU, time pulse, load control or other functions. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset.")

    # True if this end device asset is capable of supporting the means to report historical power interruption data.
    outageReport = Bool(desc="True if this end device asset is capable of supporting the means to report historical power interruption data.")

    # Automated meter reading (AMR) system responsible for communications to this end device.
    amrSystem = Str(desc="Automated meter reading (AMR) system responsible for communications to this end device.")

    # True if this EndDeviceAsset is capable of supporting detection and monitoring of reverse flow.
    reverseFlowHandling = Bool(desc="True if this EndDeviceAsset is capable of supporting detection and monitoring of reverse flow.")

    # True if this end device asset is capable of supporting load control functions through either the meter or the AMR option. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset.
    loadControl = Bool(desc="True if this end device asset is capable of supporting load control functions through either the meter or the AMR option. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset.")

    # True if this end device asset is capable of supporting the autonomous application of daylight savings time (DST).
    dstEnabled = Bool(desc="True if this end device asset is capable of supporting the autonomous application of daylight savings time (DST).")

    # Time zone offset relative to GMT for the location of this end device.
    timeZoneOffset = Minutes(desc="Time zone offset relative to GMT for the location of this end device.")

    # True if this end device asset is capable of supporting demand response functions. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset.
    demandResponse = Bool(desc="True if this end device asset is capable of supporting demand response functions. To determine whether this functionality is installed and enabled, check the 'DeviceFunction.disabled' attribute of the respective function contained by this end device asset.")

    #--------------------------------------------------------------------------
    #  Begin "EndDeviceAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "readRequest", "metrology", "disconnect", "relayCapable", "outageReport", "amrSystem", "reverseFlowHandling", "loadControl", "dstEnabled", "timeZoneOffset", "demandResponse",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "LandProperties", "Assets", "Seals", "EndDeviceGroups", "EndDeviceControls", "ElectricalInfos", "Readings", "ServiceLocation", "EndDeviceModel", "DeviceFunctions", "Customer", "ServiceDeliveryPoint",
                label="References", columns=4),
            dock="tab"),
        id="CIM.IEC61968.Metering.EndDeviceAsset",
        title="EndDeviceAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EndDeviceAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Reading" class:
#------------------------------------------------------------------------------

class Reading(MeasurementValue):
    """ Specific value measured by a meter or other asset. Each Reading is associated with a specific ReadingType.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    EndDeviceAsset = Instance("CIM.IEC61968.Metering.EndDeviceAsset",
        transient=True,
        opposite="Readings",
        editor=InstanceEditor(name="_enddeviceassets"))

    def _get_enddeviceassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.EndDeviceAsset" ]
        else:
            return []

    _enddeviceassets = Property(fget=_get_enddeviceassets)

    # Used only if quality of this reading value is different than 'Good'.
    ReadingQualities = List(Instance("CIM.IEC61968.Metering.ReadingQuality"),
        desc="Used only if quality of this reading value is different than 'Good'.")

    # Type information for this reading value.
    ReadingType = Instance("CIM.IEC61968.Metering.ReadingType",
        desc="Type information for this reading value.",
        transient=True,
        opposite="Readings",
        editor=InstanceEditor(name="_readingtypes"))

    def _get_readingtypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.ReadingType" ]
        else:
            return []

    _readingtypes = Property(fget=_get_readingtypes)

    # All meter readings (sets of values) containing this reading value.
    MeterReadings = List(Instance("CIM.IEC61968.Metering.MeterReading"),
        desc="All meter readings (sets of values) containing this reading value.")

    # Value of this reading.
    value = Float(desc="Value of this reading.")

    #--------------------------------------------------------------------------
    #  Begin "Reading" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "sensorAccuracy", "timeStamp", "value",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "GmlValues", "MeasurementValueSource", "ErpPerson", "ProcedureDataSets", "RemoteSource", "MeasurementValueQuality", "EndDeviceAsset", "ReadingQualities", "ReadingType", "MeterReadings",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Metering.Reading",
        title="Reading",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Reading" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Register" class:
#------------------------------------------------------------------------------

class Register(IdentifiedObject):
    """ Display for quantity that is metered on an end device such as a meter.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Reading type for values displayed by this register.
    ReadingType = Instance("CIM.IEC61968.Metering.ReadingType",
        desc="Reading type for values displayed by this register.",
        transient=True,
        opposite="Register",
        editor=InstanceEditor(name="_readingtypes"))

    def _get_readingtypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.ReadingType" ]
        else:
            return []

    _readingtypes = Property(fget=_get_readingtypes)

    # Device function metering quantities displayed by this register.
    DeviceFunction = Instance("CIM.IEC61968.Metering.DeviceFunction",
        desc="Device function metering quantities displayed by this register.",
        transient=True,
        opposite="Registers",
        editor=InstanceEditor(name="_devicefunctions"))

    def _get_devicefunctions(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.DeviceFunction" ]
        else:
            return []

    _devicefunctions = Property(fget=_get_devicefunctions)

    # Number of digits (dials on a mechanical meter) to the right of the decimal place.
    rightDigitCount = Int(desc="Number of digits (dials on a mechanical meter) to the right of the decimal place.")

    # Number of digits (dials on a mechanical meter) to the left of the decimal place; default is 5.
    leftDigitCount = Int(desc="Number of digits (dials on a mechanical meter) to the left of the decimal place; default is 5.")

    #--------------------------------------------------------------------------
    #  Begin "Register" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "rightDigitCount", "leftDigitCount",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ReadingType", "DeviceFunction",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Metering.Register",
        title="Register",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Register" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ReadingQuality" class:
#------------------------------------------------------------------------------

class ReadingQuality(Element):
    """ Quality of a specific reading value or interval reading value. Note that more than one Quality may be applicable to a given Reading. Typically not used unless problems or unusual conditions occur (i.e., quality for each Reading is assumed to be 'Good' unless stated otherwise in associated ReadingQuality).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Reading value to which this quality applies.
    Reading = Instance("CIM.IEC61968.Metering.Reading",
        desc="Reading value to which this quality applies.",
        transient=True,
        opposite="ReadingQualities",
        editor=InstanceEditor(name="_readings"))

    def _get_readings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.Reading" ]
        else:
            return []

    _readings = Property(fget=_get_readings)

    # Interval reading value to which this quality applies.
    IntervalReading = Instance("CIM.IEC61968.Metering.IntervalReading",
        desc="Interval reading value to which this quality applies.",
        transient=True,
        opposite="ReadingQualities",
        editor=InstanceEditor(name="_intervalreadings"))

    def _get_intervalreadings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.IntervalReading" ]
        else:
            return []

    _intervalreadings = Property(fget=_get_intervalreadings)

    # Quality, to be specified if different than 'Good'.
    quality = Str(desc="Quality, to be specified if different than 'Good'.")

    #--------------------------------------------------------------------------
    #  Begin "ReadingQuality" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "quality",
                label="Attributes"),
            VGroup("Parent", "Reading", "IntervalReading",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Metering.ReadingQuality",
        title="ReadingQuality",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ReadingQuality" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MeterServiceWork" class:
#------------------------------------------------------------------------------

class MeterServiceWork(Work):
    """ Work involving meters.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Meter asset on which this non-replacement work is performed.
    MeterAsset = Instance("CIM.IEC61968.Metering.MeterAsset",
        desc="Meter asset on which this non-replacement work is performed.",
        transient=True,
        opposite="MeterServiceWorks",
        editor=InstanceEditor(name="_meterassets"))

    def _get_meterassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.MeterAsset" ]
        else:
            return []

    _meterassets = Property(fget=_get_meterassets)

    # Old meter asset replaced by this work.
    OldMeterAsset = Instance("CIM.IEC61968.Metering.MeterAsset",
        desc="Old meter asset replaced by this work.",
        transient=True,
        opposite="MeterReplacementWorks",
        editor=InstanceEditor(name="_meterassets"))

    def _get_meterassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.MeterAsset" ]
        else:
            return []

    _meterassets = Property(fget=_get_meterassets)

    #--------------------------------------------------------------------------
    #  Begin "MeterServiceWork" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "subject", "revisionNumber", "category", "lastModifiedDateTime", "title", "createdDateTime", "kind", "requestDateTime", "priority",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ActivityRecords", "ErpOrganisationRoles", "ScheduledEvents", "FromDocumentRoles", "LocationRoles", "PowerSystemResourceRoles", "NetworkDataSets", "ErpPersonRoles", "ChangeItems", "Measurements", "docStatus", "ScheduleParameterInfos", "ElectronicAddress", "ToDocumentRoles", "status", "AssetRoles", "ChangeSets", "WorkFlowSteps", "Customers", "WorkTasks", "ErpProjectAccounting", "Project", "Designs", "BusinessCase", "WorkBillingInfo", "WorkCostDetails", "Request", "MeterAsset", "OldMeterAsset",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Metering.MeterServiceWork",
        title="MeterServiceWork",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeterServiceWork" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "IntervalBlock" class:
#------------------------------------------------------------------------------

class IntervalBlock(Element):
    """ Time sequence of Readings of the same ReadingType. Contained IntervalReadings may need conversion through the application of an offset and a scalar defined in associated Pending.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Interval reading contained in this block.
    IntervalReadings = List(Instance("CIM.IEC61968.Metering.IntervalReading"),
        desc="Interval reading contained in this block.")

    # Meter reading containing this interval block.
    MeterReading = Instance("CIM.IEC61968.Metering.MeterReading",
        desc="Meter reading containing this interval block.",
        transient=True,
        opposite="IntervalBlocks",
        editor=InstanceEditor(name="_meterreadings"))

    def _get_meterreadings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.MeterReading" ]
        else:
            return []

    _meterreadings = Property(fget=_get_meterreadings)

    # Type information for interval reading values contained in this block.
    ReadingType = Instance("CIM.IEC61968.Metering.ReadingType",
        desc="Type information for interval reading values contained in this block.",
        transient=True,
        opposite="IntervalBlocks",
        editor=InstanceEditor(name="_readingtypes"))

    def _get_readingtypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.ReadingType" ]
        else:
            return []

    _readingtypes = Property(fget=_get_readingtypes)

    # Pending conversion to apply to interval reading values contained by this block (after which the resulting reading type is different than the original because it reflects the conversion result).
    Pending = Instance("CIM.IEC61968.Metering.Pending",
        desc="Pending conversion to apply to interval reading values contained by this block (after which the resulting reading type is different than the original because it reflects the conversion result).",
        transient=True,
        opposite="IntervalBlocks",
        editor=InstanceEditor(name="_pendings"))

    def _get_pendings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.Pending" ]
        else:
            return []

    _pendings = Property(fget=_get_pendings)

    #--------------------------------------------------------------------------
    #  Begin "IntervalBlock" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            VGroup("Parent", "IntervalReadings", "MeterReading", "ReadingType", "Pending",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Metering.IntervalBlock",
        title="IntervalBlock",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "IntervalBlock" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MeterReading" class:
#------------------------------------------------------------------------------

class MeterReading(IdentifiedObject):
    """ Set of values obtained from the meter.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All interval blocks contained in this meter reading.
    IntervalBlocks = List(Instance("CIM.IEC61968.Metering.IntervalBlock"),
        desc="All interval blocks contained in this meter reading.")

    # (could be deprecated in the future) Customer agreement for this meter reading.
    CustomerAgreement = Instance("CIM.IEC61968.Customers.CustomerAgreement",
        desc="(could be deprecated in the future) Customer agreement for this meter reading.",
        transient=True,
        opposite="MeterReadings",
        editor=InstanceEditor(name="_customeragreements"))

    def _get_customeragreements(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Customers.CustomerAgreement" ]
        else:
            return []

    _customeragreements = Property(fget=_get_customeragreements)

    # Service delivery point from which this meter reading (set of values) has been obtained.
    ServiceDeliveryPoint = Instance("CIM.IEC61968.Metering.ServiceDeliveryPoint",
        desc="Service delivery point from which this meter reading (set of values) has been obtained.",
        transient=True,
        opposite="MeterReadings",
        editor=InstanceEditor(name="_servicedeliverypoints"))

    def _get_servicedeliverypoints(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.ServiceDeliveryPoint" ]
        else:
            return []

    _servicedeliverypoints = Property(fget=_get_servicedeliverypoints)

    # Meter asset providing this meter reading.
    MeterAsset = Instance("CIM.IEC61968.Metering.MeterAsset",
        desc="Meter asset providing this meter reading.",
        transient=True,
        opposite="MeterReadings",
        editor=InstanceEditor(name="_meterassets"))

    def _get_meterassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.MeterAsset" ]
        else:
            return []

    _meterassets = Property(fget=_get_meterassets)

    # Date and time interval of the data items contained within this meter reading.
    valuesInterval = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Date and time interval of the data items contained within this meter reading.",
        transient=True,
        editor=InstanceEditor(name="_datetimeintervals"))

    def _get_datetimeintervals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.DateTimeInterval" ]
        else:
            return []

    _datetimeintervals = Property(fget=_get_datetimeintervals)

    # All reading values contained within this meter reading.
    Readings = List(Instance("CIM.IEC61968.Metering.Reading"),
        desc="All reading values contained within this meter reading.")

    # All end device events associated with this set of measured values.
    EndDeviceEvents = List(Instance("CIM.IEC61968.Metering.EndDeviceEvent"),
        desc="All end device events associated with this set of measured values.")

    #--------------------------------------------------------------------------
    #  Begin "MeterReading" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "IntervalBlocks", "CustomerAgreement", "ServiceDeliveryPoint", "MeterAsset", "valuesInterval", "Readings", "EndDeviceEvents",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Metering.MeterReading",
        title="MeterReading",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeterReading" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "DemandResponseProgram" class:
#------------------------------------------------------------------------------

class DemandResponseProgram(IdentifiedObject):
    """ Demand response program.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All groups of end devices with this demand response program.
    EndDeviceGroups = List(Instance("CIM.IEC61968.Metering.EndDeviceGroup"),
        desc="All groups of end devices with this demand response program.")

    # Interval within which the program is valid.
    validityInterval = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="Interval within which the program is valid.",
        transient=True,
        editor=InstanceEditor(name="_datetimeintervals"))

    def _get_datetimeintervals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.DateTimeInterval" ]
        else:
            return []

    _datetimeintervals = Property(fget=_get_datetimeintervals)

    # All customer agreements with this demand response program.
    CustomerAgreements = List(Instance("CIM.IEC61968.Customers.CustomerAgreement"),
        desc="All customer agreements with this demand response program.")

    # All end device controls with this demand response program.
    EndDeviceControls = List(Instance("CIM.IEC61968.Metering.EndDeviceControl"),
        desc="All end device controls with this demand response program.")

    # Type of demand response program; examples are CPP (critical-peak pricing), RTP (real-time pricing), DLC (direct load control), DBP (demand bidding program), BIP (base interruptible program). Note that possible types change a lot and it would be impossible to enumerate them all.
    type = Str(desc="Type of demand response program; examples are CPP (critical-peak pricing), RTP (real-time pricing), DLC (direct load control), DBP (demand bidding program), BIP (base interruptible program). Note that possible types change a lot and it would be impossible to enumerate them all.")

    #--------------------------------------------------------------------------
    #  Begin "DemandResponseProgram" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "type",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "EndDeviceGroups", "validityInterval", "CustomerAgreements", "EndDeviceControls",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Metering.DemandResponseProgram",
        title="DemandResponseProgram",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "DemandResponseProgram" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EndDeviceEvent" class:
#------------------------------------------------------------------------------

class EndDeviceEvent(ActivityRecord):
    """ Event detected by a DeviceFunction associated with EndDeviceAsset.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Device function that reported this end device event.
    DeviceFunction = Instance("CIM.IEC61968.Metering.DeviceFunction",
        desc="Device function that reported this end device event.",
        transient=True,
        opposite="EndDeviceEvents",
        editor=InstanceEditor(name="_devicefunctions"))

    def _get_devicefunctions(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.DeviceFunction" ]
        else:
            return []

    _devicefunctions = Property(fget=_get_devicefunctions)

    # Set of measured values to which this event applies.
    MeterReading = Instance("CIM.IEC61968.Metering.MeterReading",
        desc="Set of measured values to which this event applies.",
        transient=True,
        opposite="EndDeviceEvents",
        editor=InstanceEditor(name="_meterreadings"))

    def _get_meterreadings(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.MeterReading" ]
        else:
            return []

    _meterreadings = Property(fget=_get_meterreadings)

    # (if user initiated) ID of user who initiated this end device event.
    userID = Str(desc="(if user initiated) ID of user who initiated this end device event.")

    #--------------------------------------------------------------------------
    #  Begin "EndDeviceEvent" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "reason", "category", "severity", "createdDateTime", "userID",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "MarketFactors", "Documents", "Organisations", "ScheduledEvent", "Assets", "ErpPersons", "Locations", "status", "DeviceFunction", "MeterReading",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Metering.EndDeviceEvent",
        title="EndDeviceEvent",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EndDeviceEvent" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EndDeviceControl" class:
#------------------------------------------------------------------------------

class EndDeviceControl(IdentifiedObject):
    """ Instructs an EndDeviceAsset (or EndDeviceGroup) to perform a specified action.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # End device asset receiving commands from this end device control.
    EndDeviceAsset = Instance("CIM.IEC61968.Metering.EndDeviceAsset",
        desc="End device asset receiving commands from this end device control.",
        transient=True,
        opposite="EndDeviceControls",
        editor=InstanceEditor(name="_enddeviceassets"))

    def _get_enddeviceassets(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.EndDeviceAsset" ]
        else:
            return []

    _enddeviceassets = Property(fget=_get_enddeviceassets)

    # (if control has scheduled duration) Date and time interval the control has been scheduled to execute within.
    scheduledInterval = Instance("CIM.IEC61968.Common.DateTimeInterval",
        desc="(if control has scheduled duration) Date and time interval the control has been scheduled to execute within.",
        transient=True,
        editor=InstanceEditor(name="_datetimeintervals"))

    def _get_datetimeintervals(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Common.DateTimeInterval" ]
        else:
            return []

    _datetimeintervals = Property(fget=_get_datetimeintervals)

    # End device group receiving commands from this end device control.
    EndDeviceGroup = Instance("CIM.IEC61968.Metering.EndDeviceGroup",
        desc="End device group receiving commands from this end device control.",
        transient=True,
        opposite="EndDeviceControls",
        editor=InstanceEditor(name="_enddevicegroups"))

    def _get_enddevicegroups(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.EndDeviceGroup" ]
        else:
            return []

    _enddevicegroups = Property(fget=_get_enddevicegroups)

    # Could be deprecated in the future.
    CustomerAgreement = Instance("CIM.IEC61968.Customers.CustomerAgreement",
        desc="Could be deprecated in the future.",
        transient=True,
        opposite="EndDeviceControls",
        editor=InstanceEditor(name="_customeragreements"))

    def _get_customeragreements(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Customers.CustomerAgreement" ]
        else:
            return []

    _customeragreements = Property(fget=_get_customeragreements)

    # Demand response program for this end device control.
    DemandResponseProgram = Instance("CIM.IEC61968.Metering.DemandResponseProgram",
        desc="Demand response program for this end device control.",
        transient=True,
        opposite="EndDeviceControls",
        editor=InstanceEditor(name="_demandresponseprograms"))

    def _get_demandresponseprograms(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.DemandResponseProgram" ]
        else:
            return []

    _demandresponseprograms = Property(fget=_get_demandresponseprograms)

    # Type of control.
    type = Str(desc="Type of control.")

    # Whether a demand response program request is mandatory. Note: Attribute is not defined on DemandResponseProgram as it is not its inherent property (it serves to control it).
    drProgramMandatory = Bool(desc="Whether a demand response program request is mandatory. Note: Attribute is not defined on DemandResponseProgram as it is not its inherent property (it serves to control it).")

    # (if applicable) Price signal used as parameter for this end device control.
    priceSignal = FloatQuantity(desc="(if applicable) Price signal used as parameter for this end device control.")

    # Level of a demand response program request, where 0=emergency. Note: Attribute is not defined on DemandResponseProgram as it is not its inherent property (it serves to control it).
    drProgramLevel = Int(desc="Level of a demand response program request, where 0=emergency. Note: Attribute is not defined on DemandResponseProgram as it is not its inherent property (it serves to control it).")

    #--------------------------------------------------------------------------
    #  Begin "EndDeviceControl" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "type", "drProgramMandatory", "priceSignal", "drProgramLevel",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "EndDeviceAsset", "scheduledInterval", "EndDeviceGroup", "CustomerAgreement", "DemandResponseProgram",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Metering.EndDeviceControl",
        title="EndDeviceControl",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EndDeviceControl" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ServiceDeliveryPoint" class:
#------------------------------------------------------------------------------

class ServiceDeliveryPoint(IdentifiedObject):
    """ Logical point on the network where the ownership of the service changes hands. It is one of potentially many service points within a ServiceLocation, delivering service in accordance with a CustomerAgreement. Used at the place where a meter may be installed.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # ServiceSupplier (Utility) utilising this service delivery point to deliver a service.
    ServiceSupplier = Instance("CIM.IEC61968.PaymentMetering.ServiceSupplier",
        desc="ServiceSupplier (Utility) utilising this service delivery point to deliver a service.",
        transient=True,
        opposite="ServiceDeliveryPoints",
        editor=InstanceEditor(name="_servicesuppliers"))

    def _get_servicesuppliers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.PaymentMetering.ServiceSupplier" ]
        else:
            return []

    _servicesuppliers = Property(fget=_get_servicesuppliers)

    # All locations of this service delivery point.
    SDPLocations = List(Instance("CIM.IEC61968.Metering.SDPLocation"),
        desc="All locations of this service delivery point.")

    # Customer agreement regulating this service delivery point.
    CustomerAgreement = Instance("CIM.IEC61968.Customers.CustomerAgreement",
        desc="Customer agreement regulating this service delivery point.",
        transient=True,
        opposite="ServiceDeliveryPoints",
        editor=InstanceEditor(name="_customeragreements"))

    def _get_customeragreements(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Customers.CustomerAgreement" ]
        else:
            return []

    _customeragreements = Property(fget=_get_customeragreements)

    # All meter readings obtained from this service delivery point.
    MeterReadings = List(Instance("CIM.IEC61968.Metering.MeterReading"),
        desc="All meter readings obtained from this service delivery point.")

    EnergyConsumer = Instance("CIM.IEC61970.Wires.EnergyConsumer",
        transient=True,
        opposite="ServiceDeliveryPoints",
        editor=InstanceEditor(name="_energyconsumers"))

    def _get_energyconsumers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61970.Wires.EnergyConsumer" ]
        else:
            return []

    _energyconsumers = Property(fget=_get_energyconsumers)

    # All pricing structures applicable to this service delivery point (with prepayment meter running as a stand-alone device, with no CustomerAgreement or Customer).
    PricingStructures = List(Instance("CIM.IEC61968.Customers.PricingStructure"),
        desc="All pricing structures applicable to this service delivery point (with prepayment meter running as a stand-alone device, with no CustomerAgreement or Customer).")

    # Service category delivered by this service delivery point.
    ServiceCategory = Instance("CIM.IEC61968.Customers.ServiceCategory",
        desc="Service category delivered by this service delivery point.",
        transient=True,
        opposite="ServiceDeliveryPoints",
        editor=InstanceEditor(name="_servicecategorys"))

    def _get_servicecategorys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Customers.ServiceCategory" ]
        else:
            return []

    _servicecategorys = Property(fget=_get_servicecategorys)

    PowerQualityPricings = List(Instance("CIM.IEC61968.Informative.InfCustomers.PowerQualityPricing"))

    # Service location where the service delivered by this service delivery point is consumed.
    ServiceLocation = Instance("CIM.IEC61968.Customers.ServiceLocation",
        desc="Service location where the service delivered by this service delivery point is consumed.",
        transient=True,
        opposite="ServiceDeliveryPoints",
        editor=InstanceEditor(name="_servicelocations"))

    def _get_servicelocations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Customers.ServiceLocation" ]
        else:
            return []

    _servicelocations = Property(fget=_get_servicelocations)

    # All end device assets at this service delivery point.
    EndDeviceAssets = List(Instance("CIM.IEC61968.Metering.EndDeviceAsset"),
        desc="All end device assets at this service delivery point.")

    # Phase configuration kind.
    phaseConfig = PhaseConfigurationKind(desc="Phase configuration kind.")

    # Billing cycle.
    billingCycle = Str(desc="Billing cycle.")

    # Load management code.
    loadMgmt = Str(desc="Load management code.")

    # Power that this service delivery point is configured to deliver.
    ratedPower = ActivePower(desc="Power that this service delivery point is configured to deliver.")

    # Nominal service voltage.
    nominalServiceVoltage = Int(desc="Nominal service voltage.")

    # Current that this service delivery point is configured to deliver.
    ratedCurrent = CurrentFlow(desc="Current that this service delivery point is configured to deliver.")

    # Estimated load.
    estimatedLoad = CurrentFlow(desc="Estimated load.")

    # True if as a result of an inspection or otherwise, there is a reason to suspect that a previous billing may have been performed with erroneous data. Value should be reset once this potential discrepancy has been resolved.
    checkBilling = Bool(desc="True if as a result of an inspection or otherwise, there is a reason to suspect that a previous billing may have been performed with erroneous data. Value should be reset once this potential discrepancy has been resolved.")

    # Remarks about this service delivery point, for example the reason for it being rated with a non-nominal priority.
    serviceDeliveryRemark = Str(desc="Remarks about this service delivery point, for example the reason for it being rated with a non-nominal priority.")

    # Priority of service for this service delivery point. Note that service delivery points at the same service location can have different priorities.
    servicePriority = Str(desc="Priority of service for this service delivery point. Note that service delivery points at the same service location can have different priorities.")

    # Budget bill code.
    budgetBill = Str(desc="Budget bill code.")

    # True if grounded.
    grounded = Bool(desc="True if grounded.")

    # Cumulative totalizing register of consumed service at this service delivery point over its lifetime.
    consumptionRealEnergy = RealEnergy(desc="Cumulative totalizing register of consumed service at this service delivery point over its lifetime.")

    # (optional for medium voltage connections) Reference to the low side terminal of a CT or PT that obtain readings from a medium or high voltage point.
    ctptReference = Int(desc="(optional for medium voltage connections) Reference to the low side terminal of a CT or PT that obtain readings from a medium or high voltage point.")

    #--------------------------------------------------------------------------
    #  Begin "ServiceDeliveryPoint" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "phaseConfig", "billingCycle", "loadMgmt", "ratedPower", "nominalServiceVoltage", "ratedCurrent", "estimatedLoad", "checkBilling", "serviceDeliveryRemark", "servicePriority", "budgetBill", "grounded", "consumptionRealEnergy", "ctptReference",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "ServiceSupplier", "SDPLocations", "CustomerAgreement", "MeterReadings", "EnergyConsumer", "PricingStructures", "ServiceCategory", "PowerQualityPricings", "ServiceLocation", "EndDeviceAssets",
                label="References", columns=1),
            dock="tab"),
        id="CIM.IEC61968.Metering.ServiceDeliveryPoint",
        title="ServiceDeliveryPoint",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ServiceDeliveryPoint" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EndDeviceGroup" class:
#------------------------------------------------------------------------------

class EndDeviceGroup(IdentifiedObject):
    """ Abstraction for management of group communications within a two-way AMR system or the data for a group of related meters. Commands can be issued to all of the meters that belong to a meter group using a defined group address and the underlying AMR communication infrastructure.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Demand response program for this group of end devices.
    DemandResponseProgram = Instance("CIM.IEC61968.Metering.DemandResponseProgram",
        desc="Demand response program for this group of end devices.",
        transient=True,
        opposite="EndDeviceGroups",
        editor=InstanceEditor(name="_demandresponseprograms"))

    def _get_demandresponseprograms(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.DemandResponseProgram" ]
        else:
            return []

    _demandresponseprograms = Property(fget=_get_demandresponseprograms)

    # All end device assets this end device group refers to.
    EndDeviceAssets = List(Instance("CIM.IEC61968.Metering.EndDeviceAsset"),
        desc="All end device assets this end device group refers to.")

    # All end device controls sending commands to this end device group.
    EndDeviceControls = List(Instance("CIM.IEC61968.Metering.EndDeviceControl"),
        desc="All end device controls sending commands to this end device group.")

    # Address of this end device group.
    groupAddress = Int(desc="Address of this end device group.")

    #--------------------------------------------------------------------------
    #  Begin "EndDeviceGroup" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "groupAddress",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "DemandResponseProgram", "EndDeviceAssets", "EndDeviceControls",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Metering.EndDeviceGroup",
        title="EndDeviceGroup",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EndDeviceGroup" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "Pending" class:
#------------------------------------------------------------------------------

class Pending(Element):
    """ When present, a scalar conversion that is associated with IntervalBlock and which needs to be applied to every contained IntervalReading value. This conversion results in a new associated ReadingType, reflecting the true dimensions of interval reading values after the conversion.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Reading type resulting from this pending conversion.
    ReadingType = Instance("CIM.IEC61968.Metering.ReadingType",
        desc="Reading type resulting from this pending conversion.",
        transient=True,
        opposite="Pending",
        editor=InstanceEditor(name="_readingtypes"))

    def _get_readingtypes(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Metering.ReadingType" ]
        else:
            return []

    _readingtypes = Property(fget=_get_readingtypes)

    # All blocks of interval reading values to which this pending conversion applies.
    IntervalBlocks = List(Instance("CIM.IEC61968.Metering.IntervalBlock"),
        desc="All blocks of interval reading values to which this pending conversion applies.")

    # (if applicable) Offset to be added as well as multiplication using scalars.
    offset = Int(desc="(if applicable) Offset to be added as well as multiplication using scalars.")

    # (if scalar is integer or rational number)  When the scalar is a simple integer, and this attribute is presented alone and multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'. It is never used in conjunction with 'scalarFloat', only with 'scalarDenominator'.
    scalarNumerator = Int(desc="(if scalar is integer or rational number)  When the scalar is a simple integer, and this attribute is presented alone and multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'. It is never used in conjunction with 'scalarFloat', only with 'scalarDenominator'.")

    # (if scalar is floating number) When multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'.
    scalarFloat = Float(desc="(if scalar is floating number) When multiplied with 'IntervalReading.value', it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'.")

    # (if scalar is rational number) When 'IntervalReading.value' is multiplied by this attribute and divided by 'scalarDenominator, it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'.
    scalarDenominator = Int(desc="(if scalar is rational number) When 'IntervalReading.value' is multiplied by this attribute and divided by 'scalarDenominator, it causes a unit of measure conversion to occur, resulting in the 'ReadingType.unit'.")

    # Whether scalars should be applied before adding the 'offset'.
    multiplyBeforeAdd = Bool(desc="Whether scalars should be applied before adding the 'offset'.")

    #--------------------------------------------------------------------------
    #  Begin "Pending" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "offset", "scalarNumerator", "scalarFloat", "scalarDenominator", "multiplyBeforeAdd",
                label="Attributes"),
            VGroup("Parent", "ReadingType", "IntervalBlocks",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Metering.Pending",
        title="Pending",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Pending" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ComFunction" class:
#------------------------------------------------------------------------------

class ComFunction(DeviceFunction):
    """ Communication function of communication equipment or a device such as a meter.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # True when the AMR module can both send and receive messages. Default is false (i.e., module can only send).
    twoWay = Bool(desc="True when the AMR module can both send and receive messages. Default is false (i.e., module can only send).")

    # Communication ID number (e.g. serial number, IP address, telephone number, etc.) of the AMR module which serves this meter.
    amrAddress = Str(desc="Communication ID number (e.g. serial number, IP address, telephone number, etc.) of the AMR module which serves this meter.")

    # Communication ID number (e.g. port number, serial number, data collector ID, etc.) of the parent device associated to this AMR module. Note: If someone swaps out a meter, they may inadvertently disrupt the AMR system. Some technologies route readings from nearby meters through a common collection point on an electricity meter. Removal of such a meter disrupts AMR for numerous nearby meters.
    amrRouter = Str(desc="Communication ID number (e.g. port number, serial number, data collector ID, etc.) of the parent device associated to this AMR module. Note: If someone swaps out a meter, they may inadvertently disrupt the AMR system. Some technologies route readings from nearby meters through a common collection point on an electricity meter. Removal of such a meter disrupts AMR for numerous nearby meters.")

    #--------------------------------------------------------------------------
    #  Begin "ComFunction" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "hardwareID", "configID", "programID", "password", "firmwareID", "disabled", "twoWay", "amrAddress", "amrRouter",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "Asset", "AssetFunctionAssetModel", "ComEquipmentAsset", "EndDeviceAsset", "Registers", "EndDeviceEvents",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Metering.ComFunction",
        title="ComFunction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ComFunction" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MeterAsset" class:
#------------------------------------------------------------------------------

class MeterAsset(EndDeviceAsset):
    """ Physical asset that performs the metering role of the ServiceDeliveryPoint. Used for measuring consumption and detection of events.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # All meter readings provided by this meter asset.
    MeterReadings = List(Instance("CIM.IEC61968.Metering.MeterReading"),
        desc="All meter readings provided by this meter asset.")

    # All vending transactions on this meter asset.
    VendingTransactions = List(Instance("CIM.IEC61968.PaymentMetering.Transaction"),
        desc="All vending transactions on this meter asset.")

    # All non-replacement works on this meter asset.
    MeterServiceWorks = List(Instance("CIM.IEC61968.Metering.MeterServiceWork"),
        desc="All non-replacement works on this meter asset.")

    # All works on replacement of this old meter asset.
    MeterReplacementWorks = List(Instance("CIM.IEC61968.Metering.MeterServiceWork"),
        desc="All works on replacement of this old meter asset.")

    MeterAssetModel = Instance("CIM.IEC61968.Informative.InfAssetModels.MeterAssetModel",
        transient=True,
        opposite="MeterAssets",
        editor=InstanceEditor(name="_meterassetmodels"))

    def _get_meterassetmodels(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfAssetModels.MeterAssetModel" ]
        else:
            return []

    _meterassetmodels = Property(fget=_get_meterassetmodels)

    # Meter form designation per ANSI C12.10 or other applicable standard. An alphanumeric designation denoting the circuit arrangement for which the meter is applicable and its specific terminal arrangement.
    formNumber = Str(desc="Meter form designation per ANSI C12.10 or other applicable standard. An alphanumeric designation denoting the circuit arrangement for which the meter is applicable and its specific terminal arrangement.")

    # Meter kh (watthour) constant. It is the number of watthours that must be applied to the meter to cause one disk revolution for an electromechanical meter or the number of watthours represented by one increment pulse for an electronic meter.
    kH = Float(desc="Meter kh (watthour) constant. It is the number of watthours that must be applied to the meter to cause one disk revolution for an electromechanical meter or the number of watthours represented by one increment pulse for an electronic meter.")

    # Display multiplier used to produce a displayed value from a register value.
    kR = Float(desc="Display multiplier used to produce a displayed value from a register value.")

    #--------------------------------------------------------------------------
    #  Begin "MeterAsset" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "readRequest", "metrology", "disconnect", "relayCapable", "outageReport", "amrSystem", "reverseFlowHandling", "loadControl", "dstEnabled", "timeZoneOffset", "demandResponse", "formNumber", "kH", "kR",
                label="Attributes", columns=2),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "LandProperties", "Assets", "Seals", "EndDeviceGroups", "EndDeviceControls", "ElectricalInfos", "Readings", "ServiceLocation", "EndDeviceModel", "DeviceFunctions", "Customer", "ServiceDeliveryPoint", "MeterReadings", "VendingTransactions", "MeterServiceWorks", "MeterReplacementWorks", "MeterAssetModel",
                label="References", columns=4),
            dock="tab"),
        id="CIM.IEC61968.Metering.MeterAsset",
        title="MeterAsset",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MeterAsset" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ElectricMeteringFunction" class:
#------------------------------------------------------------------------------

class ElectricMeteringFunction(DeviceFunction):
    """ Functionality performed by an electric meter.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Configuration for this electric metering function.
    MeteringFunctionConfiguration = Instance("CIM.IEC61968.Informative.InfMetering.MeteringFunctionConfiguration",
        desc="Configuration for this electric metering function.",
        transient=True,
        opposite="ElectricMeteringFunctions",
        editor=InstanceEditor(name="_meteringfunctionconfigurations"))

    def _get_meteringfunctionconfigurations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.InfMetering.MeteringFunctionConfiguration" ]
        else:
            return []

    _meteringfunctionconfigurations = Property(fget=_get_meteringfunctionconfigurations)

    # Meter kW (pulse) multiplier, used as a multiplier for a meter register reading to determine the actual amount of usage for which to bill a customer.
    kWMultiplier = Int(desc="Meter kW (pulse) multiplier, used as a multiplier for a meter register reading to determine the actual amount of usage for which to bill a customer.")

    # Customer billing value = meter multiplier * transformer ratios * reading value. The multiplier identifies the scaling value to apply to the reported value after delivery of the tagged item.
    billingMultiplier = Float(desc="Customer billing value = meter multiplier * transformer ratios * reading value. The multiplier identifies the scaling value to apply to the reported value after delivery of the tagged item.")

    # True if the billingMultiplier ratio has already been applied to the associated quantities.
    billingMultiplierApplied = Bool(desc="True if the billingMultiplier ratio has already been applied to the associated quantities.")

    # Current transformer ratio used to convert associated quantities to real measurements.
    transformerCTRatio = Float(desc="Current transformer ratio used to convert associated quantities to real measurements.")

    # An additional multiplier that may be used for normalization of the demand value to an hourly value. For example, if the demand interval were set to 15 min, the demand multiplier would be 4. If the meter design is such that the demand value reported and displayed is compensated for by the meter itself and no additional scaling is required outside of the meter, the value of the demand multiplier should be '1'.
    demandMultiplier = Float(desc="An additional multiplier that may be used for normalization of the demand value to an hourly value. For example, if the demand interval were set to 15 min, the demand multiplier would be 4. If the meter design is such that the demand value reported and displayed is compensated for by the meter itself and no additional scaling is required outside of the meter, the value of the demand multiplier should be '1'.")

    # True if transformer ratios have been already applied to the associated quantities.
    transformerRatiosApplied = Bool(desc="True if transformer ratios have been already applied to the associated quantities.")

    # Voltage transformer ratio used to convert associated quantities to real measurements.
    transformerVTRatio = Float(desc="Voltage transformer ratio used to convert associated quantities to real measurements.")

    # True if the demandMultiplier ratio has already been applied to the associated quantities.
    demandMultiplierApplied = Bool(desc="True if the demandMultiplier ratio has already been applied to the associated quantities.")

    # The current class of the meter. Typical current classes in North America are 10 A, 20 A, 100 A, 200 A, or 320 A.
    currentRating = CurrentFlow(desc="The current class of the meter. Typical current classes in North America are 10 A, 20 A, 100 A, 200 A, or 320 A.")

    # Meter kWh multiplier, used as a multiplier for a meter register reading to determine the actual amount of usage for which to bill a customer.
    kWhMultiplier = Int(desc="Meter kWh multiplier, used as a multiplier for a meter register reading to determine the actual amount of usage for which to bill a customer.")

    # The service voltage at which the meter is designed to operate. Typical voltage ratings in North America are 120 V, 240 V, 277 V or 480 V.
    voltageRating = Voltage(desc="The service voltage at which the meter is designed to operate. Typical voltage ratings in North America are 120 V, 240 V, 277 V or 480 V.")

    #--------------------------------------------------------------------------
    #  Begin "ElectricMeteringFunction" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "initialCondition", "category", "lotNumber", "application", "serialNumber", "installationDate", "corporateCode", "purchasePrice", "manufacturedDate", "initialLossOfLife", "utcNumber", "critical", "hardwareID", "configID", "programID", "password", "firmwareID", "disabled", "kWMultiplier", "billingMultiplier", "billingMultiplierApplied", "transformerCTRatio", "demandMultiplier", "transformerRatiosApplied", "transformerVTRatio", "demandMultiplierApplied", "currentRating", "kWhMultiplier", "voltageRating",
                label="Attributes", columns=3),
            VGroup("Parent", "ModelingAuthoritySet", "Measurements", "Hazards", "ErpOrganisationRoles", "DimensionsInfo", "ScheduledEvents", "Mediums", "AssetFunctions", "Properties", "AssetContainer", "Ratings", "ActivityRecords", "FromAssetRoles", "LocationRoles", "PowerSystemResourceRoles", "DocumentRoles", "ChangeItems", "ErpItemMaster", "ElectronicAddresses", "WorkTask", "ErpRecDeliveryItems", "ReliabilityInfos", "ToAssetRoles", "AssetPropertyCurves", "FinancialInfo", "ErpInventory", "acceptanceTest", "status", "Asset", "AssetFunctionAssetModel", "ComEquipmentAsset", "EndDeviceAsset", "Registers", "EndDeviceEvents", "MeteringFunctionConfiguration",
                label="References", columns=3),
            dock="tab"),
        id="CIM.IEC61968.Metering.ElectricMeteringFunction",
        title="ElectricMeteringFunction",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ElectricMeteringFunction" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
