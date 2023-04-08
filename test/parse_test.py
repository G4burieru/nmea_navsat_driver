import libnmea_navsat_driver.parser

nmea_str = "$GPVTG,52.68,T,,M,0.00,N,0.00,K,A*04"

parsed_sentence = libnmea_navsat_driver.parser.parse_nmea_sentence(nmea_str)

print(parsed_sentence)