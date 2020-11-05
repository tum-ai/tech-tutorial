# Git
Git is a version control system. It makes working together on software projects way more easy and can help avoiding data loss by human error. 
Git basically stores past versions of your work, and if you mess something up, you can go back to when everything was still working fine.
Also, you can upload your code, so that other members of your team can download and use it. All the code will be stored in a repository, similar to this tutorial.

## Installation
You can install git from this website:  
https://git-scm.com/downloads  
I recommend to add *Git Bash Here* to the context menu (can be chosen during the installation), this makes opening a shell easier.

### Opening a shell
Now, in the windows explorer, go to the folder where you want to download the repository. 
Right-click the folder and select *'Git Bash Here'*. This should open a terminal. You can use this terminal for all git commands.

## Important commands

### Creating a git repository
Upon starting a project, you first create an empty git repository on either github.com/tum-ai or gitlab.com/tum-ai . For this tutorial, I created the repository https://github.com/tum-ai/tech-tutorial .

### Downloading (Cloning) the repository
The next step is downloading the repository, also called cloning. Therefore, you open the github project page in your browser. In the top right corner, there is a green button. Click on the button and copy the HTTPS link. If you have added a SSH key to your github account, you can also copy the SSH link, the advantage of SSH is that you don't have to enter a password anymore. To generate SSH an SSH key, check out https://onestopdataanalysis.com/github-ssh-setup/ .  
Then, go to the folder where you want to download the code in your terminal and type the command:  
`git clone LINK`  
**TASK**: Clone the repository of this tutorial in a folder on your computer.

Now, you should have a folder called *tech-tutorial* on your computer. 

### Getting an overview
**TASK**: Now, change directory (cd) into the folder and type  
`git status`  
You should now see  
```
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```
Git tells you that you are in the main branch (often called master instead of main). This is the most important branch, which shall only contain working and tested code.
So if you want to implement a new function, you should do that on another branch.  

### Branching
**TASK**: Create a new branch using the command  
`git branch your-branch-name`  
Check that your branch exists using  
`git branch`  
Now, switch to that branch using  
`git checkout your-branch-name`  
Now, check that everything worked using `git status`  

### Add your changes
**TASK**: Now, open the file *your-name.txt* and enter your name in the file.
Type `git status` again.  

Git now tells you that you have changed the file. These changes are only on your computer and nobody else can see it.
Now, we want to provide these changes to other members of your project.
We first need to tell git which changes shall be given to others. This can be done using
`git add file other_file folder`  

**TASK**: Add the changes in the *your-name.txt* file and check the success via `git status`.  

### Create a checkpoint (commit)
Now, we need to create a commit (checkpoint) that contains all these changes.

**TASK**: Create a commit on your branch using `git commit -m "Describe your changes in this message"`.  

When checking `git status` now, you should see that there is now nothing to commit again, because all changes are already in a commit.
The commit is still only on your computer, so nobody except you can see it. You should do commits every now and then, since these are basically checkpoints you can jump back to. So if anything is broken, you can just jump back to your last commit and start over again. If your last commit was 4 weeks ago, this won't be that helpful.   

### Push and pull commits
If you want to upload your commit to give it to your team colleagues, you can use the command
`git push`. This pushes all the new commits on the branch you are on. This won't work on this tutorial repository however, since I have disabled it :)  
  
If your friends have pushed new commits you can download them using the command `git pull`.  

### Combining branches
Now, imagine you have finished your important function and tested it, and now you want to add it to the main/master branch.
Therefore, make sure everything is committed. Then, go to the main branch using `git checkout main`. Now, your changes should not be visible anymore, because they are not yet in this branch. You can now merge all the changes using `git merge your-branch-name`. Git will automatically detect the changes and combine them in the best way. Sometimes, for example when there are changes in the same line of code in both branches, git does not know what to do. Then it will trigger a *Merge conflict*, which you need to resolve by hand. Therefore, open the conflicting file and fix the code. Git will show you both changes, so you can pick the right one or even both and combine them.  
  
**TASK**: Merge your changes (your name) into the main branch and make sure everything worked fine.

**IMPORTANT**: There is also a nice merging GUI on github and gitlab. Just open your projects github page and click on pull requests. Now, you can create a new *pull request* which shows your changes nicely. On gitlab, you can do the same by creating a new *merge request*. These two mean exactly the same. You can also assign team members to your merge requests, so they can review your code and merge it afterwards. 

## End
This completes the git tutorial. Make sure to always work on your own branch and then merge into the master branch, this makes collaboration way easier.
There are some more git commands, especially for reverting your changes and undoing things. Please use these commands very carefully, since you can easily destroy your work by typing the wrong command. If you are not sure what you are doing, please ask a more experienced TUM.ai member for help :)