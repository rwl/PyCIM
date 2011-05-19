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

from CIM15.IEC61968.Assets.Asset import Asset

class ConductorAsset(Asset):
    """Physical asset used to perform the conductor's role.Physical asset used to perform the conductor's role.
    """

    def __init__(self, isHorizontal=False, groundingMethod='', insulated=False, CircuitSection=None, ConductorSegment=None, *args, **kw_args):
        """Initialises a new 'ConductorAsset' instance.

        @param isHorizontal: True when orientation is horizontal (e.g., transmission and distribution lines), false if vertical (e.g. a riser for underground to overhead service). 
        @param groundingMethod: Description of the method used for grounding the conductor. For a cable, the grounding/bonding shield may be multi-point, single-point, cross cable, or other. 
        @param insulated: True if conductor asset has an insulator around the core material. 
        @param CircuitSection:
        @param ConductorSegment:
        """
        #: True when orientation is horizontal (e.g., transmission and distribution lines), false if vertical (e.g. a riser for underground to overhead service).
        self.isHorizontal = isHorizontal

        #: Description of the method used for grounding the conductor. For a cable, the grounding/bonding shield may be multi-point, single-point, cross cable, or other.
        self.groundingMethod = groundingMethod

        #: True if conductor asset has an insulator around the core material.
        self.insulated = insulated

        self._CircuitSection = None
        self.CircuitSection = CircuitSection

        self._ConductorSegment = None
        self.ConductorSegment = ConductorSegment

        super(ConductorAsset, self).__init__(*args, **kw_args)

    _attrs = ["isHorizontal", "groundingMethod", "insulated"]
    _attr_types = {"isHorizontal": bool, "groundingMethod": str, "insulated": bool}
    _defaults = {"isHorizontal": False, "groundingMethod": '', "insulated": False}
    _enums = {}
    _refs = ["CircuitSection", "ConductorSegment"]
    _many_refs = []

    def getCircuitSection(self):
        
        return self._CircuitSection

    def setCircuitSection(self, value):
        if self._CircuitSection is not None:
            filtered = [x for x in self.CircuitSection.ConductorAssets if x != self]
            self._CircuitSection._ConductorAssets = filtered

        self._CircuitSection = value
        if self._CircuitSection is not None:
            if self not in self._CircuitSection._ConductorAssets:
                self._CircuitSection._ConductorAssets.append(self)

    CircuitSection = property(getCircuitSection, setCircuitSection)

    def getConductorSegment(self):
        
        return self._ConductorSegment

    def setConductorSegment(self, value):
        if self._ConductorSegment is not None:
            filtered = [x for x in self.ConductorSegment.ConductorAssets if x != self]
            self._ConductorSegment._ConductorAssets = filtered

        self._ConductorSegment = value
        if self._ConductorSegment is not None:
            if self not in self._ConductorSegment._ConductorAssets:
                self._ConductorSegment._ConductorAssets.append(self)

    ConductorSegment = property(getConductorSegment, setConductorSegment)

