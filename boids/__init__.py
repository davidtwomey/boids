import json

from matplotlib import pyplot as plt
from argparse import ArgumentParser
from Boids import Boids

def command():
	''' 
	Description: A function to communicate with the command line. This function is linked with the setup.py file.
	'''
	
	parser = ArgumentParser(prog="Boids", description = "Boids Flocking Bird Simulation")
	parser.add_argument('','',help='',default='')
	args = parser.parse_args()