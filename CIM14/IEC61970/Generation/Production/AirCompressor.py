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

from CIM14.IEC61970.Core.PowerSystemResource import PowerSystemResource

class AirCompressor(PowerSystemResource):
    """Combustion turbine air compressor which is an integral part of a compressed air energy storage (CAES) plant
    """

    def __init__(self, airCompressorRating=0.0, CAESPlant=None, CombustionTurbine=None, *args, **kw_args):
        """Initialises a new 'AirCompressor' instance.

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

        super(AirCompressor, self).__init__(*args, **kw_args)

    _attrs = ["airCompressorRating"]
    _attr_types = {"airCompressorRating": float}
    _defaults = {"airCompressorRating": 0.0}
    _enums = {}
    _refs = ["CAESPlant", "CombustionTurbine"]
    _many_refs = []

    def getCAESPlant(self):
        """An air compressor may be a member of a compressed air energy storage plant
        """
        return self._CAESPlant

    def setCAESPlant(self, value):
        if self._CAESPlant is not None:
            self._CAESPlant._AirCompressor = None

        self._CAESPlant = value
        if self._CAESPlant is not None:
            self._CAESPlant.AirCompressor = None
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
            self._CombustionTurbine.AirCompressor = None
            self._CombustionTurbine._AirCompressor = self

    CombustionTurbine = property(getCombustionTurbine, setCombustionTurbine)

