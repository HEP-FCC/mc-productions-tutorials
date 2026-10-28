# Launching productions with DIRAC/iLCDirac

Speakers: Pantelis Kontaxakis and Juraj Smiesko  
Training of the MC Production contacts, Autumn 2026

An MC Production contact takes an existing DRS request, prepares the production configuration, submits it through the iLCDirac command line, monitors the jobs and records the output references in the request.

This tutorial follows one small Pythia8 + Delphes production through that sequence. By the end, you should be able to explain your configuration, distinguish a transformation from a job, find both in iLCDirac and report what has actually run.

| Page | Purpose |
| --- | --- |
| This page | Environment, dry run, submission and monitoring. |
| [Production configuration](production-config.md) | Translate the agreed request into configuration fields. |
| [Worked example](examples/README.md) | Prepare a 100-event ZH trial at 240 GeV using pinned input cards. |
| [Practical exercise](exercise.md) | Follow a DRS request through submission and follow-up. |
| [Troubleshooting](troubleshooting.md) | Diagnose common setup, configuration and job problems. |
| [Version references](sources.md) | Identify the implementation and example used by this guide. |

## 1. Start from the DRS request

Open the request assigned to you in the [DRS](../DRS/README.md). Read its specification, discussion, approval records and campaign assignment. Resolve missing physics information with the requester and record the agreed configuration.

Before a live submission, know the process, collision energy, generator settings, detector/card revision, software release, final output, event budget and destination. In the current DRS workflow, group MC contacts give Physics approval and DRS admins give Resources approval. The contact writes or adapts the production configuration and carries out the submission. Production coordination and application experts help resolve issues.

For the training, use the request and small event budget identified by the instructors. If the exercise uses production services, keep the agreed training labels and follow the instructors' cleanup procedure.

| Object | What it tells you |
| --- | --- |
| DRS request | What has been requested and agreed. |
| Production configuration and cards | How the dataset is to be produced. |
| Transformation / production ID | The managed production created by this command. A multi-stage chain can have several IDs. |
| Job ID | One workload-management job associated with the production. |
| Output LFN and dataset reference | Where the resulting files and metadata can be found. |

A DRS status of **In Progress** can result from campaign assignment. Check iLCDirac for evidence that jobs were submitted or are running.

## 2. Open the client environment

Complete the [certificate and FCC VO setup](../Setup/README.md). Use the Linux host agreed for the session, with CVMFS available and your certificate configured. If you use a Mac, connect to that host first. Run the following commands in a fresh Bash shell on that host:

```bash
source /cvmfs/clicdp.cern.ch/DIRAC/bashrc
command -v dirac-fcc-make-productions
python -m pip show ILCDIRAC DIRAC
dirac-fcc-make-productions --help
```

Use the session's client installation if the instructors provide a different setup path. Keep the DIRAC client shell separate from a shell used to set up Key4hep for local event processing.

Production submission requires membership of the `fcc_prod` group. All MC contacts registered in fcc-auth have been assigned to this group for the training. Initialise the production proxy:

```bash
dirac-proxy-init -g fcc_prod
dirac-proxy-info -m
```

Check the identity, remaining lifetime, **DIRAC group** and uploaded proxy. The live production API requires the `ProductionManagement` property. A working `fcc_user` proxy establishes ordinary user access; it does not establish production privileges. Ask the instructors for help if `fcc_prod` is unavailable to your account.

## 3. Prepare one small configuration

Follow the [worked example](examples/README.md) to create an attempt directory in your FCCDIRAC clone containing:

- `training.conf`, your production configuration.
- `p8_ee_ZH_ecm240.cmd`, the Pythia8 card.
- `card_IDEA.tcl`, the detector card.
- `edm4hep_IDEA.tcl`, the output-content card.

The example uses one process, one energy point, `eventsPerJobs = 100` and `numberOfTasks = 1`. Keep the full statistics requested in the DRS separate from this trial budget. The training uses `campaign = summer2026`; retain the unique training name and check the software version and storage element agreed for the session. Its output will be stored alongside the summer2026 productions and must be cleaned up after training.

The local-card layout and pinned FCCDIRAC downloads are training-only shortcuts. For normal productions, use the requester's DRS generator card or a maintained FCC-config golden card, and include the detector and output cards in the configuration tarball selected by `configPackage` and `configVersion`.

Read [Production configuration](production-config.md), check the local input cards and review the one-task, 100-event trial budget. Use the iLCDirac dry run below to check the production configuration.

## 4. Run without creating a production

From the attempt directory, run:

```bash
set -o pipefail
dirac-fcc-make-productions -f training.conf 2>&1 | tee dry-run.log
```

Without `-x`, the command prepares the workflow without creating a live production. It can read service configuration and catalogue information, so this is not an offline physics simulation.

Review the messages and generated workflow XML. Check:

- The intended application, steering files and software release.
- The process, energy, campaign, detector and output destination.
- One intended transformation for this combined Pythia8/Delphes example.
- The agreed event count and number of generation tasks.
- No unresolved errors or unexpected extra stages.

