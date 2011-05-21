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

from CIM14.ENTSOE.Dynamics.IEC61970.Core.CoreIdentifiedObject import CoreIdentifiedObject

class CorePowerSystemResource(CoreIdentifiedObject):

    def __init__(self, Block=None, Location=None, ReportingGroup=None, PsrLists=None, OperatingShare=None, OutageSchedule=None, Measurements=None, Assets=None, PSRType=None, *args, **kw_args):
        """Initialises a new 'CorePowerSystemResource' instance.

        @param Block:
        @param Location:
        @param ReportingGroup:
        @param PsrLists:
        @param OperatingShare:
        @param OutageSchedule:
        @param Measurements:
        @param Assets:
        @param PSRType:
        """
        self._Block = []
        self.Block = [] if Block is None else Block

        self._Location = None
        self.Location = Location

        self._ReportingGroup = []
        self.ReportingGroup = [] if ReportingGroup is None else ReportingGroup

        self._PsrLists = []
        self.PsrLists = [] if PsrLists is None else PsrLists

        self._OperatingShare = []
        self.OperatingShare = [] if OperatingShare is None else OperatingShare

        self._OutageSchedule = None
        self.OutageSchedule = OutageSchedule

        self._Measurements = []
        self.Measurements = [] if Measurements is None else Measurements

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        self._PSRType = None
        self.PSRType = PSRType

        super(CorePowerSystemResource, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Block", "Location", "ReportingGroup", "PsrLists", "OperatingShare", "OutageSchedule", "Measurements", "Assets", "PSRType"]
    _many_refs = ["Block", "ReportingGroup", "PsrLists", "OperatingShare", "Measurements", "Assets"]

    def getBlock(self):
        
        return self._Block

    def setBlock(self, value):
        for x in self._Block:
            x.PowerSystemResource = None
        for y in value:
            y._PowerSystemResource = self
        self._Block = value

    Block = property(getBlock, setBlock)

    def addBlock(self, *Block):
        for obj in Block:
            obj.PowerSystemResource = self

    def removeBlock(self, *Block):
        for obj in Block:
            obj.PowerSystemResource = None

    def getLocation(self):
        
        return self._Location

    def setLocation(self, value):
        if self._Location is not None:
            filtered = [x for x in self.Location.PowerSystemResources if x != self]
            self._Location._PowerSystemResources = filtered

        self._Location = value
        if self._Location is not None:
            if self not in self._Location._PowerSystemResources:
                self._Location._PowerSystemResources.append(self)

    Location = property(getLocation, setLocation)

    def getReportingGroup(self):
        
        return self._ReportingGroup

    def setReportingGroup(self, value):
        for p in self._ReportingGroup:
            filtered = [q for q in p.PowerSystemResource if q != self]
            self._ReportingGroup._PowerSystemResource = filtered
        for r in value:
            if self not in r._PowerSystemResource:
                r._PowerSystemResource.append(self)
        self._ReportingGroup = value

    ReportingGroup = property(getReportingGroup, setReportingGroup)

    def addReportingGroup(self, *ReportingGroup):
        for obj in ReportingGroup:
            if self not in obj._PowerSystemResource:
                obj._PowerSystemResource.append(self)
            self._ReportingGroup.append(obj)

    def removeReportingGroup(self, *ReportingGroup):
        for obj in ReportingGroup:
            if self in obj._PowerSystemResource:
                obj._PowerSystemResource.remove(self)
            self._ReportingGroup.remove(obj)

    def getPsrLists(self):
        
        return self._PsrLists

    def setPsrLists(self, value):
        for p in self._PsrLists:
            filtered = [q for q in p.PowerSystemResources if q != self]
            self._PsrLists._PowerSystemResources = filtered
        for r in value:
            if self not in r._PowerSystemResources:
                r._PowerSystemResources.append(self)
        self._PsrLists = value

    PsrLists = property(getPsrLists, setPsrLists)

    def addPsrLists(self, *PsrLists):
        for obj in PsrLists:
            if self not in obj._PowerSystemResources:
                obj._PowerSystemResources.append(self)
            self._PsrLists.append(obj)

    def removePsrLists(self, *PsrLists):
        for obj in PsrLists:
            if self in obj._PowerSystemResources:
                obj._PowerSystemResources.remove(self)
            self._PsrLists.remove(obj)

    def getOperatingShare(self):
        
        return self._OperatingShare

    def setOperatingShare(self, value):
        for x in self._OperatingShare:
            x.PowerSystemResource = None
        for y in value:
            y._PowerSystemResource = self
        self._OperatingShare = value

    OperatingShare = property(getOperatingShare, setOperatingShare)

    def addOperatingShare(self, *OperatingShare):
        for obj in OperatingShare:
            obj.PowerSystemResource = self

    def removeOperatingShare(self, *OperatingShare):
        for obj in OperatingShare:
            obj.PowerSystemResource = None

    def getOutageSchedule(self):
        
        return self._OutageSchedule

    def setOutageSchedule(self, value):
        if self._OutageSchedule is not None:
            self._OutageSchedule._PowerSystemResource = None

        self._OutageSchedule = value
        if self._OutageSchedule is not None:
            self._OutageSchedule.PowerSystemResource = None
            self._OutageSchedule._PowerSystemResource = self

    OutageSchedule = property(getOutageSchedule, setOutageSchedule)

    def getMeasurements(self):
        
        return self._Measurements

    def setMeasurements(self, value):
        for x in self._Measurements:
            x.PowerSystemResource = None
        for y in value:
            y._PowerSystemResource = self
        self._Measurements = value

    Measurements = property(getMeasurements, setMeasurements)

    def addMeasurements(self, *Measurements):
        for obj in Measurements:
            obj.PowerSystemResource = self

    def removeMeasurements(self, *Measurements):
        for obj in Measurements:
            obj.PowerSystemResource = None

    def getAssets(self):
        
        return self._Assets

    def setAssets(self, value):
        for p in self._Assets:
            filtered = [q for q in p.PowerSystemResources if q != self]
            self._Assets._PowerSystemResources = filtered
        for r in value:
            if self not in r._PowerSystemResources:
                r._PowerSystemResources.append(self)
        self._Assets = value

    Assets = property(getAssets, setAssets)

    def addAssets(self, *Assets):
        for obj in Assets:
            if self not in obj._PowerSystemResources:
                obj._PowerSystemResources.append(self)
            self._Assets.append(obj)

    def removeAssets(self, *Assets):
        for obj in Assets:
            if self in obj._PowerSystemResources:
                obj._PowerSystemResources.remove(self)
            self._Assets.remove(obj)

    def getPSRType(self):
        
        return self._PSRType

    def setPSRType(self, value):
        if self._PSRType is not None:
            filtered = [x for x in self.PSRType.PowerSystemResources if x != self]
            self._PSRType._PowerSystemResources = filtered

        self._PSRType = value
        if self._PSRType is not None:
            if self not in self._PSRType._PowerSystemResources:
                self._PSRType._PowerSystemResources.append(self)

    PSRType = property(getPSRType, setPSRType)

