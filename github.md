## Git command Cheat Sheet

### Setting .gitignore after file in repository
To get certain file or directory out of repository, use command below.
'''
git rm --cached (-r) FILE/(DIRECTORY)
'''

Then, commit new file or directory, with the new .gitignore applied.
'''
git add .
git commit -m "COMMENT"
'''
