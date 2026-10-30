# Exercise: act on an existing dataset request

Create the request below in the [production DRS](https://fcc-drs.web.cern.ch/) as a requester would: title starting with `[TUTORIAL]`, group **Documentation and Trainings**, and the text below as its description. Submit it, then act on it as the MC Production contact.

Without DRS access, use the request below as a worksheet.

## The request to review

This is an illustrative tutorial request. Its numbers and physics choices are for discussion and do not define an approved production recipe.

> We need 100k hadronic Z events with IDEA for a performance study by the end of the month. Please use the latest software and the usual settings. Delphes should be fine. The output should be ROOT. Please put it in the autumn campaign. Priority: High.

## Your task as the MC contact

1. Read the existing fields, attachments and discussion. Check for related requests or datasets before proposing additional production.
2. Identify the clarifications needed in five areas: collision energy; process and generator configuration; detector configuration; software version; output format and content. An agreed campaign configuration can answer several of these without requiring the requester to specify every technical detail.
3. Post a short public comment asking for the missing information. As the requester of your own tutorial request, check that the DRS email notification arrives and opens this request.
4. Once the requester clarifies the need, update the existing record. Which information belongs in **Description**, and which belongs in a dedicated field? Use the mapping below.
5. Suppose Physics is Approved and Resources is Pending. Resources approval currently belongs to the DRS admins. You can prepare the configuration and review its dry run while that decision is pending; resolve the approvals before a live launch.
6. Once both approvals and campaign placement are agreed, write or adapt the production configuration and submit through the iLCDirac command line. Continue in the [production-launching tutorial](../iLCDirac/README.md) with its small trial budget. Its ZH example is a different process from this hadronic-Z review example.
7. Find the resulting transformations and associated jobs in iLCDirac. Record the real transformation IDs labelled by process and step, a job ID and its observed status. Explain why DRS **In Progress** alone does not show that jobs are running.
8. The requester asks to double the statistics after approval. What should you record and recheck before extending the production?

## A more precise request after clarification

Use this as an example of updating the existing request. The software release and cards still need agreement before production.

| DRS field | Example entry |
| --- | --- |
| Title | `[TUTORIAL] Hadronic Z-pole dataset for an IDEA performance study` |
| Description | `e+e- collisions at sqrt(s) = 91.2 GeV. Inclusive hadronic Z/gamma* production with u, d, s, c and b final states. No generator-level event filter is requested. Study: compare reconstructed jet observables. Confirm the generator/version, ISR and beam settings, decay treatment and exact configuration before launching.` |
| Group / Team | Documentation and Trainings for the tutorial. For a real request, use its responsible physics group. |
| Use Case | Physics Analysis, if agreed with the requester. |
| Final Processing Stage | Delphes |
| Format | EDM4hep, if agreed for the analysis chain. ROOT alone does not specify the event-data model or collections. |
| Detector(s) | IDEA, with the exact Delphes card revision in the configuration reference. |
| Statistics | 100,000 final events at one energy point. Keep the trial count separate. |
| Estimated Size | About 0.75 GB for 100,000 events, using 7.5 kB/event measured on Winter 2023 IDEA Delphes Z-to-qq datasets. Check the estimate for the chosen software and output content. |
| Target Campaign | The requested campaign, using its agreed spelling. |
| Key4hep Stack | The exact agreed release. Replace `latest` with that reference. |
| Due Date / Priority | The useful delivery date, its reason and the agreed relative priority. |
| Generator Cards | The agreed card or an immutable configuration reference. |

The estimate uses decimal kB and GB. For full-simulation datasets, consult the **Event Size** section of the [k4Bench reconstruction dashboard](https://k4bench-dashboard.app.cern.ch/reconstruction), using a benchmark appropriate to the requested configuration.

Keep the request Under Review while clarifications or decisions remain outstanding.

<details>
<summary>Suggested points to check your answers against</summary>

- **Energy:** establish the intended collision energy and beam conditions.
- **Physics configuration:** resolve the process, flavour/decay scope, generator/version and relevant radiation or filter settings.
- **Detector:** identify the exact IDEA card and any requested changes.
- **Software:** identify a reproducible release and configuration revision.
- **Output:** specify the event-data model, required collections and processing stage.
- **Notifications:** a saved public comment and delivery of its email notification are separate observations. Check both.
- **Approvals:** any MC contact of the request's group can give Physics approval; DRS admins give Resources approval in the current workflow.
- **Submission:** the contact prepares the configuration and uses the iLCDirac command line once the request is ready for production.
- **Monitoring:** inspect each transformation and its associated jobs. Record IDs per process and step. Three processes with Gen, Sim and Rec produce nine transformation IDs.
- **Changed statistics:** record the change, review resources and priority, inspect existing output and agree how to extend the production. Editing the request does not automatically rerun its approvals.

</details>

## Evidence to keep

Keep the request URL, clarification comment, notification check and agreed configuration reference. After a real launch, add the actual production identifiers and observed status. After delivery, add the dataset reference, validation summary and any limitations.

When done, ask for the [cleanup](../README.md#cleaning-up-after-the-tutorial) of your `[TUTORIAL]` request and its production objects. Cancelling the request in the DRS does not stop DIRAC jobs.

Return to the [DRS walkthrough](README.md).
