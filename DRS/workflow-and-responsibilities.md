# Overall workflow and responsibilities of MC Production contacts

Speakers: Pantelis Kontaxakis and Juraj Smiesko  
Training of the MC Production contacts, Autumn 2026

## Purpose

An MC Production contact follows a dataset request from its physics definition to a usable dataset. The contact connects the requesting physicists, their physics group and the central production team, and keeps the request record understandable throughout the work.

By the end of the training, a contact should be able to review a request in the DRS, prepare the information needed for a production, follow its progress and identify the output to share with the requester.

## The workflow

| Stage | Main system | Work to do | Evidence to keep |
| --- | --- | --- | --- |
| Define the request | DRS | Record the physics process, intended use, configuration and requested statistics. | Request URL, specification and generator cards. |
| Review and organise | DRS | Resolve missing information, record the agreed physics and resources decisions, and organise campaign assignment. | Comments, approval records and assigned campaign. |
| Prepare and run | iLCDirac | Validate the agreed configuration, launch the central production and monitor its jobs. | Configuration revision, software release, validation results and production identifiers. |
| Check and publish | Output storage and DaMI | Check the delivered files and statistics, publish the dataset metadata and tell the requester how to access the sample. | Validation summary, dataset reference and access information. |

The DRS records requests and coordination decisions. The iLCDirac part of the training covers job submission and monitoring. An approved request, or a request assigned to a campaign, still needs the corresponding production work.

Rucio is outside the scope of this training. Follow the storage and dataset-publication procedure demonstrated by the instructors.

## Responsibilities in practice

The following is a proposed working division for this training. The organisers should confirm who records each approval decision before participants exercise those controls.

| Participant | Main responsibility |
| --- | --- |
| Requester and physics group | Define the physics need, required statistics and timescale. Supply or agree the physics configuration and assess whether the sample serves the study. |
| MC Production contact | Check request completeness and overlap with existing samples, obtain clarifications, coordinate the production preparation and follow-up, and keep useful references in the DRS. |
| Production coordination and relevant experts | Agree capacity and campaign placement, support the production configuration and resolve infrastructure or generator issues that need specialist input. |
| Application or VO administrators | Grant the relevant access rights. DRS administration, FCC VO administration and production permissions are separate. |

The contact can organise the work without personally resolving every generator, detector or computing problem. When escalating a problem, provide the request reference, configuration revision, relevant identifiers and the smallest useful error excerpt.

## Before a production starts

- Check whether an existing dataset or request already covers the need.
- Resolve the process definition, collision energy, generation settings, filters and intended final processing stage.
- Distinguish the requested final statistics from the event count used for a small validation run.
- Identify the generator card, detector configuration and software release precisely.
- Agree the physics and resources decisions with the responsible people.
- Record the campaign assignment and who will follow the production.
- Inspect a small validation sample before scaling to the requested statistics.

These are review criteria. A form accepting a request does not by itself establish that the configuration is ready to run.

## During and after production

Record the real production identifiers as soon as the production system provides them. Use the monitoring tools to check progress and investigate failures. When the configuration changes, record what changed and whether it affects samples already produced.

Before closing a request, check the agreed delivered statistics, file access and the relevant physics or technical validation. Add a short completion comment with the dataset reference and any limitations, then use the agreed publication and completion procedure.

## References that serve different purposes

| Reference | What it identifies |
| --- | --- |
| DRS request URL / request number | The community's request and its discussion. |
| Configuration commit or tag | The exact recipe used for the sample. |
| Production / transformation identifiers | The managed processing tracked by the production system. Follow the convention demonstrated in the iLCDirac session. |
| Job identifier | One submitted job within the processing. |
| Dataset name, location or DaMI entry | The output that analysts need to discover and access. |

Keep these references together, with labels explaining their meaning. The DRS **Production IDs** control records identifiers supplied by the production system.

## Support

- [FCCSW forum: Distributed Computing](https://fccsw-forum.web.cern.ch/c/distributed-computing/12)
- [MC production support](mailto:fcc-ped-softwareandcomputing-mcproduction@cern.ch)
- [DRS walkthrough](README.md)
- [iLCDirac tutorial](../iLCDirac/README.md)
- [DaMI tutorial](../DaMI/README.md)

## Source basis

Workflow scope: [MC Productions Tutorials](https://github.com/HEP-FCC/mc-productions-tutorials/tree/e747b4a1bd250d08e66564d7807a0147d0d8ccf1). DRS behaviour: [source snapshot](https://github.com/HEP-FCC/fcc-drs/tree/ceaab4ab98d478458d559730ccebd299c693c6f8), checked 19 October 2026. Responsibilities and completion criteria above are proposed training guidance, subject to the organisers' agreement.
