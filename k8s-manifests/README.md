# K8s manifests

## Preparation
The docker image should be published at least locally.

## Deploy
Everything:
```bash
kubectl apply -f namespace.yaml -f deployment.yaml -f service.yaml
```

## Verify
Resources:
```bash
kubectl get deploy -n=dev
kubectl get pod -n=dev
kubectl get service -n=dev
```

Endpoints from pods:
```bash
kubectl proxy
```
and go to (in brouwser): `http://localhost:8001/api/v1/namespaces/dev/pods/POD_NAME:POD_PORT/proxy/`
where `POD_NAME` from `kubectl get pods` and `POD_PORT` is the exposed port from the pod container.

```bash
kubectl log POD_NAME
```

Via ephemeral pod:
```bash
kubectl run --rm -it busybox --image=busybox:latest --restart=Never -n=dev
```

From existing pod:
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
