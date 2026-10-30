# From a DRS request to a production configuration

Start from the agreed DRS specification. The MC contact selects the relevant application chain, writes the configuration, checks its inputs and submits it through `dirac-fcc-make-productions`.

## Two kinds of configuration

The production `.conf` file selects the workflow, software, statistics, naming and storage. Generator, detector and output cards define the detailed physics and event content. Keep their revisions together.

Application sections use the spelling of the application's setter names. For example, `ExecutableName` maps to `setExecutableName`. Use the exact section and option names shown in the example.

The [FCC Production Manager Guide](https://ilcdirac-doc.web.cern.ch/DOC/Files/ProdGuide/fccProdNotes.html) describes the configuration parameters and the output path, and gives example configurations for the standalone generators, the Delphes executables and a full simulation. Its examples use older software versions.

| Agreed information | Configuration entry for the worked example |
| --- | --- |
| Pythia8 generation followed by Delphes | `generatorApplication = delphesapp` and `ExecutableName = DelphesPythia8_EDM4HEP` |
| Generator physics and collision settings | `generatorSteeringFile` and the contents of that card |
| Collision energy | `energies`, consistent with `Beams:eCM` in the Pythia8 card |
| Detector response | `DetectorCard`, plus the `detectorModel` metadata label |
| Output event content | `OutputCard`; the executable writes EDM4hep output |
| Software | `softwareVersion` and the application's `Version` |
| Configuration package | `configPackage` and `configVersion`, used for configuration lookup |
| Trial statistics | `eventsPerJobs` and `numberOfTasks` |
| Campaign and naming | `campaign`, `processes`, `prodGroup` and `additionalName` |
| Output storage | `outputSE` |

`detectorModel = IDEA` is a label, not a substitute for identifying the detector card. Likewise, a process name does not define the generator settings.

## Why this Delphes example uses `ProdTypes = Gen`

The selected executable performs Pythia8 generation and Delphes processing within one application. The production script places it in one generation transformation:

```ini
generatorApplication = delphesapp
ProdTypes = Gen
```

This produces Delphes output even though the transformation type is `Gen`. Adding `Sim` would request another managed stage; it is not how to turn on the Delphes processing already performed by this executable.

## CLD full simulation: follow-up example

CLD full simulation with separate Gen, Sim and Rec stages is part of the campaign baseline. A complete worked CLD example will be added later; it is not needed for the exercise. It will need agreed generation, CLD detector and reconstruction configurations, software versions and a checked trial.

The current command supports the following stage structure:

```ini
generatorApplication = gaudiapp_gen
simulationApplication = ddsim
reconstructionApplication = gaudiapp_rec
ProdTypes = Gen, Sim, Rec
```

This is a structural example. Each application needs its own complete, compatible configuration. Use an agreed full-simulation recipe for a real request. The separate Gaudi application names allow different settings for generation, simulation and reconstruction.

## Keep the trial small and explicit

For the single-process generation example:

```ini
eventsPerJobs = 100
numberOfTasks = 1
```

This requests one generation task with 100 events. The delivered usable count must still be measured. Filtering, application failures or incomplete jobs can reduce it.

For several process/energy entries, check the correspondence between `processes`, `energies`, `eventsPerJobs`, `generatorSteeringFile` and `numberOfTasks`. The parser broadcasts some single-value lists, but do not assume that every list is broadcast. Explicit matching lists are easier to review.

The command pairs configured entries; it does not generate every possible process/energy combination. Keep one process and one energy point for this exercise.

## Cards and version references

The worked example keeps all three cards in the submission directory as a **tutorial-only shortcut**. The current Delphes application accepts local detector and output cards and adds them to the input sandbox. It reads the Pythia8 card through its card-finding utility. Missing local files can otherwise trigger lookup in configured locations.

For normal productions, obtain the generator card from the requester through the DRS upload or from the maintained "golden cards" in [FCC-config](https://github.com/HEP-FCC/FCC-config). Package the detector and output cards in the configuration tarball selected by `configPackage` and `configVersion`. The pinned FCCDIRAC downloads are used only to reproduce the tutorial example; FCCDIRAC records production history (see [Record the production in FCCDIRAC](#record-the-production-in-fccdirac)).

For the tutorial, local copies with known revisions make the chosen inputs unambiguous. The example's `key4hep_260408` and `key4hep-devel-6` values come from the referenced FCC configuration. Check that this software and configuration package are still available before submitting.

Do not use `latest` as the record of a production's software version. Do not add a fixed random seed to make all jobs identical. Use the production workflow's seed handling and record the production and job IDs.

## Record the production in FCCDIRAC

Every production is recorded in [FCCDIRAC](https://github.com/HEP-FCC/FCCDIRAC), so that anyone can read the exact configuration on GitHub without going through iLCDirac. This includes the tutorial and test productions in the `summer2026` campaign.

- Prepare the `.conf` file and all cards (generator, detector, output) in `productions/<campaign>/DRS-<n>/attempt<k>/` of your FCCDIRAC clone, for example `productions/autumn2026/DRS-42/attempt1/`, and submit from that directory. Commit the `.conf` file and the cards; the logs and workflow XML stay local.
- A submitted attempt is never changed. Any change to the configuration or a card is a new attempt: `attempt2`, `attempt3`, … Extending a production keeps its configuration and stays in the same attempt.
- Record the transformation IDs, labelled by process and step, in the commit message:

  ```
  DRS-42 attempt1: ZH, ZZ, WW at 240 GeV, IDEA Delphes

  Transformation IDs:
  - ZH / Gen: 23401
  - ZZ / Gen: 23402
  - WW / Gen: 23403
  ```

- Open the pull request after the submission, in a timely manner. The directory identifies the attempt, so no commit hash needs to be recorded and the commit can be rebased or amended freely.
- Link the attempt directory on the `master` branch in the DRS request and in DaMI.

## Naming and output location

For the tutorial, use the `summer2026` test campaign and the agreed process naming. The output is stored alongside the other summer2026 productions and needs a cleanup when you are done. These labels contribute to output paths and catalogue metadata. `prodGroup` groups transformations; `additionalName` helps distinguish attempts with otherwise identical names.

Use a unique tutorial suffix containing your CERN username and an attempt label. If a name already exists, inspect that production before deciding to create another one. Changing the suffix and resubmitting can create a second live production.

The example sets `move = False`. `MoveStatus` and `finalOutputSE` concern optional file-moving transformations. They do not disable generation or its normal output upload.

## Review before submission

- The request is ready for production and its scope matches the configuration.
- The executable and cards implement the requested physics and final stage.
- The metadata energy matches the generator card.
- The software and card revisions are recorded.
- The trial budget, naming, campaign and storage destination are correct.
- The dry-run XML and messages match the intended single transformation.

Return to [Launching productions](README.md).
