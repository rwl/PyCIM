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

from CIM15.Element import Element

class GmlObservation(Element):
    """A GML observation models the act of observing, often with a camera, a person or some form of instrument. An observation feature describes the 'metadata' associated with an information capture event, together with a value for the result of the observation. The basic structures introduced in this class are intended to serve as the foundation for more comprehensive schemas for scientific, technical and engineering measurement schemas.A GML observation models the act of observing, often with a camera, a person or some form of instrument. An observation feature describes the 'metadata' associated with an information capture event, together with a value for the result of the observation. The basic structures introduced in this class are intended to serve as the foundation for more comprehensive schemas for scientific, technical and engineering measurement schemas.
    """

    def __init__(self, resultOf='', target='', using='', dateTime='', GmlDiagramObjects=None, ChangeItems=None, GmlValues=None, *args, **kw_args):
        """Initialises a new 'GmlObservation' instance.

        @param resultOf: Indicates the result of the observation. 
        @param target: Contains or points to the specimen, region or station which is the object of the observation 
        @param using: Contains or points to a description of a sensor, instrument or procedure used for the observation. 
        @param dateTime: 
        @param GmlDiagramObjects:
        @param ChangeItems:
        @param GmlValues:
        """
        #: Indicates the result of the observation.
        self.resultOf = resultOf

        #: Contains or points to the specimen, region or station which is the object of the observation
        self.target = target

        #: Contains or points to a description of a sensor, instrument or procedure used for the observation.
        self.using = using


        self.dateTime = dateTime

        self._GmlDiagramObjects = []
        self.GmlDiagramObjects = [] if GmlDiagramObjects is None else GmlDiagramObjects

        self._ChangeItems = []
        self.ChangeItems = [] if ChangeItems is None else ChangeItems

        self._GmlValues = []
        self.GmlValues = [] if GmlValues is None else GmlValues

        super(GmlObservation, self).__init__(*args, **kw_args)

    _attrs = ["resultOf", "target", "using", "dateTime"]
    _attr_types = {"resultOf": str, "target": str, "using": str, "dateTime": str}
    _defaults = {"resultOf": '', "target": '', "using": '', "dateTime": ''}
    _enums = {}
    _refs = ["GmlDiagramObjects", "ChangeItems", "GmlValues"]
    _many_refs = ["GmlDiagramObjects", "ChangeItems", "GmlValues"]

    def getGmlDiagramObjects(self):
        
        return self._GmlDiagramObjects

    def setGmlDiagramObjects(self, value):
        for p in self._GmlDiagramObjects:
            filtered = [q for q in p.GmlObservatins if q != self]
            self._GmlDiagramObjects._GmlObservatins = filtered
        for r in value:
            if self not in r._GmlObservatins:
                r._GmlObservatins.append(self)
        self._GmlDiagramObjects = value

    GmlDiagramObjects = property(getGmlDiagramObjects, setGmlDiagramObjects)

    def addGmlDiagramObjects(self, *GmlDiagramObjects):
        for obj in GmlDiagramObjects:
            if self not in obj._GmlObservatins:
                obj._GmlObservatins.append(self)
            self._GmlDiagramObjects.append(obj)

    def removeGmlDiagramObjects(self, *GmlDiagramObjects):
        for obj in GmlDiagramObjects:
            if self in obj._GmlObservatins:
                obj._GmlObservatins.remove(self)
            self._GmlDiagramObjects.remove(obj)

    def getChangeItems(self):
        
        return self._ChangeItems

    def setChangeItems(self, value):
        for x in self._ChangeItems:
            x.GmlObservation = None
        for y in value:
            y._GmlObservation = self
        self._ChangeItems = value

    ChangeItems = property(getChangeItems, setChangeItems)

    def addChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj.GmlObservation = self

    def removeChangeItems(self, *ChangeItems):
        for obj in ChangeItems:
            obj.GmlObservation = None

    def getGmlValues(self):
        
        return self._GmlValues

    def setGmlValues(self, value):
        for x in self._GmlValues:
            x.GmlObservation = None
        for y in value:
            y._GmlObservation = self
        self._GmlValues = value

    GmlValues = property(getGmlValues, setGmlValues)

    def addGmlValues(self, *GmlValues):
        for obj in GmlValues:
            obj.GmlObservation = self

    def removeGmlValues(self, *GmlValues):
        for obj in GmlValues:
            obj.GmlObservation = None

