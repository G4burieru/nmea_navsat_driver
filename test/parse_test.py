import libnmea_navsat_driver.parser

nmea_str = "$GPHDT,256.65,T*07"

parsed_sentence = libnmea_navsat_driver.parser.parse_nmea_sentence(nmea_str)

print(parsed_sentence)