Boids <br>
==============================

The boids library simulates flocking bird-like boids with a set of parameters determining the flock behavior. 
The models used here were proposed by Craig W. Reynolds in his paper entitled *"Flocks, Herds and Schools: 
A Distributed Behavioural Model"*. A link to this paper can be found <a href="http://d1.acm.org/citation.cfm?doid=37401.37406" target="_blank">here</a>

#Package Install Instructions

- Download repository to your machine from GitHub
- Navigate to Boids folder in command line shell
- Depending on your OS type either:
- **Windows**   : `python setup.py install`
- **Mac/Other** : `sudo python setup.py install`

**pip installation**
- If pip is correctly configured in the command line shell run:
`pip install git+ https://github.com/davidtwomey/boids.git`

#Example Usage

Once installed, the boids simulation can be run using the following commands:
+ `boid --CONFIG_FILE_LOCATION.cfg`
NOTE: the `--config` is an optional parameter specifying a custom configuration file. 

Please refer to the default config.cfg within this folder for the structure & format for configuring a custom configuration file



