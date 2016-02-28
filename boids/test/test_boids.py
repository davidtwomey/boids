import sys
from boids.boids import Boids
from nose.tools import assert_almost_equal
import os
import yaml
import numpy as np

fixtures_file = os.path.join(os.path.dirname(__file__),'fixtures','fixture.yaml')
fixtures = yaml.load(open(fixtures_file))

def test_update_boids():
	for fixture in fixtures:
		before = fixture.pop('before')
		after = fixture.pop('after')
		boids = Boids()
		boids.positions = np.array(before[0:2])
		print boids.positions
		boids.velocities = np.array(before[2:4])
		boids.update_boids(boids.positions,boids.velocities)
		assert_almost_equal(boids.positions.all(), np.array(after[0:2]).all())
		assert_almost_equal(boids.velocities.all(), np.array(after[2:4]).all())