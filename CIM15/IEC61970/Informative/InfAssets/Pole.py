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

from CIM15.IEC61970.Informative.InfAssets.Structure import Structure

class Pole(Structure):
    """Pole asset.Pole asset.
    """

    def __init__(self, breastBlock=False, diameter=0.0, baseKind="dirt", jpaReference='', treatmentKind="unknown", preservativeKind="penta", length=0.0, construction='', speciesType='', classification='', treatedDateTime='', Streetlights=None, *args, **kw_args):
        """Initialises a new 'Pole' instance.

        @param breastBlock: True if a block of material has been attached to base of pole in ground for stability. This technique is used primarily when anchors can not be used. 
        @param diameter: Diameter of the pole. 
        @param baseKind: Kind of base for this pole. Values are: "dirt", "asphalt", "unknown", "cement", "other"
        @param jpaReference: Joint pole agreement reference number. 
        @param treatmentKind: Kind of treatment for this pole. Values are: "unknown", "natural", "grayStain", "greenStain", "penta", "butt", "other", "full"
        @param preservativeKind: Kind of preservative for this pole. Values are: "penta", "unknown", "chemonite", "other", "naphthena", "creosote", "cellon"
        @param length: Length of the pole (inclusive of any section of the pole that may be underground post-installation). 
        @param construction: The framing structure mounted on the pole. 
        @param speciesType: Pole species. Aluminum, Aluminum Davit, Concrete, Fiberglass, Galvanized Davit, Galvanized, Steel Davit Primed, Steel Davit, Steel Standard Primed, Steel, Truncated, Wood-Treated, Wood-Hard, Wood-Salt Treated, Wood-Soft, Wood, Other, Unknown. 
        @param classification: Pole class: 1, 2, 3, 4, 5, 6, 7, H1, H2, Other, Unknown. 
        @param treatedDateTime: Date and time pole was last treated with preservative. 
        @param Streetlights: Streetlight(s) may be attached to a pole.
        """
        #: True if a block of material has been attached to base of pole in ground for stability. This technique is used primarily when anchors can not be used.
        self.breastBlock = breastBlock

        #: Diameter of the pole.
        self.diameter = diameter

        #: Kind of base for this pole. Values are: "dirt", "asphalt", "unknown", "cement", "other"
        self.baseKind = baseKind

        #: Joint pole agreement reference number.
        self.jpaReference = jpaReference

        #: Kind of treatment for this pole. Values are: "unknown", "natural", "grayStain", "greenStain", "penta", "butt", "other", "full"
        self.treatmentKind = treatmentKind

        #: Kind of preservative for this pole. Values are: "penta", "unknown", "chemonite", "other", "naphthena", "creosote", "cellon"
        self.preservativeKind = preservativeKind

        #: Length of the pole (inclusive of any section of the pole that may be underground post-installation).
        self.length = length

        #: The framing structure mounted on the pole.
        self.construction = construction

        #: Pole species. Aluminum, Aluminum Davit, Concrete, Fiberglass, Galvanized Davit, Galvanized, Steel Davit Primed, Steel Davit, Steel Standard Primed, Steel, Truncated, Wood-Treated, Wood-Hard, Wood-Salt Treated, Wood-Soft, Wood, Other, Unknown.
        self.speciesType = speciesType

        #: Pole class: 1, 2, 3, 4, 5, 6, 7, H1, H2, Other, Unknown.
        self.classification = classification

        #: Date and time pole was last treated with preservative.
        self.treatedDateTime = treatedDateTime

        self._Streetlights = []
        self.Streetlights = [] if Streetlights is None else Streetlights

        super(Pole, self).__init__(*args, **kw_args)

    _attrs = ["breastBlock", "diameter", "baseKind", "jpaReference", "treatmentKind", "preservativeKind", "length", "construction", "speciesType", "classification", "treatedDateTime"]
    _attr_types = {"breastBlock": bool, "diameter": float, "baseKind": str, "jpaReference": str, "treatmentKind": str, "preservativeKind": str, "length": float, "construction": str, "speciesType": str, "classification": str, "treatedDateTime": str}
    _defaults = {"breastBlock": False, "diameter": 0.0, "baseKind": "dirt", "jpaReference": '', "treatmentKind": "unknown", "preservativeKind": "penta", "length": 0.0, "construction": '', "speciesType": '', "classification": '', "treatedDateTime": ''}
    _enums = {"baseKind": "PoleBaseKind", "treatmentKind": "PoleTreatmentKind", "preservativeKind": "PolePreservativeKind"}
    _refs = ["Streetlights"]
    _many_refs = ["Streetlights"]

    def getStreetlights(self):
        """Streetlight(s) may be attached to a pole.
        """
        return self._Streetlights

    def setStreetlights(self, value):
        for x in self._Streetlights:
            x.Pole = None
        for y in value:
            y._Pole = self
        self._Streetlights = value

    Streetlights = property(getStreetlights, setStreetlights)

    def addStreetlights(self, *Streetlights):
        for obj in Streetlights:
            obj.Pole = self

    def removeStreetlights(self, *Streetlights):
        for obj in Streetlights:
            obj.Pole = None

