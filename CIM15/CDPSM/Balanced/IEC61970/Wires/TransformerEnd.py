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

from CIM15.CDPSM.Balanced.IEC61970.Core.IdentifiedObject import IdentifiedObject

class TransformerEnd(IdentifiedObject):
    """TransformerEnd is a conducting connection point of a power transformer. It corresponds to a physical transformer winding terminal.  In earlier CIM versions, the TransformerWinding class served a similar purpose. This successor TransformerEnd class is more flexible and has important differences with TransformerWinding.
    """

    def __init__(self, FromMeshImpedance=None, ToMeshImpedance=None, CoreAdmittance=None, StarImpedance=None, *args, **kw_args):
        """Initialises a new 'TransformerEnd' instance.

        @param FromMeshImpedance: All mesh impedances between this 'to' and other 'from' transformer ends.
        @param ToMeshImpedance: All mesh impedances between this 'from' and other 'to' transformer ends.
        @param CoreAdmittance: Core admittance of this transformer end, representing magnetising current and core losses. The full values of the transformer should be supplied for one transformer end only.
        @param StarImpedance: (accurate for 2- or 3-winding transformers only) Pi-model impedances of this transformer end. By convention, for a two winding transformer, the full values of the transformer should be entered on the high voltage end (endNumber=1).
        """
        self._FromMeshImpedance = []
        self.FromMeshImpedance = [] if FromMeshImpedance is None else FromMeshImpedance

        self._ToMeshImpedance = []
        self.ToMeshImpedance = [] if ToMeshImpedance is None else ToMeshImpedance

        self._CoreAdmittance = None
        self.CoreAdmittance = CoreAdmittance

        self._StarImpedance = None
        self.StarImpedance = StarImpedance

        super(TransformerEnd, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["FromMeshImpedance", "ToMeshImpedance", "CoreAdmittance", "StarImpedance"]
    _many_refs = ["FromMeshImpedance", "ToMeshImpedance"]

    def getFromMeshImpedance(self):
        """All mesh impedances between this 'to' and other 'from' transformer ends.
        """
        return self._FromMeshImpedance

    def setFromMeshImpedance(self, value):
        for x in self._FromMeshImpedance:
            x.FromTransformerEnd = None
        for y in value:
            y._FromTransformerEnd = self
        self._FromMeshImpedance = value

    FromMeshImpedance = property(getFromMeshImpedance, setFromMeshImpedance)

    def addFromMeshImpedance(self, *FromMeshImpedance):
        for obj in FromMeshImpedance:
            obj.FromTransformerEnd = self

    def removeFromMeshImpedance(self, *FromMeshImpedance):
        for obj in FromMeshImpedance:
            obj.FromTransformerEnd = None

    def getToMeshImpedance(self):
        """All mesh impedances between this 'from' and other 'to' transformer ends.
        """
        return self._ToMeshImpedance

    def setToMeshImpedance(self, value):
        for p in self._ToMeshImpedance:
            filtered = [q for q in p.ToTransformerEnd if q != self]
            self._ToMeshImpedance._ToTransformerEnd = filtered
        for r in value:
            if self not in r._ToTransformerEnd:
                r._ToTransformerEnd.append(self)
        self._ToMeshImpedance = value

    ToMeshImpedance = property(getToMeshImpedance, setToMeshImpedance)

    def addToMeshImpedance(self, *ToMeshImpedance):
        for obj in ToMeshImpedance:
            if self not in obj._ToTransformerEnd:
                obj._ToTransformerEnd.append(self)
            self._ToMeshImpedance.append(obj)

    def removeToMeshImpedance(self, *ToMeshImpedance):
        for obj in ToMeshImpedance:
            if self in obj._ToTransformerEnd:
                obj._ToTransformerEnd.remove(self)
            self._ToMeshImpedance.remove(obj)

    def getCoreAdmittance(self):
        """Core admittance of this transformer end, representing magnetising current and core losses. The full values of the transformer should be supplied for one transformer end only.
        """
        return self._CoreAdmittance

    def setCoreAdmittance(self, value):
        if self._CoreAdmittance is not None:
            filtered = [x for x in self.CoreAdmittance.TransformerEnd if x != self]
            self._CoreAdmittance._TransformerEnd = filtered

        self._CoreAdmittance = value
        if self._CoreAdmittance is not None:
            if self not in self._CoreAdmittance._TransformerEnd:
                self._CoreAdmittance._TransformerEnd.append(self)

    CoreAdmittance = property(getCoreAdmittance, setCoreAdmittance)

    def getStarImpedance(self):
        """(accurate for 2- or 3-winding transformers only) Pi-model impedances of this transformer end. By convention, for a two winding transformer, the full values of the transformer should be entered on the high voltage end (endNumber=1).
        """
        return self._StarImpedance

    def setStarImpedance(self, value):
        if self._StarImpedance is not None:
            filtered = [x for x in self.StarImpedance.TransformerEnd if x != self]
            self._StarImpedance._TransformerEnd = filtered

        self._StarImpedance = value
        if self._StarImpedance is not None:
            if self not in self._StarImpedance._TransformerEnd:
                self._StarImpedance._TransformerEnd.append(self)

    StarImpedance = property(getStarImpedance, setStarImpedance)

