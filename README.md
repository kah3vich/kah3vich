# Config VSCode - Kah3vich

// mac-os | linux

```bash
cd ~/Library/Application\ Support/Code/User;

rm -rf backup-config/; mkdir backup-config; mv settings.json keybindings.json snippets/ backup-config/;

rm -rf kah3vich/; git clone -b config https://github.com/kah3vich/kah3vich.git; cd kah3vich/.vscode; mv settings.json keybindings.json snippets/ ../../; cd ../../; rm -rf kah3vich/
```

// back paht - /Code/User

```bash 
cd ~/Library/Application\ Support/Code/User; rm -rf settings.json keybindings.json snippets/; cd backup-config/; mv settings.json keybindings.json snippets/ ../; cd ../; rm -rf backup-config/
```


// win 

```bash
cd ~/AppData/Roaming/Code/User; 

rm -rf backup-config/; mkdir backup-config; mv settings.json keybindings.json snippets/ backup-config/;

rm -rf kah3vich/; git clone -b config https://github.com/kah3vich/kah3vich.git; cd kah3vich/.vscode; mv settings.json keybindings.json snippets/ ../../; cd ../../; rm -rf kah3vich/
```


// back paht - /Code/User

```bash 
cd ~/AppData/Roaming/Code/User; rm -rf settings.json keybindings.json snippets/; cd backup-config/; mv settings.json keybindings.json snippets/ ../; cd ../; rm -rf backup-config/
```

// ready snippets 

```bash
rm -rf .vscode/snippets/*.*; cd snippetsCatalog/; cp html/*.* ../.vscode/snippets/; cp javascript/*.* ../.vscode/snippets/; cp jquery/*.* ../.vscode/snippets/; cp pug/*.* ../.vscode/snippets/; cp react/*.* ../.vscode/snippets/; cp scss/*.* ../.vscode/snippets/; cp style/*.* ../.vscode/snippets/; cp typescript/*.* ../.vscode/snippets/; cd ../; echo 'Done ✅'
```
