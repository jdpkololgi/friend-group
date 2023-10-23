"""An example of how to represent a group of acquaintances in Python."""
import numpy as np
import pandas pd

class network:
    def __init__(self):
        self.network = pd.DataFrame() # A numpy array of people and their relationships

    def add_person(self, person:str):
        if person in self.network.columns:
            print("This person already exists")
        else:
            self.network[person] = ''
            self.network.loc[person] = ''
    
    def add_relationships(self, namei:str, namef:str, relation:str, asymmetric_relation:str|None = None):
    
        if namei in self.network.columns and namef in self.network.columns: # Add relationships if the people exist
            self.network.loc[namei][namef] = relation
            if asymmetric_relation != None:
                self.network.loc[namef][namei] = asymmetric_relation
            else:
                self.network.loc[namef][namei] = relation

        else: # Create the people and add their relationships if they don't exist
            self.add_person(namei)
            self.add_person(namef)
            self.network.loc[namei][namef] = relation
            if asymmetric_relation != None:
                self.network.loc[namef][namei] = asymmetric_relation
            else:
                self.network.loc[namef][namei] = relation
        
our_network = network()

class People:

    def __init__(self, name:str, age:int | float, job:str, our_network:network):
        self.name = name
        self.age = age
        self.job = job
        self.ournetwork = our_network
        self.our_network.add_person(self.name)
        self.relations = self.our_network.network.loc[self.name]

    def add_relation(self, namei:str, namef:str, relation:str, asymmtric_relation:str|None=None):
        self.ournetwork.add_relationships(namei=namei, namef=namef, relation=relation, asymmetric_relation=asymmtric_relation)
        
