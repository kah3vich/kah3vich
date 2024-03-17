<div align="center">
    <br />
    <h1>Config</h1>
    <p>
        Configuration files and parameters for simplifying and adaptive work in the code editor. Also for various systems associated with the terminal and aliases, which shorten and simplify work with systems.
    </p>
</div>

<h3 align="center">Set config</h3>

### Mac OS / Linux:

> 💡 — place it in the settings folder.

```bash
cd ~/.../Code/User
```

> 💡 — saving old settings to `backup-config`.

```bash
rm -rf backup-config/; mkdir backup-config; mv settings.json keybindings.json snippets/ backup-config/
```

> 💡 — installing a repository with settings and rolling them out (deleting the old repository `kah3vich/`)

```bash
rm -rf kah3vich/; git clone -b config https://github.com/kah3vich/kah3vich.git; cd kah3vich/.vscode; mv settings.json keybindings.json snippets/ ../../; cd ../../; rm -rf kah3vich/
```

> 💡 — restoring old settings from `backup-config`.

```bash
cd ~/.../Code/User; rm -rf settings.json keybindings.json snippets/; cd backup-config/; mv settings.json keybindings.json snippets/ ../; cd ../; rm -rf backup-config/
```

### Windows:

> 💡 — place it in the settings folder.

```bash
cd ~/.../Code/User
```

> 💡 — saving old settings to `backup-config`.

```bash
rm -rf backup-config/; mkdir backup-config; mv settings.json keybindings.json snippets/ backup-config/
```

> 💡 — installing a repository with settings and rolling them out (deleting the old repository `kah3vich/`)

```bash
rm -rf kah3vich/; git clone -b config https://github.com/kah3vich/kah3vich.git; cd kah3vich/.vscode; mv settings.json keybindings.json snippets/ ../../; cd ../../; rm -rf kah3vich/
```

> 💡 — restoring old settings from `backup-config`.

```bash
cd ~/.../Code/User; rm -rf settings.json keybindings.json snippets/; cd backup-config/; mv settings.json keybindings.json snippets/ ../; cd ../; rm -rf backup-config/
```

<h3 align="center">Alias</h3>
