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

class GmlMark(IdentifiedObject):
    """Defines a 'shape' which has coloring applied to it (i.e. square, circle, triangle, star, ...).Defines a 'shape' which has coloring applied to it (i.e. square, circle, triangle, star, ...).
    """

    def __init__(self, wellKnownName='', GmlGraphics=None, GmlStrokes=None, GmlFIlls=None, *args, **kw_args):
        """Initialises a new 'GmlMark' instance.

        @param wellKnownName: Gives the well-known name of the shape of the mark. Allowed values include at least square, circle, triangle, star, cross, and x. 
        @param GmlGraphics:
        @param GmlStrokes:
        @param GmlFIlls:
        """
        #: Gives the well-known name of the shape of the mark. Allowed values include at least square, circle, triangle, star, cross, and x.
        self.wellKnownName = wellKnownName

        self._GmlGraphics = []
        self.GmlGraphics = [] if GmlGraphics is None else GmlGraphics

        self._GmlStrokes = []
        self.GmlStrokes = [] if GmlStrokes is None else GmlStrokes

        self._GmlFIlls = []
        self.GmlFIlls = [] if GmlFIlls is None else GmlFIlls

        super(GmlMark, self).__init__(*args, **kw_args)

    _attrs = ["wellKnownName"]
    _attr_types = {"wellKnownName": str}
    _defaults = {"wellKnownName": ''}
    _enums = {}
    _refs = ["GmlGraphics", "GmlStrokes", "GmlFIlls"]
    _many_refs = ["GmlGraphics", "GmlStrokes", "GmlFIlls"]

    def getGmlGraphics(self):
        
        return self._GmlGraphics

    def setGmlGraphics(self, value):
        for p in self._GmlGraphics:
            filtered = [q for q in p.GmlMarks if q != self]
            self._GmlGraphics._GmlMarks = filtered
        for r in value:
            if self not in r._GmlMarks:
                r._GmlMarks.append(self)
        self._GmlGraphics = value

    GmlGraphics = property(getGmlGraphics, setGmlGraphics)

    def addGmlGraphics(self, *GmlGraphics):
        for obj in GmlGraphics:
            if self not in obj._GmlMarks:
                obj._GmlMarks.append(self)
            self._GmlGraphics.append(obj)

    def removeGmlGraphics(self, *GmlGraphics):
        for obj in GmlGraphics:
            if self in obj._GmlMarks:
                obj._GmlMarks.remove(self)
            self._GmlGraphics.remove(obj)

    def getGmlStrokes(self):
        
        return self._GmlStrokes

    def setGmlStrokes(self, value):
        for p in self._GmlStrokes:
            filtered = [q for q in p.GmlMarks if q != self]
            self._GmlStrokes._GmlMarks = filtered
        for r in value:
            if self not in r._GmlMarks:
                r._GmlMarks.append(self)
        self._GmlStrokes = value

    GmlStrokes = property(getGmlStrokes, setGmlStrokes)

    def addGmlStrokes(self, *GmlStrokes):
        for obj in GmlStrokes:
            if self not in obj._GmlMarks:
                obj._GmlMarks.append(self)
            self._GmlStrokes.append(obj)

    def removeGmlStrokes(self, *GmlStrokes):
        for obj in GmlStrokes:
            if self in obj._GmlMarks:
                obj._GmlMarks.remove(self)
            self._GmlStrokes.remove(obj)

    def getGmlFIlls(self):
        
        return self._GmlFIlls

    def setGmlFIlls(self, value):
        for p in self._GmlFIlls:
            filtered = [q for q in p.GmlMarks if q != self]
            self._GmlFIlls._GmlMarks = filtered
        for r in value:
            if self not in r._GmlMarks:
                r._GmlMarks.append(self)
        self._GmlFIlls = value

    GmlFIlls = property(getGmlFIlls, setGmlFIlls)

    def addGmlFIlls(self, *GmlFIlls):
        for obj in GmlFIlls:
            if self not in obj._GmlMarks:
                obj._GmlMarks.append(self)
            self._GmlFIlls.append(obj)

    def removeGmlFIlls(self, *GmlFIlls):
        for obj in GmlFIlls:
            if self in obj._GmlMarks:
                obj._GmlMarks.remove(self)
            self._GmlFIlls.remove(obj)

