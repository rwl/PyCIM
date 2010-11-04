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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class GmlLabelPlacement(IdentifiedObject):
    """Used to position a label relative to a point or a line.
    """

    def __init__(self, type='', offset='', anchorX='', rotation='', displacementY='', displacementX='', anchorY='', GmlTextSymbols=None, **kw_args):
        """Initializes a new 'GmlLabelPlacement' instance.

        @param type: Type of 'LabelPlacement' which in turn specifies where and how a text label should be rendered relative to a geometry. 
        @param offset: Perpendicular distance away from a line to draw a label. The distance is in pixels and is positive to the left-hand side of the line string. Negative numbers mean right. The default offset is 0. 
        @param anchorX: X-coordinate location inside of a label to use for anchoring the label to the main-geometry point. 
        @param rotation: Clockwise rotation of the label in degrees from the normal direction for a font. 
        @param displacementY: Y displacement from the main-geometry point to render a text label. 
        @param displacementX: X displacement from the main-geometry point to render a text label. 
        @param anchorY: Y-coordinate location inside of a label to use for anchoring the label to the main-geometry point. 
        @param GmlTextSymbols:
        """
        #: Type of 'LabelPlacement' which in turn specifies where and how a text label should be rendered relative to a geometry.
        self.type = type

        #: Perpendicular distance away from a line to draw a label. The distance is in pixels and is positive to the left-hand side of the line string. Negative numbers mean right. The default offset is 0.
        self.offset = offset

        #: X-coordinate location inside of a label to use for anchoring the label to the main-geometry point.
        self.anchorX = anchorX

        #: Clockwise rotation of the label in degrees from the normal direction for a font.
        self.rotation = rotation

        #: Y displacement from the main-geometry point to render a text label.
        self.displacementY = displacementY

        #: X displacement from the main-geometry point to render a text label.
        self.displacementX = displacementX

        #: Y-coordinate location inside of a label to use for anchoring the label to the main-geometry point.
        self.anchorY = anchorY

        self._GmlTextSymbols = []
        self.GmlTextSymbols = [] if GmlTextSymbols is None else GmlTextSymbols

        super(GmlLabelPlacement, self).__init__(**kw_args)

    def getGmlTextSymbols(self):
        
        return self._GmlTextSymbols

    def setGmlTextSymbols(self, value):
        for x in self._GmlTextSymbols:
            x._GmlLabelPlacement = None
        for y in value:
            y._GmlLabelPlacement = self
        self._GmlTextSymbols = value

    GmlTextSymbols = property(getGmlTextSymbols, setGmlTextSymbols)

    def addGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj._GmlLabelPlacement = self
            self._GmlTextSymbols.append(obj)

    def removeGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj._GmlLabelPlacement = None
            self._GmlTextSymbols.remove(obj)

