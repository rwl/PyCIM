# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61968.Assets.AssetContainer import AssetContainer

class EndDevice(AssetContainer):
    """Asset container that performs one or more end device functions. One type of end device is a meter which can perform metering, load management, connect/disconnect, accounting functions, etc. Some end devices, such as ones monitoring and controlling air conditioner, refrigerator, pool pumps may be connected to a meter. All end devices may have communication capability defined by the associated communication function(s). An end device may be owned by a consumer, a service provider, utility or otherwise. There may be a related end device function that identifies a sensor or control point within a metering application or communications systems (e.g., water, gas, electricity). Some devices may use an optical port that conforms to the ANSI C12.18 standard for communications.Asset container that performs one or more end device functions. One type of end device is a meter which can perform metering, load management, connect/disconnect, accounting functions, etc. Some end devices, such as ones monitoring and controlling air conditioner, refrigerator, pool pumps may be connected to a meter. All end devices may have communication capability defined by the associated communication function(s). An end device may be owned by a consumer, a service provider, utility or otherwise. There may be a related end device function that identifies a sensor or control point within a metering application or communications systems (e.g., water, gas, electricity). Some devices may use an optical port that conforms to the ANSI C12.18 standard for communications.
    """

    def __init__(self, timeZoneOffset=0.0, amrSystem='', EndDeviceInfo=None, ServiceDeliveryPoint=None, ServiceLocation=None, EndDeviceFunctions=None, EndDeviceControls=None, Customer=None, EndDeviceGroups=None, *args, **kw_args):
        """Initialises a new 'EndDevice' instance.

        @param timeZoneOffset: Time zone offset relative to GMT for the location of this end device. 
        @param amrSystem: Automated meter reading (AMR) system responsible for communications to this end device. 
        @param EndDeviceInfo: End device data.
        @param ServiceDeliveryPoint: Service delivery point to which this end device belongs.
        @param ServiceLocation: Service location whose service delivery is measured by this end device.
        @param EndDeviceFunctions: All end device functions this end device performs.
        @param EndDeviceControls: All end device controls sending commands to this end device.
        @param Customer: Customer owning this end device.
        @param EndDeviceGroups: All end device groups referring to this end device.
        """
        #: Time zone offset relative to GMT for the location of this end device.
        self.timeZoneOffset = timeZoneOffset

        #: Automated meter reading (AMR) system responsible for communications to this end device.
        self.amrSystem = amrSystem

        self._EndDeviceInfo = None
        self.EndDeviceInfo = EndDeviceInfo

        self._ServiceDeliveryPoint = None
        self.ServiceDeliveryPoint = ServiceDeliveryPoint

        self._ServiceLocation = None
        self.ServiceLocation = ServiceLocation

        self._EndDeviceFunctions = []
        self.EndDeviceFunctions = [] if EndDeviceFunctions is None else EndDeviceFunctions

        self._EndDeviceControls = []
        self.EndDeviceControls = [] if EndDeviceControls is None else EndDeviceControls

        self._Customer = None
        self.Customer = Customer

        self._EndDeviceGroups = []
        self.EndDeviceGroups = [] if EndDeviceGroups is None else EndDeviceGroups

        super(EndDevice, self).__init__(*args, **kw_args)

    _attrs = ["timeZoneOffset", "amrSystem"]
    _attr_types = {"timeZoneOffset": float, "amrSystem": str}
    _defaults = {"timeZoneOffset": 0.0, "amrSystem": ''}
    _enums = {}
    _refs = ["EndDeviceInfo", "ServiceDeliveryPoint", "ServiceLocation", "EndDeviceFunctions", "EndDeviceControls", "Customer", "EndDeviceGroups"]
    _many_refs = ["EndDeviceFunctions", "EndDeviceControls", "EndDeviceGroups"]

    def getEndDeviceInfo(self):
        """End device data.
        """
        return self._EndDeviceInfo

    def setEndDeviceInfo(self, value):
        if self._EndDeviceInfo is not None:
            filtered = [x for x in self.EndDeviceInfo.EndDevices if x != self]
            self._EndDeviceInfo._EndDevices = filtered

        self._EndDeviceInfo = value
        if self._EndDeviceInfo is not None:
            if self not in self._EndDeviceInfo._EndDevices:
                self._EndDeviceInfo._EndDevices.append(self)

    EndDeviceInfo = property(getEndDeviceInfo, setEndDeviceInfo)

    def getServiceDeliveryPoint(self):
        """Service delivery point to which this end device belongs.
        """
        return self._ServiceDeliveryPoint

    def setServiceDeliveryPoint(self, value):
        if self._ServiceDeliveryPoint is not None:
            filtered = [x for x in self.ServiceDeliveryPoint.EndDevices if x != self]
            self._ServiceDeliveryPoint._EndDevices = filtered

        self._ServiceDeliveryPoint = value
        if self._ServiceDeliveryPoint is not None:
            if self not in self._ServiceDeliveryPoint._EndDevices:
                self._ServiceDeliveryPoint._EndDevices.append(self)

    ServiceDeliveryPoint = property(getServiceDeliveryPoint, setServiceDeliveryPoint)

    def getServiceLocation(self):
        """Service location whose service delivery is measured by this end device.
        """
        return self._ServiceLocation

    def setServiceLocation(self, value):
        if self._ServiceLocation is not None:
            filtered = [x for x in self.ServiceLocation.EndDevices if x != self]
            self._ServiceLocation._EndDevices = filtered

        self._ServiceLocation = value
        if self._ServiceLocation is not None:
            if self not in self._ServiceLocation._EndDevices:
                self._ServiceLocation._EndDevices.append(self)

    ServiceLocation = property(getServiceLocation, setServiceLocation)

    def getEndDeviceFunctions(self):
        """All end device functions this end device performs.
        """
        return self._EndDeviceFunctions

    def setEndDeviceFunctions(self, value):
        for x in self._EndDeviceFunctions:
            x.EndDevice = None
        for y in value:
            y._EndDevice = self
        self._EndDeviceFunctions = value

    EndDeviceFunctions = property(getEndDeviceFunctions, setEndDeviceFunctions)

    def addEndDeviceFunctions(self, *EndDeviceFunctions):
        for obj in EndDeviceFunctions:
            obj.EndDevice = self

    def removeEndDeviceFunctions(self, *EndDeviceFunctions):
        for obj in EndDeviceFunctions:
            obj.EndDevice = None

    def getEndDeviceControls(self):
        """All end device controls sending commands to this end device.
        """
        return self._EndDeviceControls

    def setEndDeviceControls(self, value):
        for x in self._EndDeviceControls:
            x.EndDevice = None
        for y in value:
            y._EndDevice = self
        self._EndDeviceControls = value

    EndDeviceControls = property(getEndDeviceControls, setEndDeviceControls)

    def addEndDeviceControls(self, *EndDeviceControls):
        for obj in EndDeviceControls:
            obj.EndDevice = self

    def removeEndDeviceControls(self, *EndDeviceControls):
        for obj in EndDeviceControls:
            obj.EndDevice = None

    def getCustomer(self):
        """Customer owning this end device.
        """
        return self._Customer

    def setCustomer(self, value):
        if self._Customer is not None:
            filtered = [x for x in self.Customer.EndDevices if x != self]
            self._Customer._EndDevices = filtered

        self._Customer = value
        if self._Customer is not None:
            if self not in self._Customer._EndDevices:
                self._Customer._EndDevices.append(self)

    Customer = property(getCustomer, setCustomer)

    def getEndDeviceGroups(self):
        """All end device groups referring to this end device.
        """
        return self._EndDeviceGroups

    def setEndDeviceGroups(self, value):
        for p in self._EndDeviceGroups:
            filtered = [q for q in p.EndDevices if q != self]
            self._EndDeviceGroups._EndDevices = filtered
        for r in value:
            if self not in r._EndDevices:
                r._EndDevices.append(self)
        self._EndDeviceGroups = value

    EndDeviceGroups = property(getEndDeviceGroups, setEndDeviceGroups)

    def addEndDeviceGroups(self, *EndDeviceGroups):
        for obj in EndDeviceGroups:
            if self not in obj._EndDevices:
                obj._EndDevices.append(self)
            self._EndDeviceGroups.append(obj)

    def removeEndDeviceGroups(self, *EndDeviceGroups):
        for obj in EndDeviceGroups:
            if self in obj._EndDevices:
                obj._EndDevices.remove(self)
            self._EndDeviceGroups.remove(obj)

