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

from CIM14v13.IEC61968.Informative.InfGMLSupport.GmlSymbol import GmlSymbol

class GmlRasterSymbol(GmlSymbol):
    """Describes how to render raster/matrix-coverage data (e.g., satellite photos, DEMs).
    """

    def __init__(self, greenSourceName='', brighnessOnly=False, reliefFactor='', overlapbehaviour='', graySourcename='', opacity=0.0, redSourcename='', blueSourcename='', GmlDiagramObject=None, *args, **kw_args):
        """Initializes a new 'GmlRasterSymbol' instance.

        @param greenSourceName: Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation. 
        @param brighnessOnly: If the BrightnessOnly flag is 0 (false, default), the shading is applied to the layer being rendered as the current RasterSymbol. If BrightnessOnly is 1 (true), the shading is applied to the brightness of the colors in the rendering canvas generated so far by other layers, with the effect of relief-shading these other layers. 
        @param reliefFactor: The ReliefFactor gives the amount of exaggeration to use for the height of the 'hills'. A value of around 55 (times) gives reasonable results for Earth-based DEMs. The default value is system-dependent. 
        @param overlapbehaviour: Tells a system how to behave when multiple raster images in a layer overlap each other, for example with satellite-image scenes. 
        @param graySourcename: A single colour channel may be selected to display in grayscale. Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation. 
        @param opacity: Specifies the level of translucency to use when rendering the Graphic. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0. 
        @param redSourcename: Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation. 
        @param blueSourcename: Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation. 
        @param GmlDiagramObject:
        """
        #: Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.
        self.greenSourceName = greenSourceName

        #: If the BrightnessOnly flag is 0 (false, default), the shading is applied to the layer being rendered as the current RasterSymbol. If BrightnessOnly is 1 (true), the shading is applied to the brightness of the colors in the rendering canvas generated so far by other layers, with the effect of relief-shading these other layers.
        self.brighnessOnly = brighnessOnly

        #: The ReliefFactor gives the amount of exaggeration to use for the height of the 'hills'. A value of around 55 (times) gives reasonable results for Earth-based DEMs. The default value is system-dependent.
        self.reliefFactor = reliefFactor

        #: Tells a system how to behave when multiple raster images in a layer overlap each other, for example with satellite-image scenes.
        self.overlapbehaviour = overlapbehaviour

        #: A single colour channel may be selected to display in grayscale. Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.
        self.graySourcename = graySourcename

        #: Specifies the level of translucency to use when rendering the Graphic. The value is encoded as a floating-point value between 0.0 and 1.0 with 0.0 representing completely transparent and 1.0 representing completely opaque, with a linear scale of translucency for intermediate values. The default value is 1.0.
        self.opacity = opacity

        #: Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.
        self.redSourcename = redSourcename

        #: Colour Channels are identified by a system and data-dependent character identifier. Contrast enhancement may be applied to each channel in isolation.
        self.blueSourcename = blueSourcename

        self._GmlDiagramObject = None
        self.GmlDiagramObject = GmlDiagramObject

        super(GmlRasterSymbol, self).__init__(*args, **kw_args)

    def getGmlDiagramObject(self):
        
        return self._GmlDiagramObject

    def setGmlDiagramObject(self, value):
        if self._GmlDiagramObject is not None:
            filtered = [x for x in self.GmlDiagramObject.GmlRasterSymbols if x != self]
            self._GmlDiagramObject._GmlRasterSymbols = filtered

        self._GmlDiagramObject = value
        if self._GmlDiagramObject is not None:
            self._GmlDiagramObject._GmlRasterSymbols.append(self)

    GmlDiagramObject = property(getGmlDiagramObject, setGmlDiagramObject)

