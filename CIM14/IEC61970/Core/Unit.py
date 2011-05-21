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

from CIM14.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Unit(IdentifiedObject):
    """Quantity being measured. The Unit.name shall be unique among all specified quantities and describe the quantity. The Unit.aliasName is meant to be used for localization.
    """

    def __init__(self, Controls=None, Measurements=None, MetaBlockConOutput=None, MetaBlockConInput=None, ProtectionEquipments=None, *args, **kw_args):
        """Initialises a new 'Unit' instance.

        @param Controls: The Controls having the Unit.
        @param Measurements: The Measurements having the Unit
        @param MetaBlockConOutput:
        @param MetaBlockConInput:
        @param ProtectionEquipments: The Protection Equipments having the Unit.
        """
        self._Controls = []
        self.Controls = [] if Controls is None else Controls

        self._Measurements = []
        self.Measurements = [] if Measurements is None else Measurements

        self._MetaBlockConOutput = []
        self.MetaBlockConOutput = [] if MetaBlockConOutput is None else MetaBlockConOutput

        self._MetaBlockConInput = []
        self.MetaBlockConInput = [] if MetaBlockConInput is None else MetaBlockConInput

        self._ProtectionEquipments = []
        self.ProtectionEquipments = [] if ProtectionEquipments is None else ProtectionEquipments

        super(Unit, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Controls", "Measurements", "MetaBlockConOutput", "MetaBlockConInput", "ProtectionEquipments"]
    _many_refs = ["Controls", "Measurements", "MetaBlockConOutput", "MetaBlockConInput", "ProtectionEquipments"]

    def getControls(self):
        """The Controls having the Unit.
        """
        return self._Controls

    def setControls(self, value):
        for x in self._Controls:
            x.Unit = None
        for y in value:
            y._Unit = self
        self._Controls = value

    Controls = property(getControls, setControls)

    def addControls(self, *Controls):
        for obj in Controls:
            obj.Unit = self

    def removeControls(self, *Controls):
        for obj in Controls:
            obj.Unit = None

    def getMeasurements(self):
        """The Measurements having the Unit
        """
        return self._Measurements

    def setMeasurements(self, value):
        for x in self._Measurements:
            x.Unit = None
        for y in value:
            y._Unit = self
        self._Measurements = value

    Measurements = property(getMeasurements, setMeasurements)

    def addMeasurements(self, *Measurements):
        for obj in Measurements:
            obj.Unit = self

    def removeMeasurements(self, *Measurements):
        for obj in Measurements:
            obj.Unit = None

    def getMetaBlockConOutput(self):
        
        return self._MetaBlockConOutput

    def setMetaBlockConOutput(self, value):
        for x in self._MetaBlockConOutput:
            x.Unit = None
        for y in value:
            y._Unit = self
        self._MetaBlockConOutput = value

    MetaBlockConOutput = property(getMetaBlockConOutput, setMetaBlockConOutput)

    def addMetaBlockConOutput(self, *MetaBlockConOutput):
        for obj in MetaBlockConOutput:
            obj.Unit = self

    def removeMetaBlockConOutput(self, *MetaBlockConOutput):
        for obj in MetaBlockConOutput:
            obj.Unit = None

    def getMetaBlockConInput(self):
        
        return self._MetaBlockConInput

    def setMetaBlockConInput(self, value):
        for x in self._MetaBlockConInput:
            x.Unit = None
        for y in value:
            y._Unit = self
        self._MetaBlockConInput = value

    MetaBlockConInput = property(getMetaBlockConInput, setMetaBlockConInput)

    def addMetaBlockConInput(self, *MetaBlockConInput):
        for obj in MetaBlockConInput:
            obj.Unit = self

    def removeMetaBlockConInput(self, *MetaBlockConInput):
        for obj in MetaBlockConInput:
            obj.Unit = None

    def getProtectionEquipments(self):
        """The Protection Equipments having the Unit.
        """
        return self._ProtectionEquipments

    def setProtectionEquipments(self, value):
        for x in self._ProtectionEquipments:
            x.Unit = None
        for y in value:
            y._Unit = self
        self._ProtectionEquipments = value

    ProtectionEquipments = property(getProtectionEquipments, setProtectionEquipments)

    def addProtectionEquipments(self, *ProtectionEquipments):
        for obj in ProtectionEquipments:
            obj.Unit = self

    def removeProtectionEquipments(self, *ProtectionEquipments):
        for obj in ProtectionEquipments:
            obj.Unit = None

