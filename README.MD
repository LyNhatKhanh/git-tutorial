Command Git: 
- git init
- git status
- git add 
- git commit

Check Git: 
- git log
- git show <id commit>
- git diff

Work place: 
- Working directory
- Staging area
- Repository

Step back: 
- git checkout/restore <file>
- git reset HEAD <file>

Git checkout: 
- git checkout -b <branch>: Create a new branch => access this branch
- git checkout <branch>: Access this branch

Git merge: A <= B
- git checkout A: Access branch A
- git merge B: Merge this branch to A 

Git branch:
- git branch: List branches
- git branch -D <branch>: delete this branch

Git reset:
- git reset --soft <branch>: Back to ADD process (staging area)
- git reset --mixed <branch>: Back to before ADD process (working area)
- git reset --hard <branch>: Delete all branches after this branch