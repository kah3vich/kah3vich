for (let i = 3; i <= 11; i++) {
	console.log(
		`sed -i '1s/^/${i}\\n/' ./readme.md; git add .; git commit --amend --date='Wed Feb ${i} 14:00 2023 +0100' --no-edit; git push -f;`,
	);
}
