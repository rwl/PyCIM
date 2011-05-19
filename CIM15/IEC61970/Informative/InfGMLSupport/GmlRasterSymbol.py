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

from CIM15.IEC61970.Informative.InfGMLSupport.GmlSymbol import GmlSymbol

class GmlRasterSymbol(GmlSymbol):
    """Describes how to render raster/matrix-coverage data (e.g., satellite photos, DEMs).Describes how to render raster/matrix-coverage data (e.g., satellite photos, DEMs).
    """

    def __init__(self, graySourcename='', greenSourceName='', opacity=0.0, reliefFactor='', redSourcename='', overlapbehaviour='', brighnessOnly=False, blueSourcename='', GmlDiagramObject=None, *args, **kw_args):
        """Initialises a new 'GmlRasterSymbol' instance.

        @param graySourcename: A single colour channel may be selected to display in grayscale. Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation. 
        @param greenSourceName: Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation. 
        @param opacity: Specifies the level of translucency to use when rendering the Graphic. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0. 
        @param reliefFactor: The ReliefFactor gives the amount of exaggeration to use for the height of the 'hills'. A value of around 55 (times) gives reasonable results for Earth-based DEMs. The default value is system-dependent. 
        @param redSourcename: Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation. 
        @param overlapbehaviour: Tells a system how to behave when multiple raster images in a layer overlap each other, for example with satellite-image scenes. 
        @param brighnessOnly: If the BrightnessOnly flag is 0 (false, default), the shading is applied to the layer being rendered as the current RasterSymbol. If BrightnessOnly is 1 (true), the shading is applied to the brightness of the colors in the rendering canvas generated so far by other layers, with the effect of relief-shading these other layers. 
        @param blueSourcename: Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation. 
        @param GmlDiagramObject:
        """
        #: A single colour channel may be selected to display in grayscale. Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.
        self.graySourcename = graySourcename

        #: Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.
        self.greenSourceName = greenSourceName

        #: Specifies the level of translucency to use when rendering the Graphic. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0.
        self.opacity = opacity

        #: The ReliefFactor gives the amount of exaggeration to use for the height of the 'hills'. A value of around 55 (times) gives reasonable results for Earth-based DEMs. The default value is system-dependent.
        self.reliefFactor = reliefFactor

        #: Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.
        self.redSourcename = redSourcename

        #: Tells a system how to behave when multiple raster images in a layer overlap each other, for example with satellite-image scenes.
        self.overlapbehaviour = overlapbehaviour

        #: If the BrightnessOnly flag is 0 (false, default), the shading is applied to the layer being rendered as the current RasterSymbol. If BrightnessOnly is 1 (true), the shading is applied to the brightness of the colors in the rendering canvas generated so far by other layers, with the effect of relief-shading these other layers.
        self.brighnessOnly = brighnessOnly

        #: Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.
        self.blueSourcename = blueSourcename

        self._GmlDiagramObject = None
        self.GmlDiagramObject = GmlDiagramObject

        super(GmlRasterSymbol, self).__init__(*args, **kw_args)

    _attrs = ["graySourcename", "greenSourceName", "opacity", "reliefFactor", "redSourcename", "overlapbehaviour", "brighnessOnly", "blueSourcename"]
    _attr_types = {"graySourcename": str, "greenSourceName": str, "opacity": float, "reliefFactor": str, "redSourcename": str, "overlapbehaviour": str, "brighnessOnly": bool, "blueSourcename": str}
    _defaults = {"graySourcename": '', "greenSourceName": '', "opacity": 0.0, "reliefFactor": '', "redSourcename": '', "overlapbehaviour": '', "brighnessOnly": False, "blueSourcename": ''}
    _enums = {}
    _refs = ["GmlDiagramObject"]
    _many_refs = []

    def getGmlDiagramObject(self):
        
        return self._GmlDiagramObject

    def setGmlDiagramObject(self, value):
        if self._GmlDiagramObject is not None:
            filtered = [x for x in self.GmlDiagramObject.GmlRasterSymbols if x != self]
            self._GmlDiagramObject._GmlRasterSymbols = filtered

        self._GmlDiagramObject = value
        if self._GmlDiagramObject is not None:
            if self not in self._GmlDiagramObject._GmlRasterSymbols:
                self._GmlDiagramObject._GmlRasterSymbols.append(self)

    GmlDiagramObject = property(getGmlDiagramObject, setGmlDiagramObject)

