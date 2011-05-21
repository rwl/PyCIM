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

class HeatExchanger(Equipment):
    """Equipment for the cooling of electrical equipment and the extraction of heat
    """

    def __init__(self, PowerTransformer=None, *args, **kw_args):
        """Initialises a new 'HeatExchanger' instance.

        @param PowerTransformer: A transformer may have a heat exchanger
        """
        self._PowerTransformer = None
        self.PowerTransformer = PowerTransformer

        super(HeatExchanger, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["PowerTransformer"]
    _many_refs = []

    def getPowerTransformer(self):
        """A transformer may have a heat exchanger
        """
        return self._PowerTransformer

    def setPowerTransformer(self, value):
        if self._PowerTransformer is not None:
            self._PowerTransformer._HeatExchanger = None

        self._PowerTransformer = value
        if self._PowerTransformer is not None:
            self._PowerTransformer.HeatExchanger = None
            self._PowerTransformer._HeatExchanger = self

    PowerTransformer = property(getPowerTransformer, setPowerTransformer)

