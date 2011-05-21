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

import unittest

from CIM14.IEC61970.Core import \
    ConnectivityNode, Terminal

from CIM14.IEC61970.LoadModel import \
    ConformLoad, ConformLoadGroup, LoadArea, ConformLoadSchedule

from CIM14.IEC61970.Meas import \
    AnalogLimit, AnalogValue, Analog

from CIM14.IEC61970.Protection import \
    SurgeProtector, CurrentRelay

from CIM14.IEC61970.Topology import \
    TopologicalNode

from CIM14.IEC61970.Wires import \
    Breaker, SynchronousMachine, BusbarSection, ACLineSegment, \
    PowerTransformer, TransformerWinding, ReactiveCapabilityCurve

from CIM14.IEC61970.Generation.Production import \
    ThermalGeneratingUnit, GenUnitOpCostCurve, GenUnitOpSchedule, StartupModel

class CIMTestCase(unittest.TestCase):
    """Test the full CIM package.
    """

    def setUp(self):
        """The test runner will execute this method prior to each test.
        """
        pass


    def testInstantiation(self):
        """Test element instantiation.
        """
        ThermalGeneratingUnit(oMCost=6.0, variableCost=10.0)
        GenUnitOpCostCurve(name="curve1", isNetGrossP=True)
        GenUnitOpSchedule(timeStep=1.0)
        StartupModel(name="model1", startupCost=20.0)

        ConformLoad(phases="A", pfixed=30.0)
        clg = ConformLoadGroup(description="group")
        LoadArea(name="area1")
        cls = ConformLoadSchedule(ConformLoadGroup=clg)
        self.assertEqual(cls.ConformLoadGroup, clg)

        AnalogLimit(value=100.0)
        AnalogValue(value=6.0)
        Analog(maxValue=100.0)
        SurgeProtector(normaIlyInService=True)
        CurrentRelay(inverseTimeFlag=True)

        tn = TopologicalNode(name="tn1")
        cn = ConnectivityNode(TopologicalNode=tn)
        self.assertTrue(cn.TopologicalNode, tn)
        Terminal(connected=True)

        Breaker(ratedCurrent=20.0)
        SynchronousMachine(coolantType="water")
        BusbarSection(phases="ABC")
        ACLineSegment(r=0.1, length=10.0)
        ReactiveCapabilityCurve(coolantTemperature=20.0)
        tw = TransformerWinding(windingType="primary")
        pt = PowerTransformer(TransformerWindings=[tw])
        self.assertTrue(tw in pt.TransformerWindings)


    def testOneToOne(self):
        """Test one-to-one bidirectional references.
        """
        sm1 = StartupModel()
        tgu1 = ThermalGeneratingUnit(StartupModel=sm1)

        self.assertEqual(tgu1.StartupModel, sm1)
        self.assertEqual(sm1.ThermalGeneratingUnit, tgu1)

        tgu2 = ThermalGeneratingUnit()
        tgu2.setStartupModel(sm1)

        self.assertEqual(tgu1.StartupModel, None)
        self.assertEqual(tgu2.StartupModel, sm1)
        self.assertNotEqual(sm1.ThermalGeneratingUnit, tgu1)
        self.assertTrue(sm1.ThermalGeneratingUnit, tgu2)


    def testOneToMany(self):
        """Test one-to-many bidirectional references.
        """
        lg1 = ConformLoadGroup(name="CLG1")
        lg2 = ConformLoadGroup(name="CLG2")
        cl = ConformLoad(name="Load 1", LoadGroup=lg1)

        self.assertEqual(cl.LoadGroup, lg1)
        self.assertTrue(cl in lg1.EnergyConsumers)

        cl.setLoadGroup(lg2)

        self.assertNotEqual(cl.LoadGroup, lg1)
        self.assertEqual(cl.LoadGroup, lg2)
        self.assertFalse(cl in lg1.EnergyConsumers)
        self.assertTrue(cl in lg2.EnergyConsumers)


    def testManyToOne(self):
        """Test many-to-one bidirectional references.
        """
        tw1 = TransformerWinding()
        tw2 = TransformerWinding()
        pt1 = PowerTransformer(TransformerWindings=[tw1])
        pt1.addTransformerWindings(tw2)

        self.assertTrue(tw1 in pt1.TransformerWindings)
        self.assertTrue(tw2 in pt1.TransformerWindings)
        self.assertEqual(tw1.PowerTransformer, pt1)
        self.assertEqual(tw2.PowerTransformer, pt1)

        pt2 = PowerTransformer()
        pt2.addTransformerWindings(tw2)

        self.assertTrue(tw1 in pt1.TransformerWindings)
        self.assertTrue(tw2 in pt2.TransformerWindings)
        self.assertFalse(tw2 in pt1.TransformerWindings)
        self.assertNotEqual(tw2.PowerTransformer, pt1)
        self.assertEqual(tw2.PowerTransformer, pt2)

        tw3 = TransformerWinding()
        pt1.setTransformerWindings([tw3])

        self.assertFalse(tw1 in pt1.TransformerWindings)
        self.assertTrue(tw3 in pt1.TransformerWindings)
        self.assertEqual(tw1.PowerTransformer, None)
        self.assertEqual(tw3.PowerTransformer, pt1)

        pt1.removeTransformerWindings(tw3)

        self.assertFalse(tw3 in pt1.TransformerWindings)
        self.assertEqual(tw3.PowerTransformer, None)


if __name__ == "__main__":
    unittest.main()
