import libnmea_navsat_driver.parser

nmea_str = "$AGRSA,0.14,A,,V*4A"

parsed_sentence = libnmea_navsat_driver.parser.parse_nmea_sentence(nmea_str)

print(parsed_sentence)