# Version references

The command and parameter descriptions in this guide follow the CERN-hosted iLCDirac `Rel-v35r0` source at commit `ef8854aea4a037463e4323044840227f7e447d74`, inspected on 20 October 2026. The release notes identify version 35.0.12. Use the client version supplied for the session and retain it with your production record.

| Reference | What it supports |
| --- | --- |
| [FCC production command](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/-/blob/ef8854aea4a037463e4323044840227f7e447d74/src/ILCDIRAC/ILCTransformationSystem/scripts/dirac_fcc_make_productions.py) | CLI flags, production parameters, application selection and list handling. |
| [ProductionJob](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/-/blob/ef8854aea4a037463e4323044840227f7e447d74/src/ILCDIRAC/Interfaces/API/NewInterface/ProductionJob.py) | Production permissions, dry-run ID, transformation creation, activation and task limit. |
| [Delphes application](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/-/blob/ef8854aea4a037463e4323044840227f7e447d74/src/ILCDIRAC/Interfaces/API/NewInterface/Applications/DelphesApp.py) | Accepted executable, local cards, event count and energy consistency. |
| [Production proxy check](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/-/blob/ef8854aea4a037463e4323044840227f7e447d74/src/ILCDIRAC/Core/Utilities/CheckAndGetProdProxy.py) | Proxy-group checking. |
| [Production summary](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/-/blob/ef8854aea4a037463e4323044840227f7e447d74/src/ILCDIRAC/ILCTransformationSystem/scripts/dirac_ilc_production_summary.py) and [production log retrieval](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/-/blob/ef8854aea4a037463e4323044840227f7e447d74/src/ILCDIRAC/ILCTransformationSystem/scripts/dirac_ilc_get_prod_log.py) | Monitoring CLI options. |
| [Client environment](https://gitlab.cern.ch/CLICdp/iLCDirac/ILCDIRAC/-/blob/ef8854aea4a037463e4323044840227f7e447d74/docs/Files/UserGuide/ilcdiracclient.rst) | Dedicated shell and CVMFS setup. |
| [FCCDIRAC example revision](https://github.com/HEP-FCC/FCCDIRAC/tree/d178d5e3e6484a4cb468ef5b1bcfbf117d58b9d6/productions/summer2026/ZH_ZZ_WW) | Source configuration and input cards used for the worked example. PR #19 was open when this material was prepared. |
| [FCC distributed-computing setup](https://github.com/HEP-FCC/fcc-tutorials/blob/14b8f9b94ebdcb70b6c842c606b04c23ec948ac3/5-distributed-computing/RegisteringToFccVO.md) | FCC user proxy and web portal. |

The new template reduces the referenced three-process example to one ZH process, one task and 100 events, replaces its campaign and name with session-specific values, and explicitly disables optional file-moving transformations.

Return to [Launching productions](README.md).
