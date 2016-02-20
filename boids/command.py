from argparse import ArgumentParser
from boids import Boids
import json
import ConfigParser

def process():
	''' 
	Description: A function to communicate with the command line. This function is linked with the setup.py file.
	'''
	parser = ArgumentParser(description = "The Boids Flocking Bird Simulation")
	parser.add_argument('--config','-c',help='Config file',default='config.cfg')
	args = parser.parse_args()
	
	config = ConfigParser.ConfigParser()
	with open(args.config) as f:
		config.readfp(f)
		
		count =config.getint('Boids','count')
		position_limits =  json.loads(config.get('Boids', 'position_limits'))
		velocity_limits =  json.loads(config.get('Boids', 'velocity_limits'))
		move_to_middle_strength = config.getfloat('Dynamics', 'move_to_middle_strength')
		alert_distance = config.getfloat('Dynamics', 'alert_distance')
		formation_flying_distance = config.getfloat('Dynamics', 'formation_flying_distance')
		formation_flying_strength = config.getfloat('Dynamics', 'formation_flying_strength')

		boids = Boids(count, position_limits, velocity_limits,
                      move_to_middle_strength, 
                      alert_distance,
                      formation_flying_distance,
                      formation_flying_strength)
		boids.deploySimulation()

		
	
if __name__ == "__main__":
	process()