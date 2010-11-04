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

class GmlMark(IdentifiedObject):
    """Defines a 'shape' which has coloring applied to it (i.e. square, circle, triangle, star, ...).
    """

    def __init__(self, wellKnownName='', GmlFIlls=None, GmlGraphics=None, GmlStrokes=None, **kw_args):
        """Initializes a new 'GmlMark' instance.

        @param wellKnownName: Gives the well-known name of the shape of the mark. Allowed values include at least square, circle, triangle, star, cross, and x. 
        @param GmlFIlls:
        @param GmlGraphics:
        @param GmlStrokes:
        """
        #: Gives the well-known name of the shape of the mark. Allowed values include at least square, circle, triangle, star, cross, and x.
        self.wellKnownName = wellKnownName

        self._GmlFIlls = []
        self.GmlFIlls = [] if GmlFIlls is None else GmlFIlls

        self._GmlGraphics = []
        self.GmlGraphics = [] if GmlGraphics is None else GmlGraphics

        self._GmlStrokes = []
        self.GmlStrokes = [] if GmlStrokes is None else GmlStrokes

        super(GmlMark, self).__init__(**kw_args)

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

