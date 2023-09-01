
# Python for Environmental Data Science
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/environmental-data-science/eds217_2023/main?labpath=index.ipynb)


Course Website
==================

The course description, learning goals, format, and outline with links to all activities can be found at the [course Website](https://bit.ly/eds217_2023)

How to use this repository
=============

### If you are a student in EDS 217:

1. Fork this repository to create a local copy in your github account. Do this by clicking the "Fork" button in the upper right corner of the [repository home page](https://github.com/environmental-data-science/eds-217/).

1. Clone the forked repository to your local computer

	* Open your `Terminal`.

	* Type `git clone` and the the url for your forked copy of this repository, which is `https://github.com/<your username>/eds217_2023`, where <your username> is your github user id.

	     The entire command will look like this:

		`$ git clone https://github.com/<your username>/eds217_2023`

		**Note:** In the line above, the `$` is your terminal prompt. On other systems, the command prompt is something like `>`, or `[username]$`. To keep these directions more general, I will just use `$` to represent the command prompt throughout our docs. The key point is that you *don't* need to type this as part of the command.

	* Press **Enter**. A local clone of the class repository will be created in your JupyterLab instance.

		```
		$ git clone https://github.com/<your username>/eds217_2023
		> Cloning into eds-217...
		> remote: Counting objects: 10, done.
		> remote: Compressing objects: 100% (8/8), done.
		> remove: Total 10 (delta 1), reused 10 (delta 1)
		> Unpacking objects: 100% (10/10), done.
		```

	     You will now have a new local directory in your instance called `eds217_2023/`, which contains all of the course materials. We will download and practice using all of the required software to use these course materials on Day 0 of the course. 

### For full local installation (for Instructors or non-students)

1. Install Conda & Git.

	* Mac OS: Use [homebrew](https://medium.com/ayuth/install-anaconda-on-macos-with-homebrew-c94437d63a37)
		
		`$ brew install anaconda`

		`$ brew install git`

	* Windows: ??

	* Linux: Use homebrew??

1. Clone the repository to your local machine and `cd` into the class repo directory

	`$ git clone https://github.com/environmental-data-science/eds217_2023`

	`$ cd eds217_2023`

1. Create a `conda` environment using the `environment.yml` file included in the repository.

	`$ conda env create --file environment.yml`

	**Note:** We are using python version [3.10.5](https://www.python.org/downloads/release/python-3105/) in this class. That may change in the future, but for now it matches the python that `taylor.bren.ucsb.edu` is using in RStudio's version of JupyterHub. 

1. Activate the `conda` envrionment

	`$ conda activate eds217_2023`

1. Install `pip` into the local conda environment.

	`$ conda install pip`

1. Add additional libaries to your conda environment using `pip`.

	`$ pip install -r requirements.txt`

	**Note:** We are using `pip` to manage dependencies within this conda environment. The use of `pip` and the `requirements.txt` file ensures consistency with our insallations on the JupyterHub server. This allows us to make sure that the working environment on our local machines matches *exactly* the working environment on JupyterHub. 

	**Note:** If you add a package to your local environment that is used in any of the course materials, you must use `pip freeze > requirements.txt` and push the new commit to our repo. 
	
	Update

