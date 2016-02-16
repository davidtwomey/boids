from setuptools import setup, find_packages

setup(
    name = "Boids",
	author = "David Twomey",
	author_email = "David.Twomey.15@ucl.ac.uk",
	version = "0.1",
	license = 'MIT',
	description = "The Boids Flocking Bird Simulation",
	packages = find_packages(exclude=['*test']),
	install_requires = ['mock','nose','argparse','numpy','matplotlib'],
	scripts = ['scripts/boid']

)