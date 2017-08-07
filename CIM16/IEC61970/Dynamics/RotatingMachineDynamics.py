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

# Modified by Gustav Holm (guholm@kth.se) & Francis J. Gómez (fragom@kth.se)
# Modified date: 05/06/2017

from CIM16.IEC61970.Dynamics.DynamicsFunctionBlock import DynamicsFunctionBlock
#unclear what this should refeer to

class RotatingMachineDynamics(DynamicsFunctionBlock):

    def __init__(self, damping=0.0, inertia=0.0, saturationFactor=0.0, saturationFactor120=0.0, statorLeakageReactance=0.0, statorResistance=0.0, *args, **kw_args):
        """Initialises a new 'RotatingMachineDynamics' instance."""
        
        self.damping = damping

        self.inertia = inertia

        self.saturationFactor = saturationFactor

        self.saturationFactor120 = saturationFactor120

        self.statorLeakageReactance = statorLeakageReactance

        self.statorResistance = statorResistance

        super(RotatingMachineDynamics, self).__init__(*args, **kw_args)

    _attrs = ["damping", "inertia", "saturationFactor", "saturationFactor120", "statorLeakageReactance", "statorResistance"]
    _attr_types = {"damping": float, "inertia": float,"saturationFactor": float, "saturationFactor120": float, "statorLeakageReactance": float, "statorResistance": float}
    _defaults = {"damping": 0.0, "inertia": 0.0,"saturationFactor": 0.0, "saturationFactor120": 0.0, "statorLeakageReactance": 0.0, "statorResistance": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []


