for (let i = 1; i <= 12; i++) {
	console.log(
		`sed -i '1s/^/${i}\\n/' ./readme.md; git add .; git commit --amend --date='Wed Aug ${i} 14:00 2023 +0100' --no-edit; git push -f;`,
	);
}
