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

from CIM14.CDPSM.Balanced.IEC61970.Core.IdentifiedObject import IdentifiedObject

class TransformerInfo(IdentifiedObject):
    """Set of transformer data, from an equipment library.
    """

    def __init__(self, Transformers=None, WindingInfos=None, *args, **kw_args):
        """Initialises a new 'TransformerInfo' instance.

        @param Transformers: All transformers that can be described with this transformer data.
        @param WindingInfos: Data for all the windings described by this transformer data.
        """
        self._Transformers = []
        self.Transformers = [] if Transformers is None else Transformers

        self._WindingInfos = []
        self.WindingInfos = [] if WindingInfos is None else WindingInfos

        super(TransformerInfo, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["Transformers", "WindingInfos"]
    _many_refs = ["Transformers", "WindingInfos"]

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

