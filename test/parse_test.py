import libnmea_navsat_driver.parser

nmea_str = "!AIVDM,1,1,,B,1:U8M80P00trH>QjqB`qdwvp2D2d,0*0A"

parsed_sentence = libnmea_navsat_driver.parser.parse_nmea_sentence(nmea_str)

print(parsed_sentence)