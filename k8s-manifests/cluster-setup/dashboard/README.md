# Kubernetes dashboard

https://github.com/kubernetes/dashboard
https://artifacthub.io/packages/helm/k8s-dashboard/kubernetes-dashboard

```bash
# Add kubernetes-dashboard repository
helm repo add kubernetes-dashboard https://kubernetes.github.io/dashboard/
# Deploy a Helm Release named "kubernetes-dashboard" using the kubernetes-dashboard chart
helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dashboard
```

Access guide (create a simple admin user): https://github.com/kubernetes/dashboard/blob/master/docs/user/access-control/creating-sample-user.md

Create a service account, bind the role and create a secret:
```bash
kubectl apply -f admin-dashboard-user.yaml
```

Access the board (**MUST** use port-forwarding; with _proxy_ Bearer token auth doesn't work):

```bash
# port-forwarding
kubectl -n kubernetes-dashboard port-forward svc/kubernetes-dashboard-kong-proxy 8443:443

# get the ServiceAccount token
kubectl -n kubernetes-dashboard create token admin-dashboard-user
```

Go to `https://localhost:8443/` and pass the token there.
