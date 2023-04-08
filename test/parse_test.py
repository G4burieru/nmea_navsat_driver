import libnmea_navsat_driver.parser

nmea_str = "$TIROT,1.29,A*01"

parsed_sentence = libnmea_navsat_driver.parser.parse_nmea_sentence(nmea_str)

print(parsed_sentence)