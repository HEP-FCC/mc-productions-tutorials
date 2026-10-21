# DaMI: Dataset Metadata Interface

Speakers: Pantelis Kontaxakis and Juraj Smiesko  
Training of the MC Production contacts, Autumn 2026

DaMI is the metadata catalogue for FCC physics datasets, formerly the FCC Physics Events website. It helps analysts find a sample, understand its configuration and identify where its files are stored. The MC Production contact keeps the catalogue record consistent with the production and the original dataset request.

- [DaMI test instance](https://fcc-dami-test.web.cern.ch/)
- [FCC Physics Events production portal](https://fcc-physics-events.web.cern.ch/)
- [DRS walkthrough](../DRS/README.md)
- [iLCDirac tutorial](../iLCDirac/README.md)

**For the practical session:** open the DaMI instance announced by the instructors and use the dataset assigned to you. Make changes only to that record.

## 1. Access and responsibilities

Open the agreed instance. In the account menu, select **Sign in** and complete CERN authentication. The account badge shows the current role.

| Role | Relevant capabilities |
| --- | --- |
| Viewer | Read and search the catalogue and export metadata. |
| Editor | Viewer capabilities plus creating datasets, editing metadata and deleting catalogue entries. |
| Admin | Editor capabilities plus granting and revoking editor access through **Users**. |

A signed-in user without an editor or administrator grant has the viewer role. The instructors will grant editor access to MC contacts during the training. Check that your account shows the Editor role once it is assigned. DaMI roles are separate from DRS roles, FCC VO membership and production permissions.

MC contacts need editor access for the creation and editing tasks in this tutorial. With viewer access, you can complete the search, inspection and export steps.

## 2. Find a dataset and inspect its metadata

1. Use the search field to find the dataset named by the instructor.
2. Narrow the results using the navigation categories: accelerator, stage, campaign, detector and file type.
3. Expand the dataset metadata. **All Metadata** can expand the displayed records together.
4. Read the dataset name, campaign, processing stage, detector, event count and available configuration information.
5. Inspect the recorded file location and check whether it identifies the required output. A catalogue entry alone does not establish that the files are accessible or validated.
6. Copy the displayed **UUID** and keep the dataset name and campaign with it. These identify the catalogue record and help distinguish samples with similar names.

Before creating a record, search for the same sample and configuration to avoid duplicates.

## 3. Prepare the publication information

The MC contact inserts datasets into DaMI manually through the interface or with a script. **Insert a real dataset only after it has passed validation.** Check the output files, event statistics and required physics or technical criteria, and retain the validation reference with the production information.

| Information | What the contact should check |
| --- | --- |
| Dataset name and categories | Agreed name, accelerator, processing stage, campaign, detector and file type. Reuse the agreed category spellings. |
| Physics definition | Process, collision energy, relevant filters, generator settings and purpose. |
| Configuration | Generator and detector/card revisions, software release and relevant production settings. |
| Delivered statistics | Actual usable event count. Distinguish requested, generated and accepted events where relevant. |
| Normalisation | Cross section, efficiency or weights required by the analysis, including their definitions and units. |
| File location | The actual location or file-list reference, with access checked using the agreed analysis environment. |
| People responsible | The requester and the MC Production contact. |
| Production traceability | Original DRS request, transformation IDs labelled by process and step, and validation reference. |
| Limitations | Incomplete statistics, known issues and the intended use of the sample. |

The campaign metadata fields will be discussed during the training, including the requester and MC contact. After the discussion, replace the table above with the agreed list of metadata fields required for the campaign, including their names, definitions and units. DaMI supports fields such as `n-events`, `path`, `size`, `description`, `comment` and `status`, and permits additional metadata. Completing the form does not establish that the dataset passed validation.

## 4. Add a dataset

### One dataset through the form

1. Sign in with editor or administrator access.
2. Select **Add Data** to open **Dataset Tools**. On a narrow screen, this control may appear as an icon.
3. Select **Add Dataset**.
4. Enter **Dataset Name** and fill all the displayed category fields. The form allows existing values or new text. Use the agreed values, because new spellings can create new categories.
5. Enter the agreed extra information in **Metadata (optional JSON object)**. Keep the dataset name and category fields in their dedicated controls.
6. Review the information, then select **Create Dataset**.
7. Check the result message, close the dialog and find the new record. Expand it and verify its metadata and UUID.

Creating the record adds metadata to the catalogue. It does not run a production, transfer physics files or validate the sample. The MC contact is responsible for inserting the validated dataset, either through the interface or using a script following the agreed campaign conventions.

### Several datasets from JSON

Use this route with metadata prepared by the MC contact for datasets that have passed validation:

1. Open **Add Data**, then **Bulk Upload (JSON)**.
2. Select **Select JSON File**. The file must contain an object with a `datasets` array.
3. Leave **Force Override Locked Fields** unchecked for the training.
4. Select **Upload Datasets** and inspect the counts of created, updated and failed records, together with any lock conflicts.
5. Search for each affected dataset and verify the resulting metadata. Entries are processed independently, so a batch can succeed only in part.

An entry without a `uuid` follows the creation route. An entry with a `uuid` targets an existing record and updates its metadata. The update route protects the record's name and category fields and fails if the UUID does not exist. Retain the UUID when updating a record exported from DaMI. Removing it changes the operation to creation.

The exported JSON shape is suitable for the application's import workflow, but review the file before uploading it. A bulk import is a write operation, even when the file originally came from a download.

## 5. Edit an existing record

1. Locate the agreed dataset and expand its metadata.
2. Note its UUID and retain a copy of the existing metadata, for example by exporting that record.
3. Select **Edit**, make the agreed change in the JSON editor and select **Save changes**. Use **Cancel** to discard an unfinished edit.
4. Reload the record and verify that the intended change persists.

Metadata fields can be locked to protect values from later updates. Review a lock conflict with the responsible editor instead of using force override as a routine fix. Changing a stored event count, file path or normalisation value requires checking the corresponding production information.

For the exercise, change only the comment on a designated test record. Dataset deletion is outside the participant exercise.

## 6. Export metadata and hand the sample to an analyst

Select the record's checkbox, open **Actions**, then choose **Download Selected**. **Download All Matching** exports all results matching the current filters, so check the filters before using it.

These actions download dataset metadata as JSON. Obtain the physics event files through the storage location and access method agreed for the production.

The handover to the requester should include:

- Dataset name, campaign and catalogue UUID.
- The full EOS path to the dataset, checked for access.
- Processing stage, event-data format and configuration/software reference.
- Delivered statistics, normalisation information and validation limitations.
- The requester and the MC contact responsible for the sample.

Record the catalogue reference in the original DRS request and tell the requester how to use the output. Follow the agreed DRS completion procedure once the required checks and handover are complete.

## 7. Using the sample in FCCAnalyses

For the current central productions, obtain the output path as follows:

1. In the [iLCDirac web portal](https://voilcdiracwebapp2.cern.ch/DIRAC/), right-click the relevant transformation and open its details.
2. Copy its logical file name (LFN) for the output location.
3. Prepend `/eos/experiment/fcc/prod` to that LFN to obtain the full EOS path. For example:

| Transformation LFN | Full EOS path |
| --- | --- |
| `/fcc/ee/summer2026/240gev/ZH/IDEA/delphes/...` | `/eos/experiment/fcc/prod/fcc/ee/summer2026/240gev/ZH/IDEA/delphes/...` |

The `...` represents the remaining path components. Copy the complete actual LFN. For now, the MC contact inserts the resulting full EOS path into DaMI's `path` metadata by hand and checks file access. Historical datasets can use different storage layouts; keep their actual recorded paths.

Use the dataset by providing its **full path on EOS** to your FCCAnalyses analysis. Copy the path from the validated catalogue record and check that you can access the files in your analysis environment. DaMI metadata downloads contain catalogue information; the event files are accessed at the recorded location.

Distributed-computing capabilities are still evolving. An API is planned for programmatic access; instructions for using it will be added when it is available.

## 8. Practical exercise

Estimated time: 10 minutes. Use the instance and reference dataset identified by the instructors.

1. Find the reference dataset and record its name, campaign, stage, detector, event count and UUID.
2. Identify its full EOS path, validation reference, requester and MC contact. Note any information that is missing.
3. Export only that dataset using **Download Selected**. Inspect the JSON and identify the UUID and metadata fields.
4. If the instructors assign you a validated sample that is not yet catalogued, add its actual metadata with **Add Dataset** using the agreed fields and categories. Search first to avoid duplicating an existing record. Otherwise, follow the creation demonstration without adding another record.
5. On a record assigned to you for editing, make the agreed comment change, save and reload. Leave other records unchanged.
6. Explain what validation evidence and metadata are needed before a new dataset can be published.

Discuss your answers with the instructors. With viewer access, complete the inspection and export steps while editor access is being assigned. Follow the instructors' directions for cleanup of any training entries.

## Help and sources

For production questions, use the [FCCSW Distributed Computing forum](https://fccsw-forum.web.cern.ch/c/distributed-computing/12) or contact [MC production support](mailto:fcc-ped-softwareandcomputing-mcproduction@cern.ch). Report application problems through [DaMI issues](https://github.com/HEP-FCC/fcc-physics-events/issues), including the action, dataset reference and error message.

Version references for this guide:

- DaMI [`d04fee4`](https://github.com/HEP-FCC/fcc-physics-events/tree/d04fee42070c388ea00231a628abe6e9855af161): [creation and import controls](https://github.com/HEP-FCC/fcc-physics-events/blob/d04fee42070c388ea00231a628abe6e9855af161/frontend/components/EditModal.vue), [upload and export behaviour](https://github.com/HEP-FCC/fcc-physics-events/blob/d04fee42070c388ea00231a628abe6e9855af161/backend/app/routers/entities_router.py), [metadata model](https://github.com/HEP-FCC/fcc-physics-events/blob/d04fee42070c388ea00231a628abe6e9855af161/backend/app/storage/json_data_model.py), [role checks](https://github.com/HEP-FCC/fcc-physics-events/blob/d04fee42070c388ea00231a628abe6e9855af161/backend/app/utils/auth_utils.py) and [editor administration](https://github.com/HEP-FCC/fcc-physics-events/blob/d04fee42070c388ea00231a628abe6e9855af161/frontend/components/UserManagementModal.vue).
