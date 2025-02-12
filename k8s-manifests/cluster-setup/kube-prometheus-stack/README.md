# Prometheus stack

https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack
https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack

## Installation (from official docs)

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm install prometheus-stack prometheus-community/kube-prometheus-stack --namespace monitoring --create-namespace
```

## Access

Use port-forwarding.

```bash
$ kubectl get svc -n monitoring
NAME                                        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                      AGE
alertmanager-operated                       ClusterIP   None             <none>        9093/TCP,9094/TCP,9094/UDP   23h
prometheus-operated                         ClusterIP   None             <none>        9090/TCP                     23h
prometheus-stack-grafana                    ClusterIP   10.105.252.125   <none>        80/TCP                       23h
prometheus-stack-kube-prom-alertmanager     ClusterIP   10.102.200.126   <none>        9093/TCP,8080/TCP            23h
prometheus-stack-kube-prom-operator         ClusterIP   10.98.179.211    <none>        443/TCP                      23h
prometheus-stack-kube-prom-prometheus       ClusterIP   10.109.2.23      <none>        9090/TCP,8080/TCP            23h
prometheus-stack-kube-state-metrics         ClusterIP   10.98.191.207    <none>        8080/TCP                     23h
prometheus-stack-prometheus-node-exporter   ClusterIP   10.108.51.228    <none>        9100/TCP                     23h
```

- `prometheus-operated` - main Prometheus instance;
- `prometheus-stack-grafana` - Grafana instance;

### Prometheus

```bash
kubectl port-forward -n monitoring svc/prometheus-operated 9090:9090
```

And go to `localhost:9090` to access prometheus UI.

### Grafana

```bash
kubectl port-forward -n monitoring svc/prometheus-stack-grafana 3000:80
```

And go to `localhost:3000` to access Grafana UI.
Usename: `admin`, password is in `kubectl get -n monitoring secret prometheus-stack-grafana -o yaml` (then `base64 -d`).
