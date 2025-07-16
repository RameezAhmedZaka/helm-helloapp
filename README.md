This is a Helm chart for deploying the `helloapp` application on a Kubernetes cluster using Helm.

Project Structure

hellohelm/
├── Chart.yaml # Metadata for the Helm chart
├── values.yaml # Default configuration values
├── charts/ # Directory for dependent charts
├── templates/ # Kubernetes resource templates
│ ├── deployment.yaml
│ ├── service.yaml
│ ├── ingress.yaml
│ ├── _helpers.tpl
│ └── NOTES.txt

helm install hellohelm ~/hellohelm --namespace hellohelm-ns
helm upgrade hellohelm ~/hellohelm --namespace hellohelm-ns
helm history hellohelm --namespace hellohelm-ns
helm uninstall hellohelm --namespace hellohelm-ns
