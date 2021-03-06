import processData
import goodweData
import copy

class test:
   
   def do_tests( self):
      self.test_1()
      
      
   def test_1( self):
      gw1 = goodweData.goodweData('<tr class=\"DG_Item\"><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>')

      gw1.m_inverter_sn = 1
      gw1.m_vpv1 = 1.0
      gw1.m_vpv2 = 1.0
      gw1.m_ipv1 = 1.0
      gw1.m_ipv2 = 1.0
      gw1.m_vac1 = 1.0
      gw1.m_vac2 = 1.0
      gw1.m_vac3 = 1.0
      gw1.m_iac1 = 1.0
      gw1.m_iac2 = 1.0
      gw1.m_iac3 = 1.0
      gw1.m_fac1 = 1.0
      gw1.m_fac2 = 1.0
      gw1.m_fac3 = 1.0
      gw1.m_pgrid= 1.0
      gw1.m_eday = 1.0
      gw1.m_etotal= 1.0
      gw1.m_htotal= 1.0
      gw1.m_temperature= 1.0

      gw2 = copy.deepcopy(gw1)
      gw2.m_inverter_sn = 2
      gw3 = copy.deepcopy(gw1)
      gw3.m_inverter_sn = 3
      gw4 = copy.deepcopy(gw1)
      gw4.m_inverter_sn = 4
      gw5 = copy.deepcopy(gw1)
      gw5.m_inverter_sn = 5
      gw6 = copy.deepcopy(gw1)
      gw6.m_inverter_sn = 6
      gw10 = copy.deepcopy(gw1)

      gw10.m_inverter_sn = 10
      gw10.m_vpv1 = 10.0
      gw10.m_vpv2 = 10.0
      gw10.m_ipv1 = 10.0
      gw10.m_ipv2 = 10.0
      gw10.m_vac1 = 10.0
      gw10.m_vac2 = 10.0
      gw10.m_vac3 = 10.0
      gw10.m_iac1 = 10.0
      gw10.m_iac2 = 10.0
      gw10.m_iac3 = 10.0
      gw10.m_fac1 = 10.0
      gw10.m_fac2 = 10.0
      gw10.m_fac3 = 10.0
      gw10.m_pgrid= 10.0
      gw10.m_eday = 10.0
      gw10.m_etotal= 10.0
      gw10.m_htotal= 10.0
      gw10.m_temperature= 10.0

      gw11 = copy.deepcopy(gw10)
      gw11.m_inverter_sn = 11

      gw12 = copy.deepcopy(gw10)
      gw12.m_inverter_sn = 12
      
      process = processData.processData(None, 4*60)
      process.reset()
      print "State:" + process.state_to_string()
      process.processSample( gw1)
      print "State:" + process.state_to_string()
      process.processSample( gw2)
      print "State:" + process.state_to_string()
      process.processSample( gw3)
      print "State:" + process.state_to_string()
      process.processSample( gw4)
      print "State:" + process.state_to_string()
      process.processSample( gw10)
      print "State:" + process.state_to_string()
      process.processSample( gw11)
      print "State:" + process.state_to_string()
      process.processSample( gw5)
      print "State:" + process.state_to_string()
      process.processSample( gw6)
      print "State:" + process.state_to_string()
      process.processSample( gw12)
      print "State:" + process.state_to_string()
      process.reset()
      print "State:" + process.state_to_string()

if __name__ == "__main__":
   t = test()
   t.do_tests()
