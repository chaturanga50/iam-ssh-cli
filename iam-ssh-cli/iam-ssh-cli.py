#!/usr/bin/env python
# Copyright 2023 Chathuranga Abeyrathna. All Rights Reserved.
# iam-ssh-cli to sync IAM ssh keys to Linux boxes

import sys
import argparse
from functions.ssh_users import ssh_users
from functions.ssh_sudo_users import ssh_sudo_users


class ArgParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


def IamSshCLI():
    parser = ArgParser() 
    subparser = parser.add_subparsers(dest='subcommand')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s {{VERSION_PLACEHOLDER}}')
    parser.add_argument('-u', '--users-group', dest='users', required=True, help='IAM users group to fetch users to server [required]')
    parser.add_argument('-s', '--sudo-users-group', dest='sudo_users', required=True, help='IAM sudo group to fetch users to add to sudo [required]')
    args = parser.parse_args()
    ssh_users(group=args.users)
    ssh_sudo_users(group=args.sudo_users)

if __name__ == '__main__':
    IamSshCLI()
