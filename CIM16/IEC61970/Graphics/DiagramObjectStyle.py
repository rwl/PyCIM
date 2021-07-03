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

from CIM16.IEC61970.Core.IdentifiedObject import IdentifiedObject

class DiagramObjectStyle(IdentifiedObject):
    """A reference to a style used by the originating system for a DiagramObject.  A DiagramObjectStyle describes information such as  &bull; line thickness &bull; shape, e.g circle, rectangle ... &bull; colorA reference to a style used by the originating system for a DiagramObject.  A DiagramObjectStyle describes information such as  &bull; line thickness &bull; shape, e.g circle, rectangle ... &bull; color
    """

    def __init__(self, DiagramObjects=None, *args, **kw_args):
        """Initialises a new 'DiagramObjectStyle' instance.

        @param DiagramObjects: A style can be assigned to multiple DiagramObjects
        """
        self._DiagramObjects = []
        self.DiagramObjects = [] if DiagramObjects is None else DiagramObjects

        super(DiagramObjectStyle, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["DiagramObjects"]
    _many_refs = ["DiagramObjects"]

    def getDiagramObjects(self):
        """A style can be assigned to multiple DiagramObjects
        """
        return self._DiagramObjects

    def setDiagramObjects(self, value):
        for x in self._DiagramObjects:
            x.DiagramObjectStyle = None
        for y in value:
            y._DiagramObjectStyle = self
        self._DiagramObjects = value

    DiagramObjects = property(getDiagramObjects, setDiagramObjects)

    def addDiagramObjects(self, *DiagramObjects):
        for obj in DiagramObjects:
            obj.DiagramObjectStyle = self

    def removeDiagramObjects(self, *DiagramObjects):
        for obj in DiagramObjects:
            obj.DiagramObjectStyle = None

