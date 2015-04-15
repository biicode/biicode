#!/usr/bin/env python
import sys, os
sys.path.append(os.path.join(os.getcwd(), "../"))
from biicode.client.shell.bii import main
main(sys.argv[1:])
