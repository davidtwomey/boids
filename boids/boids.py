"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np

#------------------To be moved to fixtures file ------------
boids_x=[random.uniform(-450,50.0) for x in range(50)]
boids_y=[random.uniform(300.0,600.0) for x in range(50)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)
#---------------------------------------------------------

class Boids(object):
	'''
	Description: A class to model aggregate motion of a flock of simulated birds (boids)
	'''
	def __init__(self, boid_count, position_limits, 
                                   velocity_limits,
                                   move_to_middle_strength):
		self.positions = self.new_flock(boid_count,
            np.array(position_limits[0:2]),
            np.array(position_limits[2:4]))
		self.velocities = self.new_flock(boid_count,
            np.array(velocity_limits[0:2]),
            np.array(velocity_limits[2:4]))
		self.move_to_middle_strength = move_to_middle_strength
		

	def update_boids(self, positions, velocities):
		xs,ys,xvs,yvs=boids
		# Fly towards the middle
		self.fly_towards_middle(positions,velocities,
                                move_to_middle_strength= self.move_to_middle_strength)
		# Fly away from nearby boids
		for i in range(len(xs)):
			for j in range(len(xs)):
				if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100:
					xvs[i]=xvs[i]+(xs[i]-xs[j])
					yvs[i]=yvs[i]+(ys[i]-ys[j])
		# Try to match speed with nearby boids
		for i in range(len(xs)):
			for j in range(len(xs)):
				if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
					xvs[i]=xvs[i]+(xvs[j]-xvs[i])*0.125/len(xs)
					yvs[i]=yvs[i]+(yvs[j]-yvs[i])*0.125/len(xs)
		# Move according to velocities
		positions += velocities

	def deploySimulation(self):
		figure=plt.figure()
		axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
		self.scatter=axes.scatter(boids[0],boids[1])
		anim = animation.FuncAnimation(figure, self.animate,
                               frames=50, interval=50)
		plt.show()
	def animate(self, frame):
		self.update_boids(self.positions,self.velocities)
		self.scatter.set_offsets(self.positions.transpose())

	def new_flock(self, count,lower_limits, upper_limits):
		width = upper_limits-lower_limits
		return (lower_limits[:,np.newaxis] + np.random.rand(2,count)*width[:,np.newaxis])

	def fly_towards_middle(self, positions, velocities,
                                 move_to_middle_strength):
		middle = np.mean(positions, 1)
		direction_to_middle = positions - middle[:, np.newaxis]
		velocities -= direction_to_middle * move_to_middle_strength

if __name__ == "__main__":
	obj_boid = Boids()
	obj_boid.deploySimulation()