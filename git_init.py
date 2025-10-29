#! python3
import git
import os
import sys

COMMIT_HASH = '324eb30cb78162376cdba3781f1b7a73e5685118'

try:
    try:
        # Initialize the repository object (assumes running in the repo root or subdirectory)
        repo = git.Repo(os.getcwd(), search_parent_directories=True)
    except git.InvalidGitRepositoryError:
        print("Error: Not a valid Git repository.")
        sys.exit(1)

    # Ensure the repository is not dirty (optional but recommended)
    if repo.is_dirty():
        print("Warning: Repository has uncommitted changes. Stash or commit them first.")
    
    # Get the reference for the commit
    # GitPython will find the commit object whether it's a full hash, short hash, or a tag/branch name
    commit_ref = repo.commit(COMMIT_HASH)

    # Checkout the commit
    # This detaches HEAD, meaning you are no longer on a branch.
    repo.git.checkout(commit_ref)

    print(f"Successfully checked out commit: {COMMIT_HASH}")
    print(f"Current HEAD: {repo.head.commit.hexsha}")

except Exception as e:
    print(f"An error occurred: {e}")