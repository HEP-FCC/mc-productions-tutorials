# Exercise: review a dataset request

Allow 8 minutes for the exercise and 5 minutes for discussion. Work in pairs if useful. Complete this as a worksheet, or use the instructor's designated training request.

## The incoming request

This is an invented training example. The numbers and physics choices are for discussion, not an approved production specification.

> We need 100k hadronic Z events with IDEA for a performance study by the end of the month. Please use the latest software and the usual settings. Delphes should be fine. The output should be ROOT. Please put it in the autumn campaign. Priority: High.

## Your task

1. Identify at least five details that need clarification before launching a production.
2. Write a short public comment asking the requester for the missing information.
3. Map the information you already have to the DRS form. Which details belong in **Description**?
4. Suppose Physics is Approved and Resources is Pending, with the request Under Review. What should happen next?
5. The request now has both approvals. A coordinator assigns it to a campaign and its status becomes In Progress. What evidence would you need to know whether jobs are running?
6. The requester asks to double the statistics after approval. What should you record and recheck?

## A more precise request after discussion

Use this as a worked mapping example. The configuration release, cards and resource estimate still need agreement before production.

| DRS field | Example entry |
| --- | --- |
| Title | `[TRAINING] Hadronic Z-pole sample for an IDEA performance study` |
| Description | `e+e- collisions at sqrt(s) = 91.2 GeV. Inclusive hadronic Z/gamma* production with u, d, s, c and b final states. No generator-level event filter is requested. Study: compare reconstructed jet observables. Confirm the generator/version, ISR and beam settings, decay treatment and the exact configuration with the production team before launching.` |
| Group / Team | The training group chosen by the instructor. For a real request, select its actual responsible group. |
| Use Case | Physics Analysis, assuming that this is the purpose agreed with the requester. |
| Final Processing Stage | Delphes |
| Format | EDM4hep, if agreed for the analysis chain. The term ROOT alone does not specify the event-data model. |
| Detector(s) | IDEA. Record the exact Delphes card revision in the description/configuration reference. |
| Statistics | 100,000 final events at one energy point. Keep the pilot event count separate. |
| Estimated Size | Pending a pilot measurement. For arithmetic only, an assumed 50 kB/event would imply 5 GB for 100,000 events, using decimal units. This is not a measurement. |
| Target Campaign | The requested autumn campaign name, once its spelling is confirmed. |
| Key4hep Stack | The exact release agreed with the production team. Do not substitute `latest` in the production specification. |
| Due Date / Priority | Confirm the useful delivery date and why it matters. Agree priority relative to other requests. |
| Generator Cards | Attach or reference the agreed card and its revision once available. |

Keep this as a draft or a request awaiting clarification until the missing specification is resolved. A successful form submission is not the completion criterion for the review.

## Evidence to keep

Your result should contain a clarification comment, a suggested next action and the information still needed for production. After a real launch, add the real production identifiers and configuration reference. After delivery, add the dataset reference and validation summary.

Return to the [DRS walkthrough](README.md).
