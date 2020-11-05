#!/usr/bin/env bash

echo "Username: $1"
echo "Password: ******"

curl --connect-timeout 15 -v --insecure "smtp://smtp.mailbox.org:465" -u "$1:$2" \
    --mail-from "sender@sorc3r3r.io" --mail-rcpt "receiver@sorc3r3r.io" \
    -T email-contents.txt --ssl