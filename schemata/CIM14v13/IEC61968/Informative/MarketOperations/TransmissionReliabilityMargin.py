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

class TransmissionReliabilityMargin(IdentifiedObject):
    """Transmission Reliability Margin (TRM) is defined as that amount of transmission transfer capability necessary to ensure that the interconnected transmission network is secure under a reasonable range of uncertainties in system conditions.
    """

    def __init__(self, valueUnit='', trmValue=0.0, TrmType='', Flowgate=None, **kw_args):
        """Initializes a new 'TransmissionReliabilityMargin' instance.

        @param valueUnit: unit of the TRM value. Could be MW or Percentage. 
        @param trmValue: Value of the TRM 
        @param TrmType: the type of TRM 
        @param Flowgate: A fowgate may have 0 to 1 TRM
        """
        #: unit of the TRM value. Could be MW or Percentage.
        self.valueUnit = valueUnit

        #: Value of the TRM
        self.trmValue = trmValue

        #: the type of TRM
        self.TrmType = TrmType

        self._Flowgate = []
        self.Flowgate = [] if Flowgate is None else Flowgate

        super(TransmissionReliabilityMargin, self).__init__(**kw_args)

    def getFlowgate(self):
        """A fowgate may have 0 to 1 TRM
        """
        return self._Flowgate

    def setFlowgate(self, value):
        for x in self._Flowgate:
            x._TransmissionReliabilityMargin = None
        for y in value:
            y._TransmissionReliabilityMargin = self
        self._Flowgate = value

    Flowgate = property(getFlowgate, setFlowgate)

    def addFlowgate(self, *Flowgate):
        for obj in Flowgate:
            obj._TransmissionReliabilityMargin = self
            self._Flowgate.append(obj)

    def removeFlowgate(self, *Flowgate):
        for obj in Flowgate:
            obj._TransmissionReliabilityMargin = None
            self._Flowgate.remove(obj)

