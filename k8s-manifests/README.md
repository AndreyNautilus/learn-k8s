# K8s manifests

Deploy everything:
```bash
kubectl apply -f deployment.yaml -f service.yaml
```

Verify:
```bash
kubectl get deploy
kubectl get pod
kubectl get service
```

Cleanup:
```bash
kubectl delete deploy ...
kubectl delete service ...
```
