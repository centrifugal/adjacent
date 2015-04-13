0.2.0
=====

Changes to reflect Centrifuge 0.8.0 changes

* `project_id` renamed to `key` when creating `Client` instance
* `secret_key` renamed to `secret` when creating `Client` instance
* rename `CENTRIFUGE_PROJECT_ID` setting to `CENTRIFUGE_PROJECT_KEY`

How to migrate:
~~~~~~~~~~~~~~~

* change kwargs names if you use `Client` from `adjacent`
* change `CENTRIFUGE_PROJECT_ID` setting name to `CENTRIFUGE_PROJECT_KEY`


0.1.0
=====

* use cent>=0.3.0 to work with Centrifuge>=0.7.0
* `user_info` kwarg in `get_connection_parameters` function renamed to `info`

0.0.5
=====

* Added `json_encoder` keyword argument to use custom JsonEncoder