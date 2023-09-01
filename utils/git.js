for (let i = 1; i <= 1; i++) {
	console.log(
		`sed -i '1s/^/${i}\\n/' ./readme.md; git add .; git commit --amend --date='Wed Sep ${i} 14:00 2023 +0100' --no-edit; git push -f;`,
	);
}
