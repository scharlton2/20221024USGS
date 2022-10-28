import os
from git import Git, Repo

home_dir = os.path.expanduser('~')
repo_dir  = os.path.join(home_dir, "myproject")
local_clone_dir = os.path.join(home_dir, "myclone")
remote_clone_dir = os.path.join(home_dir, "myremoteclone")
print(f"repo_dir: {repo_dir}")
print(f"local_clone_dir: {local_clone_dir}")
print(f"remote_clone_dir: {remote_clone_dir}")

repo = Repo(repo_dir)
repo.clone(local_clone_dir)
Repo.clone_from("https://github.com/jstrickler/myproject.git", remote_clone_dir)
