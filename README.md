# Finance-Tracking-System (Preliminary Right Up)
<p>&nbsp;&nbsp;&nbsp;&nbsp;As a college student, one of the struggles I face is finding time to track and categorize my expenses
in a format where I can easily identify areas to improve my financial situation. This program is designed
to assist in keeping track of expenses in an easily digestible format. Currently, there are four planned phases 
in this project. Phase I is to create an internal structure that will turn into a CSV file. Phase II will allow for 
verified inputs through REGEX to be inputted into the CSV file. Phase III will then be API implementation to
upload the data into google sheets. Phase IV will create allow the user to text a number to have the data uploaded 
into google sheets automatically.</p>
<p>System Requirements:
  <ul>
    <li>Programming Language: Python [P1]</li>
    <li>Required Knowledge:</li>
      <ul>
        <li>Python</li>
        <li>CSV/Excel formatting</li>
        <li>REGEX</li>
        <li>Google Sheets API</li>
        <li>Sending and receiving SMS with Python</li>
    </ul>
    </ul>
</p>
<p>Constraints:
<p>&nbsp;&nbsp;&nbsp;&nbsp;Practical inexperience will cause a problem when trying to utilize API and SMS using python.</p></p>

# Phase 1: Internal Structure

<p>
The FTS system will first use a python structure to process data into an existing CSV file. This will be done by a class that
  will solely handle information that can mutate the CSV file. It is important to note that all inputs are excepted to follow the 
  format below. Any input not specified will return a -1 and no change will occur to the CSV. Inputs that meet the specified requirements 
  will return a 1.</p>
[NAME (STRING)] [COST (INT)] 

# Phase 2: Line Authentication

<p>
The FTS system will have a separate class for line authentication to ensure inputs to the internal structure are correctly formatted. 
  This class will be using regular expressions to verify inputs. The regular expression used to check to format is below.
</p>

```bash
 REGULAR_EXPRESSION = r"^fts_dat(\(\d?\d?\))?.csv$"
```
# Phase 3: GSheets API Implementation
	
  <p>Future concept</p>

Resources
<ul>
  <li>https://hevodata.com/learn/python-connect-to-google-sheets/</li>
  <li>https://blog.coupler.io/python-to-google-sheets/</li>
  <li>https://github.com/googleapis/google-api-python-client</li>
</ul>

# Phase 3.5: GSheets User Readability Formatting
	
  <p>Future concept</p>

# Phase 4: Text to Sheets

  <p>Future concept</p>
Resources
<ul>
  <li>https://www.bandwidth.com/blog/make-a-call-python-send-sms-python/</li>
</ul> 

# Future Developments:
Using machine learning to read receipts, allow users to take a picture of the receipt and have the data uploaded from the photo. 
