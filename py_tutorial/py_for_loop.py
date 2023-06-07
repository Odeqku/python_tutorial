#!/usr/bin/python3

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
print("Before deletion of the inactive key:", users)
"""
#Strategy: Iterate over a copy
for user, status in users.copy().items():
	if status == 'inactive':
#This line below deletes the key-value pair with an inactive status
		del users[user]
#This line below updates the status of the user that is inactive
		#users[user] = 'active'
print("After deletion of the inactive key:", users)

"""

#Strategy: Create a new collection
active_users = {}
for user, status in users.items():
	if status == 'active':
		active_users[user] = status
		
print("After the new creation:", active_users)
