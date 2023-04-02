import libnmea_navsat_driver.parser

nmea_str = "$GPZDA,130015.280,14,02,2023,,*5E"

parsed_sentence = libnmea_navsat_driver.parser.parse_nmea_sentence(nmea_str)

print(parsed_sentence)