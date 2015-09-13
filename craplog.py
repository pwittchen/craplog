#!/usr/bin/python -u

# This script checks, if git log of the repository is a crap or not
# Usage: ./craplog.py <path_to_your_git_repository>

import os, sys
from subprocess import Popen, PIPE
from time import sleep

def git_log():
    GIT_COMMIT_FIELDS = ['id', 'author_name', 'author_email', 'date', 'message']
    GIT_LOG_FORMAT = ['%H', '%an', '%ae', '%ad', '%s']
    GIT_LOG_FORMAT = '%x1f'.join(GIT_LOG_FORMAT) + '%x1e'

    p = Popen('git log --format="%s"' % GIT_LOG_FORMAT, shell=True, stdout=PIPE)
    (log, _) = p.communicate()
    log = log.strip('\n\x1e').split("\x1e")
    log = [row.strip().split("\x1f") for row in log]
    log = [dict(zip(GIT_COMMIT_FIELDS, row)) for row in log]
    return log

def git_checkout(branch_name):
    Popen('git checkout "%s"' % branch_name, shell=True, stdout=PIPE)

def is_git_log_crap():
    if len(sys.argv) == 1:
        print 'ERROR: path to repository is not defined as a parameter'
        print 'USAGE: ./craplog.py <path_to_your_repository>'
        return

    # go to directory with repository and checkout to master branch
    path_to_repository = sys.argv[1]
    os.chdir(path_to_repository)
    git_checkout('master')

    log = git_log()
    number_of_commits = len(log)
    number_of_crappy_commits = 0

    for commit in log:
        if is_commit_message_crap(commit['message']):
            number_of_crappy_commits += 1

    crappiness_factor = float(number_of_crappy_commits)/float(number_of_commits) * 100
    print 'Number of crappy commits %s/%s (%s %%)' % (number_of_crappy_commits, number_of_commits, crappiness_factor)
    if crappiness_factor >= 50:
        print 'More than a half of commit messages seems to have poor quality. :-('
        print 'Git log is crappy. Please, pay more attention to your commits.'
    else:
        print 'More than half of commit messages seems to have good quality'
        print 'Git log is fine. Keep it up. :-)'

    return

def is_commit_message_crap(message):
    words = message.split()
    number_of_words = len(words)
    number_of_short_words = 0
    has_too_little_words = number_of_words < 3

    for word in words:
        if len(word) < 3:
            number_of_short_words += 1

    short_words_percentage = float(number_of_short_words)/float(number_of_words) * 100
    has_to_many_short_words = short_words_percentage >= 50

    return has_too_little_words or has_to_many_short_words

is_git_log_crap()
