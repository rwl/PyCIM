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

from CIM14v13.IEC61970.Core.Equipment import Equipment

class FaultIndicator(Equipment):
    """A FaultIndicator is typically only an indicator (which may or may not be remotely monitored), and not a piece of equipment that actually initiates a protection event. It is used for FLISR (Fault Location, Isolation and Restoration) purposes, assisting with the dispatch of crews to 'most likely' part of the network (i.e. assists with determining circuit section where the fault most likely happened).
    """

    def __init__(self, FaultIndicatorAssets=None, FaultIndicatorTypeAsset=None, **kw_args):
        """Initializes a new 'FaultIndicator' instance.

        @param FaultIndicatorAssets:
        @param FaultIndicatorTypeAsset:
        """
        self._FaultIndicatorAssets = []
        self.FaultIndicatorAssets = [] if FaultIndicatorAssets is None else FaultIndicatorAssets

        self._FaultIndicatorTypeAsset = None
        self.FaultIndicatorTypeAsset = FaultIndicatorTypeAsset

        super(FaultIndicator, self).__init__(**kw_args)

    def getFaultIndicatorAssets(self):
        
        return self._FaultIndicatorAssets

    def setFaultIndicatorAssets(self, value):
        for x in self._FaultIndicatorAssets:
            x._FaultIndicator = None
        for y in value:
            y._FaultIndicator = self
        self._FaultIndicatorAssets = value

    FaultIndicatorAssets = property(getFaultIndicatorAssets, setFaultIndicatorAssets)

    def addFaultIndicatorAssets(self, *FaultIndicatorAssets):
        for obj in FaultIndicatorAssets:
            obj._FaultIndicator = self
            self._FaultIndicatorAssets.append(obj)

    def removeFaultIndicatorAssets(self, *FaultIndicatorAssets):
        for obj in FaultIndicatorAssets:
            obj._FaultIndicator = None
            self._FaultIndicatorAssets.remove(obj)

    def getFaultIndicatorTypeAsset(self):
        
        return self._FaultIndicatorTypeAsset

    def setFaultIndicatorTypeAsset(self, value):
        if self._FaultIndicatorTypeAsset is not None:
            filtered = [x for x in self.FaultIndicatorTypeAsset.FaultIndicators if x != self]
            self._FaultIndicatorTypeAsset._FaultIndicators = filtered

        self._FaultIndicatorTypeAsset = value
        if self._FaultIndicatorTypeAsset is not None:
            self._FaultIndicatorTypeAsset._FaultIndicators.append(self)

    FaultIndicatorTypeAsset = property(getFaultIndicatorTypeAsset, setFaultIndicatorTypeAsset)

