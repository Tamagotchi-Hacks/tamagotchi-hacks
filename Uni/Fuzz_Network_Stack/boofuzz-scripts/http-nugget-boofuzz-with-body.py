#!/usr/bin/env python3
# Designed for use with boofuzz v0.2.0

# More advanced request definitions can be found in the request_definitions directory.
from boofuzz import *
import datetime;

def main():
    port = 80
    host = '192.168.4.1'
    web_interface_listen='0.0.0.0'
    web_interface_listen_port=2600
    ct = datetime.datetime.now()
    output_filename=f'./boofuzz-results/nugget-prime-4-{ct}.db'
    session_persistsant_filename='./boofuzz-results/session-save-2024-03-26 14:57:51.015154.dat'
#    session_persistsant_filename=f'./boofuzz-results/session-save-{ct}.dat'
#    csv_log = open('fuzz_results.csv', 'wb') ## create a csv file
#    my_logger = [FuzzLoggerCsv(file_handle=csv_log)] ### create a FuzzLoggerCSV object with the file handle of our csv file

    session = Session(
        target=Target(connection=TCPSocketConnection(host, port)),
        receive_data_after_fuzz=True,
        web_address=web_interface_listen,
	web_port=web_interface_listen_port,
        db_filename=output_filename,
        session_filename=session_persistsant_filename,
#        console_gui=True
# 	 fuzz_loggers=my_logger ## set my_logger (csv) as the logger for the session
    )


    s_initialize(name="Request")
    with s_block("Request-Line"):
        s_group("Method", ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE"])
        s_delim(" ", name="space-1")
        s_string("/index.html", name="Request-URI")
        s_delim(" ", name="space-2")
        s_string("HTTP/1.1", name="HTTP-Version")
        s_static("\r\n", name="Request-Line-CRLF")
        s_string("Host:", name="Host-Line")
        s_delim(" ", name="space-3")
        s_string("example.com", name="Host-Line-Value")
        s_static("\r\n", name="Host-Line-CRLF")
        s_static("Content-Length:", name="Content-Length-Header")
        s_delim(" ", name="space-4")
        s_size("Body-Content", output_format="ascii", name="Content-Length-Value")
        s_static("\r\n", "Content-Length-CRLF")
    s_static("\r\n", "Request-CRLF")

    with s_block("Body-Content"):
        s_string("Body content ...", name="Body-Content-Value")

    session.connect(s_get("Request"))

    session.fuzz()


if __name__ == "__main__":
    main()
