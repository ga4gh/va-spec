# VA-Spec

See official Documentation at https://va-spec.ga4gh.org/en/latest.

**Administrative / Project Management Resources**:
  - [Github Issue Tracker](https://github.com/ga4gh/va-spec/issues)
  - [VA Google Group](https://groups.google.com/a/ga4gh.org/g/ga4gh-variant-annotation) - email list-serv for project communications
  - [GA4GH-VA Google Drive](https://docs.google.com/document/d/1pnwvYBl8GOMFUw4_-VseHPGWwaWw-kQkBvfZPQ331ME/edit#heading=h.9x8o4qogo9jq)  Other documents associated with this effort
  - [GA4GH VA Slack channel](https://ga4gh.slack.com/archives/CBGR3P1GR)

 *Contact beatrice.amos@ga4gh.org for access to the documents/systems above*

## Installing for development

Fork the repo at <https://github.com/ga4gh/va-spec>.

    git clone --recurse-submodules git@github.com:YOUR_GITHUB_ID/va-spec.git
    cd va-spec
    make devready
    source venv/3.12/bin/activate
    pre-commit install

If you already cloned the repo, but forgot to include `--recurse-submodules` you can run:

    git submodule update --init --recursive

## Contributing to the schema

VA-Spec uses the below `-source.yaml` files as the source document for JSON Schema:

- [./schema/va-spec/aac-2017/profile-source.yaml](./schema/va-spec/aac-2017/profile-source.yaml)
- [./schema/va-spec/acmg-2015/profile-source.yaml](./schema/va-spec/acmg-2015/profile-source.yaml)
- [./schema/va-spec/base/domain-entities-source.yaml](./schema/va-spec/base/domain-entities-source.yaml)
- [./schema/va-spec/base/va-core-source.yaml](./schema/va-spec/base/va-core-source.yaml)
- [./schema/va-spec/ccv-2022/profile-source.yaml](./schema/va-spec/ccv-2022/profile-source.yaml)

To create the corresponding def and JSON files after making changes to any one of the source documents, from the root directory:

    cd schema
    make clean
    make all

> **Note:** We have a custom pre-commit hook to run these commands after you stage a source document.

## Contributing to the docs

The VA-Spec documentation is written in reStructuredText and located in [docs/source](docs/source/). Commits to this repo are built automatically at <https://va-spec.ga4gh.org/en/latest/index.html>.

To build documentation locally, you must install [entr](https://eradman.com/entrproject/):

    brew install entr

Then from the root directory:

    cd docs
    make clean watch &

Then, open [docs/build/html/index.html](./docs/build/html/index.html). The above make
command should build docs when source changes. (Some types of changes require recleaning and building.)

## Testing

The VA-Spec repo contains tests to validate [examples](./tests/fixtures/) against
the current schema.

To run tests:

    make test
