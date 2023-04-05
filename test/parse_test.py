import libnmea_navsat_driver.parser

nmea_str = "$HCHDG,280.0,0.0,E,23.3,W*68"

parsed_sentence = libnmea_navsat_driver.parser.parse_nmea_sentence(nmea_str)

print(parsed_sentence)