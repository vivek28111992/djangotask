This repository contains django task code & same is uploaded on heroku

GET Api to access projects details Heroku endpoint is https://djangotask.herokuapp.com/api/v1/

This api is filterable by project name, start date, end date & status

Example of Api: https://djangotask.herokuapp.com/api/v1/?start_date__gte=2017-10-01&end_date__lte=2018-11-01

This endpoint will get projects whose start date is greater than or equal to 2017-10-10 & end date is less than or equal to 2018-11-10

Another example of Api: https://djangotask.herokuapp.com/api/v1/?project_name=Hyperloop

This endpoint will filter using project name.

Both project name & other filterable parameter can also be used at same time in endpoint.
