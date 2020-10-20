# WelcomeLite
A Basic CRUD Django App using:
PostgreSQL
Docker
Bootstrap

After cloning repo, to Run:
`make build`
`make compose-start`

*Note* 
- `JobOffer`s and `JobTitle`s are related and there has to be at least 1 `JobTitle` 
in order to create a `JobOffer`. 
- So after building and starting the app,
run `make compose-manage-py cmd="createsuperuser"`
- After creating a super user, you can login to `/admin` path and add records into `JobTitle`
table, while will auto-populate in the create job offer form.

*Testing*
Only one simple test has been addded into `tests.py` checking the index view;
if no job offers exist, an appropriate message is displayed.
Other tests for following endpoints could include, but are not limited to:
`addOffer/`
    - get request expects form with data fields & status code 200
    - posting incomplete/incorrect form data and expecting proper response 
        (frontend form validation active)
    - posting complete/correct form data and expecting proper response
`editOffer/<int:job_offer_id>/`
    - get request with invalid job offer id, expect status code 404 and proper response
    - get request with valid job offer id, expect 200 and form pre-populated with offer data
    - posting complete data with invalid job offer id, expect status code 404
    - posting incomplete/incorrect form data and expecting proper response 
        (frontend form validation active)
    - posting complete/correct form data and expecting proper response
`deleteOffer/<int:job_offer_id>/`
    - get request with invalid job offer id, expect redirect to index and proper response 
        (Job offer does not exist)
    - get request with valid job offer id, expect redirect to index with status code 200
        and proper response (Job offer successfully deleted)


Author: Harold Fich
License: MIT
