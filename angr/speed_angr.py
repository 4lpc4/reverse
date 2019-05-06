import os
os.system("sudo apt install pypy -y && wget https://bootstrap.pypa.io/get-pip.py && sudo pypy get-pip.py ")
os.system("pypy -m pip install angr")
#p = angr.Project(xxx’)
#st = p.factory.full_init_state(add_options=angr.options.unicorn)
#st = p.factory.entry_state(add_options=angr.options.unicorn)
