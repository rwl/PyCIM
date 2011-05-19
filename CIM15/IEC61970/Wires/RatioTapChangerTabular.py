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

from CIM15.Element import Element

class RatioTapChangerTabular(Element):
    """With RatioTapChangerTabular it is possible to describe curve how the voltage magnitude and reactance varies with the tap step.With RatioTapChangerTabular it is possible to describe curve how the voltage magnitude and reactance varies with the tap step.
    """

    def __init__(self, RatioTapChangerTabularPoint=None, RatioTapChanger=None, *args, **kw_args):
        """Initialises a new 'RatioTapChangerTabular' instance.

        @param RatioTapChangerTabularPoint:
        @param RatioTapChanger:
        """
        self._RatioTapChangerTabularPoint = []
        self.RatioTapChangerTabularPoint = [] if RatioTapChangerTabularPoint is None else RatioTapChangerTabularPoint

        self._RatioTapChanger = []
        self.RatioTapChanger = [] if RatioTapChanger is None else RatioTapChanger

        super(RatioTapChangerTabular, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["RatioTapChangerTabularPoint", "RatioTapChanger"]
    _many_refs = ["RatioTapChangerTabularPoint", "RatioTapChanger"]

    def getRatioTapChangerTabularPoint(self):
        
        return self._RatioTapChangerTabularPoint

    def setRatioTapChangerTabularPoint(self, value):
        for x in self._RatioTapChangerTabularPoint:
            x.RatioTapChangerTabular = None
        for y in value:
            y._RatioTapChangerTabular = self
        self._RatioTapChangerTabularPoint = value

    RatioTapChangerTabularPoint = property(getRatioTapChangerTabularPoint, setRatioTapChangerTabularPoint)

    def addRatioTapChangerTabularPoint(self, *RatioTapChangerTabularPoint):
        for obj in RatioTapChangerTabularPoint:
            obj.RatioTapChangerTabular = self

    def removeRatioTapChangerTabularPoint(self, *RatioTapChangerTabularPoint):
        for obj in RatioTapChangerTabularPoint:
            obj.RatioTapChangerTabular = None

    def getRatioTapChanger(self):
        
        return self._RatioTapChanger

    def setRatioTapChanger(self, value):
        for x in self._RatioTapChanger:
            x.RatioTapChangerTabular = None
        for y in value:
            y._RatioTapChangerTabular = self
        self._RatioTapChanger = value

    RatioTapChanger = property(getRatioTapChanger, setRatioTapChanger)

    def addRatioTapChanger(self, *RatioTapChanger):
        for obj in RatioTapChanger:
            obj.RatioTapChangerTabular = self

    def removeRatioTapChanger(self, *RatioTapChanger):
        for obj in RatioTapChanger:
            obj.RatioTapChangerTabular = None

