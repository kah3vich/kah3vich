[Back](../)

<div align="center">
  <br />
  <h1 align="center">ZSH</h1>
</div>

### Settings:

1. Установите образ zsh на устройство - [ZSH](https://ohmyz.sh/)

- Конфиг файл zsh - `~/.zshrc`

2. Тема для образа - [PowerLevel10K](https://github.com/romkatv/powerlevel10k?tab=readme-ov-file#installation)

- Пример конфиг файла с темой `~/.zshrc`:

  ```
  if [[-r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
  fi

  export ZSH="$HOME/.oh-my-zsh"

  ZSH_THEME="powerlevel10k/powerlevel10k"

  plugins=(git)

  source $ZSH/oh-my-zsh.sh

  [[! -f ~/.p10k.zsh]] || source ~/.p10k.zsh
  ```

- Для вызова найстроки темы, можно использовать команду: `p10k configure`

- Конфиг файл темы для `PowerLevel10K` - `~/.p10k.zsh`

3. Шрифт - Meslo LG S DZ

- MacOS ошибка шрифта - [Here](https://stackoverflow.com/questions/64973308/why-does-oh-my-zsh-terminal-macos-missing-symbols)

4. Иконки - [Icons](https://github.com/sebastiencs/icons-in-terminal/tree/master)

5. Плагины:

- Автоподсказки ввода команд - [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)

  Установка:

  ```
  git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
  ```

- Подсветка команд - [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)

  ```
  git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
  ```

> 💡 — Для запуска плагинов в `zsh`, нужно прописать их в конфиг файле `~/.zshrc`: `plugins=(git zsh-autosuggestions zsh-syntax-highlighting)`

6. Дополнение: 

- Перезапуск системы `zsh` в терминале: `source ~/.zshrc` или `exec zsh`

- Пакет начального экрана - [PokemonSay](https://github.com/possatti/pokemonsay/tree/master)
  - [Pokemons List](https://www.pokemon.com/ru/pokedex/charizard)
  - [Translate](https://vse-zadarma.ru/translit.php)

<div align="center">
  <br />
  <h3>🌏 Links 🌏</h3>
</div>

0. [Config File](./config.sh)
1. [Список плагинов](https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins)
2. [Статья про установку](https://www.sitepoint.com/zsh-tips-tricks/)
3. [5 плагинов](https://catalins.tech/zsh-plugins/)
4. [ZSH + PowerLevel10K](https://habr.com/ru/articles/739376/)
5. [Advanced Settings](https://medium.com/swlh/the-ultimate-terminal-emulator-with-oh-my-zsh-experience-f81f838c6daf)
