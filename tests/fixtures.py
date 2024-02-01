# Ruthlessly stolen from python-kafka.
# This is real live data from Kafka 11 broker
from typing import Final

record_batch_data_v2: Final = (
    # First Batch value == "123"
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00;\x00\x00\x00\x01\x02\x03"
    b"\x18\xa2p\x00\x00\x00\x00\x00\x00\x00\x00\x01]\xff{\x06<\x00\x00\x01]"
    b"\xff{\x06<\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00"
    b"\x00\x00\x01\x12\x00\x00\x00\x01\x06123\x00",
    # Second Batch value = "" and value = "". 2 records
    b"\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00@\x00\x00\x00\x02\x02\xc8"
    b"\\\xbd#\x00\x00\x00\x00\x00\x01\x00\x00\x01]\xff|\xddl\x00\x00\x01]\xff"
    b"|\xde\x14\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x00"
    b"\x00\x00\x02\x0c\x00\x00\x00\x01\x00\x00\x0e\x00\xd0\x02\x02\x01\x00"
    b"\x00",
    # Third batch value = "123"
    b"\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00;\x00\x00\x00\x02\x02.\x0b"
    b"\x85\xb7\x00\x00\x00\x00\x00\x00\x00\x00\x01]\xff|\xe7\x9d\x00\x00\x01]"
    b"\xff|\xe7\x9d\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\x00\x00\x00\x01\x12\x00\x00\x00\x01\x06123\x00"
    # Fourth batch value = "hdr" with header hkey=hval
    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00E\x00\x00\x00\x00\x02\\"
    b"\xd8\xefR\x00\x00\x00\x00\x00\x00\x00\x00\x01e\x85\xb6\xf3\xc1\x00\x00"
    b"\x01e\x85\xb6\xf3\xc1\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff"
    b"\xff\xff\x00\x00\x00\x01&\x00\x00\x00\x01\x06hdr\x02\x08hkey\x08hval",
)