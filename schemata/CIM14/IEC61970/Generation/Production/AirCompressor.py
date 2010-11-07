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

from CIM14.IEC61970.Core.PowerSystemResource import PowerSystemResource

class AirCompressor(PowerSystemResource):
    """Combustion turbine air compressor which is an integral part of a compressed air energy storage (CAES) plant
    """

    def __init__(self, airCompressorRating=0.0, CAESPlant=None, CombustionTurbine=None, **kw_args):
        """Initializes a new 'AirCompressor' instance.

        @param airCompressorRating: Rating of the CAES air compressor 
        @param CAESPlant: An air compressor may be a member of a compressed air energy storage plant
        @param CombustionTurbine: A CAES air compressor is driven by combustion turbine
        """
        #: Rating of the CAES air compressor
        self.airCompressorRating = airCompressorRating

        self._CAESPlant = None
        self.CAESPlant = CAESPlant

        self._CombustionTurbine = None
        self.CombustionTurbine = CombustionTurbine

        super(AirCompressor, self).__init__(**kw_args)

    def getCAESPlant(self):
        """An air compressor may be a member of a compressed air energy storage plant
        """
        return self._CAESPlant

    def setCAESPlant(self, value):
        if self._CAESPlant is not None:
            self._CAESPlant._AirCompressor = None

        self._CAESPlant = value
        if self._CAESPlant is not None:
            self._CAESPlant._AirCompressor = self

    CAESPlant = property(getCAESPlant, setCAESPlant)

    def getCombustionTurbine(self):
        """A CAES air compressor is driven by combustion turbine
        """
        return self._CombustionTurbine

    def setCombustionTurbine(self, value):
        if self._CombustionTurbine is not None:
            self._CombustionTurbine._AirCompressor = None

        self._CombustionTurbine = value
        if self._CombustionTurbine is not None:
            self._CombustionTurbine._AirCompressor = self

    CombustionTurbine = property(getCombustionTurbine, setCombustionTurbine)

