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

from CIM15.CDPSM.Asset.IEC61970.Core.IdentifiedObject import IdentifiedObject

class TransformerEnd(IdentifiedObject):
    """TransformerEnd is a conducting connection point of a power transformer. It corresponds to a physical transformer winding terminal.  In earlier CIM versions, the TransformerWinding class served a similar purpose. This successor TransformerEnd class is more flexible and has important differences with TransformerWinding.
    """

    def __init__(self, CoreAdmittance=None, TransformerEndInfo=None, StarImpedance=None, *args, **kw_args):
        """Initialises a new 'TransformerEnd' instance.

        @param CoreAdmittance: Core admittance of this transformer end, representing magnetising current and core losses. The full values of the transformer should be supplied for one transformer end only.
        @param TransformerEndInfo: Data for this transformer end.
        @param StarImpedance: (accurate for 2- or 3-winding transformers only) Pi-model impedances of this transformer end. By convention, for a two winding transformer, the full values of the transformer should be entered on the high voltage end (endNumber=1).
        """
        self._CoreAdmittance = None
        self.CoreAdmittance = CoreAdmittance

        self._TransformerEndInfo = None
        self.TransformerEndInfo = TransformerEndInfo

        self._StarImpedance = None
        self.StarImpedance = StarImpedance

        super(TransformerEnd, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["CoreAdmittance", "TransformerEndInfo", "StarImpedance"]
    _many_refs = []

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

    def getTransformerEndInfo(self):
        """Data for this transformer end.
        """
        return self._TransformerEndInfo

    def setTransformerEndInfo(self, value):
        if self._TransformerEndInfo is not None:
            filtered = [x for x in self.TransformerEndInfo.TransformerEnd if x != self]
            self._TransformerEndInfo._TransformerEnd = filtered

        self._TransformerEndInfo = value
        if self._TransformerEndInfo is not None:
            if self not in self._TransformerEndInfo._TransformerEnd:
                self._TransformerEndInfo._TransformerEnd.append(self)

    TransformerEndInfo = property(getTransformerEndInfo, setTransformerEndInfo)

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

