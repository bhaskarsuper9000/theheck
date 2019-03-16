# Report issues
If you have any issue with The Heck, sorry about that, but we will do what we
can to fix that. Actually, maybe we already have, so first thing to do is to
update The Heck and see if the bug is still there.

If it is (sorry again), check if the problem has not already been reported and
if not, just open an issue on [GitHub](https://github.com/nvbn/theheck) with
the following basic information:
  - the output of `theheck --version` (something like `The Heck 3.1 using
    Python 3.5.0`);
  - your shell and its version (`bash`, `zsh`, *Windows PowerShell*, etc.);
  - your system (Debian 7, ArchLinux, Windows, etc.);
  - how to reproduce the bug;
  - the output of The Heck with `THEHECK_DEBUG=true` exported (typically execute
    `export THEHECK_DEBUG=true` in your shell before The Heck);
  - if the bug only appears with a specific application, the output of that
    application and its version;
  - anything else you think is relevant.

It's only with enough information that we can do something to fix the problem.

# Make a pull request
We gladly accept pull request on the [official
repository](https://github.com/nvbn/theheck) for new rules, new features, bug
fixes, etc.

# Developing

Install `The Heck` for development:

```bash
pip install -r requirements.txt
python setup.py develop
```

Run code style checks:

```bash
flake8
```

Run unit tests:

```bash
py.test
```

Run unit and functional tests (requires docker):

```bash
py.test --enable-functional
```

For sending package to pypi:

```bash
sudo apt-get install pandoc
./release.py
```
