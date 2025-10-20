# Cluster setup

## Supported clusters

- Docker Desktop - integrated one-node custer
- [kind](https://kind.sigs.k8s.io/docs/user/quick-start/)

```bash
# list available contexts
kubectl config get-contexts
# show current context
kubectl config current-context
# switch context
kubectl config use-context NAME
```

### Docker Desktop

Settings -> Kubernetes -> "Enable Kubernetes" toggle -> Apply.

```bash
# should give 'docker-desktop' context name
kubectl config current-context
```

### kind cluster

Manage a multi-node local cluster (named `kind-messages`):

```bash
# create a cluster
kind create cluster --config kind-cluster.yaml
# list kind clusters
kind get clusters
# delete the kind cluster (permanently erase everything)
kind delete cluster --name=kind-messages
```

Verify the `kubectl` config after the cluster is created:

```bash
# should give 'kind-kind-messages' context name
kubectl config current-context
```

#### Load images into the kind cluster

kind doesn't see local images (from local Docker Desktop registry).
Images have to loaded into the kind cluster manually:

```bash
kind --name kind-messages load docker-image app-backend:1.0.0 app-frontend-vue:1.0.0 mysql-msgs:9.1.0
```

## 3rd party tools

Necessary 3rd party tools to be installed in the cluster.

1. `metrics-server` to enable HPA
1. (optional) `dashboard` to get basic monitoring
1. `ingress-nginx` to enable ingress resources
1. `kube-prometheus-stack` to enable performance monitoring
