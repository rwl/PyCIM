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

class GmlHalo(IdentifiedObject):
    """A type of Fill that is applied to the backgrounds of font glyphs. The use of halos greatly improves the readability of text labels.A type of Fill that is applied to the backgrounds of font glyphs. The use of halos greatly improves the readability of text labels.
    """

    def __init__(self, radius='', opacity=0.0, GmlTextSymbols=None, *args, **kw_args):
        """Initialises a new 'GmlHalo' instance.

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

    _attrs = ["radius", "opacity"]
    _attr_types = {"radius": str, "opacity": float}
    _defaults = {"radius": '', "opacity": 0.0}
    _enums = {}
    _refs = ["GmlTextSymbols"]
    _many_refs = ["GmlTextSymbols"]

    def getGmlTextSymbols(self):
        
        return self._GmlTextSymbols

    def setGmlTextSymbols(self, value):
        for x in self._GmlTextSymbols:
            x.GmlHalo = None
        for y in value:
            y._GmlHalo = self
        self._GmlTextSymbols = value

    GmlTextSymbols = property(getGmlTextSymbols, setGmlTextSymbols)

    def addGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj.GmlHalo = self

    def removeGmlTextSymbols(self, *GmlTextSymbols):
        for obj in GmlTextSymbols:
            obj.GmlHalo = None

