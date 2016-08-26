import os
import json
from ansible.module_utils.basic import *
from pwgen import pwgen
from openpyxl import load_workbook
from glob import glob
from jinja2 import Template
from netaddr import *
import yaml

def main():
    global module
    
    module = AnsibleModule(
        argument_spec = dict(    
		filename = dict(required=True)),   
        supports_check_mode=False)
    
    filename = module.params['filename']
   
    try:
        wb = load_workbook(filename=os.path.expanduser(filename), data_only=True)
    except:
        module.fail_json(msg='Failed to load workbook')
        
    try:
        configvarsTab = wb.get_sheet_by_name('configvars')
            
    except:
        module.fail_json(msg='Failed to locate required sheets')
        
      ###########################
	  # add my xls to dict code #
      ###########################	
    configvars = {'key1': 'Hello World'}	  
           
    module.exit_json(ansible_facts={'configvars': configvars, })

if __name__ == '__main__':
    main()
