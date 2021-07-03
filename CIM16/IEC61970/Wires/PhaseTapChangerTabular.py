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

from CIM16.Element import Element

class PhaseTapChangerTabular(Element):
    """With PhaseTapChangerTabular it is possible to describe curve how the the phase angle difference and reactance varies with the tap step.With PhaseTapChangerTabular it is possible to describe curve how the the phase angle difference and reactance varies with the tap step.
    """

    def __init__(self, PhaseTapChangerTabularPoint=None, PhaseTapChanger=None, *args, **kw_args):
        """Initialises a new 'PhaseTapChangerTabular' instance.

        @param PhaseTapChangerTabularPoint:
        @param PhaseTapChanger:
        """
        self._PhaseTapChangerTabularPoint = []
        self.PhaseTapChangerTabularPoint = [] if PhaseTapChangerTabularPoint is None else PhaseTapChangerTabularPoint

        self._PhaseTapChanger = []
        self.PhaseTapChanger = [] if PhaseTapChanger is None else PhaseTapChanger

        super(PhaseTapChangerTabular, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["PhaseTapChangerTabularPoint", "PhaseTapChanger"]
    _many_refs = ["PhaseTapChangerTabularPoint", "PhaseTapChanger"]

    def getPhaseTapChangerTabularPoint(self):
        
        return self._PhaseTapChangerTabularPoint

    def setPhaseTapChangerTabularPoint(self, value):
        for x in self._PhaseTapChangerTabularPoint:
            x.PhaseTapChangerTabular = None
        for y in value:
            y._PhaseTapChangerTabular = self
        self._PhaseTapChangerTabularPoint = value

    PhaseTapChangerTabularPoint = property(getPhaseTapChangerTabularPoint, setPhaseTapChangerTabularPoint)

    def addPhaseTapChangerTabularPoint(self, *PhaseTapChangerTabularPoint):
        for obj in PhaseTapChangerTabularPoint:
            obj.PhaseTapChangerTabular = self

    def removePhaseTapChangerTabularPoint(self, *PhaseTapChangerTabularPoint):
        for obj in PhaseTapChangerTabularPoint:
            obj.PhaseTapChangerTabular = None

    def getPhaseTapChanger(self):
        
        return self._PhaseTapChanger

    def setPhaseTapChanger(self, value):
        for x in self._PhaseTapChanger:
            x.PhaseTapChangerTabular = None
        for y in value:
            y._PhaseTapChangerTabular = self
        self._PhaseTapChanger = value

    PhaseTapChanger = property(getPhaseTapChanger, setPhaseTapChanger)

    def addPhaseTapChanger(self, *PhaseTapChanger):
        for obj in PhaseTapChanger:
            obj.PhaseTapChangerTabular = self

    def removePhaseTapChanger(self, *PhaseTapChanger):
        for obj in PhaseTapChanger:
            obj.PhaseTapChangerTabular = None

