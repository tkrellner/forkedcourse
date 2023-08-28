# Getting ready to Python

## Page Contents
- [General Plan](#general-plan)
- [Tools for managing computing environments, libraries, and dependencies](#tools-for-managing-computing-environments-libraries-and-dependencies)
- [Installing `conda`](#installing-conda)
    - [Installing `conda` using the `Miniconda` installer on Windows:](#installing-conda-using-the-miniconda-installer-on-windows)
    - [Installing `conda` via Miniconda on MacOS:](#installing-conda-via-miniconda-on-macos)
    - [Installing `conda` via Miniconda on Linux:](#installing-conda-via-miniconda-on-linux)
- [Managing computing environments using `conda`](#managing-computing-environments-using-conda)
    - [Creating a new environment](#creating-a-new-environment)
    - [Activating an environment](#activating-an-environment)
    - [Deactivating an environment](#deactivating-an-environment)
    - [Removing an environment](#removing-an-environment-generally-you-wont-want-to-do-this)
- [Managing code and execution (IDEs)](#managing-code-and-execution-ides)
- [Installing and configuring VSCode](#installing-and-configuring-vscode)
    - [Installing VSCode](#installing-vscode)
    - [Installing the `eds217_2023` Python Environment](#installing-the-eds217_2023-python-environment)
    - [Setting Up the `eds217_2023` Environment in VSCode](#setting-up-the-eds217_2023-environment-in-vscode)
- [Installing the `eds217_2023` Python Environment](#installing-the-eds217_2023-python-environment)
  - [Setting Up the `eds217_2023` Environment in VSCode](#setting-up-the-eds217_2023-environment-in-vscode)

## General plan

There are many ways to set up your local machine to run maintainable python data science code. In addition to the usual need to build your code using version control (e.g. GitHub), any strategy for local computation requires three critical components:

1. A system for managing computing environments to ensure that code runs in a consistent environment.
1. A system for managing python packages to ensure that code runs with consistent dependencies.
1. A system for managing python code, which is usually an integrated development environment (IDE) in which editing and running code occur interactively.

In the past, these three components were often managed separately, but in recent years, there has been a trend towards integrating these components into a single system. For example, the [RStudio IDE](https://rstudio.com) is a single system that manages all three components for R code. Similarly, the [Data Spell IDE](https://www.jetbrains.com/dataspell/) is a single system that manages all three components for python code.

In this class, we will use a combination of tools to manage these three components. We will use `conda` to manage computing environments and python packages, and we will use [Visual Studio Code](https://code.visualstudio.com) as our IDE.

These are both very popular tools in the python data science community, and they are both free and open source. However, there are many other options for managing computing environments, python packages, and code execution. We will discuss some of these options below, or you can skip ahead to the [instructions](#instructions) for setting up your local machine.

## Tools for managing computing environments, libraries, and dependencies

There are many options for managing computing environments. These days, a common method is to use `containers`, in which an entire computational system (including processes, memory, disk space) is spun up as an isolated service on your local (or remote) machine. Tools such as [docker](https://www.docker.com) or python-specific [shiv](https://shiv.readthedocs.io/en/latest/) allow for isolated packaging and execution of python programs. Generally, these are better-suited for deployment of code on remote servers, but they can be used locally too. In this class, we're not going to use containers. Instead we will use a more traditional approach to managing computing environments and packages.

More traditional approaches to managing computing environments and/or packages and dependencies include a suite of diverse tools. Some of these focus only on managing computing environments, while others focus on managing python packages. Some are designed to work with python only (e.g `venv`, `conda`), while others are designed to work with any programming language (e.g `virtualenv`). A few of the most popular options in each category are listed below. 

#### Package management tools for python
[`pip`](https://pip.pypa.io/en/stable/) is the standard package management tool for python. It is included with the standard python distribution, and it is the most widely used package management tool for python. However, it does not manage computing environments, so it is not as widely used as other tools below.

[`pipx`](https://pipxproject.github.io/pipx/) is a tool designed to manage python packages. It has the advantage of being able to install any package hosted on [PyPI](https://pypi.org), as well as packages hosted on github and even packages you’ve made on your local machine. However, it does not manage computing environments, and it does not manage package dependencies.

#### Environment management tools for python 
[`virtualenv`](https://virtualenv.pypa.io/en/latest/) is a tool to create isolated Python environments. Since Python 3.3, a subset of it has been integrated into the standard library as [`venv`](https://docs.python.org/3/library/venv.html). While `venv` is sufficient to create virtual environments, it does not manage package dependencies, so it is also not as widely used as other tools below. 

### Tools that manage both environments and packages

[`conda`](https://docs.conda.io/en/latest/) is a tool developed by [Anaconda](https://anaconda.org) that is designed to manage computing environments. However, it also allows you to install packages, and even install binaries of packages directly without the need for local compilation. It also manages package dependencies, ensuring libraries are inter-operable.

[`mamba`](https://mamba.readthedocs.io/en/latest/) is a new tool developed by the [QuantStack](https://quantstack.net) team that is designed to be a drop-in replacement for `conda`. It allows you to create new environments, install packages, and even install binaries of packages directly without the need for local compilation. It also manages package dependencies, ensuring libraries are inter-operable. It is designed to be faster than `conda` and to use fewer resources. It is also designed to be more compatible with `pip` than `conda`. However, it is not as widely used as `conda` and it is not as well-supported by IDEs.

[`poetry`](https://python-poetry.org) is another new tool that is designed to manage computing environments and python packages. Advantages of `poetry` include a simplified approach to dependency management and a simplified approach to building and packaging your own code for distribution. Disadvantages include a lack of support for `conda` environments and a lack of support for `pip` packages that are not hosted on [PyPI](https://pypi.org) (although this may change in the future).

Throughout this course, **we will use `conda` for our environment management**. We can access `conda` through the terminal/command line or within a terminal inside an IDE.

## `conda` installation and usage

### Installing `conda`

If you want to install just `conda` without the entire Anaconda distribution (which includes many packages you may not need and is quite large), you can use **Miniconda**. Miniconda is a minimal installer for `conda` and includes only `conda`, Python, and the packages they depend on. Once installed, you can add any other packages you need using `conda` or `pip`.

---

### Installing `conda` using the `Miniconda` installer on Windows:

1. **Download Miniconda Installer**:
    - Go to the [Miniconda download page](https://docs.conda.io/en/latest/miniconda.html).
    - Download the Miniconda installer for Windows. Make sure to choose the appropriate version (Python 3.9, either 32 or 64-bit) based on your machine.

2. **Run the Installer**:
    - Locate the downloaded installer and double-click on it to start the installation process.
    - Follow the on-screen instructions. Here are some recommendations for the installation:
        - Choose "Just Me" unless you're sure about the "All Users" option.
        - Use the default installation location unless you have a specific need to change it.
        - It's recommended to check the box "Add Miniconda to my PATH environment variable" for easier command-line use. However, be aware that this can interfere with other Python installations.

3. **Verify Installation**:
    - Open the Command Prompt (you can search for `cmd` in the Windows search bar).
    - Type `conda --version` and press Enter. This should display the version of `conda` installed, confirming that the installation was successful.

4. **Update Conda** (Optional but Recommended):
    - It's a good practice to ensure you have the latest version of `conda` after installation. In the Command Prompt, type:
        ```bash
        conda update conda
        ```
    - Press Enter and follow any on-screen instructions to update `conda`.

Of course! Here are the instructions for installing Miniconda on MacOS and Linux:

---

### Installing `conda` via Miniconda on MacOS:

1. **Download Miniconda Installer**:
    - Go to the [Miniconda download page](https://docs.conda.io/en/latest/miniconda.html).
    - Download the Miniconda installer for MacOS. Make sure to choose the appropriate version (Python 3.x) based on your preference.

2. **Run the Installer**:
    - Open a terminal.
    - Navigate to the directory where the installer was downloaded.
    - Make the installer executable with the command:
      ```bash
      chmod +x Miniconda3-latest-MacOSX-x86_64.sh
      ```
      (Note: the filename may be different depending on the version of Miniconda you downloaded)

    - Start the installation process with:
      ```bash
      ./Miniconda3-latest-MacOSX-x86_64.sh
      ```
    - Follow the on-screen instructions to complete the installation.

3. **Verify Installation**:
    - In the terminal, type:
      ```bash
      conda --version
      ```
    - This should display the version of `conda` installed, confirming that the installation was successful.

4. **Update Conda** (Optional but Recommended):
    - To ensure you have the latest version of `conda`, type:
      ```bash
      conda update conda
      ```

---

### Installing `conda` via Miniconda on Linux:

1. **Download Miniconda Installer**:
    - Go to the [Miniconda download page](https://docs.conda.io/en/latest/miniconda.html).
    - Download the Miniconda installer for Linux. Make sure to choose the appropriate version (Python 3.x) based on your preference.

2. **Run the Installer**:
    - Open a terminal.
    - Navigate to the directory where the installer was downloaded.
    - Make the installer executable with the command:
      ```bash
      chmod +x Miniconda3-latest-Linux-x86_64.sh
      ```
      (Note: the filename may be different depending on the version of Miniconda you downloaded)
    - Start the installation process with:
      ```bash
      ./Miniconda3-latest-Linux-x86_64.sh
      ```
    - Follow the on-screen instructions to complete the installation.

3. **Verify Installation**:
    - In the terminal, type:
      ```bash
      conda --version
      ```
    - This should display the version of `conda` installed, confirming that the installation was successful.

4. **Update Conda** (Optional but Recommended):
    - To ensure you have the latest version of `conda`, type:
      ```bash
      conda update conda
      ```

## Managing computing environments using `conda`

### Creating a new environment

Conda can create new environments using a markup language specification called `yaml`. We will use an environment file created for our course to create an `eds-217` environment on your local machine.

You can create a new environment using the following command:

```bash
    conda create -n my_cool_environment
```

### Activating an environment

You can activate an environment using the following command:

```bash
    conda activate my_cool_environment
```

### Deactivating an environment

You can deactivate an environment using the following command:

```bash
    conda deactivate
``` 
There is no need to deactivate an environment before activating a different environment.

### Removing an environment (generally, you won't want to do this!)

You can remove an environment using the following command:

```bash
    conda env remove -n my_cool_environment
```

## Managing code and execution (IDEs)

Finally, we come to the tool you will use most when coding on your local computer – the Integrated Development Environment, or IDE. The possibilities for IDEs is even more expansive than for either of the other tools. Common python IDEs include:

- [Visual Studio Code](https://code.visualstudio.com)
- [Jupyter Notebooks](https://jupyter.org)
- [Jupyter Labs](https://jupyter.org)
- [Spyder](https://www.spyder-ide.org)
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Data Spell](https://www.jetbrains.com/dataspell/)
- [Atom](https://atom.io)
- [RStudio](https://www.rstudio.com)

Any of these would work well for a python data science workflow, but definitely some have more features focused on data science than others. For example, PyCharm is more focused on software engineering, but a new IDE called Data Spell, by the same company (Jet Brains), is squarely centered on data science workflows.

The best IDE is usually the one you are most familiar with. For that reason, RStudio isn’t a bad choice for an IDE. Although you will only be able to write code in quarto (.qmd) files, RStudio will be sufficient for many of your python needs.

However, if you need to edit .ipynb files natively (without conversion to .py or .qmd), you will probably want to use an IDE that is designed to efficiently parse these files and allow you to execute code directly.

We’ve been using `Jupyter` (both notebooks and lab) this class, and you can continue to do so on your local machine. However, it’s probably best to use a non-browser IDE if possible, since that will provide more opportunities for customization and removes a layer of complication required when executing your code.

**In this class, we will focus on using Visual Studio Code (VSCode).**

Having covered all the bases, we need to go ahead and get to work. Here are the steps for getting our class environment working on your machine, and within your IDE.

## Installing and Configuring VSCode

### Installing VSCode

1. Go to the [VSCode download page](https://code.visualstudio.com/download) and download the appropriate version for your operating system.
1. Run the installer and follow the instructions.
1. Open VSCode from the Start Menu (Windows) or Applications folder (MacOS).
1. Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for VSCode from the Visual Studio Code Marketplace.
1. Install the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) for VSCode from the Visual Studio Code Marketplace.
1. Restart VSCode.

### Installing the `eds217_2023` python environment.

#### Prerequisites:

1. Ensure you have already installed `conda` ([see above](#installing-conda)).

#### Instructions:

##### 1. Fork the `eds217_2023` repository:

Go to the [eds217_2023](https://github.com/environmental-data-science/eds217_2023) repository and click the "Fork" button in the upper right corner of the page. This will create a copy of the repository in your GitHub account.

##### 2. Clone Your forked repository

Open a terminal (Command Prompt on Windows, Terminal on MacOS/Linux) and navigate to the directory where you want to clone the repository.

```bash
git clone https://github.com/YOUR_USERNAME/eds217_2023.git
cd eds217_2023
```

Replace `YOUR_USERNAME` with your GitHub username.

##### 3. Create the `conda` environment

Windows:

```bash
conda env create -f environment.yml
conda activate eds217_2023
```

MacOS/Linux:

```bash
conda env create -f environment.yml
source activate eds217_2023
```

##### 4. Set up the `eds217_2023` environment as an `ipykernel`

In order to make sure our python environment is used when running code within an interactive editor such as a Jupyter notebook or in an IDE, you need ensure that the correct kernel is used to run our code. A python kernel is a program that runs and introspects the user's code. Interactive tools such as Jupyter and IDEs use the kernel to execute code when you run a cell in the editor. `ipykernel`` is a tool that allows you to use specific python kernels when running code interactively within Jupyter notebooks and IDEs.

After activating the `eds-217` environment, run the following command:

```bash
python -m ipykernel install --user --name eds217_2023 --display-name "Python (eds217_2023)"
```

This will allow you to select the `eds217_2023` environment as a kernel in Jupyter or in your IDE.

##### 5. Launching `VSCode`:

With the environment activated, you can launch VSCode from the command line:

```bash
code .
```
Alternatively, you can launch VSCode from the Windows Start Menu or MacOS Applications folder, or however you normally launch applications on your machine.

Once VSCode is open, you can open a new Python file. Ensure you select the "Python (eds217_2023)" kernel for your file. VSCode will prompt you to install the `ipykernel` package if it is not already installed. In addition, VSCode will remember the kernel you selected for each file, so you will only need to select the kernel once for each file.

### Setting Up the `eds217_2023` environment in VSCode

#### Prerequisites:

1. Ensure you have [Visual Studio Code](https://code.visualstudio.com/) installed.
2. Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) for VSCode from the Visual Studio Code Marketplace.
3. Follow the previous instructions to set up the `eds217_2023` environment on your machine.

#### Instructions:

##### 1. Open the `eds217_2023` Directory in VSCode:

Launch VSCode, then go to `File` > `Open Folder` (or `File` > `Open` on MacOS) and select the `eds217_2023` directory that you cloned from GitHub.

##### 2. Selecting the Python Interpreter:

Once the folder is open in VSCode:

- Click on the Python version in the  corner of the VSCode window.
- A list of available Python interpreters will appear at the top. Look for the one that corresponds to the `eds217_2023` environment. It should look something like this: `Python (eds217_2023)`.
- Click on it to select it. This ensures that any Python file or Jupyter notebook you open in VSCode will use the `eds217_2023` environment.

##### 3. Verify the Jupyter Kernel:

If you're working with Jupyter notebooks in VSCode:

- Open or create a new Jupyter notebook (`.ipynb` file).
- In the top-right corner of the notebook editor, you'll see the kernel that the notebook is using. Ensure it says `Python (eds217_2023)`. If not, click on it and select `Python (eds217_2023)` from the dropdown list.

##### 4. Troubleshooting:

If you don't see the `eds217_2023` environment in the list of available interpreters or kernels:

- Ensure you've activated the environment in your terminal and installed the Jupyter kernel as described in the previous instructions.

- Restart VSCode.
