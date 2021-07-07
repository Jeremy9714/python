# -*- coding: utf-8 -*-
"""
Spyder Editor

writeable attributes, compositor and policies
decision generation
multiple policies avaiable 
"""
import random

#permit-override, deny-override, permit-unless-deny, deny-unless-permit, first-applicable, only-one-applicable
compositor = ["POV", "DOV", "PUD", "DUP", "FA", "OPO", "ODO", "OOA"]
ATT = ["True", "False", "Unknown"]

def policy_generator(att_count):
    body = {}
    body['policy'] = "R0: Permit if ATT_0 // "
    body['attribute'] = {}
    body['attribute']["ATT_0"] = "True"
    final = 'P: {}(R0'.format(random.choices(compositor), k=1)
    
    for i in range(1, att_count):
        body['policy'] += "R{}: Deny if ATT_{} // ".format(i,i)
        body['attribute']['ATT_{}'.format(i)] = random.choices(ATT)
        final += ', R{}'.format(i)
    body['policy'] += final + ")"
    print(body)
    return body

#define compositors
def Compositor():

    return 

#decision generation 
def decision():
    return

#real world policy aspect
def realWorld():
    return

#output generated policies to a file
def outputAsFile():
    return

if __name__ == '__main__':
    policy_generator(4)
    
    