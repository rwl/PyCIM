# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14v13.Element import Element

class GmlObservation(Element):
    """A GML observation models the act of observing, often with a camera, a person or some form of instrument. An observation feature describes the 'metadata' associated with an information capture event, together with a value for the result of the observation. The basic structures introduced in this class are intended to serve as the foundation for more comprehensive schemas for scientific, technical and engineering measurement schemas.
    """

    def __init__(self, target='', using='', dateTime='', resultOf='', ChangeItems=None, GmlValues=None, Locations=None, *args, **kw_args):
        """Initializes a new 'GmlObservation' instance.

        @param target: Contains or points to the specimen, region or station which is the object of the observation 
        @param using: Contains or points to a description of a sensor, instrument or procedure used for the observation. 
        @param dateTime: 
        @param resultOf: Indicates the result of the observation. 
        @param ChangeItems:
        @param GmlValues:
        @param Locations:
        """
        #: Contains or points to the specimen, region or station which is the object of the observation
        self.target = target

        #: Contains or points to a description of a sensor, instrument or procedure used for the observation.
        self.using = using


        self.dateTime = dateTime

        #: Indicates the result of the observation.
        self.resultOf = resultOf

        self._ChangeItems = []
        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        self._GmlValues = []
        self.GmlValues = [] if GmlValues is None else GmlValues

        self._Locations = []
        self.Locations = [] if Locations is None else Locations

        super(GmlObservation, self).__init__(*args, **kw_args)

    def getChangeItems(self):
        
        return self._ChangeItems

    def setChangeItems(self, value):
        for x in self._ChangeItems:
            x._GmlObservation = None
        for y in value:
            y._GmlObservation = self
        self._ChangeItems = value

    ChangeItems = property(getChangeItems, setChangeItems)

    def addChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._GmlObservation = self
            self._ChangeItems.append(obj)

    def removeChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj._GmlObservation = None
            self._ChangeItems.remove(obj)

    def getGmlValues(self):
        
        return self._GmlValues

    def setGmlValues(self, value):
        for x in self._GmlValues:
            x._GmlObservation = None
        for y in value:
            y._GmlObservation = self
        self._GmlValues = value

    GmlValues = property(getGmlValues, setGmlValues)

    def addGmlValues(self, *GmlValues):
        for obj in GmlValues:
            obj._GmlObservation = self
            self._GmlValues.append(obj)

    def removeGmlValues(self, *GmlValues):
        for obj in GmlValues:
            obj._GmlObservation = None
            self._GmlValues.remove(obj)

    def getLocations(self):
        
        return self._Locations

    def setLocations(self, value):
        for p in self._Locations:
            filtered = [q for q in p.GmlObservatins if q != self]
            self._Locations._GmlObservatins = filtered
        for r in value:
            if self not in r._GmlObservatins:
                r._GmlObservatins.append(self)
        self._Locations = value

    Locations = property(getLocations, setLocations)

    def addLocations(self, *Locations):
        for obj in Locations:
            if self not in obj._GmlObservatins:
                obj._GmlObservatins.append(self)
            self._Locations.append(obj)

    def removeLocations(self, *Locations):
        for obj in Locations:
            if self in obj._GmlObservatins:
                obj._GmlObservatins.remove(self)
            self._Locations.remove(obj)

