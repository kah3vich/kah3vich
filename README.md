# Config VSCode - Kah3vich

// mac os

```bash
cd ~/Library/Application\ Support/Code/User;

mkdir backup-config; mv settings.json keybindings.json snippets/ backup-config/;

git clone -b config https://github.com/kah3vich/kah3vich.git; cd kah3vich/.vscode; mv settings.json keybindings.json snippets/ ../../; cd ../../; rm -rf kah3vich/
```


// win 

```bash
cd ~/AppData/Roaming/Code/User; 

mkdir backup-config; mv settings.json keybindings.json snippets/ backup-config/;

git clone -b config https://github.com/kah3vich/kah3vich.git; cd kah3vich/.vscode; mv settings.json keybindings.json snippets/ ../../; cd ../../; rm -rf kah3vich/
```


// back paht - /Code/User

```bash 
rm -rf settings.json keybindings.json snippets/; cd backup-config/; mv settings.json keybindings.json snippets/ ../; cd ../; rm -rf backup-config/
```



snippets - task
1. pug loop
2. scss include 