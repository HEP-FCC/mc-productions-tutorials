# Exercise: follow a request through a pilot production

Use the DRS request, campaign and event budget identified by the instructors. Work in pairs if useful. This exercise follows the workflow in the [main tutorial](README.md).

## 1. Identify the task

Open the existing DRS request. Record its URL and agreed process, energy, detector, output format, software release and requested total statistics. Identify any unresolved question before preparing the production.

For the bundled ZH example, use the corresponding ZH request. Keep its 100-event pilot separate from the full requested statistics.

## 2. Prepare and explain

Prepare the [worked example](examples/README.md), keep `campaign = summer2026`, fill your CERN username in the unique name and review the local cards and pilot budget. Explain to your partner:

- Which file defines the generator physics?
- Which settings determine the event content and detector response?
- Why does this combined Pythia8/Delphes example use `ProdTypes = Gen`?
- How many tasks and events does this pilot request?

## 3. Inspect the dry run

Run without `-x`. Locate the workflow XML and identify the application, software, output location and pilot budget. Explain why any displayed dry-run ID, including `12345`, is not evidence of a production submission.

## 4. Submit and find the work

When the instructors start the live-submission part, submit once with `-x`. Find the resulting transformation in iLCDirac. Record its real ID and one associated job ID when a job appears.

Inspect the job's status and details. If it is not running yet, report the observed state. Use an existing demonstration production if the training job cannot finish during the session.

## 5. Record the production in FCCDIRAC

In your attempt directory, `productions/summer2026/DRS-<n>/attempt1/` of your FCCDIRAC clone, commit the `.conf` file and the three cards with the transformation ID in the commit message. Push the branch to your fork and open a pull request to [FCCDIRAC](https://github.com/HEP-FCC/FCCDIRAC). Follow [Record the production in FCCDIRAC](production-config.md#record-the-production-in-fccdirac).

## 6. Return to the DRS

Add the real production reference and the link to the FCCDIRAC attempt directory to the request. Write a short factual update with the pilot budget and observed status. Identify the output checks still needed before scaling or publishing the dataset.

| Evidence | Your result |
| --- | --- |
| DRS request URL | |
| FCCDIRAC attempt directory and pull request | |
| Client and Key4hep versions | |
| Pilot task/event budget | |
| Transformation ID | |
| Associated job ID and observed status | |
| Transformation LFN and full EOS path, if available | |
| Validation completed and next action | |

If production access is unavailable, complete preparation and the dry run where possible, then inspect the instructor's demonstration production. Do not invent IDs or submit through another person's credentials.

In the portal, right-click the transformation and open its details to obtain its output LFN. Prepend `/eos/experiment/fcc/prod` to obtain the full EOS path for DaMI.

The training uses `summer2026`, so its output sits alongside real production output. Retain the exact training IDs and paths and follow the instructors' directions for cleanup after the session. A change of DRS status does not cancel DIRAC jobs.

Return to [Launching productions](README.md).
