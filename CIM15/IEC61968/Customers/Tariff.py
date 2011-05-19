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

from CIM15.IEC61968.Common.Document import Document

class Tariff(Document):
    """Document, approved by the responsible regulatory agency, listing the terms and conditions, including a schedule of prices, under which utility services will be provided. It has a unique number within the state or province. For rate schedules it is frequently allocated by the affiliated Public utilities commission (PUC).Document, approved by the responsible regulatory agency, listing the terms and conditions, including a schedule of prices, under which utility services will be provided. It has a unique number within the state or province. For rate schedules it is frequently allocated by the affiliated Public utilities commission (PUC).
    """

    def __init__(self, startDate='', endDate='', PricingStructures=None, TariffProfiles=None, *args, **kw_args):
        """Initialises a new 'Tariff' instance.

        @param startDate: Date tariff was activated. 
        @param endDate: (if tariff became inactive) Date tariff was terminated. 
        @param PricingStructures: All pricing structures using this tariff.
        @param TariffProfiles: All tariff profiles using this tariff.
        """
        #: Date tariff was activated.
        self.startDate = startDate

        #: (if tariff became inactive) Date tariff was terminated.
        self.endDate = endDate

        self._PricingStructures = []
        self.PricingStructures = [] if PricingStructures is None else PricingStructures

        self._TariffProfiles = []
        self.TariffProfiles = [] if TariffProfiles is None else TariffProfiles

        super(Tariff, self).__init__(*args, **kw_args)

    _attrs = ["startDate", "endDate"]
    _attr_types = {"startDate": str, "endDate": str}
    _defaults = {"startDate": '', "endDate": ''}
    _enums = {}
    _refs = ["PricingStructures", "TariffProfiles"]
    _many_refs = ["PricingStructures", "TariffProfiles"]

    def getPricingStructures(self):
        """All pricing structures using this tariff.
        """
        return self._PricingStructures

    def setPricingStructures(self, value):
        for p in self._PricingStructures:
            filtered = [q for q in p.Tariffs if q != self]
            self._PricingStructures._Tariffs = filtered
        for r in value:
            if self not in r._Tariffs:
                r._Tariffs.append(self)
        self._PricingStructures = value

    PricingStructures = property(getPricingStructures, setPricingStructures)

    def addPricingStructures(self, *PricingStructures):
        for obj in PricingStructures:
            if self not in obj._Tariffs:
                obj._Tariffs.append(self)
            self._PricingStructures.append(obj)

    def removePricingStructures(self, *PricingStructures):
        for obj in PricingStructures:
            if self in obj._Tariffs:
                obj._Tariffs.remove(self)
            self._PricingStructures.remove(obj)

    def getTariffProfiles(self):
        """All tariff profiles using this tariff.
        """
        return self._TariffProfiles

    def setTariffProfiles(self, value):
        for p in self._TariffProfiles:
            filtered = [q for q in p.Tariffs if q != self]
            self._TariffProfiles._Tariffs = filtered
        for r in value:
            if self not in r._Tariffs:
                r._Tariffs.append(self)
        self._TariffProfiles = value

    TariffProfiles = property(getTariffProfiles, setTariffProfiles)

    def addTariffProfiles(self, *TariffProfiles):
        for obj in TariffProfiles:
            if self not in obj._Tariffs:
                obj._Tariffs.append(self)
            self._TariffProfiles.append(obj)

    def removeTariffProfiles(self, *TariffProfiles):
        for obj in TariffProfiles:
            if self in obj._Tariffs:
                obj._Tariffs.remove(self)
            self._TariffProfiles.remove(obj)

