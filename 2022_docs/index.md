
# EDS 217 - Python for Environmental Data Science

## Python for Environmental Data Science

![code_screen.jpg](images/code_screen.jpg)

These notebooks provide an introduction to the Python programming language, the major libraries associated with the python data science stack, and opportunities to explore applications of python to environmental data science via analysis of rainfall variability, the development of stochastic models for daily rainfall in tropical drylands, investigation of water balance, and landscape energy balance.

The content in this module is more than possibly be done in a two-week course, but it is designed to allow students from any background to work through the material at their own pace.

The module assumes no prior experience with python, pandas, or jupyter notebooks. Where relevant, links to external resources, course presentations, and relevant XKCD comics are provided.

### Learning Goals

(what you will be able to do) - Read and write basic-to-intermediate scripts and programs in the Python programming language - Conduct reproducible analyses within interactive jupyter notebook environments - Perform analyses on structured data using numpy - Load, aggregate, analyze, and display data using pandas - Learn basics of matplotlib for plotting data. - Use scipy functions to develop fits of distributions to empirical data - Apply all of these tools to analyze environmental datasets - Develop a short tutorial on how to use a python data science library for environmental analysis^*

^* Final group presentation

### Course Outline

#### New For Week 2: TryPy

To create more open-ended opportunities for you to apply your python skills, I’ve ported over some exercises from EDS221. They are *essentially* the same, but now you will work on solving the problems using Python instead of R.

[**TryPy Exercises**](TryPy/TryPy.html)

#### Day 1 - Introduction to Python

The materials for Day 1 are designed to introduce the basics of working with Python.

- [Intro to Python Data Science](Lecture_1_Slides.html)
- [The Zen of Python](Lecture_2_Slides.html)
- [Exercise 1-0 - Hello World](./Exercise1-0_HelloWorld.html)
- [Exercise 1-1 - Variables & Operators](./Exercise1-1_Variables.html)

#### Day 2 - Introduction to Python

On Day 2, we will explore lists and learn the fundamentals of controlling the flow of programs.

- [Getting Help](Lecture_3_Slides.html)
- [Exercise 1-2 - Lists and Indexing](Exercise1-2_Lists.html)
- [Simple example of `enumerate` and `zip`](./enumerate_and_zip.html)
- [Exercise 1-3 - `If`s or `Else`s](./Exercise1-3_ControlFlowStatements.html)

#### Day 3 - Introduction to Python

On Day 3, we will journey into advanced topics related to Python, including structured data and object-oriented programming concepts.

- [Exercise 1-4 - Structured Data](./Exercise1-4_Structured-Data.html)
- [Exercise 1-5 - Functions 🦁, Objects 🐯, and Classes 🐻, Oh my!](./Exercise1-5_FunctionsObjectsClasses.html)

#### Day 4 - Numpy 🧮

Our journey into Python’s Data Science toolkit begins with NumPy, a library designed to perform advanced calculations on matrices.

- [Exercise 2-1 - NumPy](./Exercise2-1_Numpy.html)

#### Day 5 - Pandas 🐼

We end our first week with arguably the most important library in the Python data science ecosystem: Pandas.

- [Exercise 2-2 - Pandas](./Exercise2-2_Pandas.html)

#### Day 6 - Matplotlib 📈

Now that we’ve learned how to import, manage, and analyze data using pandas, it’s time to make some graphs! Matplotlib is the primary libary used for plotting data in Python (although there are some great alternatives), so we will start there.

- [Setting up your local Python](Setting_up_local.html)
- [Exercise 2-3 - Matplotlib](./Exercise2-3_Matplotlib.html)

#### Day 7 - Scipy 🔬

[Seaborn](./Seaborn.html) + [TryPy](TryPy/index.html) + Group work.

#### Extra Stuff:

Prediction and forecasting requires understanding how to fit distributions and functions to data sets. Today we will combine what we’ve learned so far and take a brief look at SciPy, which is a large library of tools that can be used to fit distributions.

- [Exercise 3 - SciPy](./Exercise3_Scipy.html)

#### Days 8 & 9 - Group Projects ✏️

Our final activity will be a group project in which you work with a team of 2-3 of your classmates to create a brief tutorial introducting one of the many other libraries available to conduct environmental data science in Python. You will develop your tutorial using the same Jupyter Notebook structures that we’ve been using throughout the class. On our last day, we’ll spend the afternoon conducting a **Python Data Science Show and Tell**

#### Bonus Content

Here are a couple more advanced - and interactive - examples of environmental data science. We won’t get to these during our brief time together, but feel free to explore them any time you feel like learning more about what you can do with Python!

- [Catchment Water Balance in Python](./Lab-1_Catchment_Water_Balance.html)
- [Landscape Energy Balance in Python](./Lab-2_Energy_Balance.html)

---

Note: This conversion is a direct representation of the HTML content into Markdown. Some elements, like styles and scripts, have been omitted as they are not directly translatable to Markdown.