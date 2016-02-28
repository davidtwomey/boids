import sys
from boids.boids import Boids
from nose.tools import assert_almost_equal, assert_equal
import os
import yaml
import numpy as np
from mock import Mock, patch
fixtures_file = os.path.join(os.path.dirname(__file__),'fixtures','fixture.yaml')
fixtures = yaml.load(open(fixtures_file))

def test_update_boids():
	for fixture in fixtures:
		print fixture
		before = fixture.pop('before')
		after = fixture.pop('after')
		boids = Boids()
		boids.positions = np.array(before[0:2])
		boids.velocities = np.array(before[2:4])
		boids.update_boids(boids.positions,boids.velocities)
		assert_almost_equal(boids.positions.all(), np.array(after[0:2]).all())
		assert_almost_equal(boids.velocities.all(), np.array(after[2:4]).all())
		
def test_new_flock():
	for fixture in fixtures:
		new_flock = fixture.pop('new_flock')
		rand = new_flock['rand']
		positions = new_flock['positions']
		velocities= new_flock['velocity']
		with patch.object(np.random, 'rand', return_value=rand) as mock_method:
			boids = Boids()
			assert_equal(np.array(positions).all(),boids.positions.all())
			assert_equal(np.array(velocities).all(),boids.velocities.all())