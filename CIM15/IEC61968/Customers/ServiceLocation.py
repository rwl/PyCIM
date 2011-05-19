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

from CIM15.IEC61968.Common.Location import Location

class ServiceLocation(Location):
    """A customer service location has one or more service delivery points, which in turn relate to Meters. The location may be a point or a polygon, depending on the specific circumstances. For distribution, the service location is typically the location of the utility customer's premise. Because a customer's premise may have one or more meters, the service delivery point is used to define the actual conducting equipment that the end device attaches to at the utility customer's service location. For transmission, it is the point(s) of interconnection on the transmission provider's transmission system where capacity and/or energy transmitted by the transmission provider is made available to the receiving party.A customer service location has one or more service delivery points, which in turn relate to Meters. The location may be a point or a polygon, depending on the specific circumstances. For distribution, the service location is typically the location of the utility customer's premise. Because a customer's premise may have one or more meters, the service delivery point is used to define the actual conducting equipment that the end device attaches to at the utility customer's service location. For transmission, it is the point(s) of interconnection on the transmission provider's transmission system where capacity and/or energy transmitted by the transmission provider is made available to the receiving party.
    """

    def __init__(self, siteAccessProblem='', accessMethod='', needsInspection=False, EndDevices=None, ErpPersons=None, ServiceDeliveryPoints=None, CustomerAgreements=None, *args, **kw_args):
        """Initialises a new 'ServiceLocation' instance.

        @param siteAccessProblem: Problems previously encountered when visiting or performing work on this site. Examples include: bad dog, violent customer, verbally abusive occupant, obstructions, safety hazards, etc. 
        @param accessMethod: Method for the service person to access the appropriate service locations. For example, a description of where to obtain a key if the facility is unmanned and secured. 
        @param needsInspection: True if inspection is needed of facilities at this service location. This could be requested by a customer, due to suspected tampering, environmental concerns (e.g., a fire in the vicinity), or to correct incompatible data. 
        @param EndDevices: All end devices that measure the service delivered to this service location.
        @param ErpPersons:
        @param ServiceDeliveryPoints: All service delivery points delivering service (of the same type) to this service location.
        @param CustomerAgreements: All customer agreements regulating this service location.
        """
        #: Problems previously encountered when visiting or performing work on this site. Examples include: bad dog, violent customer, verbally abusive occupant, obstructions, safety hazards, etc.
        self.siteAccessProblem = siteAccessProblem

        #: Method for the service person to access the appropriate service locations. For example, a description of where to obtain a key if the facility is unmanned and secured.
        self.accessMethod = accessMethod

        #: True if inspection is needed of facilities at this service location. This could be requested by a customer, due to suspected tampering, environmental concerns (e.g., a fire in the vicinity), or to correct incompatible data.
        self.needsInspection = needsInspection

        self._EndDevices = []
        self.EndDevices = [] if EndDevices is None else EndDevices

        self._ErpPersons = []
        self.ErpPersons = [] if ErpPersons is None else ErpPersons

        self._ServiceDeliveryPoints = []
        self.ServiceDeliveryPoints = [] if ServiceDeliveryPoints is None else ServiceDeliveryPoints

        self._CustomerAgreements = []
        self.CustomerAgreements = [] if CustomerAgreements is None else CustomerAgreements

        super(ServiceLocation, self).__init__(*args, **kw_args)

    _attrs = ["siteAccessProblem", "accessMethod", "needsInspection"]
    _attr_types = {"siteAccessProblem": str, "accessMethod": str, "needsInspection": bool}
    _defaults = {"siteAccessProblem": '', "accessMethod": '', "needsInspection": False}
    _enums = {}
    _refs = ["EndDevices", "ErpPersons", "ServiceDeliveryPoints", "CustomerAgreements"]
    _many_refs = ["EndDevices", "ErpPersons", "ServiceDeliveryPoints", "CustomerAgreements"]

    def getEndDevices(self):
        """All end devices that measure the service delivered to this service location.
        """
        return self._EndDevices

    def setEndDevices(self, value):
        for x in self._EndDevices:
            x.ServiceLocation = None
        for y in value:
            y._ServiceLocation = self
        self._EndDevices = value

    EndDevices = property(getEndDevices, setEndDevices)

    def addEndDevices(self, *EndDevices):
        for obj in EndDevices:
            obj.ServiceLocation = self

    def removeEndDevices(self, *EndDevices):
        for obj in EndDevices:
            obj.ServiceLocation = None

    def getErpPersons(self):
        
        return self._ErpPersons

    def setErpPersons(self, value):
        for x in self._ErpPersons:
            x.ServiceLocation = None
        for y in value:
            y._ServiceLocation = self
        self._ErpPersons = value

    ErpPersons = property(getErpPersons, setErpPersons)

    def addErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            obj.ServiceLocation = self

    def removeErpPersons(self, *ErpPersons):
        for obj in ErpPersons:
            obj.ServiceLocation = None

    def getServiceDeliveryPoints(self):
        """All service delivery points delivering service (of the same type) to this service location.
        """
        return self._ServiceDeliveryPoints

    def setServiceDeliveryPoints(self, value):
        for x in self._ServiceDeliveryPoints:
            x.ServiceLocation = None
        for y in value:
            y._ServiceLocation = self
        self._ServiceDeliveryPoints = value

    ServiceDeliveryPoints = property(getServiceDeliveryPoints, setServiceDeliveryPoints)

    def addServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj.ServiceLocation = self

    def removeServiceDeliveryPoints(self, *ServiceDeliveryPoints):
        for obj in ServiceDeliveryPoints:
            obj.ServiceLocation = None

    def getCustomerAgreements(self):
        """All customer agreements regulating this service location.
        """
        return self._CustomerAgreements

    def setCustomerAgreements(self, value):
        for p in self._CustomerAgreements:
            filtered = [q for q in p.ServiceLocations if q != self]
            self._CustomerAgreements._ServiceLocations = filtered
        for r in value:
            if self not in r._ServiceLocations:
                r._ServiceLocations.append(self)
        self._CustomerAgreements = value

    CustomerAgreements = property(getCustomerAgreements, setCustomerAgreements)

    def addCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            if self not in obj._ServiceLocations:
                obj._ServiceLocations.append(self)
            self._CustomerAgreements.append(obj)

    def removeCustomerAgreements(self, *CustomerAgreements):
        for obj in CustomerAgreements:
            if self in obj._ServiceLocations:
                obj._ServiceLocations.remove(self)
            self._CustomerAgreements.remove(obj)

