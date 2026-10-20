# Troubleshooting a production

Start with the first relevant error. Keep the DRS request, configuration revision, transformation ID and job ID together. A short error excerpt is more useful than an unfiltered terminal transcript.

| Symptom | What to check |
| --- | --- |
| `dirac-fcc-make-productions` is missing | Source the session's iLCDirac client in a fresh shell. Check the client version and setup path. |
| Proxy creation fails | Certificate setup, password, expiry, FCC registration and the requested group. Ask the instructors to check the account mapping. |
| `fcc_user` works but live production is denied | Obtain the assigned `fcc_prod` access. Production submission requires `ProductionManagement`. |
| Local checker finds a placeholder or too many events | Fill the session values and restore the one-task, at-most-100-event pilot budget. |
| Card is missing or the energy is inconsistent | Run from the work directory containing the cards. Compare `energies` with the Pythia `Beams:eCM` setting. |
| Unknown application option | Check the exact section and option spelling against the installed version. Application keys map to setter names. |
| Parameter-list lengths disagree | Pair process, energy, event count, steering file and task count explicitly. Start with one process and one energy. |
| Software or configuration package cannot be found | Compare `softwareVersion`, application `Version`, `configPackage` and `configVersion` with the session setup. A source repository containing a recipe does not establish deployment availability. |
| Transformation name already exists | Inspect the existing production. Establish whether it is your previous attempt before choosing a new unique suffix. |
| Submission errors after creating an ID | Inspect the transformation and task limit before retrying. Partial creation is possible. |
| Active transformation has no jobs | Inspect the tasks and service processing. Ask production support with the ID and time of submission. Repeated submission is not a diagnostic step. |
| Job is queued for a long time | Inspect its detailed status and site/resource information. Compare with the instructor's demonstration production. |
| Job fails | Read the minor status and logs. Distinguish application/configuration errors from access, transfer or site failures. |
| Job is Done but the sample is not usable | Check output registration, replicas, file access, event count and collections. Sandbox retrieval does not retrieve all event data. |
| No sandbox or production log is available yet | Check the job phase and output-upload status. Inspect the portal and the production log location in the job details. |

## Recovery and cleanup

Agree the recovery action with the responsible production expert after identifying the cause. A configuration bug usually needs a corrected recipe and an explicit decision about existing output. An infrastructure failure may have a different recovery path.

Do not bulk-resubmit, delete transformations or remove files as a diagnostic shortcut. The training cleanup should identify the exact transformations, jobs and output involved. Stopping further task processing and cancelling jobs already submitted are separate actions. Cancelling the DRS request performs neither.

Return to [Launching productions](README.md).
