# Istio System – Traffic Management & Service Mesh Demo

This repository showcases a hands-on Istio setup focused on **traffic management**, **zero-trust networking**, and **observability** across Kubernetes workloads.  
It accompanies the concepts and walkthroughs from my two-part blog series on entering the Istio ecosystem and taming traffic flows inside a service mesh.

## Scope of the Project
- **Istio installation manifests** for a clean, reproducible setup  
- **Namespace-scoped deployments** demonstrating how workloads behave inside the mesh  
- **VirtualService & DestinationRule configs** for canarying, traffic splitting, retries, and fault injection  
- **mTLS policies** to lock down pod-to-pod communication  
- **Kiali, Prometheus, and Grafana integration** for real-time mesh visualization  

## How to Use This Repo
1. Deploy a Kubernetes cluster (minikube, kind, EKS, GKE—your choice).  
2. Install Istio using the official documentation.  
3. Apply workloads and traffic rules to see live routing changes.  

This project documents my learning path with Istio and provides a simple, reproducible reference for engineers exploring real-world service mesh patterns.
