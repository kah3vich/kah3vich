#!/bin/bash

if [ -z "$1" ]; then
	echo "Error: need argument username"
	exit 1
fi

local username=$1
local github_token=$2
local reposition_dir="repos"
local count_clone=0

mkdir -p "$reposition_dir"
cd "$reposition_dir"
rm -rf * 2>/dev/null || true

if [ ! -z "$github_token" ]; then
	api_url="https://api.github.com/user/repos?per_page=100"
	auth_token="Authorization: token $github_token"
	echo "All reposition user (public/private): $username"
else
	api_url="https://api.github.com/users/${username}/repos?per_page=100"
	echo "All reposition user (public): $username"
fi

if [ ! -z "$github_token" ]; then
  response_json=$(curl -s -H "$auth_token" "$api_url")
else
  response_json=$(curl -s "$api_url")
fi

if echo "$response_json" | grep -q "message"; then
	if echo "$response_json" | grep -q "Bad credentials"; then
		echo "Error: invalid token"
		exit 1
	elif echo "$response_json" | grep -q "Not Found"; then
		echo "Error: user not found"
		exit 1
	fi
fi

echo "$response_json" | jq -r '.[] | "\(.name)|\(.ssh_url)"' 2>/dev/null | while IFS='|' read -r name ssh_url; do
	if [ ! -z "$name" ] && [ ! -z "$ssh_url" ]; then
		echo "Info: clone reposition $name"
		git clone "$ssh_url" && ((count_clone++))
	fi
done
