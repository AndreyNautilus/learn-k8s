# K8s manifests

Deploy everything:
```bash
kubectl apply -f namespace.yaml -f deployment.yaml -f service.yaml
```

Verify:
```bash
kubectl get deploy
kubectl get pod
kubectl get service
```

Cleanup (takes some time). Delete the namespace to delete all from it:
```bash
kubectl delete -f namespace.yaml
```
