# app manifests

- `backend.yaml` and `frontend.yaml` - deployments and services for backend and frontend
- `backend-*.yaml` and `frontend-*.yaml` - additional tools

## Deploy

```bash
kubectl -n dev apply .  # to deploy everything
kubectl -n dev get all  # list created resources
```
