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

from CIM14.IEC61970.Core.Equipment import Equipment

class PotentialTransformer(Equipment):
    """Instrument transformer (also known as Voltage Transformer) used to measure electrical qualities of the circuit that is being protected and/or monitored. Typically used as voltage transducer for the purpose of metering, protection, or sometimes auxiliary substation supply. A typical secondary voltage rating would be 120V.
    """

    def __init__(self, ptClass='', accuracyClass='', nominalRatio=0.0, *args, **kw_args):
        """Initialises a new 'PotentialTransformer' instance.

        @param ptClass: PT classification. 
        @param accuracyClass: PT accuracy classification. 
        @param nominalRatio: Nominal ratio between the primary and secondary voltage. 
        """
        #: PT classification.
        self.ptClass = ptClass

        #: PT accuracy classification.
        self.accuracyClass = accuracyClass

        #: Nominal ratio between the primary and secondary voltage.
        self.nominalRatio = nominalRatio

        super(PotentialTransformer, self).__init__(*args, **kw_args)

    _attrs = ["ptClass", "accuracyClass", "nominalRatio"]
    _attr_types = {"ptClass": str, "accuracyClass": str, "nominalRatio": float}
    _defaults = {"ptClass": '', "accuracyClass": '', "nominalRatio": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

