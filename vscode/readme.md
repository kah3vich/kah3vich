<div align="center">
  <img
    width="40%" src="https://raw.githubusercontent.com/kah3vich/kah3vich/main/assets/icon/vscode.svg"
  />
  <br />
  <h1>VSCode</h1>
</div>

<h3 align="center">Settings</h3>

1. [Keybindings](./config/keybindings.json)
2. [Settigns](./config/settings.json)
3. [Tasks](./config/tasks.json)

<h3 align="center">Plugins</h3>

#### List plugins: [Here](./extensions.txt)

#### Get all your plugins from `VSCode`.

> 💡 — Mac OS / Linux

```bash
code --list-extensions | while read line; do echo "code --install-extension $line"; done
```

> 💡 — Windows

```bash
code --list-extensions | % { "code --install-extension $_" }
```
