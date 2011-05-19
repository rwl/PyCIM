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

class GmlLabelPlacement(IdentifiedObject):
    """Used to position a label relative to a point or a line.Used to position a label relative to a point or a line.
    """

    def __init__(self, displacementX='', rotation='', displacementY='', type='', anchorX='', anchorY='', offset='', GmlTextSymbols=None, *args, **kw_args):
        """Initialises a new 'GmlLabelPlacement' instance.

        @param displacementX: X displacement from the main-geometry point to render a text label. 
        @param rotation: Clockwise rotation of the label in degrees from the normal direction for a font. 
        @param displacementY: Y displacement from the main-geometry point to render a text label. 
        @param type: Type of 'LabelPlacement' which in turn specifies where and how a text label should be rendered relative to a geometry. 
        @param anchorX: X-coordinate location inside of a label to use for anchoring the label to the main-geometry point. 
        @param anchorY: Y-coordinate location inside of a label to use for anchoring the label to the main-geometry point. 
        @param offset: Perpendicular distance away from a line to draw a label. The distance is in pixels and is positive to the left-hand side of the line string. Negative numbers mean right. The default offset is 0. 
        @param GmlTextSymbols:
        """
        #: X displacement from the main-geometry point to render a text label.
        self.displacementX = displacementX

        #: Clockwise rotation of the label in degrees from the normal direction for a font.
        self.rotation = rotation

        #: Y displacement from the main-geometry point to render a text label.
        self.displacementY = displacementY

        #: Type of 'LabelPlacement' which in turn specifies where and how a text label should be rendered relative to a geometry.
        self.type = type

        #: X-coordinate location inside of a label to use for anchoring the label to the main-geometry point.
        self.anchorX = anchorX

        #: Y-coordinate location inside of a label to use for anchoring the label to the main-geometry point.
        self.anchorY = anchorY

        #: Perpendicular distance away from a line to draw a label. The distance is in pixels and is positive to the left-hand side of the line string. Negative numbers mean right. The default offset is 0.
        self.offset = offset

        self._GmlTextSymbols = []
        self.GmlTextSymbols = [] if GmlTextSymbols is None else GmlTextSymbols

        super(GmlLabelPlacement, self).__init__(*args, **kw_args)

    _attrs = ["displacementX", "rotation", "displacementY", "type", "anchorX", "anchorY", "offset"]
    _attr_types = {"displacementX": str, "rotation": str, "displacementY": str, "type": str, "anchorX": str, "anchorY": str, "offset": str}
    _defaults = {"displacementX": '', "rotation": '', "displacementY": '', "type": '', "anchorX": '', "anchorY": '', "offset": ''}
    _enums = {}
    _refs = ["GmlTextSymbols"]
    _many_refs = ["GmlTextSymbols"]

    def getGmlTextSymbols(self):
        
        return self._GmlTextSymbols

    def setGmlTextSymbols(self, value):
        for x in self._GmlTextSymbols:
            x.GmlLabelPlacement = None
        for y in value:
            y._GmlLabelPlacement = self
        self._GmlTextSymbols = value

    GmlTextSymbols = property(getGmlTextSymbols, setGmlTextSymbols)

    def addGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj.GmlLabelPlacement = self

    def removeGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj.GmlLabelPlacement = None

