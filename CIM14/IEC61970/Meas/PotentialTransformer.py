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

