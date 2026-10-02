import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from judge import main

sys.argv.insert(1, os.path.basename(os.path.dirname(os.path.abspath(__file__))))
main()
