#!/bin/bash

if date --version >/dev/null 2>&1; then
	DATE_CMD="gnu"
else
	DATE_CMD="bsd"
fi

to_iso() {
	IFS=- read -r d m y <<< "$1"
	echo "$y-$m-$d"
}

validate_date_format() {
	local date="$1"
	[[ $date =~ ^[0-9]{2}-[0-9]{2}-[0-9]{4}$ ]] && return 0
	echo "Error: invalid format use dd-mm-yyyy" >&2
	return 1
}

generate_date_range() {
	local start_date="$1" end_date="$2"

	[[ $# -ne 2 ]] && { echo "Error: need 2 args date" >&2; return 1; }
	validate_date_format "$start_date" || return 1
	validate_date_format "$end_date"   || return 1

	local start_iso=$(to_iso "$start_date")
	local end_iso=$(to_iso "$end_date")
	local start_sec end_sec step=86400
	local print_date

	[[ "$start_iso" > "$end_iso" ]] && {
		echo "Error: start date <= end date" >&2
		return 1
	}

	if [[ $DATE_CMD == "gnu" ]]; then
		start_sec=$(date -d "$start_iso" +%s)
		end_sec=$(date -d "$end_iso" +%s)
		print_date() { date -d "@$1" "+%Y-%m-%d"; }
	else
		start_sec=$(date -j -f "%Y-%m-%d" "$start_iso" +%s)
		end_sec=$(date -j -f "%Y-%m-%d" "$end_iso" +%s)
		print_date() { date -j -f "%s" "$1" "+%Y-%m-%d"; }
	fi

	for ((sec = start_sec; sec <= end_sec; sec += step)); do
		print_date "$sec"
	done
}

validate_file_keep() {
	if [ -f ".gitkeep" ]; then
		rm ".gitkeep"
	else
		touch ".gitkeep"
	fi
}

validate_git_commit() {
	git add -A
	GIT_AUTHOR_DATE="$1 14:00" GIT_COMMITTER_DATE="$1 14:00" git commit -m "chrome: keep"
}

process_date_range() {
	local dates=$(generate_date_range "$1" "$2") || return 1

	while IFS= read -r date; do
    validate_file_keep
    validate_git_commit "$date"
    echo "Info: commit date $date"
	done <<< "$dates"

	git push -f
}

process_date_range "$1" "$2"
