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

from CIM14.IEC61970.Equivalents.EquivalentEquipment import EquivalentEquipment

class EquivalentInjection(EquivalentEquipment):
    """This class represents equivalent injections (generation or load).  Voltage regulation is allowed only at the local connectivity node.
    """

    def __init__(self, maxP=0.0, regulationCapability=False, regulationTarget=0.0, minP=0.0, regulationStatus=False, *args, **kw_args):
        """Initialises a new 'EquivalentInjection' instance.

        @param maxP: Minimum active power of the injection. 
        @param regulationCapability: Specifies whether or not the EquivalentInjection has the capability to regulate the local voltage. 
        @param regulationTarget: The target voltage for voltage regulation. 
        @param minP: Maximum active power of the injection. 
        @param regulationStatus: Specifies the default regulation status of the EquivalentInjection.  True is regulating.  False is not regulating. 
        """
        #: Minimum active power of the injection.
        self.maxP = maxP

        #: Specifies whether or not the EquivalentInjection has the capability to regulate the local voltage.
        self.regulationCapability = regulationCapability

        #: The target voltage for voltage regulation.
        self.regulationTarget = regulationTarget

        #: Maximum active power of the injection.
        self.minP = minP

        #: Specifies the default regulation status of the EquivalentInjection.  True is regulating.  False is not regulating.
        self.regulationStatus = regulationStatus

        super(EquivalentInjection, self).__init__(*args, **kw_args)

    _attrs = ["maxP", "regulationCapability", "regulationTarget", "minP", "regulationStatus"]
    _attr_types = {"maxP": float, "regulationCapability": bool, "regulationTarget": float, "minP": float, "regulationStatus": bool}
    _defaults = {"maxP": 0.0, "regulationCapability": False, "regulationTarget": 0.0, "minP": 0.0, "regulationStatus": False}
    _enums = {}
    _refs = []
    _many_refs = []

