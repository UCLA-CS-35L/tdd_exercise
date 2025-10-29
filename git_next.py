#! python3
import git
import os
import sys

def move_branch_forward_one_commit(branch_name: str = 'main'):
    """
    Moves the currently checked-out branch one commit forward (to a newer commit)
    in the history of the specified branch (default: 'main').
    Performs a hard reset to the next commit.
    """
    try:
        # Initialize the repository object (assumes running in the repo root or subdirectory)
        repo = git.Repo(os.getcwd(), search_parent_directories=True)
    except git.InvalidGitRepositoryError:
        print("Error: Not a valid Git repository.")
        sys.exit(1)

    # Ensure the repository is not dirty before performing a hard reset
    if repo.is_dirty(untracked_files=True):
        print("Warning: Repository is dirty. Please commit or stash your changes before proceeding.")
        #sys.exit(1)


    current_commit = repo.head.commit

    # 2. Find all commits on the target branch, ordered newest to oldest
    # This list will be: [Newest_Commit, Commit_2, Commit_3, ..., Oldest_Commit]
    all_commits_on_branch = list(repo.iter_commits(branch_name))

    # 3. Find the index of the current commit in the history
    try:
        current_index = all_commits_on_branch.index(current_commit)
    except ValueError:
        print(f"Error: Current HEAD is detached or the commit is not reachable on the '{branch_name}' branch.")
        sys.exit(1)

    # 4. Check if we are at the newest commit (index 0)
    if current_index == 0:
        print(f"Success: Branch '{branch_name}' is already at the newest commit ({current_commit.hexsha[:7]}). Cannot move forward.")
        return

    # 5. The commit immediately "forward" (newer) in history is at the preceding index
    next_commit = all_commits_on_branch[current_index - 1]

    # 6. Perform the hard reset
    print(f"--- Current Commit: {current_commit.hexsha[:7]} ---")
    print(f"Attempting to move '{branch_name}' forward to: {next_commit.hexsha[:7]}")

    # Reset the branch HEAD to the target commit (equivalent to 'git reset --hard <next_commit_hash>')
    repo.head.reset(next_commit, index=True, working_tree=True)

    print(f"\nSuccessfully moved '{branch_name}' one commit forward!")
    print(f"New HEAD is: {repo.head.commit.hexsha[:7]} - {repo.head.commit.summary}")
    
    # Optional: Display the file changes caused by the reset
    print("\nFiles in the working tree have been updated to reflect the new state.")


if __name__ == '__main__':
    # You might need to install gitpython: pip install gitpython
    
    # Example usage for a 'main' branch:
    move_branch_forward_one_commit('main')

    # If your main branch is called 'master', use:
    # move_branch_forward_one_commit('master')