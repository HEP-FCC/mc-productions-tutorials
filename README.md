# MC Productions Tutorials

FCC tutorial for the MC Production contacts of the FCC PED Physics groups,
covering the chain from a **dataset request** through the **central
production** on the GRID to the **publication** of the produced datasets.


## Workflow

1. A physicist submits a dataset request in the **DRS** (Dataset Request
   System) and selects the Physics group, which notifies the group's MC
   Production contact(s)
2. The MC Production contact prepares the request and launches the production
   with **iLCDirac**
3. The produced files are managed by **Rucio** (not covered yet)
4. The datasets are published in **DaMI** (former FCC Physics Events website)

Read the [overall workflow and contact responsibilities](DRS/workflow-and-responsibilities.md),
then continue with the [DRS walkthrough and exercise](DRS/README.md).

## Structure

Each system has its own top-level directory, in the order of the workflow:

```
Setup/      GRID certificate, FCC VO registration, proxy
DRS/        Dataset Request System: registration, roles, managing requests
iLCDirac/   launching and monitoring productions
Rucio/      data management of the produced datasets (disabled for now)
DaMI/       publishing the datasets
```


## Questions

Ask in the
[Distributed Computing category](https://fccsw-forum.web.cern.ch/c/distributed-computing/12)
of the FCCSW forum, or write to
fcc-ped-softwareandcomputing-mcproduction@cern.ch.


## How to follow it

The tutorial is self-paced: read the pages in the order above and try out
each step. Before starting, complete the [Setup](Setup/README.md) and ask for
the roles you need (see [Access](#access)).

Everything you create while trying it out is labelled as a tutorial object
(`[TUTORIAL]` DRS requests, the `summer2026` test campaign in iLCDirac). Keep
their identifiers and ask for the cleanup when you are done, see
[Cleaning up after the tutorial](#cleaning-up-after-the-tutorial).


## Access

The roles are granted by the administrators of each system. Ask for them at
fcc-ped-softwareandcomputing-mcproduction@cern.ch:

- FCC VO membership and the `fcc_prod` group, for launching productions
- **coordinator** role in the [DRS](https://fcc-drs.web.cern.ch/)
- **editor** role in [DaMI](https://fcc-dami.web.cern.ch/)


## Cleaning up after the tutorial

Tutorial objects live in the production systems, next to real ones. When you
are done, write to fcc-ped-softwareandcomputing-mcproduction@cern.ch with:

- the URL of your `[TUTORIAL]` DRS request
- the transformation IDs and job IDs of your trial
- the EOS path of its output
- the UUID of any DaMI record you created

Do not delete transformations or files yourself.


## Past trainings

The state of the material used at a training is kept as a tag, e.g.
`training-2026-10-21`.


## License

Copyright (c) 2026 CERN. The documentation and material in this repository
is licensed under the
[Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)
license --- see [LICENSE](LICENSE).
