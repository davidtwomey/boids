from argparse import ArgumentParser
from Boids import Boids

def process():
	''' 
	Description: A function to communicate with the command line. This function is linked with the setup.py file.
	'''
	parser = ArgumentParser(description = "The Boids Flocking Bird Simulation")
	parser.add_argument('','',help='',default='')
	args = parser.parse_args()
	
if __name__ == "__main__":
	process()