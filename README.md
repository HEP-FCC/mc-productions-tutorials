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


## Format

Each section is introduced with brief slides, then the participants work
through the markdown material directly in this repo.


## Branches

Specific trainings/dates are tracked as branches or tags off `main`.


## License

Copyright (c) 2026 CERN. The documentation and material in this repository
is licensed under the
[Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)
license --- see [LICENSE](LICENSE).
