# k8s metrics-server

https://github.com/kubernetes-sigs/metrics-server

We can't use [helm chart](https://artifacthub.io/packages/helm/metrics-server/metrics-server)
for installing into Docker Desktop, because metrics-server requires
a signed TLS certificate, which we don't have yet. Helm chart doesn't provide a config option
to bypass this requirement.

We have to download k8s manifest file from a [GitHub release](https://github.com/kubernetes-sigs/metrics-server/releases),
patch it:

```diff
diff --git a/k8s-manifests/metrics-server/components-v0.7.2.yaml b/k8s-manifests/metrics-server/components-v0.7.2.yaml
index 91c2dc8..60082c1 100644
--- a/k8s-manifests/metrics-server/components-v0.7.2.yaml
+++ b/k8s-manifests/metrics-server/components-v0.7.2.yaml
@@ -136,6 +136,7 @@ spec:
         - --secure-port=10250
         - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
         - --kubelet-use-node-status-port
+        - --kubelet-insecure-tls  # added as suggested by README
         - --metric-resolution=15s
         image: registry.k8s.io/metrics-server/metrics-server:v0.7.2
         imagePullPolicy: IfNotPresent
```

And install it manually:

```bash
kubectl apply -f components-v0.7.2.yaml

# check it (wait a couple of minutes before checking)
kubectl top pods
```
