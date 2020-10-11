# TUM.ai Onboarding - Tech Setup

Hello and welcome at TUM.ai. This short tutorial gives an introduction into the technologies that will be used often at TUM.ai.
If you have already worked on software projects, you might already know most of these technologies. Then fell free to skip the tutorial or parts of it.

This tutorial is made for Linux, if you are using Windows, please have a look at the **WINDOWS_README.md** file in this repository.

The technologies included in this tutorial are:
1. Git
2. Python3
3. Python3 - venvs
4. Python3 - Important packages overview
5. Python3 - Jupyter Notebook

Throughout this tutorial, you will see some **TASK**s. These tasks should be completed to complete the tutorial.

# Git
Git is a version control system. It makes working together on software projects way more easy and can help avoiding data loss by human error.
You can install git by typing  
`sudo apt-get install git`  
into the terminal.  
Git basically stores past versions of your work, and if you mess something up, you can go back to when everything was still working fine.
Also, you can upload your code, so that other members of your team can download and use it. All the code will be stored in a repository, similar to this tutorial.    
**Basic workflow**:  
*Creating a git repository*: Upon starting a project, you first create an empty git repository on either github.com/tum-ai or gitlab.com/tum-ai . For this tutorial, I created the repository https://github.com/tum-ai/tech-tutorial .  
*Downloading (Cloning) the repository*: The next step is downloading the repository, also called cloning. Therefore, you open the github project page in your browser. In the top right corner, there is a green button. Click on the button and copy the HTTPS link. If you have added a SSH key to your github account, you can also copy the SSH link, the advantage of SSH is that you don't have to enter a password anymore. To generate SSH an SSH key, check out https://onestopdataanalysis.com/github-ssh-setup/ .  
Then, go to the folder where you want to download the code in your terminal and type the command:  
`git clone LINK`  
**TASK**: Clone the repository of this tutorial in a folder on your computer.

Now, you should have a folder called *tech-tutorial* on your computer. Now, change directory (cd) into the folder and type  
`git status`  
