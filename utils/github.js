const getUserRepos = username => {
	const baseUrl = 'https://api.github.com';
	const endpoint = `/users/${username}/repos`;

	return fetch(baseUrl + endpoint)
		.then(response => response.json())
		.then(data => {
			const repos = data.map(repo => repo.name);
			return repos;
		});
};

getUserRepos('kah3vich').then(repos => {
	console.log('rm -rf github/*; cd github/;');
	repos.push(...['Blender', 'ThreeJS']); // private repos
	repos.forEach(repo => {
		console.log(`git clone https://github.com/kah3vich/${repo}.git;`);
	});
	console.log('git clone https://github.com/Holdesher/Holdesher.git;');
});
