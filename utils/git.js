for (let i = 10; i <= 13; i++) {
	console.log(
		`sed -i '1s/^/${i}\\n/' ./readme.md; git add .; git commit --amend --date='Wed Jul ${i} 14:00 2023 +0100' --no-edit; git push -f;`,
	);
}
