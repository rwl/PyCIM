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

class GmlTopologyStyle(IdentifiedObject):
    """The style for one topology property. Similarly to the Geometry style, a feature can have multiple topology properties, thus multiple topology style descriptors can be specified within one feature style.The style for one topology property. Similarly to the Geometry style, a feature can have multiple topology properties, thus multiple topology style descriptors can be specified within one feature style.
    """

    def __init__(self, GmlLableStyle=None, GmlFeatureStyle=None, *args, **kw_args):
        """Initialises a new 'GmlTopologyStyle' instance.

        @param GmlLableStyle:
        @param GmlFeatureStyle:
        """
        self._GmlLableStyle = None
        self.GmlLableStyle = GmlLableStyle

        self._GmlFeatureStyle = None
        self.GmlFeatureStyle = GmlFeatureStyle

        super(GmlTopologyStyle, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["GmlLableStyle", "GmlFeatureStyle"]
    _many_refs = []

    def getGmlLableStyle(self):
        
        return self._GmlLableStyle

    def setGmlLableStyle(self, value):
        if self._GmlLableStyle is not None:
            filtered = [x for x in self.GmlLableStyle.GmlTopologyStyles if x != self]
            self._GmlLableStyle._GmlTopologyStyles = filtered

        self._GmlLableStyle = value
        if self._GmlLableStyle is not None:
            if self not in self._GmlLableStyle._GmlTopologyStyles:
                self._GmlLableStyle._GmlTopologyStyles.append(self)

    GmlLableStyle = property(getGmlLableStyle, setGmlLableStyle)

    def getGmlFeatureStyle(self):
        
        return self._GmlFeatureStyle

    def setGmlFeatureStyle(self, value):
        if self._GmlFeatureStyle is not None:
            filtered = [x for x in self.GmlFeatureStyle.GmlTobologyStyles if x != self]
            self._GmlFeatureStyle._GmlTobologyStyles = filtered

        self._GmlFeatureStyle = value
        if self._GmlFeatureStyle is not None:
            if self not in self._GmlFeatureStyle._GmlTobologyStyles:
                self._GmlFeatureStyle._GmlTobologyStyles.append(self)

    GmlFeatureStyle = property(getGmlFeatureStyle, setGmlFeatureStyle)

