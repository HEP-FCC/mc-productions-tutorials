# Worked example: a small ZH production

This example prepares a Pythia8 + Delphes trial for ZH at 240 GeV with IDEA and EDM4hep output. It adapts the configuration in [FCCDIRAC PR #19](https://github.com/HEP-FCC/FCCDIRAC/pull/19), pinned to commit `d178d5e3e6484a4cb468ef5b1bcfbf117d58b9d6`.

Use the DRS request assigned for this dataset. The hadronic-Z example in the DRS review exercise is a different physics request and should not be submitted with this ZH configuration.

## Prepare the attempt directory

Productions are prepared and submitted from within [FCCDIRAC](https://github.com/HEP-FCC/FCCDIRAC), see [Record the production in FCCDIRAC](../production-config.md#record-the-production-in-fccdirac). Fork it on GitHub, then, in your tutorial checkout on the training host:

```bash
cd "$(git rev-parse --show-toplevel)"
tutorial_dir="$PWD"
read -r -p "GitHub username: " github_user
read -r -p "DRS request number: " drs_number
git clone "git@github.com:${github_user}/FCCDIRAC.git" "$HOME/FCCDIRAC"
cd "$HOME/FCCDIRAC"
git switch -c "summer2026/DRS-${drs_number}"
mkdir -p "productions/summer2026/DRS-${drs_number}/attempt1"
cd "productions/summer2026/DRS-${drs_number}/attempt1"
cp "$tutorial_dir/iLCDirac/examples/pythia-delphes.conf.template" training.conf
```

A new attempt gets a new directory, `attempt2`, `attempt3`, …; do not reuse a directory that was already submitted.

**Training-only card source and layout:** the downloads below reproduce a pinned historical example from FCCDIRAC. For normal productions, obtain the generator card from the requester through the DRS upload or from the maintained "golden cards" in [FCC-config](https://github.com/HEP-FCC/FCC-config). The detector and output cards (`card_IDEA.tcl`, `edm4hep_IDEA.tcl`) should be included in the configuration tarball selected by `configPackage` and `configVersion`. Reading those two cards from the submission directory is a convenience used only for this training. FCCDIRAC serves as the historical record of production configurations.

For this training, retrieve the three input cards from the pinned historical source:

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

Keep `campaign = summer2026` and replace `REPLACE_WITH_CERN_USERNAME` with your CERN username. Check the agreed software versions and `outputSE`. Keep the example at **one task and 100 events**.

The output is stored alongside the summer2026 productions. Retain the unique training suffix and the exact transformation IDs and output paths so the instructors can coordinate cleanup after the session.

The Pythia card contains its original standalone event count. The production workflow supplies the per-task event count from `eventsPerJobs`. Verify the effective count in the trial log and output.

## Review the inputs and run the dry run

Check that all three local cards are present, the CERN username is filled, the Pythia card's `Beams:eCM` agrees with `energies = 240`, and the configuration still requests one task and 100 events in `summer2026`.

Use the existing [iLCDirac dry run](../README.md#4-run-without-creating-a-production) to check the configuration. Inspect its messages and workflow XML before a live submission. A successful dry run checks workflow preparation; the trial execution and output checks establish whether the dataset was produced as intended.
