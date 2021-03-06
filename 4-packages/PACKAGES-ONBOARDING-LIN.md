# Python3 Packages
Packages are extensions, which you can import into your python code to gain powerful functionality.

## Installation
There are different options how to install packages. You can install them via the command line, via PyCharm or the Anaconda navigator. 
  
### PyCharm
To install packages in PyCharm, select  
`File > Settings > Project > Project Interpreter`.  
On the page, you can see a list of the packages you have installed. Make sure that the correct venv is selected.  
To install a new package, click on the **+** icon on the right
side of the page. Then, search for the package and click *Install Package* in the bottom left corner. Optionally, you can specify a version before installing, which may be required sometimes.  
  
### Terminal
Alternatively, you can use the terminal to install packages. Therefore, make sure that the correct venv is activated and then type  
`pip install package-name`  
into the terminal.  

**TASK**: Install the packages `numpy` and `matplotlib`

### requirements.txt
To make collaboration on a project easier, it is common practice to write down all the packages you are using in a requirements.txt file which is located in the root of the project.  
**TASK**: Take a look at the `requirements.txt` file.  
  
You can also automatically install all packages in the requirements.rxt file by typing  
`pip install -r requirements.txt`.  
**TASK**: Install all packages in the requirements.txt file.

## Importing packages into your code
Importing packages into your Python code is done via the `import` keyword.
**Examples:**  
Imagine that we want to use the function numpy.zeros((3,3)) that creates a 3x3 matrix with zeros.
- `import numpy` -> Imports entire numpy package. We can then use the function `numpy.zeros((3, 3))`
- `import numpy as np` -> Imports entire numpy package, but under another name (np). We can then use the function `np.zeros((3, 3))`
- `from numpy import zeros` -> Imports only the zeros(...) function. We can then use `zeros((3, 3))` without numpy or np  
  
This means that the way you import the package also influences the way you can use it.
  
**TASK**: Take a look at and run the python file `4-packages/packages.py`. Try to understand what is happening in the file and especially understand where and how the packages are imported.

## Package Overview
An overview with lots of great and powerful packages can be found under   
`4-packages/Cool_Python_Packages.pdf`

## End
You have now installed packages in your virtual environment and imported and used them in some code.  
The next and last part of this tutorial runs a small machine learning example in a jupyter notebook.