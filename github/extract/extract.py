#!/usr/bin/env python

import sys
import pygit2 as g
import datetime


_SORT = g.GIT_SORT_TOPOLOGICAL

def main(reporoot):
    # Make the repo
    repo = g.Repository(reporoot + "/.git")

    # Iterate through every commit in every reference (branch or tag)
    # and print out a CSV row of its data
    for refname in repo.listall_references():
        ref = repo.lookup_reference(refname)
        for commit in repo.walk(ref.oid, _SORT):

            # Calculate the diff
            if commit.parents:
                diff = commit.tree.diff(commit.parents[0].tree)
                for changehunk in diff.changes['hunks']:
                    
                    # TODO: make this more readable than just the raw dump
                    changedata = changehunk.data

                    format = "%s,%s,%s,%s"
                    data = (
                        refname,
                        datetime
                            .datetime
                            .fromtimestamp(commit.commit_time),
                        commit.message.strip(),
                        changedata
                    )

            print format % data;

if __name__ == "__main__":
    main(sys.argv[1])
