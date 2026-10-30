# Exercise: follow a request through a trial production

Use your `[TUTORIAL]` request from the [DRS exercise](../DRS/exercise.md), the `summer2026` test campaign and the event budget of the worked example. This exercise follows the workflow in the [main tutorial](README.md).

## 1. Identify the task

Open the existing DRS request. Record its URL and agreed process, energy, detector, output format, software release and requested total statistics. Identify any unresolved question before preparing the production.

For the bundled ZH example, use the corresponding ZH request. Keep its 100-event trial separate from the full requested statistics.

## 2. Prepare and explain

Prepare the [worked example](examples/README.md), keep `campaign = summer2026`, fill your CERN username in the unique name and review the local cards and trial budget. Check that you can answer:

- Which file defines the generator physics?
- Which settings determine the event content and detector response?
- Why does this combined Pythia8/Delphes example use `ProdTypes = Gen`?
- How many tasks and events does this trial request?

## 3. Inspect the dry run

Run without `-x`. Locate the workflow XML and identify the application, software, output location and trial budget. Explain why any displayed dry-run ID, including `12345`, is not evidence of a production submission.

## 4. Submit and find the work

When the dry run looks right, submit once with `-x`. Find the resulting transformation in iLCDirac. Record its real ID and one associated job ID when a job appears.

Inspect the job's status and details. If it is not running yet, report the observed state and check again later.

## 5. Record the production in FCCDIRAC

In your attempt directory, `productions/summer2026/DRS-<n>/attempt1/` of your FCCDIRAC clone, commit the `.conf` file and the three cards with the transformation ID in the commit message. Push the branch to your fork and open a pull request to [FCCDIRAC](https://github.com/HEP-FCC/FCCDIRAC). Follow [Record the production in FCCDIRAC](production-config.md#record-the-production-in-fccdirac).

## 6. Return to the DRS

Add the real production reference and the link to the FCCDIRAC attempt directory to the request. Write a short factual update with the trial budget and observed status. Identify the output checks still needed before scaling or publishing the dataset.

| Evidence | Your result |
| --- | --- |
| DRS request URL | |
| FCCDIRAC attempt directory and pull request | |
| Client and Key4hep versions | |
| Trial task/event budget | |
| Transformation ID | |
| Associated job ID and observed status | |
| Transformation LFN and full EOS path, if available | |
| Validation completed and next action | |

If production access is unavailable, complete preparation and the dry run where possible, then inspect an existing summer2026 production in the web portal. Do not invent IDs or submit through another person's credentials.

In the portal, right-click the transformation and open its details to obtain its output LFN. Prepend `/eos/experiment/fcc/prod` to obtain the full EOS path for DaMI.

The tutorial uses the `summer2026` test campaign, so its output sits alongside other productions. Retain the exact IDs and paths and ask for the [cleanup](../README.md#cleaning-up-after-the-tutorial) when you are done. A change of DRS status does not cancel DIRAC jobs.

Return to [Launching productions](README.md).
