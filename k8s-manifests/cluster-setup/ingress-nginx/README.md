# NGINX ingress controller

GitHub: https://github.com/kubernetes/ingress-nginx
Docs: https://kubernetes.github.io/ingress-nginx/

Installation: https://kubernetes.github.io/ingress-nginx/deploy/#quick-start

```bash
helm upgrade --install ingress-nginx ingress-nginx --repo https://kubernetes.github.io/ingress-nginx --namespace ingress-nginx --create-namespace
```
