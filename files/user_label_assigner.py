#!/bin/python
from shell import Shell
import pprint

pp = pprint.PrettyPrinter(indent=4)
student_users = []
faculty_users = []
sh = Shell()
sh.run('oc get groups')
for index, oc_groups in enumerate(sh.output()):
    if index > 0:    
        print(oc_groups)
        groups_temp = oc_groups.split()
        group_dn = groups_temp[0]
        group_users= groups_temp[1:]
        if group_dn == 'CN=ist-students,OU=IST,DC=lab,DC=local':
            for user in group_users:
                student_users.append(group_users.strip(','))
            # student_users.append(group_users.split(',').strip())
        elif group_dn == 'CN=ist-faculty,OU=IST,DC=lab,DC=local':
            for user in group_users:
                faculty_users.append(group_users.strip(','))
            # faculty_users.append(group_users.split(',').strip())

pp.pprint(student_users)
pp.pprint(faculty_users)
