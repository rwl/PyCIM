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

class TransformerInfo(IdentifiedObject):
    """Set of transformer data, from an equipment library.
    """

    def __init__(self, WindingInfos=None, Transformers=None, *args, **kw_args):
        """Initialises a new 'TransformerInfo' instance.

        @param WindingInfos: Data for all the windings described by this transformer data.
        @param Transformers: All transformers that can be described with this transformer data.
        """
        self._WindingInfos = []
        self.WindingInfos = [] if WindingInfos is None else WindingInfos

        self._Transformers = []
        self.Transformers = [] if Transformers is None else Transformers

        super(TransformerInfo, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["WindingInfos", "Transformers"]
    _many_refs = ["WindingInfos", "Transformers"]

    def getWindingInfos(self):
        """Data for all the windings described by this transformer data.
        """
        return self._WindingInfos

    def setWindingInfos(self, value):
        for x in self._WindingInfos:
            x.TransformerInfo = None
        for y in value:
            y._TransformerInfo = self
        self._WindingInfos = value

    WindingInfos = property(getWindingInfos, setWindingInfos)

    def addWindingInfos(self, *WindingInfos):
        for obj in WindingInfos:
            obj.TransformerInfo = self

    def removeWindingInfos(self, *WindingInfos):
        for obj in WindingInfos:
            obj.TransformerInfo = None

    def getTransformers(self):
        """All transformers that can be described with this transformer data.
        """
        return self._Transformers

    def setTransformers(self, value):
        for x in self._Transformers:
            x.TransformerInfo = None
        for y in value:
            y._TransformerInfo = self
        self._Transformers = value

    Transformers = property(getTransformers, setTransformers)

    def addTransformers(self, *Transformers):
        for obj in Transformers:
            obj.TransformerInfo = self

    def removeTransformers(self, *Transformers):
        for obj in Transformers:
            obj.TransformerInfo = None

