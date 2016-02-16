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
	def __init__(self,boid_count, position_limits, velocity_limits, fields):
		self.positions = self.new_flock(boid_count,
            np.array(position_limits[0:2]),
            np.array(position_limits[2:4]))
		self.velocities = self.new_flock(boid_count,
            np.array(velocity_limits[0:2]),
            np.array(velocity_limits[2:4]))
		#self.fields = fields
		

	def update_boids(self, boids):
		xs,ys,xvs,yvs=boids
		# Fly towards the middle
		for i in range(len(xs)):
			for j in range(len(xs)):
				xvs[i]=xvs[i]+(xs[j]-xs[i])*0.01/len(xs)
		for i in range(len(xs)):
			for j in range(len(xs)):
				yvs[i]=yvs[i]+(ys[j]-ys[i])*0.01/len(xs)
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
		for i in range(len(xs)):
			xs[i]=xs[i]+xvs[i]
			ys[i]=ys[i]+yvs[i]

	def deploySimulation(self):
		figure=plt.figure()
		axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
		self.scatter=axes.scatter(boids[0],boids[1])
		anim = animation.FuncAnimation(figure, self.animate,
                               frames=50, interval=50)
		plt.show()
	def animate(self, frame):
		self.update_boids(boids)
		self.scatter.set_offsets(zip(boids[0],boids[1]))
		
	def new_flock(self, count,lower_limits, upper_limits):
		width = upper_limits-lower_limits
		return (lower_limits[:,np.newaxis] + np.random.rand(2,count)*width[:,np.newaxis])

	
		
		

if __name__ == "__main__":
	obj_boid = Boids()
	obj_boid.deploySimulation()