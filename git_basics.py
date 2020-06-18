# Jewel Newman
# Important github commands and workflow

'''
--Non git commands--

pwd = displays present working directory path on local machine
cd = change directory, cannot use backslash unless using " "
    ex to change to C:\Users\jewel\SLAC do cd "C:\Users\jewel\SLAC" or
    cd /c/Users/jewel/SLAC
ls = lists files content in directory
mv = moving a file or renaming file
    ex mv pathtofile.ext differentpathtofile.ext
    or mv oldfilename.ext newfilename.ext
mkdir = make new folder
    ex mkdir newfoldername
touch = makes new files
    ex touch filename.ext
ctrl-l = clears screen

--Git commands--

git status = list all changed files 

git init = create new local repo in current directory or git init project name
git clone = copies repo
    ex git clone githuburl (copying repo from github)
    or git clone pathtorepo (local repo)
    
git add = to add files to staging
    ex git add filename.ext or git add . (select all files in current directory
    or git add -A (select all files)
git rm = removes file from repository
    ex git rm --cached (removes file from repo but keeps it in local machine)
git commit -m" " = saves staged changes to git directory

git push = sends changes to remote repo
    ex git push remotename branchname (pushes branch to remote repo)
git pull = fetches and merges changes on remote repo to local repo

git branch = lists all the branches in repo
    ex git branch -a (lists all branches in local and remote repo)
    or git branch -d branchname (deletes branch)
git checkout = switches to other branches
    ex git checkout -b branchname (creates new branch and switches to it)
git merge = merges branch into active branch

--Git workflow--
1. pull lastest changes from repo
2. create a new branch for problem
3. on new branch edit, stage, commit changes, push to remote
4. pull request

'''





