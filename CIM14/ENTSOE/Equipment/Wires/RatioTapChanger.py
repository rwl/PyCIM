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

from CIM14.ENTSOE.Equipment.Wires.TapChanger import TapChanger

class RatioTapChanger(TapChanger):
    """A tap changer that changes the voltage ratio impacting the voltage magnitude but not direclty the phase angle across the transformer..-  The attribute ltcflag specifies whether or not a TapChanger has load tap changing capabilities.  If the ltcFlag is true,  the attributes “highStep”, “lowStep”, “neutralStep”, “normalStep”, “neutralU” and “stepVoltageIncrement” are required. 
    """

    def __init__(self, tculControlMode="reactive", TransformerWinding=None, *args, **kw_args):
        """Initialises a new 'RatioTapChanger' instance.

        @param tculControlMode: Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger. Values are: "reactive", "volt"
        @param TransformerWinding: The transformer winding to which the ratio tap changer belongs.
        """
        #: Specifies the regulation control mode (voltage or reactive) of the RatioTapChanger. Values are: "reactive", "volt"
        self.tculControlMode = tculControlMode

        self._TransformerWinding = None
        self.TransformerWinding = TransformerWinding

        super(RatioTapChanger, self).__init__(*args, **kw_args)

    _attrs = ["tculControlMode"]
    _attr_types = {"tculControlMode": str}
    _defaults = {"tculControlMode": "reactive"}
    _enums = {"tculControlMode": "TransformerControlMode"}
    _refs = ["TransformerWinding"]
    _many_refs = []

    def getTransformerWinding(self):
        """The transformer winding to which the ratio tap changer belongs.
        """
        return self._TransformerWinding

    def setTransformerWinding(self, value):
        if self._TransformerWinding is not None:
            self._TransformerWinding._RatioTapChanger = None

        self._TransformerWinding = value
        if self._TransformerWinding is not None:
            self._TransformerWinding.RatioTapChanger = None
            self._TransformerWinding._RatioTapChanger = self

    TransformerWinding = property(getTransformerWinding, setTransformerWinding)

