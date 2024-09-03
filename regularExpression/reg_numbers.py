invalid_numbers = [
    "KA 01 AB 1234",     # Karnataka registration, not Kerala
    "KL 1 AB 1234",      # Single-digit district code
    "KL 07 XYZ 5678",    # Three-letter series, should be two letters
    "KL 23 4567",        # Missing letter group
    "KL12CD5678",        # Missing spaces between parts
    "KL 00 AB 1234",     # Invalid district code "00"
    "KL 13 AB 12",       # Numeric part has only two digits
    "K 07 AB 1234",      # Missing "L" in the state code
    "KL 99 AB 1234",     # Invalid district code "99"
    "KL 06 Z 8901",      # Single-letter series, should be two letters
    "KL AB 1234",        # Missing district code
    "KL 12 34 5678",     # Incorrect format
    "KL 13 AB 12345",    # Numeric part has five digits
    "KL 04 5678",        # Missing letter group
    "KL12XY3456",        # Missing spaces
    "KL 03 AB CDEF",     # Alphabetic characters in place of numeric part
    "KL 07 AB 123"       # Numeric part has only three digits
]

valid_numbers = [
    "KL 01 AB 1234",
    "KL 15 CD 5678",
    "KL 07 EF 9101",
    "KL 12 GH 2345",
    "KL 09 IJ 6789",
    "KL 20 KL 1122",
    "KL 05 MN 3344",
    "KL 11 OP 5566",
    "KL 21 QR 7890",
    "KL 33 ST 4567",
    "KL 08 UV 3456",
    "KL 04 WX 8901",
    "KL 17 YZ 2345",
    "KL 18 AA 6789",
    "KL 28 BB 1234",
    "KL 16 CC 5678",
    "KL 02 DD 9101",
    "KL 31 EE 1122"
]

f=open("C:\\Users\\Luminar\\Desktop\\PythonJuneWorks\\regularExpression\\regnumbers.txt","a")



for num in valid_numbers:

    f.write(num+"\n")