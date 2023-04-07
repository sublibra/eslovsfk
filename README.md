# eslovsfk
Short hack to get the calendar from idrottonline and push it to an external storage

# How to run

* Install packages `pip ...`
* Rename the `.env-template` to `.env` and fill in username and password to idrottonline and the sftp for the calendar to end up in
* Run the script using `python get-calendar.py`
* Optional: Schedule updates using a cron job running the fetch, i.e. `0 0,12,18 * * * python get-calendar.py`

# Additional notes

* Firefox is used in the example but chromium worked better in a 32 bit raspberry. Adapt the script accordingly
* Download folder varies - can possibly be configured (TODO)
