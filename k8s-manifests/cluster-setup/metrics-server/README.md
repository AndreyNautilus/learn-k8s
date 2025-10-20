# k8s metrics-server

GitHub: https://github.com/kubernetes-sigs/metrics-server

Helm chart: https://artifacthub.io/packages/helm/metrics-server/metrics-server

See installation guide in the chart docs.

```bash
# list configuration values
helm show values metrics-server --repo https://kubernetes-sigs.github.io/metrics-server/ > chart-values.yaml
# deploy
helm upgrade --install metrics-server metrics-server --repo https://kubernetes-sigs.github.io/metrics-server/ --namespace metrics-server --create-namespace -f values.yaml
```

Check (wait a couple of minutes):

```bash
kubectl top pods
kubectl top nodes
```
