# Contributing

This repo is a living tutorial: the instructors maintain the material between
trainings, and participants are welcome to send fixes for anything they hit
while following it.


## For participants

- Found a typo, a broken command, or a step that doesn't match the current
  setup of the systems? Open an issue, or fork the repo and open a pull
  request with the fix.
- Keep questions about the productions themselves for the
  [Distributed Computing category](https://fccsw-forum.web.cern.ch/c/distributed-computing/12)
  of the FCCSW forum, so others can see the answer too, or write to
  fcc-ped-softwareandcomputing-mcproduction@cern.ch, rather than opening
  GitHub issues.
- Small, focused PRs (one fix per PR) are easier to review than bundled ones.


## For instructors

- New material goes under the relevant system folder
  (`Setup|DRS|iLCDirac|Rucio|DaMI/`).
- `main` holds the canonical, up-to-date version of the tutorial. Cut a
  branch (or tag) per training/date before making training-specific tweaks
  (campaign names, pinned stack versions, schedule-specific trimming), and
  merge generally-useful fixes back to `main`.
- When a command or a production script changes, note the iLCDirac and
  Key4hep stack versions it was validated against in the relevant README.


## Style

- Material is plain Markdown; keep prose short and code blocks
  copy-pasteable.
- Prefer relative links between tutorial pages so branches/tags stay
  self-contained.
- Never put certificates, proxies or tokens into the repo, not even in
  examples.


## License

By contributing, you agree that your contribution is licensed under this
repository's [CC BY-SA 4.0 license](LICENSE).
