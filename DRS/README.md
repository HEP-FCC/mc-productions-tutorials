# DRS: Dataset Request System

Speakers: Pantelis Kontaxakis and Juraj Smiesko  
Training of the MC Production contacts, Autumn 2026

The DRS records FCC dataset requests, their review and the references needed to follow their production.

- [Production DRS](https://fcc-drs.web.cern.ch/)
- [Test DRS](https://fcc-drs-test.web.cern.ch/)
- [Overall workflow and contact responsibilities](workflow-and-responsibilities.md)

**For the practical session:** use the instance and demonstration request identified by the instructor. The exercise also works as a worksheet without changing a request. The public source lists the test instance, but its availability and deployed version must be checked before the session.

These instructions follow DRS source commit [`ceaab4a`](https://github.com/HEP-FCC/fcc-drs/tree/ceaab4ab98d478458d559730ccebd299c693c6f8), checked on 19 October 2026. The live interface has not been verified for this draft.

## 1. Access and role

1. Open the agreed DRS instance and use **Login** with CERN SSO.
2. Open **Requests**. A first login normally creates a **requester** account.
3. Ask a DRS administrator to confirm your **coordinator** role and membership of the appropriate coordinator group for your MC-contact duties.
4. On the demonstration request, check that the coordinator controls are available. The **Campaigns** navigation item is also available to coordinators.
5. Check your profile notification preferences and the coordinator group shown on the request. Email delivery also depends on the service configuration.

| DRS role | Relevant capabilities |
| --- | --- |
| Requester | Create requests, view requests, comment, and edit their own request while it is Draft or Under Review. |
| Coordinator | Review and edit requests, record approval decisions, adjust priority/status and group/campaign assignment, add production IDs and use internal notes. |
| Admin | Coordinator capabilities plus user-role, coordinator-group and campaign administration. |

In the inspected source, coordinator powers apply across requests. A **Coordinator Group** assignment organises responsibility and notifications; it does not restrict the coordinator role to that group's requests. Work on the requests agreed with your group and the organisers.

DRS permissions are separate from FCC VO membership, iLCDirac production permissions and DaMI editing rights.

## 2. Find an existing request first

Open **Requests** and use the search and status/priority filters. Look for the same process, energy, detector and sample purpose before creating another request. Open a request to read its description, generator cards, related requests and activity.

For an existing need, discuss whether to reuse the request, extend the statistics or create a genuinely different configuration. The **Related Requests** control supports **Extends**, **Depends on**, **Variant of** and **Related to**. A reference such as `#123` in description or notes can also create a mention relation.

There is no dedicated duplicate status in this source version. If a request duplicates another, agree which record to retain, link the records and explain the resolution in a comment. Use the agreed status for the redundant request rather than silently removing its history.

## 3. Understand and create a request

Select **New Request**. CERN SSO supplies the requester identity.

| Form label | What to enter or check |
| --- | --- |
| Title | A short description that distinguishes the sample. Include process, energy and purpose where helpful. |
| Description | Physics process, collision energy and beams, generator/version, relevant radiation and decay settings, filters, purpose and configuration references. There are no separate process, energy or generator fields in this form. |
| Group / Team | The group responsible for the request. Verify the resulting **Coordinator Group** on the detail page. |
| Use Case | The intended use, for example Physics Analysis or Reconstruction Development. |
| Final Processing Stage | Generation, Simulation, Delphes, Reconstruction or Other. State the desired final output and any required intermediate products in the description. |
| Format | The requested format, for example EDM4hep or HepMC3. It must be compatible with the requested processing. |
| Detector(s) | Required by the form for stages beyond Generation. Give the concept and identify the relevant configuration precisely. |
| Statistics | The requested event count. Say whether it is before or after a filter, and specify counts per energy point or configuration where needed. |
| Estimated Size | An estimate with units and its basis. Update it using the validation sample when possible. |
| Target Campaign | A requested campaign preference, entered as text. Actual assignment uses the separate **Campaign** control after review. |
| Key4hep Stack | The exact release agreed for the production. Resolve this before launching. |
| Due Date and Priority | The useful delivery date and its reason. Priorities available are Low, Medium, High and Critical. Agree relative priority with the responsible people. |
| Generator Cards | Upload the relevant plain-text configuration files. The interface states a limit of 1 MB per file. Verify that every intended file appears after upload. |
| Notes / Tags | Additional context and useful search labels. Use the explicit internal-comment option for coordinator-only discussion. |

Use **Save as Draft** while information is incomplete. A draft still needs a title. Use **Submit Request** when the request is ready for review. The source labels the submitted state **Under Review**.

The submission form requires the description, group, use case, final stage, format, statistics and estimated size, plus detector information for stages beyond Generation. Required form fields are a minimum. A runnable production also needs sufficiently precise configuration and validation.

On the request detail page, edit the relevant sections to correct or clarify the specification. Under **Generator Cards**, use **Choose file…** and **Upload** to attach a card, or select an existing filename to inspect it. Record an immutable configuration reference, such as a commit, when available.

## 4. Review and discuss

Read the full request and check:

- Is the sample needed, and can an existing sample cover it?
- Are the process, collision conditions, requested output and event count unambiguous?
- Are the generator card, detector configuration and software release identified?
- Are the size and timescale plausible, and is a pilot benchmark needed?
- Who must agree the physics and resources decisions?

Use **Add a comment…** and **Comment** to ask the requester for clarification. Leave **Internal (coordinators only)** unchecked for a question the requester should see. Internal notes are suitable for coordinator discussion.

Keep a request **Under Review** while clarifications or decisions are pending. In the detail page, coordinators can adjust **Coordinator Group** and **Priority** when the responsible people agree the change.

## 5. Approvals and request status

The request has separate **Physics** and **Resources** approval rows. Each row offers **Approve**, **Reject** or, once a decision exists, **Revert**.

The interface gives coordinators access to both rows. The organisers must agree who is authorised to record each decision. Possessing the button is not itself an assignment of physics or resource responsibility.

| State or action | Behaviour in the inspected source |
| --- | --- |
| Save as Draft | Keeps an initial request in Draft. |
| Submit Request | Moves the draft into Under Review, once the required information is present. |
| Both approvals granted while Under Review | Automatically changes the request to Approved. |
| Either approval rejected while Under Review | Automatically changes the request to Rejected. |
| Revert an approval | Clears that approval. From Approved, Rejected, In Progress or Completed, it also returns the request to Under Review. |
| Assign an Approved request to a campaign | Automatically changes the request to In Progress. |
| Completed, Failed or Cancelled | Available status labels for recording the agreed outcome. |

Coordinators also have a status selector. The source permits manual changes, including exceptions to the normal approval sequence. Teach the approval rows as the normal review procedure and record the reason for an exceptional change. A status label alone does not prove that both approval records are present.

**In Progress can mean that the request has entered a campaign. Check iLCDirac to determine whether jobs have actually been submitted or are running.**

## 6. Campaign assignment and production references

After the approvals and campaign placement have been agreed:

1. Find **Campaign** on the request detail page.
2. Select the agreed campaign and read the confirmation before applying it. The normal entry point is an Approved request. Assignments belonging to a closed campaign are locked.
3. Check the campaign name, request status and activity record.
4. Follow the [iLCDirac tutorial](../iLCDirac/README.md) to prepare, validate and launch the actual production.
5. When the production system supplies identifiers, return to the request. **Production IDs** appears when a campaign is assigned.
6. Enter the real positive numeric identifier, add a label explaining its role and select **Add**. Follow the identifier convention agreed with Juraj for the production/transformation workflow.
7. Add a comment linking the configuration revision and useful monitoring or validation information.

Entering a production ID stores a reference in the DRS. It does not create the corresponding production. A DRS request number and a job number identify different objects and should be labelled accordingly.

## 7. Completion and publication

The recommended completion check is to confirm the agreed output statistics, file accessibility and validation, then record the dataset reference and any limitations. Follow the [DaMI tutorial](../DaMI/README.md) for publication. Tell the requester where to find the output and record **Completed** according to the agreed campaign procedure.

For a failed or interrupted production, record the relevant identifiers and useful error context. Agree whether the next action is a retry, a revised configuration or a change to the request.

## 8. Practical exercise

Work through [the request-review exercise](exercise.md). The exercise uses an illustrative physics request and does not supply a validated production recipe. Discuss your proposed clarifications and next steps with the instructors during the debrief.

## Help and sources

- Questions about a production: [FCCSW Distributed Computing forum](https://fccsw-forum.web.cern.ch/c/distributed-computing/12) or [MC production support](mailto:fcc-ped-softwareandcomputing-mcproduction@cern.ch).
- DRS application problems: [FCC-DRS issues](https://github.com/HEP-FCC/fcc-drs/issues).
- Source for [form labels](https://github.com/HEP-FCC/fcc-drs/blob/ceaab4ab98d478458d559730ccebd299c693c6f8/templates/partials/request_form.html), [roles and protected actions](https://github.com/HEP-FCC/fcc-drs/blob/ceaab4ab98d478458d559730ccebd299c693c6f8/cmd/fcc-drs/main.go), [approval behaviour](https://github.com/HEP-FCC/fcc-drs/blob/ceaab4ab98d478458d559730ccebd299c693c6f8/internal/handlers/handlers.go), [campaign behaviour](https://github.com/HEP-FCC/fcc-drs/blob/ceaab4ab98d478458d559730ccebd299c693c6f8/internal/handlers/pipeline.go) and [production-ID recording](https://github.com/HEP-FCC/fcc-drs/blob/ceaab4ab98d478458d559730ccebd299c693c6f8/internal/handlers/production_ids.go).
