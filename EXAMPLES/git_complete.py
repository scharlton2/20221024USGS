import os
import shutil
from git import Git, Repo
home_dir = os.path.expanduser('~')

repo_dir = os.path.join(home_dir, 'myproject')

r = Repo.init(repo_dir)  # Create new empty repo

file_to_add = 'creating_classes.py'
shutil.copy(file_to_add, repo_dir)  # Copy file to add (typically created with IDE, so no need to copy)

os.chdir(repo_dir)

repo = Git(r)

repo.add(file_to_add)  # Stage file for commit
repo.commit(file_to_add, message="initial commit")  # Commit file
print(repo.log())  # Show repo log
