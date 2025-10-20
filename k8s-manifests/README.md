# Kubernetes manifests

## Preparation

Docker images should be published at least locally.

Cluster should include required tools, see [cluster-setup](cluster-setup/README.md).

## Deploy and verify

See [README in app folder](app/README.md).

## Debug

```bash
kubectl log POD_NAME
```

where `POD_NAME` from `kubectl get pods` and `POD_PORT` is the exposed port from the pod container.

```bash
kubectl proxy
curl http://localhost:8001/api/v1/namespaces/dev/pods/POD_NAME:POD_PORT/proxy/
```

```bash
kubectl run --rm -it busybox --image=busybox:latest --restart=Never -n=dev
```

or

```bash
kubectl exec POD_NAME -n=dev -- curl IP
```

where `IP` is the IP and exposed port of (other) pods.

## Clean up

Delete the namespace to delete everything in it:

```bash
kubectl delete -f namespace.yaml
```

or

```bash
kubectl delete dev
```

## Generate fake load

### simple low load

Just make a request every second. fish shell:

```bash
while true;
    date && curl -I http://localhost;
    sleep 1s;
end
```

### high load

Use `wrk` [tool](https://github.com/wg/wrk):

```bash
wrk --connections 10 --threads 10 --duration 5m -H "Connection: Close" "http://localhost:8000/backend/stress"
```
