# GitHub API Cheat Sheet [^document] <!-- omit in toc -->
[^document]: [Official document references](https://docs.github.com/en/graphql)

## Table of Content <!-- omit in toc -->
- [Authenticating to API](#authenticating-to-api)
- [Communicating with GraphQL API](#communicating-with-graphql-api)
  - [GraphQL API endpoint](#graphql-api-endpoint)
  - [Queries](#queries)
  - [Mutations](#mutations)
  - [Variables](#variables)
- [Using on GitHub Actions](#using-on-github-actions)


## Authenticating to API
One way of authenticating to the API is to use a personal access token.
1. Under `Settings` > `Developer settings` > `Personal access tokens`, create the access token.
  - Tokens will only be able to access resources owned by the selected resource owner.
  - For organizations as resource owner, under `Settings` > `Personal access tokens`, `allow access via fine-grained personal access tokens`.

## Communicating with GraphQL API
### GraphQL API endpoint
The GraphQL API only has a single endpoint.
```
https://api.github.com/graphql
```

To make GraphQL calls:
1. Use the [GitHub GraphQL API Explorer](https://docs.github.com/en/graphql/overview/explorer).
2. Use HTTP-speaking library like `curl`, sending a `POST` request with a JSON payload containing a string called `query`.
```sh
curl -H "Authorization: bearer TOKEN" -X POST -d " \
  { \
    \"query\": \"query { JSON-OBJECT-TO-RETURN }\" \
  } \
" https://api.github.com/graphql
```

### Queries
Queries are structured as below:
```graphql
query {
  JSON-OBJECT-TO-RETURN
}
```

Forming query requires specification of nested subfields of [objects](https://docs.github.com/en/graphql/reference/objects), until returning only scalars.

```graphql
query {
  # designating a `Repository` object
  repository(owner: OWNER, name: REPOSITORY_NAME) {

    # `IssueConnection` type object
    issues() {

      # `IssueEdge` type object
      edges {

        # `Issue` type object
        node {
          title
          url
        }
      }
    }

  }
}
```

### Mutations
Mutations are structured as below:
```graphql
mutation {
  MUTATION-NAME(input: {MUTATION-NAME-INPUT!}) {
    MUTATION-NAME-PAYLOAD
  }
}
```

Forming mutations require 3 specifications: [mutation name](https://docs.github.com/en/graphql/reference/mutations), input object, and payload object.

```graphql
mutation {
  # designating a mutation operation
  # for multiple operation with the same mutation name,
  # a unique name must be given
  NAME1: createIssue(input: CreateIssueInput!) {

    clientMutationId

    # `Issue` type object
    issue {
      title
      url
    }

  }

  NAME2: createIssue(...) {...}
}
```

### Variables
[Variables](https://graphql.org/learn/queries/) can be prepared in a separate variable dictionary, usually JSON.

```graphql
# valid JSON object named `variables`
variables{
  "owner_name": OWNER,
  "repo_name": REPOSITORY_NAME,
}

# `!` is added for required types
query($owner_name: String! = "default", $repo_name: String!) {
  repository(owner: $owner_name, name: $repo_name) {
    ...
  }
}
```

## Using on GitHub Actions
1. Use [official action](https://github.com/octokit/graphql-action).
```yaml
jobs:
  graphQLAPI:
    runs-on: ubuntu-latest
    steps:
      - uses: octokit/graphql-action@v2.x
        with:
          query: |
            query QUERY_NAME($owner: String!, $repo: String!) {
              repository(owner: $owner, name: $repo) {
                ...
              }
            }
          variables: |
            owner: ${{ github.event.repository.owner.name }}
            repo: ${{ github.event.repository.name }}
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
