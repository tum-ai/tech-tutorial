# Python3 Virtual Environments
Virtual environments are a very important tool if you want to use python professionally.  

**WHY TO USE?**  
When programming in python, you will always use packages, which are basically python code written by others for you.
These packages are sometimes very large and complex and will be installed in your python interpreter.  
Up until now, you only have one interpreter, which you installed in the last part of this tutorial, called the system interpreter.  
Now, imagine the following: You are working on 6 python projects simultaneously, which all require different packages. You probably don't want to install all these packages in the same interpreter.
Thats's where the virtual environments come into place.  

**WHAT IT DOES**  
The solution is to create a virtual environment for every project you work on.  
This basically creates a new python interpreter for your project.  
You then install the packages to the virtual environment's interpreter. By doing this, you only have the packages you need and your system interpreter stays clean.

## Installation
When using PyCharm and Anaconda, no installation is necessary.  
If you want to use the command line interface you can use the terminal command:  
`pip3 install virtualenv --user`

## Creating a venv for a project
**PyCharm**  
For Windows, I recommend to use conda environments.  
In PyCharm, goto `File > Settings > Project > Project Interpreter`.  
Now, select the gear button and *'Add'* in the top right corner to add a new interpreter.  
Now, select *Conda Environment* on the left and create a new environment. You can select your desired python version.  
After clicking *OK*, the new environment will be created and activated.  

After creating the environment, make sure to close all PyCharm Terminal and Python Console windows in the bottom of PyCharm, since these will still be using the old interpreter.
When opening a new terminal window, on the left of the path, the name of the venv should be written. It should look similar to that:  
`(tech-tutorial) C:\your\path\tech-tutorial>`

**Terminal**  
Create the virtualenv using 
`python -m venv venv`.  
You now need to activate the venv using 
`source venv/bin/activate`

**TASK**: Setup and activate a virtual environment for the tech tutorial project.

## End
You have now created a new virtual environment for your python project. In the next part, we will install and use some packages in this environment.