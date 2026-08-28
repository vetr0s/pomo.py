# pomo.py

A minimal command-line Pomodoro timer written in Python.

## Usage

```sh
pomo
```

Defaults to a 25-minute work session and 5-minute break.

```sh
pomo 50
pomo 50 --break 10
```

Press `Ctrl-C` at any time to quit.

I usually want to have the timer visible while I work.
To solve this I usually increase the text and crop a
floating terminal window that is on the top layer of the
windows. For example:

![Screenshot of pomo running on my desktop](./imgs/pomo.py.png)

## Install

Requires Python 3.

```sh
chmod +x pomo.py
mkdir -p ~/.local/bin
ln -s $(pwd)/pomo.py ~/.local/bin/pomo
```

Make sure `~/.local/bin` is in your `PATH`.
