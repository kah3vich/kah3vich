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