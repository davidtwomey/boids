"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np

#------------------To be moved to fixtures file ------------
#boids_x=[random.uniform(-450,50.0) for x in range(50)]
#boids_y=[random.uniform(300.0,600.0) for x in range(50)]
#boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
#boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
#boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)
#---------------------------------------------------------

class Boids(object):
	'''
	Description: A class to model aggregate motion of a flock of simulated birds (boids)
	'''
	def __init__(self, boid_count, position_limits, 
                                   velocity_limits,
                                   move_to_middle_strength,
                                   alert_distance,
                                   formation_flying_distance,
                                   formation_flying_strength):
		self.positions = self.new_flock(boid_count,
            np.array(position_limits[0:2]),
            np.array(position_limits[2:4]))
		self.velocities = self.new_flock(boid_count,
            np.array(velocity_limits[0:2]),
            np.array(velocity_limits[2:4]))
		self.move_to_middle_strength = move_to_middle_strength
		self.alert_distance = alert_distance
		self.formation_flying_distance = formation_flying_distance
		self.formation_flying_strength = formation_flying_strength


	def update_boids(self, positions, velocities):
		#Calculation of boid separations and square distances
		separations, square_distances = self.separations_square_distances(positions)
		# Fly towards the middle
		self.fly_towards_middle(positions,velocities,
                                move_to_middle_strength= self.move_to_middle_strength)
		# Fly away from nearby boids
		self.fly_away_from_nearby_boids(positions, velocities, separations, square_distances,
			alert_distance = self.alert_distance)
		# Try to match speed with nearby boids
		self.match_speed_with_nearby_birds(positions, velocities, square_distances,
                formation_flying_distance = self.formation_flying_distance, 
                formation_flying_strength = self.formation_flying_strength)
		# Move according to velocities
		positions += velocities

	def deploySimulation(self):
		figure=plt.figure()
		axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
		self.scatter=axes.scatter(self.positions[0,:],self.positions[1,:])
		anim = animation.FuncAnimation(figure, self.animate,
                               frames=50, interval=50)
		plt.show()
	def animate(self, frame):
		self.update_boids(self.positions,self.velocities)
		self.scatter.set_offsets(self.positions.transpose())

	def new_flock(self, count,lower_limits, upper_limits):
		width = upper_limits-lower_limits
		return (lower_limits[:,np.newaxis] + np.random.rand(2,count)*width[:,np.newaxis])

	def separations_square_distances(self, positions):
		separations = positions[:,np.newaxis,:] - positions[:,:,np.newaxis]
		squared_displacements = separations*separations
		square_distances = np.sum(squared_displacements, 0)
		return separations, square_distances

	def fly_towards_middle(self, positions, velocities,
                                 move_to_middle_strength):
		middle = np.mean(positions, 1)
		direction_to_middle = positions - middle[:, np.newaxis]
		velocities -= direction_to_middle * move_to_middle_strength

	def fly_away_from_nearby_boids(self, positions, velocities, separations, square_distances,
                                   alert_distance = 100):
		far_away = square_distances > alert_distance
		separations_if_close = np.copy(separations)
		separations_if_close[0,:,:][far_away] = 0
		separations_if_close[1,:,:][far_away] = 0
		velocities += np.sum(separations_if_close, 1)

	def match_speed_with_nearby_birds(self, positions, velocities, square_distances,
                                      formation_flying_distance = 10000, formation_flying_strength = 0.125):
		very_far = square_distances > formation_flying_distance
		velocity_differences = velocities[:,np.newaxis,:] - velocities[:,:,np.newaxis]
		velocity_differences_if_close = np.copy(velocity_differences)
		velocity_differences_if_close[0,:,:][very_far] = 0
		velocity_differences_if_close[1,:,:][very_far] = 0
		velocities -= np.mean(velocity_differences_if_close, 1) * formation_flying_strength

