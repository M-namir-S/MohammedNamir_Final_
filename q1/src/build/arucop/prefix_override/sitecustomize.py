import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/hp/MohammedNamir_Final_Test/q1/src/install/arucop'
