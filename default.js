define({
    //Default configuration settings for the applciation. This is where you"ll define things like a bing maps key,
    //default web map, default app color theme and more. These values can be overwritten by template configuration settings
    //and url parameters.
    "appid": "",
    "webmap": "31bfda7f16044265a18b23afdb080981",
    "form_layer": {
        "id": ""
    },
    "details": {
        "Title": "RTCA Data Entry Form",
        "Logo": "https://www.nps.gov/common/uploads/organizations/nri/organization/rtca/6E1FB8A3-155D-4519-3EEB94864D134084/6E1FB8A3-155D-4519-3EEB94864D134084.jpg",
        "Description": ""
    },
    "fields": {
      "RTCA_Project_3023": [{
        "name": "Project_Name", // field ID
        "alias": "Project Name", // label
        "fieldDescription": "Use a name that is descriptive of the project and will be recognized by our partners, using the geographical place name as the first word - the name of the ridge, river, city, canal, etc. (e.g. Cahaba River Watershed Protection, Odgen's East Bench Trail, Texas State Trail Network).  If a place name is not part of the project name used by our cooperator and including it might create confusion, put it in parentheses, (e.g. (San Francisco) Bay Area Ridge Trail). Name should focus on the outcome, not the output.  Avoid using the words “plan” or “project” in the name. (* field published on RTCA State Pages).", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "NPS_Program", // field ID
        "alias": "NPS Program", // label
        "fieldDescription": "Choose a NPS program type that relates to a subset of RTCA’s work.  These subset NPS Programs include Challenge Cost Share, Groundwork, Special Initiative, Community of Practice, Training, or Program Development.  If this is a regular RTCA project, just choose “Rivers, Trail and Conservation Assistance”.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Strategic_Goal", // field ID
        "alias": "Primary Strategic Goal", // label
        "fieldDescription": "Choose the Strategic Goal of the RTCA Program that best determines the overall initiative a project and meets project criteria and the RTCA strategic plan.  This attribute will be used to assist WASO in responding to public or Congressional inquiries about the project.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Secondary_Strategic_Goal", // field ID
        "alias": "Secondary Strategic Goal", // label
        "fieldDescription": "If available, choose a secondary Strategic Goal.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Strategic_Goal_IfOtherExplain", // field ID
        "alias": "Strategic Goal - If Other Explain", // label
        "fieldDescription": "Write in another strategic goal that if it is missing from the Strategic Goal attribute.  If a trend starts to appear of a missing Strategic Goal type, it will be added to the drop down list during database updates.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Anticipated_Outcome", // field ID
        "alias": "Primary Anticipated Outcome", // label
        "fieldDescription": "The anticipated conservation success (es) that will be achieved in the long-term; the final outcome of project beyond our RTCA involvement.    An outcome is not a plan or a meeting; it is an on-the-ground conservation success – a trail or park created, a river conserved, etc. This attribute will be used to assist WASO in responding to public or Congressional inquiries about the project.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Secondary_Anticipated_Outcome", // field ID
        "alias": "Secondary Anticipated Outcome", // label
        "fieldDescription": "If available, choose a secondary Anticipated Outcome.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Anticipated_IfOtherExplain", // field ID
        "alias": "Anticipated Outcome - If Other Explain", // label
        "fieldDescription": "Write in another anticipated outcome if it is missing from the Anticipated Outcome selection above.  If a trend starts to appear of a missing Anticipated Outcome, it will be added to the drop down list during database updates.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Project_Goal", // field ID
        "alias": "Project Goal", // label
        "fieldDescription": "Briefly state the project goal.  A project goal might be to achieve consensus in a community about the need for a trail along the such-and-such river or to create an organization that will assure the conservation of the such-and-such river.  A sentence or two should do.  The Project Goal narrative must start as “The project goal is to…”.  Writing this narrative as such, will provide consistency when producing text for the RTCA State Pages.  This attribute will be used to assist WASO in responding to public or Congressional inquiries about the project, include commitments made to the project by other cooperators and other information that might be useful in responding to such inquiries.  (* field published on RTCA State Pages)", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "textarea" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "NPS_Role_Category", // field ID
        "alias": "Primary NPS Role Category", // label
        "fieldDescription": "Choose the NPS’s general role in the project.  This attribute will be used to assist WASO in responding to public or Congressional inquiries about the project.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Secondary_NPS_Role_Category", // field ID
        "alias": "Secondary NPS Role Category", // label
        "fieldDescription": "If available, choose a secondary NPS Role Category.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "NPSRoleCat_IfOtherExplain", // field ID
        "alias": "NPS Role Category - If Other Explain", // label
        "fieldDescription": "Write in another NPS role category if it is missing from the NPS Role Category selection above.  If a trend starts to appear of a missing NPS role, it will be added to the drop down list during database updates.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "NPS_Role_Narrative", // field ID
        "alias": "NPS Role Narrative", // label
        "fieldDescription": "Briefly state the NPS role for the project.  The narrative must begin as “The National Park Service will…”.  Writing this narrative as such, will provide consistency when producing text for the RTCA State Pages.  (* field published on RTCA State Pages)", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "textarea" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Project_Status", // field ID
        "alias": "Project Status", // label
        "fieldDescription": "Choose the current status of the project.  Options include new, continuing, finished, or dropped.  This attribute can be updated at a later date.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Fiscal_Year_Start", // field ID
        "alias": "Fiscal Year Start", // label
        "fieldDescription": "Enter the starting year of a project.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Fiscal_Year_End", // field ID
        "alias": "Fiscal Year End", // label
        "fieldDescription": "Enter ending year of a project.  This attribute can be updated at a later date.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "NPS_Regional_Office", // field ID
        "alias": "NPS Regional Office", // label
        "fieldDescription": "Enter the regional office that is responsible for a project.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "NPS_Project_Manager", // field ID
        "alias": "NPS Project Manager", // label
        "fieldDescription": "Enter the name of the primary NPS staff contact who is the manager for the project.  (* field published on RTCA State Pages)", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "NPS_Project_Manager_Email", // field ID
        "alias": "NPS Project Manager Email", // label
        "fieldDescription": "Enter the project manager’s government email address.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "email" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "NPS_Project_Team_Members", // field ID
        "alias": "NPS Project Team Members", // label
        "fieldDescription": "Enter additional NPS (RTCA) staff members who are participating in a project.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Project_Location_City_Town", // field ID
        "alias": "Project Location - City or Town", // label
        "fieldDescription": "Enter the primary city(s) / town(s) where the project is taking place.  If there are many cities or towns, enter the key places as you deem appropriate.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Project_Location_State", // field ID
        "alias": "Project Location - State", // label
        "fieldDescription": "Choose the primary state the project is taking place.  If the project goes across multiple states, choose “Multiple States”.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Project_Location_Zipcodes", // field ID
        "alias": "Project Location - Zipcodes", // label
        "fieldDescription": "Enter the zipcode central to the project.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Project_Location_Description", // field ID
        "alias": "Project Location - Description", // label
        "fieldDescription": "Enter a brief description of project location (*field published on RTCA website).", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "textarea" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "ApplicantOrganization", // field ID
        "alias": "Applicant - Name of Organization", // label
        "fieldDescription": "Enter the full name of the principal nonprofit organization or State or local government agency cooperating in the project.  This organization will be contacted for the GPRA customer satisfaction survey at the end of the year.  Since our GPRA goal requires us to measure satisfaction of nonprofits and State or local government agencies only, do not list a for-profit or Federal agency here.  (*field published on website)", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "ApplicantContactName", // field ID
        "alias": "Applicant - Contact Name", // label
        "fieldDescription": "Enter the name of primary applicant., mailing address, city, state, zip, phone number, and email address for primary cooperator. This is the person who will receive the annual satisfaction survey called for by GPRA, therefore it is critical to keep this email address current.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "ApplicantTelephoneNumber", // field ID
        "alias": "Applicant - Telephone Number", // label
        "fieldDescription": "Enter the telephone number of the primary applicant.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "ApplicantEmail", // field ID
        "alias": "Applicant - Email", // label
        "fieldDescription": "Enter the email address of primary applicant.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "email" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "ApplicantMailingAddress", // field ID
        "alias": "Applicant - Mailing Address", // label
        "fieldDescription": "Enter the mailing address of primary applicant.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "ApplicantCity", // field ID
        "alias": "Applicant - City", // label
        "fieldDescription": "Enter the city of primary applicant.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "ApplicantState", // field ID
        "alias": "Applicant - State", // label
        "fieldDescription": "Enter the state of primary applicant.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "ApplicantZip", // field ID
        "alias": "Applicant - Zipcode", // label
        "fieldDescription": "Enter the zipcode of primary applicant.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "ApplicantWebsite", // field ID
        "alias": "Applicant - Website", // label
        "fieldDescription": "Enter the website of primary applicant.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "url" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "AssociatedPartnersOrganization", // field ID
        "alias": "Associated Partners - Name of Organization", // label
        "fieldDescription": "Enter the organization name(s) that are important to the success of the local project and those associated with this project that might be important and have the opportunity to carry the national program message to any of the key audience – internal and/or external.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "textarea" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "AssociatedPartnersContactName", // field ID
        "alias": "Associated Partners - Contact Name", // label
        "fieldDescription": "Enter contact name(s) for the associated partners.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "textarea" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "AssociatedPartnersEmail", // field ID
        "alias": "Associated Partners - Email", // label
        "fieldDescription": "Enter the email address(s) of associated partners.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "textarea" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "NationalCopName", // field ID
        "alias": "National Cooperator - Name of Organization", // label
        "fieldDescription": "Using the drop-down list identify the national cooperator with significant involvement, that is the cooperator is (or soon will be) aware of the project; is (or can be expected to be) involved in it (committing the equivalent of a day or more of staff time); and supports its anticipated outcome.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Secondary_National_Cooperator", // field ID
        "alias": "Secondary National Cooperator", // label
        "fieldDescription": "If available, choose a secondary National Cooperator.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "NatCooperatorOrg_IfOtherExplain", // field ID
        "alias": "National Cooperator - If Other Explain", // label
        "fieldDescription": "Provides the opportunity to write in another National Cooperator that is missing from the National Cooperator – Name of Organization selection above.  If a trend starts to appear of a missing National Cooperator, it will be added to the drop down list during database updates.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "textarea" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "NationalCopContactName", // field ID
        "alias": "National Cooperator - Contact Name", // label
        "fieldDescription": "Enter the point of contact for the National Cooperator.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "textarea" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "NationalCopEmail", // field ID
        "alias": "National Cooperator - Email", // label
        "fieldDescription": "Enter the National Cooperator contact’s email address.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "textarea" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "NPS_Unit_Name", // field ID
        "alias": "Primary NPS Unit Name", // label
        "fieldDescription": "Using the drop-down list identify the NPS Unit with significant involvement, is (or soon will be) aware of the project; is (or can be expected to be) involved in it (committing the equivalent of a day or more of staff time); and supports its anticipated outcome.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Secondary_NPS_Unit", // field ID
        "alias": "Secondary NPS Unit Name", // label
        "fieldDescription": "If available, choose a secondary NPS Unit.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Project_Website", // field ID
        "alias": "Project Website", // label
        "fieldDescription": "The website may or may not be directly relate to RTCA project, but should give a sense of cooperator’s mission and goals.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "email" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Trail_Miles", // field ID
        "alias": "Trail Miles", // label
        "fieldDescription": "Provide the total trail length associated with this project, in miles.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "River_Miles", // field ID
        "alias": "River Miles", // label
        "fieldDescription": "Provide the total river length associated with this project, in miles.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Park_Open_Space_Acres", // field ID
        "alias": "Park Open Space Acres", // label
        "fieldDescription": "Provide the total park open spaces associated with this project, in acres.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Partner_Next_Steps", // field ID
        "alias": "Partner Next Steps", // label
        "fieldDescription": "Provide the next steps for the partner associated with this project.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "ProjectApplicationAttachment", // field ID
        "alias": "Project Application - Attachment", // label
        "fieldDescription": "Choose whether or not a project application is attached.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Project_Agreement_Attachment", // field ID
        "alias": "Project Agreement - Attachment", // label
        "fieldDescription": "Choose whether or not a project agreement is attached.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "ProjectWorkPlanAttachment", // field ID
        "alias": "Project Work Plan - Attachment", // label
        "fieldDescription": "Choose whether or not a project work plan is attached.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Photo_Attachment", // field ID
        "alias": "Photo - Attachment", // label
        "fieldDescription": "Choose whether or not a project photo is attached.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "PhotoCaptionCreditAttachment", // field ID
        "alias": "Photo Caption Credit - Attachment", // label
        "fieldDescription": "If a photo is attached, also attach a word document that states the photo caption and credit (if other the NPS photo) associated with the attached photo.  Providing a photo caption and credit will assist in creating the RTCA State Pages by ensuring Section 508 compliancy for public webpages.  (*field published on website)", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "SuccessStory_Attachment", // field ID
        "alias": "Success Story - Attachment", // label
        "fieldDescription": "Choose whether or not any success story is attached.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      },
      {
        "name": "Other_Attachment", // field ID
        "alias": "Other - Attachment", // label
        "fieldDescription": "Choose whether or not any “other” type of project document is attached.", // help text
        "visible": true, // show this field?
        "typeField": false, // subtype field?
        "tooltip": "", // placeholder text
        "displayType": "text" // text, checkbox, radio, textarea, url, email
      }]
    },
    "theme": "journal", // see values in themes.js
    "oauthappid": null,
    //Enter the url to the proxy if needed by the applcation. See the "Using the proxy page" help topic for details
    // //developers.arcgis.com/en/javascript/jshelp/ags_proxy.html
    //esriConfig.defaults.io.proxyUrl = "http://rtca.cnr.ncsu.edu/DotNet/"
    //esriConfig.defaults.io.alwaysUseProxy = true;
    // "proxyurl": "http://rtca.cnr.ncsu.edu/DotNet/",
    //Example of a template specific property. If your template had several color schemes
    //you could define the default here and setup configuration settings to allow users to choose a different
    //color theme.
    //Enter the url to your organizations bing maps key if you want to use bing basemaps
    "bingmapskey": "",
    //Defaults to arcgis.com. Set this value to your portal or organization host name.
    "sharinghost": "https://www.arcgis.com",
    "units": null,
    "useSmallHeader": true,
    "enableSharing": true,
    "defaultMapExtent": true,
    "pushpinColor": "red",
    "nextBasemap": "hybrid",
    "defaultBasemap": "topo",
    "selectedTitleField": {},
    "disableViewer": true,
    "enableAttachments": true,
    "attachmentIsRequired": true,
    "attachmentLabel": "hello",
    "attachmentHelpText": "hello",
    "showLayer": true,
    "disableLogo": false,
    "enableBasemapToggle": false,
    "enableOfflineSupport": true,
    "locate":false,
    "locationSearchOptions": {
        "enableMyLocation": true,
        "enableSearch": true,
        "enableLatLng": true,
        "enableUSNG": false,
        "enableMGRS": false,
        "enableUTM": false
    },
    "locationSearch": true,
    //When searchExtent is true the locator will prioritize results within the current map extent.
    "searchExtent": false,
    "searchLayers":[{
        "id": "",
        "fields": []
    }],
    "attachmentInfo":{
      "RTCA_Project_3023": {
        "enableAttachments": true,
        "attachmentIsRequired": false,
        "attachmentLabel": "Attachments",
        "attachmentHelpText": ""
      }
    },
    "submitButtonText": "",
    "viewSubmissionsText": "",
    "helperServices": {
        "geometry": {
            "url": null
        },
        "printTask": {
            "url": null
        },
        "elevationSync": {
            "url": null
        },
        "geocode": [{
            "url": null
        }]
    }
});