**The dry-run implementation uses `12345` as a placeholder production ID. It is not a real submission result and must not be entered in the DRS.**

A successful dry run checks workflow preparation. The small live trial checks execution, file transfer and output content. A local generator test or a separately submitted `UserJob` also does not create the central transformation needed here.

## 5. Create the trial production

Before submission, import your personal GRID certificate, including its private key, into the browser you will use for the [iLCDirac web portal](https://voilcdiracwebapp2.cern.ch/DIRAC/), then check that you can log in. Browser certificate authentication is separate from the command-line proxy setup.

Once the request is ready for production and the instructors have reviewed the trial configuration, run:

```bash
dirac-fcc-make-productions -f training.conf -x 2>&1 | tee submit.log
```

**`-x` creates live transformations. In the referenced implementation they are set to `Active` with automatic agent processing.** Jobs may follow as the services process their tasks. `MoveStatus = Stopped` controls optional file-moving transformations; it does not hold the generation production.

Save the real transformation ID and find the production in the [iLCDirac web portal](https://voilcdiracwebapp2.cern.ch/DIRAC/). Check its name, configuration and task limit. If submission fails partway through, inspect the portal and log before retrying: an earlier stage may already exist.

Return to the DRS request. Under **Transformation IDs**, record each real transformation ID labelled by **process and step**, for example `ZH / Gen`. Add the configuration revision and trial budget in a comment. Record every process/step combination: three processes with Gen, Sim and Rec give nine transformation IDs.

Also commit the configuration and cards to FCCDIRAC with the transformation IDs in the commit message, and link the attempt directory in the request. See [Record the production in FCCDIRAC](production-config.md#record-the-production-in-fccdirac).

## 6. Monitor transformations and jobs

In the portal, open the transformation listing and find your ID or unique production name. Inspect its task count and status. Then open the associated jobs, or use the job listing to find jobs belonging to that transformation. Select one job and record its ID, status and any minor status or application error.

| Observation | Interpretation |
| --- | --- |
| Transformation exists and is Active | The production is registered and enabled. This does not prove a job is running. |
| No jobs yet | Inspect the transformation's tasks and service processing before deciding that submission failed. |
| Job is Waiting or another pre-execution state | The job has not yet reached running execution. |
| Job is Running | That job is executing. |
| Job is Done | Check the output and delivered statistics before reporting completion. |
| Job is Failed | Inspect the detailed status and logs before choosing a recovery action. |

For command-line checks, replace the prompted values with actual IDs from your production:

```bash
read -r -p "Transformation ID: " training_prod_id
dirac-ilc-production-summary -P "$training_prod_id"

read -r -p "Job ID: " training_job_id
dirac-wms-job-status "$training_job_id"
dirac-wms-job-get-output "$training_job_id"
```

The production summary provides an aggregate view and may write local summary files. The job-output command retrieves the output sandbox, where available. Large event files are normally separate output data. Use the job details and catalogue to find their logical file names (LFNs) and replicas.

For production logs stored separately:

```bash
dirac-ilc-get-prod-log -P "$training_prod_id"
```

Read the offered download information before confirming. See [Troubleshooting](troubleshooting.md) if an output sandbox or production log is not yet available.

## 7. Check the output and update the request

In the web portal, right-click the relevant transformation and open its details to find the output logical file name (LFN). For these central productions, prepend `/eos/experiment/fcc/prod` to the transformation LFN to obtain the full EOS path:

| Transformation LFN | Full EOS path |
| --- | --- |
| `/fcc/ee/summer2026/240gev/ZH/IDEA/delphes/...` | `/eos/experiment/fcc/prod/fcc/ee/summer2026/240gev/ZH/IDEA/delphes/...` |

Use the complete actual LFN in place of the abbreviated example. This full EOS path is the value to enter manually in DaMI's `path` metadata.

For the trial, locate at least one output file and verify that it opens in the agreed analysis environment. Check the event count, expected collections, generator/configuration information and a basic observable appropriate to the dataset. Retain the file reference and validation result.

Report separately what is configured, submitted, running and delivered. A successful job status alone is not a physics-validation result.

After the trial, follow the campaign's agreed scaling procedure. Before retrying or extending a production, inspect existing tasks and outputs to avoid duplicating work. Keep any configuration change and its effect on existing output in the DRS discussion.

After the dataset passes validation, the MC contact inserts it into DaMI manually or with a script. Follow the [DaMI tutorial](../DaMI/README.md) and include the requester, MC contact, production references and full EOS path in the agreed metadata. Cancelling a DRS request does not stop its DIRAC transformations or jobs. The training output is stored alongside real `summer2026` production output. Keep the exact training transformation IDs, job IDs and EOS paths, and follow the instructors' cleanup procedure after the session. Cleanup must target only those training objects and files.

## Support

For production questions, use the [FCCSW Distributed Computing forum](https://fccsw-forum.web.cern.ch/c/distributed-computing/12) or [MC production support](mailto:fcc-ped-softwareandcomputing-mcproduction@cern.ch). Include the request URL, transformation and job IDs, configuration revision and a short error excerpt.

Continue with the [practical exercise](exercise.md).
