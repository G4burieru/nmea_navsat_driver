import libnmea_navsat_driver.parser

nmea_str = "$ERRPM,E,0,729.00,,A*52"

parsed_sentence = libnmea_navsat_driver.parser.parse_nmea_sentence(nmea_str)

print(parsed_sentence)