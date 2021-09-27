# Git workflows

A git workflow is a recipe or recommendation for how to use Git to accomplish work in a consistent and productive manner.

Some things to consider when evaluating a Git workflow:

- Does this workflow scale with team size?
- Is it easy to undo mistakes and errors with this workflow?
- Does this workflow impose any new unnecessary cognitive overhead to the team?

## Centralized Workflow

Remote server-side hosted repository that developers push and pull form. Compared to other workflows, the Centralized Workflow has no defined PR or forking patterns.

### How it works

Devs clone de repo and, commit locally and push to the remote repo. In this process may occur conflicts that need to be resolved.

The recommended to do is the developer before push the changes that he have been made, to make a `git pull` to update the remote repo locally and fix the conflicts.

You may use `git pull --rebase main origin` to rebase. Rebasing works by transferring each local commit to the updated main branch one at a time. This means that you catch merge conflicts on a commit-by-commit basis rather than resolving all of them in one massive merge commit.

Rebase commands:

- `git rebase --continue`
- `git rebase --abort`


## Feature Branching

The core idea behind is that all feature development should take place in a dedicated branch instead of the main branch. This encapsulation makes it easy for multiple developers to work on a particular feature without disturbing the mains codebase. **The main allways clean**


## Gitflow Workflow

Assigns very specific roles to different branches and defines how and when they should interact.


## Forking Workflow

Instead of using a single server-side repository to act as the 'central' codebase, it gives every developer a server-side repository. This means that each contributor has not one, but two Git repos: a private local one and a public server-side one.

