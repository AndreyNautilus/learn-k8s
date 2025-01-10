# NGINX ingress controller

GitHub: https://github.com/kubernetes/ingress-nginx
Docs: https://kubernetes.github.io/ingress-nginx/

Installation: https://kubernetes.github.io/ingress-nginx/deploy/#quick-start

```bash
# list configuration values
helm show values ingress-nginx --repo https://kubernetes.github.io/ingress-nginx > values.yaml
# deploy
helm upgrade --install ingress-nginx ingress-nginx --repo https://kubernetes.github.io/ingress-nginx --namespace ingress-nginx --create-namespace
```

Check:
```bash
kubectl -n ingress-nginx get all
# Should list:
# - at least 1 pod
# - one LoadBalancer service

kubectl get ingressclasses
# should list 'nginx' Ingress Class. It's used in the app deployment
```
