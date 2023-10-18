conctacts = {
    'number':4,
    'students':[
        {'name':'Sara Holder', 'email':'sara@example.com'},
        {'name':'Emlia Holder', 'email':'emlia@example.com'},
        {'name':'Juan Holder', 'email':'juan@example.com'},
        {'name':'Martha Holder', 'email':'martha@example.com'},
    ]
}

print('Student emails:')
for student in conctacts['students']:
    print(student['email'])