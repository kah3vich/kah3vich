for (let i = 22; i <= 22; i++) {
	console.log(
		`sed -i '1s/^/${i}\\n/' ./readme.md; git add .; git commit --amend --date='Wed Jul ${i} 14:00 2023 +0100' --no-edit; git push -f;`,
	);
}
