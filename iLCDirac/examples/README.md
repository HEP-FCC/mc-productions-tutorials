# Worked example: a small ZH production

This example prepares a Pythia8 + Delphes pilot for ZH at 240 GeV with IDEA and EDM4hep output. It adapts the configuration in [FCCDIRAC PR #19](https://github.com/HEP-FCC/FCCDIRAC/pull/19), pinned to commit `d178d5e3e6484a4cb468ef5b1bcfbf117d58b9d6`.

Use the DRS request assigned for this sample. The hadronic-Z example in the DRS review exercise is a different physics request and should not be submitted with this ZH configuration.

## Prepare the work directory

In your tutorial checkout on the training host:

```bash
cd "$(git rev-parse --show-toplevel)"
tutorial_dir="$PWD"
mkdir -p "$HOME/fcc-mc-training/zh-pilot"
cd "$HOME/fcc-mc-training/zh-pilot"
cp "$tutorial_dir/iLCDirac/examples/pythia-delphes.conf.template" training.conf
```

Use an empty work directory for your first attempt. If you already have files here, preserve your previous configuration and logs before preparing a new attempt.

Retrieve the three input cards from the pinned source:

```bash
card_source="https://raw.githubusercontent.com/HEP-FCC/FCCDIRAC/d178d5e3e6484a4cb468ef5b1bcfbf117d58b9d6/productions/summer2026/ZH_ZZ_WW"
curl --fail --location --output p8_ee_ZH_ecm240.cmd "$card_source/p8_ee_ZH_ecm240.cmd"
curl --fail --location --output card_IDEA.tcl "$card_source/card_IDEA.tcl"
curl --fail --location --output edm4hep_IDEA.tcl "$card_source/edm4hep_IDEA.tcl"
```

Check that all three downloads succeeded. The original card authors and comments are retained in these upstream files. If network access fails, obtain the same pinned files from the instructors.

## Adapt the configuration

```bash
nano training.conf
```

Replace `REPLACE_WITH_TRAINING_CAMPAIGN` with the exact session campaign and `REPLACE_WITH_CERN_USERNAME` with your CERN username. Check the agreed software versions and `outputSE`. Keep the example at **one task and 100 events**.

The Pythia card contains its original standalone event count. The production workflow supplies the per-task event count from `eventsPerJobs`. Verify the effective count in the pilot log and output.

## Check the local inputs

```bash
python "$tutorial_dir/iLCDirac/scripts/check_training_config.py" training.conf
```

The checker verifies that required values are filled, the tutorial has one task and at most 100 events, the local cards exist, and the Pythia energy matches the configuration. It also checks the intended application and stage selection. It reads only local files and does not submit anything.

Passing this check does not validate the detector response, software availability, proxy, storage permissions or physics. Continue with the [iLCDirac dry run and live pilot](../README.md#4-run-without-creating-a-production).
