# helm charts

## Prerequesites

We need [metrics server](https://github.com/kubernetes-sigs/metrics-server),
see `k8s-manifests/metrics-server` for details.

We need a `dev` namespace in the cluster (preferably empty):
```bash
kubectl create namespace dev
```

## Install/upgrade the chart

```bash
helm install app-flask app-flask -n=dev
helm upgrade app-flask app-flask -n=dev
```
the first "app-flask" is the name of the chart, the second - the folder.

## Cleanup

```bash
helm uninstall app-flask
```
