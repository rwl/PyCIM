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

from CIM14.IEC61970.Generation.GenerationDynamics.SteamSupply import SteamSupply

class PWRSteamSupply(SteamSupply):
    """Pressurized water reactor used as a steam supply to a steam turbine
    """

    def __init__(self, pressureCG=0.0, throttlePressureSP=0.0, coldLegFBLagTC=0.0, hotLegSteamGain=0.0, coreHTLagTC2=0.0, coreHTLagTC1=0.0, coreNeutronicsHT=0.0, coldLegFBLeadTC1=0.0, feedbackFactor=0.0, coreNeutronicsEffTC=0.0, steamFlowFG=0.0, steamPressureDropLagTC=0.0, steamPressureFG=0.0, coldLegFG1=0.0, throttlePressureFactor=0.0, coldLegFBLeadTC2=0.0, hotLegToColdLegGain=0.0, coldLegFG2=0.0, hotLegLagTC=0.0, coldLegLagTC=0.0, *args, **kw_args):
        """Initialises a new 'PWRSteamSupply' instance.

        @param pressureCG: Pressure Control Gain 
        @param throttlePressureSP: Throttle Pressure Setpoint 
        @param coldLegFBLagTC: Cold Leg Feedback Lag Time Constant 
        @param hotLegSteamGain: Hot Leg Steam Gain 
        @param coreHTLagTC2: Core Heat Transfer Lag Time Constant 
        @param coreHTLagTC1: Core Heat Transfer Lag Time Constant 
        @param coreNeutronicsHT: Core Neutronics And Heat Transfer 
        @param coldLegFBLeadTC1: Cold Leg Feedback Lead Time Constant 
        @param feedbackFactor: Feedback Factor 
        @param coreNeutronicsEffTC: Core Neutronics Effective Time Constant 
        @param steamFlowFG: Steam Flow Feedback Gain 
        @param steamPressureDropLagTC: Steam Pressure Drop Lag Time Constant 
        @param steamPressureFG: Steam Pressure Feedback Gain 
        @param coldLegFG1: Cold Leg Feedback Gain 1 
        @param throttlePressureFactor: Throttle Pressure Factor 
        @param coldLegFBLeadTC2: Cold Leg Feedback Lead Time Constant 
        @param hotLegToColdLegGain: Hot Leg To Cold Leg Gain 
        @param coldLegFG2: Cold Leg Feedback Gain 2 
        @param hotLegLagTC: Hot Leg Lag Time Constant 
        @param coldLegLagTC: Cold Leg Lag Time Constant 
        """
        #: Pressure Control Gain
        self.pressureCG = pressureCG

        #: Throttle Pressure Setpoint
        self.throttlePressureSP = throttlePressureSP

        #: Cold Leg Feedback Lag Time Constant
        self.coldLegFBLagTC = coldLegFBLagTC

        #: Hot Leg Steam Gain
        self.hotLegSteamGain = hotLegSteamGain

        #: Core Heat Transfer Lag Time Constant
        self.coreHTLagTC2 = coreHTLagTC2

        #: Core Heat Transfer Lag Time Constant
        self.coreHTLagTC1 = coreHTLagTC1

        #: Core Neutronics And Heat Transfer
        self.coreNeutronicsHT = coreNeutronicsHT

        #: Cold Leg Feedback Lead Time Constant
        self.coldLegFBLeadTC1 = coldLegFBLeadTC1

        #: Feedback Factor
        self.feedbackFactor = feedbackFactor

        #: Core Neutronics Effective Time Constant
        self.coreNeutronicsEffTC = coreNeutronicsEffTC

        #: Steam Flow Feedback Gain
        self.steamFlowFG = steamFlowFG

        #: Steam Pressure Drop Lag Time Constant
        self.steamPressureDropLagTC = steamPressureDropLagTC

        #: Steam Pressure Feedback Gain
        self.steamPressureFG = steamPressureFG

        #: Cold Leg Feedback Gain 1
        self.coldLegFG1 = coldLegFG1

        #: Throttle Pressure Factor
        self.throttlePressureFactor = throttlePressureFactor

        #: Cold Leg Feedback Lead Time Constant
        self.coldLegFBLeadTC2 = coldLegFBLeadTC2

        #: Hot Leg To Cold Leg Gain
        self.hotLegToColdLegGain = hotLegToColdLegGain

        #: Cold Leg Feedback Gain 2
        self.coldLegFG2 = coldLegFG2

        #: Hot Leg Lag Time Constant
        self.hotLegLagTC = hotLegLagTC

        #: Cold Leg Lag Time Constant
        self.coldLegLagTC = coldLegLagTC

        super(PWRSteamSupply, self).__init__(*args, **kw_args)

    _attrs = ["pressureCG", "throttlePressureSP", "coldLegFBLagTC", "hotLegSteamGain", "coreHTLagTC2", "coreHTLagTC1", "coreNeutronicsHT", "coldLegFBLeadTC1", "feedbackFactor", "coreNeutronicsEffTC", "steamFlowFG", "steamPressureDropLagTC", "steamPressureFG", "coldLegFG1", "throttlePressureFactor", "coldLegFBLeadTC2", "hotLegToColdLegGain", "coldLegFG2", "hotLegLagTC", "coldLegLagTC"]
    _attr_types = {"pressureCG": float, "throttlePressureSP": float, "coldLegFBLagTC": float, "hotLegSteamGain": float, "coreHTLagTC2": float, "coreHTLagTC1": float, "coreNeutronicsHT": float, "coldLegFBLeadTC1": float, "feedbackFactor": float, "coreNeutronicsEffTC": float, "steamFlowFG": float, "steamPressureDropLagTC": float, "steamPressureFG": float, "coldLegFG1": float, "throttlePressureFactor": float, "coldLegFBLeadTC2": float, "hotLegToColdLegGain": float, "coldLegFG2": float, "hotLegLagTC": float, "coldLegLagTC": float}
    _defaults = {"pressureCG": 0.0, "throttlePressureSP": 0.0, "coldLegFBLagTC": 0.0, "hotLegSteamGain": 0.0, "coreHTLagTC2": 0.0, "coreHTLagTC1": 0.0, "coreNeutronicsHT": 0.0, "coldLegFBLeadTC1": 0.0, "feedbackFactor": 0.0, "coreNeutronicsEffTC": 0.0, "steamFlowFG": 0.0, "steamPressureDropLagTC": 0.0, "steamPressureFG": 0.0, "coldLegFG1": 0.0, "throttlePressureFactor": 0.0, "coldLegFBLeadTC2": 0.0, "hotLegToColdLegGain": 0.0, "coldLegFG2": 0.0, "hotLegLagTC": 0.0, "coldLegLagTC": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

