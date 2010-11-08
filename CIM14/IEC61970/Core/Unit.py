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
            x._Unit = None
        for y in value:
            y._Unit = self
        self._Controls = value

    Controls = property(getControls, setControls)

    def addControls(self, *Controls):
        for obj in Controls:
            obj._Unit = self
            self._Controls.append(obj)

    def removeControls(self, *Controls):
        for obj in Controls:
            obj._Unit = None
            self._Controls.remove(obj)

    def getMeasurements(self):
        """The Measurements having the Unit
        """
        return self._Measurements

    def setMeasurements(self, value):
        for x in self._Measurements:
            x._Unit = None
        for y in value:
            y._Unit = self
        self._Measurements = value

    Measurements = property(getMeasurements, setMeasurements)

    def addMeasurements(self, *Measurements):
        for obj in Measurements:
            obj._Unit = self
            self._Measurements.append(obj)

    def removeMeasurements(self, *Measurements):
        for obj in Measurements:
            obj._Unit = None
            self._Measurements.remove(obj)

    def getMetaBlockConOutput(self):
        
        return self._MetaBlockConOutput

    def setMetaBlockConOutput(self, value):
        for x in self._MetaBlockConOutput:
            x._Unit = None
        for y in value:
            y._Unit = self
        self._MetaBlockConOutput = value

    MetaBlockConOutput = property(getMetaBlockConOutput, setMetaBlockConOutput)

    def addMetaBlockConOutput(self, *MetaBlockConOutput):
        for obj in MetaBlockConOutput:
            obj._Unit = self
            self._MetaBlockConOutput.append(obj)

    def removeMetaBlockConOutput(self, *MetaBlockConOutput):
        for obj in MetaBlockConOutput:
            obj._Unit = None
            self._MetaBlockConOutput.remove(obj)

    def getMetaBlockConInput(self):
        
        return self._MetaBlockConInput

    def setMetaBlockConInput(self, value):
        for x in self._MetaBlockConInput:
            x._Unit = None
        for y in value:
            y._Unit = self
        self._MetaBlockConInput = value

    MetaBlockConInput = property(getMetaBlockConInput, setMetaBlockConInput)

    def addMetaBlockConInput(self, *MetaBlockConInput):
        for obj in MetaBlockConInput:
            obj._Unit = self
            self._MetaBlockConInput.append(obj)

    def removeMetaBlockConInput(self, *MetaBlockConInput):
        for obj in MetaBlockConInput:
            obj._Unit = None
            self._MetaBlockConInput.remove(obj)

    def getProtectionEquipments(self):
        """The Protection Equipments having the Unit.
        """
        return self._ProtectionEquipments

    def setProtectionEquipments(self, value):
        for x in self._ProtectionEquipments:
            x._Unit = None
        for y in value:
            y._Unit = self
        self._ProtectionEquipments = value

    ProtectionEquipments = property(getProtectionEquipments, setProtectionEquipments)

    def addProtectionEquipments(self, *ProtectionEquipments):
        for obj in ProtectionEquipments:
            obj._Unit = self
            self._ProtectionEquipments.append(obj)

    def removeProtectionEquipments(self, *ProtectionEquipments):
        for obj in ProtectionEquipments:
            obj._Unit = None
            self._ProtectionEquipments.remove(obj)

