# Kubernetes Cheat Sheet <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->
- [Writing a Manifest file](#writing-a-manifest-file)
- [Using the command line tool](#using-the-command-line-tool)

## Writing a Manifest file
Kubernetes creates Pods according to what is written in the Manifest file. When uploading the contents, the desired state gets saved in the database, and the server environment gets maintained.

The Manifest file can be written in either JSON or YAML format, and can be given any name.

```yaml
# specification about resource
# https://kubernetes.io/docs/reference/kubernetes-api/
apiVersion: apps/v1
kind: Deployment

# metadata of resource
# https://kubernetes.io/docs/reference/kubernetes-api/common-definitions/object-meta/#ObjectMeta
metadata:
  # name of resource, should be a unique string
  name: deployment-1
  # list of arbitrary key value pair,
  # used by selector to conditionally apply actions
  labels:
    key1: value1
    key2: value2

# details about resource, content depends on type of resource
spec:
  # eg. for deployment resource
  # https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/deployment-v1/
  selector:
    matchLabels:
      app: pod-1
  template:
    metadata:
      labels:
        app: pod-1
    spec:
      # https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1
      containers:
        - name: container-1
          image: ubuntu
          ports:
            - containerPort: 80
  replicas: 1

# within a file multiple resource settings can be written, using a divider
---

apiVersion: v1
kind: Service
metadata:
  name: service-1
spec:
  selector:
    app: pod-1
  ports:
    - port: 8099
      targetPort: 80
      protocol: TCP
      nodePort: 30080
  type: NodePort
```

## Using the command line tool
- Create or upload resourcees, by loading Manifest file to Kubernetes.
```sh
$ kubectl apply -f FILE.yml
```

- Delete resources, by loading Manifest file to Kubernetes.
```sh
$ kubectl delete -f FILE.yml
```

- Get list of [resources](https://kubernetes.io/docs/reference/kubectl/#resource-types).
```sh
$ kubectl get RESOURCE
```
