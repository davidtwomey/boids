import os
import yaml
import numpy as np
from boids.boids import Boids
from nose.tools import assert_almost_equal, assert_equal

#Regression testing of boids
def test_bad_boids_regression():
	regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixtures','regression.yaml')))
	boid_data=np.array(regression_data.pop("before"))
	boids = Boids()
	boids.positions = boid_data[0:2]
	boids.velocities = boid_data[2:4]
	boids.update_boids(boids.positions, boids.velocities)
	for after,before in zip(regression_data["after"],boid_data):
		for after_value,before_value in zip(after,before): 
			assert_almost_equal(after_value,before_value,delta=0.1)
