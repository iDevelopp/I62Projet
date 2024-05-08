import entity

'''
    Behaviors:
        -Detection
        -Static vs Patrol
        -Attack

'''

def check_nearby_units(pos,range):
    pass
    #Retourne la liste des unités à porté de détection

def move_to_patrol_point():
    pass


class enemy_unit(entity):
    def __init__(situation, pos):
        #Utilise la situation pour lire ses alentours.
        self.situation = situation
        self.pos = pos

    def set_patrol_behavior(pos_list, speed):
        pass

    def update():
        pass

#Radar
class OF_R(enemy_unit):
    def __init__(situation, pos):
        super(enemy_unit, self).__init__(situation, pos)

'''
#Surface Ship
class OF_SF(enemy_unit):
    def __init__(situation, pos):
        pass

#Submarine
class OF_SM(enemy_unit):
    def __init__(situation, pos):
        pass

#AA
class OF_AA(enemy_unit):
    def __init__(situation, pos):
        pass

#Drone
class OF_D(enemy_unit):
    def __init__(situation, pos):
        pass
'''
