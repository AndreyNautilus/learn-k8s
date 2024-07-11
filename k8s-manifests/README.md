# K8s manifests

Deploy:
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
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