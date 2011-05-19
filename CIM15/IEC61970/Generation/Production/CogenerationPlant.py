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

from CIM15.IEC61970.Core.PowerSystemResource import PowerSystemResource

class CogenerationPlant(PowerSystemResource):
    """A set of thermal generating units for the production of electrical energy and process steam (usually from the output of the steam turbines). The steam sendout is typically used for industrial purposes or for municipal heating and cooling.A set of thermal generating units for the production of electrical energy and process steam (usually from the output of the steam turbines). The steam sendout is typically used for industrial purposes or for municipal heating and cooling.
    """

    def __init__(self, cogenLPSteamRating=0.0, cogenLPSendoutRating=0.0, ratedP=0.0, cogenHPSendoutRating=0.0, cogenHPSteamRating=0.0, SteamSendoutSchedule=None, ThermalGeneratingUnits=None, *args, **kw_args):
        """Initialises a new 'CogenerationPlant' instance.

        @param cogenLPSteamRating: The low pressure steam rating 
        @param cogenLPSendoutRating: The low pressure steam sendout 
        @param ratedP: The rated output active power of the cogeneration plant 
        @param cogenHPSendoutRating: The high pressure steam sendout 
        @param cogenHPSteamRating: The high pressure steam rating 
        @param SteamSendoutSchedule: A cogeneration plant has a steam sendout schedule
        @param ThermalGeneratingUnits: A thermal generating unit may be a member of a cogeneration plant
        """
        #: The low pressure steam rating
        self.cogenLPSteamRating = cogenLPSteamRating

        #: The low pressure steam sendout
        self.cogenLPSendoutRating = cogenLPSendoutRating

        #: The rated output active power of the cogeneration plant
        self.ratedP = ratedP

        #: The high pressure steam sendout
        self.cogenHPSendoutRating = cogenHPSendoutRating

        #: The high pressure steam rating
        self.cogenHPSteamRating = cogenHPSteamRating

        self._SteamSendoutSchedule = None
        self.SteamSendoutSchedule = SteamSendoutSchedule

        self._ThermalGeneratingUnits = []
        self.ThermalGeneratingUnits = [] if ThermalGeneratingUnits is None else ThermalGeneratingUnits

        super(CogenerationPlant, self).__init__(*args, **kw_args)

    _attrs = ["cogenLPSteamRating", "cogenLPSendoutRating", "ratedP", "cogenHPSendoutRating", "cogenHPSteamRating"]
    _attr_types = {"cogenLPSteamRating": float, "cogenLPSendoutRating": float, "ratedP": float, "cogenHPSendoutRating": float, "cogenHPSteamRating": float}
    _defaults = {"cogenLPSteamRating": 0.0, "cogenLPSendoutRating": 0.0, "ratedP": 0.0, "cogenHPSendoutRating": 0.0, "cogenHPSteamRating": 0.0}
    _enums = {}
    _refs = ["SteamSendoutSchedule", "ThermalGeneratingUnits"]
    _many_refs = ["ThermalGeneratingUnits"]

    def getSteamSendoutSchedule(self):
        """A cogeneration plant has a steam sendout schedule
        """
        return self._SteamSendoutSchedule

    def setSteamSendoutSchedule(self, value):
        if self._SteamSendoutSchedule is not None:
            self._SteamSendoutSchedule._CogenerationPlant = None

        self._SteamSendoutSchedule = value
        if self._SteamSendoutSchedule is not None:
            self._SteamSendoutSchedule.CogenerationPlant = None
            self._SteamSendoutSchedule._CogenerationPlant = self

    SteamSendoutSchedule = property(getSteamSendoutSchedule, setSteamSendoutSchedule)

    def getThermalGeneratingUnits(self):
        """A thermal generating unit may be a member of a cogeneration plant
        """
        return self._ThermalGeneratingUnits

    def setThermalGeneratingUnits(self, value):
        for x in self._ThermalGeneratingUnits:
            x.CogenerationPlant = None
        for y in value:
            y._CogenerationPlant = self
        self._ThermalGeneratingUnits = value

    ThermalGeneratingUnits = property(getThermalGeneratingUnits, setThermalGeneratingUnits)

    def addThermalGeneratingUnits(self, *ThermalGeneratingUnits):
        for obj in ThermalGeneratingUnits:
            obj.CogenerationPlant = self

    def removeThermalGeneratingUnits(self, *ThermalGeneratingUnits):
        for obj in ThermalGeneratingUnits:
            obj.CogenerationPlant = None

