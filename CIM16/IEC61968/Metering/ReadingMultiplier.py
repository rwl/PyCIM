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


class ReadingMultiplier(object):
    """The multiplier value with its application status.The multiplier value with its application status.
    """

    def __init__(self, value=0.0, isApplied=False):
        """Initialises a new 'ReadingMultiplier' instance.

        @param value: Value of the multiplier. 
        @param isApplied: True if the multiplier has been applied to associated quantities. 
        """
        #: Value of the multiplier.
        self.value = value

        #: True if the multiplier has been applied to associated quantities.
        self.isApplied = isApplied


    _attrs = ["value", "isApplied"]
    _attr_types = {"value": float, "isApplied": bool}
    _defaults = {"value": 0.0, "isApplied": False}
    _enums = {}
    _refs = []
    _many_refs = []

