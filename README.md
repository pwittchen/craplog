# craplog
verifies whether your git log is a crap or not (beta version)

Motivation
----------

I've read one discussion under [one of the pull requests to Linux kernel](https://github.com/torvalds/linux/pull/17). It made me think about quality of Git commit messages. Of course, Linux kernel is a specific project and has its own standards. Maybe not all of these standards will be valid for a simpler projects. Nevertheless, a lot of people don't pay attention to git commit messages. They put crappy stuff inside like random letters and numbers or stupid expressions, which has no specific meaning or aren't related to the project or aren't informative enough. In my opinion, good git log is one of the factors determining good quality of the project. Sometimes, we need to browse log find some changes or analyze project history. It's easier, when git log is good. I've made some of the mentioned mistakes in the past, but I try to avoid them now.

Overview
--------

This project checks if git git log of the given project is crappy.
Right now, script is very simple. It just checks if more than half of the commit messages are good.
Commit message is considered as good, when it contains more than two words. Of course, this is not the only condition determining the quality of the commit message, but this is early version of the script and can be improved later.

Usage
-----

```
./craplog.py <path_to_your_repository>
```
