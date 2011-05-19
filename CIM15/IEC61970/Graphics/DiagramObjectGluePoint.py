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

class DiagramObjectGluePoint(Element):
    """This is used for grouping DiagramObjectPoints from different DiagramObjects that are considered to be &lsquo;glued&rsquo; together in a diagram even if they are not at the exact same coordinates.This is used for grouping DiagramObjectPoints from different DiagramObjects that are considered to be &lsquo;glued&rsquo; together in a diagram even if they are not at the exact same coordinates.
    """

    def __init__(self, DiagramObjectPoints=None, *args, **kw_args):
        """Initialises a new 'DiagramObjectGluePoint' instance.

        @param DiagramObjectPoints: A diagram object glue point is associated with 2 or more object points that are considered to be 'glued' together.
        """
        self._DiagramObjectPoints = []
        self.DiagramObjectPoints = [] if DiagramObjectPoints is None else DiagramObjectPoints

        super(DiagramObjectGluePoint, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["DiagramObjectPoints"]
    _many_refs = ["DiagramObjectPoints"]

    def getDiagramObjectPoints(self):
        """A diagram object glue point is associated with 2 or more object points that are considered to be 'glued' together.
        """
        return self._DiagramObjectPoints

    def setDiagramObjectPoints(self, value):
        for x in self._DiagramObjectPoints:
            x.DiagramObjectGluePoint = None
        for y in value:
            y._DiagramObjectGluePoint = self
        self._DiagramObjectPoints = value

    DiagramObjectPoints = property(getDiagramObjectPoints, setDiagramObjectPoints)

    def addDiagramObjectPoints(self, *DiagramObjectPoints):
        for obj in DiagramObjectPoints:
            obj.DiagramObjectGluePoint = self

    def removeDiagramObjectPoints(self, *DiagramObjectPoints):
        for obj in DiagramObjectPoints:
            obj.DiagramObjectGluePoint = None

