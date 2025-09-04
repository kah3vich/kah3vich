# Contributing

## Request for changes/ Pull Requests

You first need to create a fork of the [repository](https://github.com/kah3vich/kah3vich) repository to commit your changes to it. Methods to fork a repository can be found in the [GitHub Documentation](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

Then add your fork as a local project:

- Using HTTPS

```bash
git clone https://github.com/kah3vich/kah3vich.git
```

- Using SSH

```bash
git clone git@github.com:kah3vich/kah3vich.git
```

> [Which remote URL should be used ?](https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories)

Then, go to your local folder:

```bash
cd kah3vich
```

Add git remote controls:

- Using HTTPS

```bash
git remote add fork https://github.com/YOUR-USERNAME/kah3vich.git
git remote add upstream https://github.com/kah3vich/kah3vich.git
```

- Using SSH

```bash
git remote add fork git@github.com:YOUR-USERNAME/kah3vich.git
git remote add upstream git@github.com/kah3vich/kah3vich.git
```

You can now verify that you have your two git remotes:

```bash
git remote -v
```

## Receive remote updates

In view of staying up to date with the central repository:

```bash
git pull upstream master
```

## Choose a base branch

Before starting development, you need to know which branch to base your modifications/additions on. When in doubt, use master:

| Type of change    |     |              Branches |
| :---------------- | :-: | --------------------: |
| Documentation     |     |              `master` |
| Bug fixes         |     |              `master` |
| New features      |     |              `master` |
| New issues models |     | `YOUR-USERNAME:patch` |

```bash
# Switch to the desired branch
git switch master

# Pull down any upstream changes
git pull

# Create a new branch to work on
git switch --create patch/1234-name-issue
```

Commit your changes, then push the branch to your fork with `git push -u fork` and open a pull request on [repository](https://github.com/kah3vich/kah3vich) following the template provided.
