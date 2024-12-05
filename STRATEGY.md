# Overall

After the initial assesment it became apparent that business logic itself is rather simple, but
the the service has non-functional authentication and many problems in validating the input data,
so the testing effort was focused on validating the input/output data schema and value constrains.

# The tooling

In case of many endpoints, probably an full-scale API-client could be considered, but in this case a simple
HTTP [request library](https://pypi.org/project/requests/) would suffice.

To ease validation of the declarative schema, the [schema library](https://pypi.org/project/schema/) was used.
Although due to high number of schema bugs proved less useful at the moment, may become much more useful to
validate the messages schema and constrains contract after fixing the bugs.

To improve test and test results readability, the combination of Python de-facto standard [pytest](https://pypi.org/project/pytest/) and
[spec-style plugin](https://pypi.org/project/pytest-describe/) was chosen.

To ensure code quality and standard formatting, high-performan linter and formatter [ruff](https://pypi.org/project/ruff/) was chosen.

# The quality of spec

It looks like the provided openapi document is far from being a complete and comprehensive openapi specification.
Though it is out of the scope of the assignment, specification validation may be used to discover the problems in the
specification itself (e.g. https://openapi.tools/#description-validators)

# Typical bugs

Majority of the discovered bugs are due to differences in handling `x-www-form-urlencoded` and JSON payloads,
the differences not only arised on transport layer due to different typed data serialization in JSON and URL encoding,
but also affected the actual response, suggesting that differences may go deep into implented logic.
Thus all test are executed twice for both input payload type (and results do differ!)

The field types and values validation is also very incomplete.

API randomly responses with Internal Server Error.

An error in business logic, as simple as it is, was also discovered - discount is ignored.

Authorization is pretty much ignored as well.

# Grouping the tests

All tests are divided in 4 suites:
* authentication testing
* business logic testing
* response schema validation
* the biggest and the buggiest: request schema validation

The failed test are marked as intentionally failing and linked to respective bug report.

Nice to have:
Performance testing or parallel user scenarios would be nice in future, but probably won't make sense 
in the present state of the service.

