#!/bin/python
from shell import Shell
import pprint

pp = pprint.PrettyPrinter(indent=4)
student_users = []
faculty_users = []
sh = Shell()
sh.run('oc get groups')
for index, oc_groups in enumerate(sh.output()):
    if index > 2:    
        # print(oc_groups)
        pp.pprint(oc_groups)
        group_dn, group_users = oc_groups.split()
        if group_dn == 'CN=ist-students,OU=IST,DC=lab,DC=local':
            student_users.append(group_users.split(',').strip())
        elif group_dn == 'CN=ist-faculty,OU=IST,DC=lab,DC=local':
            faculty_users.append(group_users.split(',').strip())

pp.pprint(student_users)
pp.pprint(faculty_users)