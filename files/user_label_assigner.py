#!/bin/python
from shell import Shell
import pprint, re

pp = pprint.PrettyPrinter(indent=4)
student_users = []
faculty_users = []
admin_users = []

sh = Shell()
sh.run('oc get groups --no-headers=true')
''' Extract users and assign them to lists depending on groups '''
for oc_groups in sh.output():
    print(oc_groups)
    groups_temp = oc_groups.split()
    group_dn = groups_temp[0]
    group_users= groups_temp[1:]
    if group_dn == 'CN=ist-students,OU=IST,DC=lab,DC=local':
        for user in group_users:
            student_users.append(user.strip(','))
    elif group_dn == 'CN=ist-faculty,OU=IST,DC=lab,DC=local':
        for user in group_users:
            faculty_users.append(user.strip(','))
    elif group_dn == 'CN=ist-administrators,OU=IST,DC=lab,DC=local':
        for user in group_users:
            admin_users.append(user.strip(','))

pp.pprint(student_users)
pp.pprint(faculty_users)
pp.pprint(admin_users)

# for user in student_users:
#     sh.run('oc ')
sh.run('oc get users')
re.split('\s+', sh.output())