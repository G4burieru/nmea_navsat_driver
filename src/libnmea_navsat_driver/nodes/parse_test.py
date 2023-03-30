import libnmea_navsat_driver.parser

nmea_str = "$GPGSA,A,3,02,10,16,18,23,26,29,32,66,81,67,68,1.30,1.10,1.10*04"

parsed_sentence = libnmea_navsat_driver.parser.parse_nmea_sentence(nmea_str)

print(parsed_sentence)