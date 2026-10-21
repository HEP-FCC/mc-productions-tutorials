# From a DRS request to a production configuration

Start from the agreed DRS specification. The MC contact selects the relevant application chain, writes the configuration, checks its inputs and submits it through `dirac-fcc-make-productions`.

## Two kinds of configuration

The production `.conf` file selects the workflow, software, statistics, naming and storage. Generator, detector and output cards define the detailed physics and event content. Keep their revisions together.

Application sections use the spelling of the application's setter names. For example, `ExecutableName` maps to `setExecutableName`. Use the exact section and option names shown in the example.

| Agreed information | Configuration entry for the worked example |
| --- | --- |
| Pythia8 generation followed by Delphes | `generatorApplication = delphesapp` and `ExecutableName = DelphesPythia8_EDM4HEP` |
| Generator physics and collision settings | `generatorSteeringFile` and the contents of that card |
| Collision energy | `energies`, consistent with `Beams:eCM` in the Pythia8 card |
| Detector response | `DetectorCard`, plus the `detectorModel` metadata label |
| Output event content | `OutputCard`; the executable writes EDM4hep output |
| Software | `softwareVersion` and the application's `Version` |
| Configuration package | `configPackage` and `configVersion`, used for configuration lookup |
| Pilot statistics | `eventsPerJobs` and `numberOfTasks` |
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

CLD full simulation with separate Gen, Sim and Rec stages is part of the campaign baseline. A complete worked CLD example will be added after the training; it is not required for today's live exercise. It will need agreed generation, CLD detector and reconstruction configurations, software versions and a checked pilot.

The current command supports the following stage structure:

```ini
generatorApplication = gaudiapp_gen
simulationApplication = ddsim
reconstructionApplication = gaudiapp_rec
ProdTypes = Gen, Sim, Rec
```

This is a structural example. Each application needs its own complete, compatible configuration. Use an agreed full-simulation recipe for a real request. The separate Gaudi application names allow different settings for generation, simulation and reconstruction.

## Keep the pilot small and explicit

For the single-process generation example:

```ini
eventsPerJobs = 100
numberOfTasks = 1
```

This requests one generation task with 100 events. The delivered usable count must still be measured. Filtering, application failures or incomplete jobs can reduce it.

For several process/energy entries, check the correspondence between `processes`, `energies`, `eventsPerJobs`, `generatorSteeringFile` and `numberOfTasks`. The parser broadcasts some single-value lists, but do not assume that every list is broadcast. Explicit matching lists are easier to review.

The command pairs configured entries; it does not generate every possible process/energy combination. Keep one process and one energy point for this exercise.

## Cards and version references

The worked example keeps all three cards in the submission directory as a **training-only shortcut**. The current Delphes application accepts local detector and output cards and adds them to the input sandbox. It reads the Pythia8 card through its card-finding utility. Missing local files can otherwise trigger lookup in configured locations.

For normal productions, obtain the generator card from the requester through the DRS upload or from the maintained "golden cards" in [FCC-config](https://github.com/HEP-FCC/FCC-config). Package the detector and output cards in the configuration tarball selected by `configPackage` and `configVersion`. The pinned FCCDIRAC downloads are used only to reproduce the training example; FCCDIRAC records production history.

For the training, local copies with known revisions make the chosen inputs unambiguous. Record the immutable source commit and your changes. The example's `key4hep_260408` and `key4hep-devel-6` values come from the referenced FCC configuration. Use them only when they match the session's available software and configuration package.

Do not use `latest` as the record of a production's software version. Do not add a fixed random seed to make all training jobs identical. Use the production workflow's seed handling and record the production and job IDs.

## Naming and output location

For the training, use `campaign = summer2026` and the agreed process naming. The output is stored alongside summer2026 production output and requires cleanup after the session. These labels contribute to output paths and catalogue metadata. `prodGroup` groups transformations; `additionalName` helps distinguish attempts with otherwise identical names.

Use a unique training suffix containing your CERN username and an attempt label. If a name already exists, inspect that production before deciding to create another one. Changing the suffix and resubmitting can create a second live production.

The example sets `move = False`. `MoveStatus` and `finalOutputSE` concern optional file-moving transformations. They do not disable generation or its normal output upload.

## Review before submission

- The request is ready for production and its scope matches the configuration.
- The executable and cards implement the requested physics and final stage.
- The metadata energy matches the generator card.
- The software and card revisions are recorded.
- The pilot budget, naming, campaign and storage destination are correct.
- The dry-run XML and messages match the intended single transformation.

Return to [Launching productions](README.md).
