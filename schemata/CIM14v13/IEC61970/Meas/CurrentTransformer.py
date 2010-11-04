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

class CurrentTransformer(Equipment):
    """Instrument transformer used to measure electrical qualities of the circuit that is being protected and/or monitored. Typically used as current transducer for the purpose of metering or protection. A typical secondary current rating would be 5A.
    """

    def __init__(self, accuracyClass='', accuracyLimit='', usage='', coreCount=0, maxRatio=0.0, ctClass='', CurrentTransformerTypeAsset=None, CurrentTransformerAsset=None, *args, **kw_args):
        """Initializes a new 'CurrentTransformer' instance.

        @param accuracyClass: CT accuracy classification. 
        @param accuracyLimit: Percent of rated current for which the CT remains accurate within specified limits. 
        @param usage: Intended usage of the CT; i.e. metering, protection. 
        @param coreCount: Number of cores. 
        @param maxRatio: For multi-ratio CT's, the maximum permissable ratio attainable. 
        @param ctClass: CT classification; i.e. class 10P. 
        @param CurrentTransformerTypeAsset:
        @param CurrentTransformerAsset:
        """
        #: CT accuracy classification.
        self.accuracyClass = accuracyClass

        #: Percent of rated current for which the CT remains accurate within specified limits.
        self.accuracyLimit = accuracyLimit

        #: Intended usage of the CT; i.e. metering, protection.
        self.usage = usage

        #: Number of cores.
        self.coreCount = coreCount

        #: For multi-ratio CT's, the maximum permissable ratio attainable.
        self.maxRatio = maxRatio

        #: CT classification; i.e. class 10P.
        self.ctClass = ctClass

        self._CurrentTransformerTypeAsset = None
        self.CurrentTransformerTypeAsset = CurrentTransformerTypeAsset

        self._CurrentTransformerAsset = None
        self.CurrentTransformerAsset = CurrentTransformerAsset

        super(CurrentTransformer, self).__init__(*args, **kw_args)

    def getCurrentTransformerTypeAsset(self):
        
        return self._CurrentTransformerTypeAsset

    def setCurrentTransformerTypeAsset(self, value):
        if self._CurrentTransformerTypeAsset is not None:
            filtered = [x for x in self.CurrentTransformerTypeAsset.CurrentTransformers if x != self]
            self._CurrentTransformerTypeAsset._CurrentTransformers = filtered

        self._CurrentTransformerTypeAsset = value
        if self._CurrentTransformerTypeAsset is not None:
            self._CurrentTransformerTypeAsset._CurrentTransformers.append(self)

    CurrentTransformerTypeAsset = property(getCurrentTransformerTypeAsset, setCurrentTransformerTypeAsset)

    def getCurrentTransformerAsset(self):
        
        return self._CurrentTransformerAsset

    def setCurrentTransformerAsset(self, value):
        if self._CurrentTransformerAsset is not None:
            self._CurrentTransformerAsset._CurrentTransformer = None

        self._CurrentTransformerAsset = value
        if self._CurrentTransformerAsset is not None:
            self._CurrentTransformerAsset._CurrentTransformer = self

    CurrentTransformerAsset = property(getCurrentTransformerAsset, setCurrentTransformerAsset)

