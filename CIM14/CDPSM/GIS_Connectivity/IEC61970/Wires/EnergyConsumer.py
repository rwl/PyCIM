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

from CIM14.CDPSM.GIS_Connectivity.IEC61970.Core.ConductingEquipment import ConductingEquipment

class EnergyConsumer(ConductingEquipment):
    """Generic user of energy - a  point of consumption on the power system model
    """

    def __init__(self, pfixed=0.0, qfixed=0.0, customerCount=0, *args, **kw_args):
        """Initialises a new 'EnergyConsumer' instance.

        @param pfixed: Active power of the load that is a fixed quantity. 
        @param qfixed: Reactive power of the load that is a fixed quantity. 
        @param customerCount: Number of individual customers represented by this Demand 
        """
        #: Active power of the load that is a fixed quantity.
        self.pfixed = pfixed

        #: Reactive power of the load that is a fixed quantity.
        self.qfixed = qfixed

        #: Number of individual customers represented by this Demand
        self.customerCount = customerCount

        super(EnergyConsumer, self).__init__(*args, **kw_args)

    _attrs = ["pfixed", "qfixed", "customerCount"]
    _attr_types = {"pfixed": float, "qfixed": float, "customerCount": int}
    _defaults = {"pfixed": 0.0, "qfixed": 0.0, "customerCount": 0}
    _enums = {}
    _refs = []
    _many_refs = []

