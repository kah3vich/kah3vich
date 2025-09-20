#!/bin/bash

if [ -z "$1" ]; then
	echo "Error: need argument username"
	exit 1
fi

local USERNAME=$1
local GITHUB_TOKEN=$2
local REPOSITION_DIR="repos"
local COUNT_CLONE=0

mkdir -p "$REPOS_DIR"
cd "$REPOS_DIR"
rm -rf * 2>/dev/null || true

if [ ! -z "$GITHUB_TOKEN" ]; then
	API_URL="https://api.github.com/user/repos?per_page=100"
	AUTH_HEADER="-H 'Authorization: token $GITHUB_TOKEN'"
	echo "All reposition user (public/private): $USERNAME"
else
	API_URL="https://api.github.com/users/${USERNAME}/repos?per_page=100"
	AUTH_HEADER=""
	echo "All reposition user (public): $USERNAME"
fi

if [ ! -z "$GITHUB_TOKEN" ]; then
    REPOS_JSON=$(curl -s -H "Authorization: token $GITHUB_TOKEN" "$API_URL")
else
    REPOS_JSON=$(curl -s "$API_URL")
fi

if echo "$REPOS_JSON" | grep -q "message"; then
	if echo "$REPOS_JSON" | grep -q "Bad credentials"; then
		echo "Error: invalid token"
		exit 1
	elif echo "$REPOS_JSON" | grep -q "Not Found"; then
		echo "Error: user not found"
		exit 1
	fi
fi


echo "$REPOS_JSON" | jq -r '.[] | "\(.name)|\(.ssh_url)"' 2>/dev/null | while IFS='|' read -r name ssh_url; do
	if [ ! -z "$name" ] && [ ! -z "$ssh_url" ]; then
		echo "Info: clone reposition $name"
		git clone "$ssh_url" && ((COUNT_CLONE++))
	fi
done
