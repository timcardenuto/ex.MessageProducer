#!/usr/bin/env python
#
#
# AUTO-GENERATED
#
# Source: ex.MessageProducer.spd.xml
from ossie.resource import start_component
import logging
import time

from MessageProducer_base import *

class MessageProducer_i(MessageProducer_base):

    def constructor(self):
        ''' something needed here '''
        
    def process(self):
        # build message
        geo_msg = MessageProducer_i.Geolocation()
        geo_msg.lat = 41.384586
        geo_msg.lon = -73.957693
        geo_msg.majoraxis = 10
        geo_msg.minoraxis = 5
        geo_msg.confidence = 'high'
        self._log.debug(geo_msg)
        
        # send message
        self.port_geo_out.sendMessage(geo_msg)
        
        time.sleep(self.update_rate)
        return NORMAL

  
if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    logging.debug("Starting Component")
    start_component(MessageProducer_i)

