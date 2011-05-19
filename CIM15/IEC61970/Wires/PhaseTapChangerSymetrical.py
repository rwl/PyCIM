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

from CIM15.IEC61970.Wires.PhaseTapChangerNonLinear import PhaseTapChangerNonLinear

class PhaseTapChangerSymetrical(PhaseTapChangerNonLinear):
    """In a PhaseTapChangerSymetrical tranformer the secondary side voltage magnitude is the same as at the primary side. The difference voltage magnitude, &Delta;U, is the base in an equal-sided triangle where the sides corresponds to the primary and secondary voltages. The phase angle difference correpsonds the top angle and can be expressed as follows &alpha; = 2arctan(&Delta;U/2)In a PhaseTapChangerSymetrical tranformer the secondary side voltage magnitude is the same as at the primary side. The difference voltage magnitude, &Delta;U, is the base in an equal-sided triangle where the sides corresponds to the primary and secondary voltages. The phase angle difference correpsonds the top angle and can be expressed as follows &alpha; = 2arctan(&Delta;U/2)
    """

    def __init__(self, *args, **kw_args):
        """Initialises a new 'PhaseTapChangerSymetrical' instance.

        """
        super(PhaseTapChangerSymetrical, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = []
    _many_refs = []

