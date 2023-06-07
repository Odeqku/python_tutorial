#!/usr/bin/python3

class Gizmo:
    object_no = 0

    def __init__(self):
        Gizmo.object_no += 1
        print('Gizmo Class Object_{} id: {}'.format(Gizmo.object_no, id(self)))

x = Gizmo()
y = Gizmo()
