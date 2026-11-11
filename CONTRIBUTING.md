# Contributing

This repo is a living, self-paced tutorial: the maintainers keep the material
current, and readers are welcome to send fixes for anything they hit while
following it.


## For readers

- Found a typo, a broken command, or a step that doesn't match the current
  setup of the systems? Open an issue, or fork the repo and open a pull
  request with the fix.
- Keep questions about the productions themselves for the
  [Distributed Computing category](https://fccsw-forum.web.cern.ch/c/distributed-computing/12)
  of the FCCSW forum, so others can see the answer too, or write to
  fcc-ped-softwareandcomputing-mcproduction@cern.ch, rather than opening
  GitHub issues.
- Small, focused PRs (one fix per PR) are easier to review than bundled ones.


## For maintainers

- New material goes under the relevant system folder
  (`Setup|DRS|iLCDirac|Rucio|DaMI/`).
- `main` holds the canonical, up-to-date, self-paced version of the
  tutorial. Keep it free of references to a specific session (dates, rooms,
  speakers, "the instructors"). Tag the state used at a training, e.g.
  `training-2026-10-21`, and put any session-specific tweaks on a branch
  off that tag.
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
