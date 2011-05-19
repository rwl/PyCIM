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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class Medium(IdentifiedObject):
    """A substance that either (1) provides the means of transmission of a force or effect, such as hydraulic fluid, or (2) is used for a surrounding or enveloping substance, such as oil in a transformer or circuit breaker.A substance that either (1) provides the means of transmission of a force or effect, such as hydraulic fluid, or (2) is used for a surrounding or enveloping substance, such as oil in a transformer or circuit breaker.
    """

    def __init__(self, kind="gas", volumeSpec=0.0, Specification=None, Assets=None, *args, **kw_args):
        """Initialises a new 'Medium' instance.

        @param kind: Kind of this medium. Values are: "gas", "liquid", "solid"
        @param volumeSpec: The volume of the medium specified for this application. Note that the actual volume is a type of measurement associated witht the asset. 
        @param Specification:
        @param Assets:
        """
        #: Kind of this medium. Values are: "gas", "liquid", "solid"
        self.kind = kind

        #: The volume of the medium specified for this application. Note that the actual volume is a type of measurement associated witht the asset.
        self.volumeSpec = volumeSpec

        self._Specification = None
        self.Specification = Specification

        self._Assets = []
        self.Assets = [] if Assets is None else Assets

        super(Medium, self).__init__(*args, **kw_args)

    _attrs = ["kind", "volumeSpec"]
    _attr_types = {"kind": str, "volumeSpec": float}
    _defaults = {"kind": "gas", "volumeSpec": 0.0}
    _enums = {"kind": "MediumKind"}
    _refs = ["Specification", "Assets"]
    _many_refs = ["Assets"]

    def getSpecification(self):
        
        return self._Specification

    def setSpecification(self, value):
        if self._Specification is not None:
            filtered = [x for x in self.Specification.Mediums if x != self]
            self._Specification._Mediums = filtered

        self._Specification = value
        if self._Specification is not None:
            if self not in self._Specification._Mediums:
                self._Specification._Mediums.append(self)

    Specification = property(getSpecification, setSpecification)

    def getAssets(self):
        
        return self._Assets

    def setAssets(self, value):
        for p in self._Assets:
            filtered = [q for q in p.Mediums if q != self]
            self._Assets._Mediums = filtered
        for r in value:
            if self not in r._Mediums:
                r._Mediums.append(self)
        self._Assets = value

    Assets = property(getAssets, setAssets)

    def addAssets(self, *Assets):
        for obj in Assets:
            if self not in obj._Mediums:
                obj._Mediums.append(self)
            self._Assets.append(obj)

    def removeAssets(self, *Assets):
        for obj in Assets:
            if self in obj._Mediums:
                obj._Mediums.remove(self)
            self._Assets.remove(obj)

