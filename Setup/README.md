# Setup

Before working with the productions, every MC Production contact needs a
GRID certificate, has to be registered in the FCC VO (Virtual Organisation)
and needs the iLCDirac client.

The steps are described in the existing documentation linked below. Parts of
it might be outdated, so please ask if something does not work.


## Step 1: GRID certificate

* Request the certificate from the CERN Certification Authority:
  https://ca.cern.ch/ca/
* Export and convert it, as described in the iLCDirac documentation:
  https://ilcdirac-doc.web.cern.ch/DOC/Files/UserGuide/registration.html


## Step 2: FCC VO registration

* Register in the FCC VO, as described in the FCC tutorial:
  https://github.com/HEP-FCC/fcc-tutorials/blob/main/5-distributed-computing/RegisteringToFccVO.md
* Check in https://fcc-auth.cern.ch/ that you are in the `fcc_prod` group and
  that your iLCDirac nickname is set. If not, ask at
  fcc-ped-softwareandcomputing-mcproduction@cern.ch


## Step 3: iLCDirac client and proxy

* Use only the existing iLCDirac client installation from CVMFS, do not
  install your own:
  `source /cvmfs/clicdp.cern.ch/DIRAC/bashrc`
  (https://ilcdirac-doc.web.cern.ch/DOC/Files/UserGuide/ilcdiracclient.html)
* Create the production proxy, as shown in the
  [iLCDirac tutorial](../iLCDirac/README.md)


## Step 4: GitHub and FCCDIRAC

* Productions are prepared and submitted from within a clone of
  [FCCDIRAC](https://github.com/HEP-FCC/FCCDIRAC), and recorded there through
  pull requests
* Create a GitHub account, add an SSH key from the host you submit from
  (https://docs.github.com/en/authentication/connecting-to-github-with-ssh),
  and fork FCCDIRAC
