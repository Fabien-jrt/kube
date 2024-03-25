# KUBE API

## API Side

the api.py file is the api build with python3 and fastapi.  
use the /docs route to see the documentation and use the "try it" button to upload a file.

## Kube Side

1. minikube strat
2. minikube addons enable metrics-server
3. kubectl apply -f deployment.yaml
4. kubectl apply -f service.yaml
5. kubectl apply -f ingress.yaml
6. kubectl apply -f hpa.yaml
7. minikube dashboard
8. kubectl port-forward service/my-app-service 9808:80
9. go to localhost:9808



