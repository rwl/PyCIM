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

class GmlHalo(IdentifiedObject):
    """A type of Fill that is applied to the backgrounds of font glyphs. The use of halos greatly improves the readability of text labels.
    """

    def __init__(self, radius='', opacity=0.0, GmlTextSymbols=None, *args, **kw_args):
        """Initializes a new 'GmlHalo' instance.

        @param radius: The Radius element gives the absolute size of a halo radius in pixels encoded as a floating-point number. The radius is taken from the outside edge of a font glyph to extend the area of coverage of the glyph (and the inside edge of ?holes? in the glyphs). The default radius is one pixel. Negative values are not allowed. 
        @param opacity: Specifies the level of translucency to use when rendering the Fill. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0 
        @param GmlTextSymbols:
        """
        #: The Radius element gives the absolute size of a halo radius in pixels encoded as a floating-point number. The radius is taken from the outside edge of a font glyph to extend the area of coverage of the glyph (and the inside edge of ?holes? in the glyphs). The default radius is one pixel. Negative values are not allowed.
        self.radius = radius

        #: Specifies the level of translucency to use when rendering the Fill. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0
        self.opacity = opacity

        self._GmlTextSymbols = []
        self.GmlTextSymbols = [] if GmlTextSymbols is None else GmlTextSymbols

        super(GmlHalo, self).__init__(*args, **kw_args)

    def getGmlTextSymbols(self):
        
        return self._GmlTextSymbols

    def setGmlTextSymbols(self, value):
        for x in self._GmlTextSymbols:
            x._GmlHalo = None
        for y in value:
            y._GmlHalo = self
        self._GmlTextSymbols = value

    GmlTextSymbols = property(getGmlTextSymbols, setGmlTextSymbols)

    def addGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj._GmlHalo = self
            self._GmlTextSymbols.append(obj)

    def removeGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj._GmlHalo = None
            self._GmlTextSymbols.remove(obj)

